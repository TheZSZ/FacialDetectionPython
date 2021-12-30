# FacialDetectionPython
A Facial Detection Program in Python that I created to learn about the OpenCV Library

Required Libraries:
- OpenCV (needs to be installed)
- NumPy (needs to by installed)
- OS (included with python)
- Sys (included with python) 

Library Installation with pip package manager:
- 'pip install numpy' to install NumPy
- 'pip install opencv-python' to install OpenCV

Commands:
- 'python faceDetect.py' to see usage cases
- 'python faceDetect.py [path/to/file]' to pass an image into the program
- 'python faceDetect.py camera' to pass camera stream into the program



Comments:
- Works well with clear front-facing images
![Screenshot](images/007.jpg)
![Screenshot](images/007-detection.png)
![Screenshot](images/gandhi.jpg)
![Screenshot](images/gandhi-detection.png)
- Semi-realistic cartoon charater (Heavy from Team Fortress 2)
![Screenshot](images/tf2heavy.jpg)
![Screenshot](images/tf2heavy-detection.png)
- Works with multiple people
![Screenshot](images/HouseoftheRisingSun.jpg)
![Screenshot](images/HouseoftheRisingSun-detection.png)
![Screenshot](images/SabreFencers.jpg)
![Screenshot](images/SabreFencers-detection.png)
- Cannot detect faces if wearing objects around or on face like Hijab or if side profile :(
