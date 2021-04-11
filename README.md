# Client Side Object Detection App

This project was one of the modules developed as part of Smart India Hackathon 2020.  
It's a Python app that processes a live video stream and runs a complete Machine Learning Pipeline with multiple models.
The video is supposed to be coming from a dashcam mounted in front of any vehicle.

It detects vehicles, pedestrians and traffic signs in the first pass.  
Traffic signs are analyzed and classified in the second pass.  
They are further processed and information is extracted from them in the third pass.  

All of this information is fed to a mathematical algorithm that calculates an appropriate speed to drive the vehicle at.

## Executing the script:
1. Create a virtual environment using something like `conda` or `virualenv`.  
2. Install the necessary dependencies listed in `requirements.py`.  
3. Run `python3 src/main.py`.
