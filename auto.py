import os
import subprocess

script_directory = os.path.dirname(os.path.abspath(__file__))
print(script_directory)

activate_this_file = os.path.join(script_directory, '/tflite1-env/bin/python/bin/activate_this.py')
print(activate_this_file)

subprocess.call('python3 TFLite_detection_webcam.py --modeldir=Sample_TFLite_Model --resolution=400x200')