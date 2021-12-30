# Zeeshan Khan
# Facial Detection Program
# 12/29/2021

import cv2, sys, numpy, os                                                                              # cv2 is openCV library, sys for getting argv, numpy for counting in camera, and os for path

if len(sys.argv) == 1:                                                                                  # Help Message is argv[1] doesn't exist
    print("\nUsage: 'python faceDetect.py [path/to/image]\nUsage: 'python faceDetect.py camera'\n")     # Tells user that they can input file path or "camera" for Live capture
    sys.exit(0)                                                                                         # Exit Program to avoid seg fault

def Photo():
    imagePath = sys.argv[1]                                                                                 # argv (image file)
    exists = os.path.exists(imagePath)                                                                      # Checking if the path exists
    if exists == False:                                                                                     # If the path does not exist
        print("\nPath does not exist!\n")                                                                   # Print message
        sys.exit(0)                                                                                         # Exit program, otherwise
    image = cv2.imread(imagePath)                                                                           # Read image
    grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)                                                     # Convert to grayscale for better facial detection
    faces = cascade.detectMultiScale(grayScale, scaleFactor = 1.2, minNeighbors = 5, minSize = (30, 30))    # Detect faces in image
    for (x, y, width, height) in faces:                                                                     # Draw a rectangle around the faces
        cv2.rectangle(image, (x, y), (x + width, y + height), (255, 0, 255), 3)                             # Magenta Color and box size (3)
    print(len(faces), "faces")                                                                              # Print amount of faces detected
    cv2.imshow("Faces detected", image)                                                                     # Display image in window
    cv2.waitKey(0)                                                                                          # Waitkey to display image

def Live():
    capture = cv2.VideoCapture(0)                                                                               # Open camera
    while(True):                                                                                                # Constant loop
        a, image = capture.read()                                                                               # Read video capture
        grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)                                                     # Convert to grayscale for better facial detection
        faces = cascade.detectMultiScale(grayScale, scaleFactor = 1.2, minNeighbors = 5, minSize = (30, 30))   	# Detect faces in the image
        for (x, y, width, height) in faces:                                                                     # Draw a rectangle around the faces
            cv2.rectangle(image, (x, y), (x+width, y+height), (255, 0, 255), 3)                                 # Magenta Color and box size (3)
        print(len(faces), "faces")                                                                              # Print amount of faces detected
        cv2.imshow('Q to exit program', image)                                                                  # Header for window and what to display
        if cv2.waitKey(1) & 0xFF == ord('q'):                                                                   # Waitkey and quit program if Q pressed
            break                                                                                               # Break loop
    capture.release()                                                                                           # Release video capture
    cv2.destroyAllWindows()                                                                                     # Destroy Opened Windows


cascade = cv2.CascadeClassifier("cascadium.xml")                                                        # Open cascade XML file for facial detection
if sys.argv[1] == "camera":                                                                             # If camera typed, go to Live() function
    print("Opening Camera...")
    Live()
else:                                                                                                   # Else go to Photo() function
    print("Opening Photo...")
    Photo()