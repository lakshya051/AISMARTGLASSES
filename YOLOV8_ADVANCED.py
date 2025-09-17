# smart_glasses_yolov8_complete.py
import os
import cv2
import numpy as np
import time
from threading import Thread, Lock
import tempfile

# Feature libraries
import pytesseract
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from ultralytics import YOLO

# --- Configuration ---
FOCAL_LENGTH = 700 
KNOWN_WIDTHS = { "person": 0.5, "car": 1.8, "bicycle": 1.0, "stop sign": 0.76, "chair": 0.6 }

# --- Model & Helper Initialization ---
print("Loading YOLOv8 model...")
model = YOLO('yolov8n.pt')
recognizer = sr.Recognizer()
microphone = sr.Microphone()
print("Model loaded.")

# --- Thread-Safe State Management ---
app_state = {
    "is_listening": False,
    "is_answering": False,
    "last_spoken": {},
    "lock": Lock()
}

# --- Core Functions ---
def speak(text):
    """Thread-safe text-to-speech function."""
    with app_state["lock"]:
        if app_state["is_answering"]: return
        app_state["is_answering"] = True
    
    try:
        if not text: return
        tts = gTTS(text=text, lang='en')
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
            tts.save(fp.name)
            temp_filename = fp.name
        playsound(temp_filename)
        os.remove(temp_filename)
    except Exception as e:
        print(f"TTS Error: {e}")
    finally:
        with app_state["lock"]:
            app_state["is_answering"] = False

def get_distance(object_name, box_pixel_width):
    """Calculates distance in meters."""
    if object_name in KNOWN_WIDTHS and box_pixel_width > 0:
        distance = (KNOWN_WIDTHS[object_name] * FOCAL_LENGTH) / box_pixel_width
        return f"{distance:.1f} meters"
    return None

def process_question(question, frame):
    """Analyzes a question and generates an answer."""
    answer = ""
    if not question: return

    if "how far" in question:
        target = next((obj for obj in KNOWN_WIDTHS if obj in question), None)
        if target:
            results = model(frame, verbose=False)
            found = False
            for r in results:
                for box in r.boxes:
                    if model.names[int(box.cls[0])] == target and box.conf[0] > 0.5:
                        dist = get_distance(target, box.xyxy[0][2] - box.xyxy[0][0])
                        answer = f"The {target} is about {dist} away."
                        found = True
                        break
                if found: break
            if not found: answer = f"I don't see a {target}."
        else:
            answer = "I can only measure distances for objects like people, cars, or chairs."
    
    elif "see" in question:
        results = model(frame, verbose=False)
        objects = {model.names[int(box.cls[0])] for r in results for box in r.boxes if box.conf[0] > 0.5}
        answer = "I see " + ", ".join(objects) if objects else "I don't see anything clearly."

    elif "read" in question or "say" in question:
        text = pytesseract.image_to_string(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)).strip()
        answer = f"It says: {text}" if text else "I can't read anything."
        
    else:
        answer = "Sorry, I can only answer questions about what I see or how far things are."
        
    Thread(target=speak, args=(answer,), daemon=True).start()

def voice_listener_thread(frame_ref):
    """Dedicated thread to listen for a question."""
    with app_state["lock"]:
        if app_state["is_listening"]: return
        app_state["is_listening"] = True

    speak("Ask a question.")
    
    with microphone as source:
        try:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening for question...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            question = recognizer.recognize_google(audio)
            print(f"Heard: '{question}'")
            process_question(question.lower(), frame_ref[0])
        except (sr.UnknownValueError, sr.WaitTimeoutError):
            speak("I didn't catch that.")
        except sr.RequestError as e:
            print(f"API Error: {e}")
    
    with app_state["lock"]:
        app_state["is_listening"] = False

# --- Main Application Loop ---
imW, imH = 1280, 720
videostream = cv2.VideoCapture(0)
videostream.set(cv2.CAP_PROP_FRAME_WIDTH, imW)
videostream.set(cv2.CAP_PROP_FRAME_HEIGHT, imH)
frame_ref = [None] 

print("Starting... Press 'q' to quit, 'a' to ask a question.")

while True:
    ret, frame = videostream.read()
    if not ret: break
    frame_ref[0] = frame.copy()

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'): break
    
    if key == ord('a'):
        listener_thread = Thread(target=voice_listener_thread, args=(frame_ref,), daemon=True)
        listener_thread.start()

    with app_state["lock"]:
        is_busy = app_state["is_listening"] or app_state["is_answering"]
    
    # --- Ambient Mode (Now with distance!) ---
    if not is_busy:
        results = model(frame, stream=True, verbose=False)
        for result in results:
            for box in result.boxes:
                if box.conf[0] > 0.6:
                    object_name = model.names[int(box.cls[0])]
                    if time.time() - app_state["last_spoken"].get(object_name, 0) > 10:
                        # **DISTANCE CALCULATION RESTORED HERE**
                        pixel_width = box.xyxy[0][2] - box.xyxy[0][0]
                        distance_str = get_distance(object_name, pixel_width)
                        speak_text = f"{object_name}" + (f", about {distance_str} away" if distance_str else "")
                        
                        app_state["last_spoken"][object_name] = time.time()
                        Thread(target=speak, args=(speak_text,), daemon=True).start()
    
    # Drawing on the frame always happens for a smooth UI
    results = model(frame, verbose=False)
    for r in results:
        for box in r.boxes:
            if box.conf[0] > 0.5:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                object_name = model.names[int(box.cls[0])]
                distance_str = get_distance(object_name, x2 - x1)
                label = f'{object_name} {box.conf[0]:.2f}' + (f' ({distance_str})' if distance_str else '')
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    cv2.imshow('Smart Glasses', frame)

# Cleanup
cv2.destroyAllWindows()
videostream.release()

