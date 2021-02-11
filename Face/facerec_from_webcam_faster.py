import face_recognition
import cv2
import numpy as np

    # This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
    # other example, but it includes some basic performance tweaks to make things run a lot faster:
    #   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
    #   2. Only detect faces in every other frame of video.
def humanFace():
    # Get a reference to webcam #0 (the default one)
    video_capture = cv2.VideoCapture(0)

    # Load a sample photo
    person1_image = face_recognition.load_image_file("Capture.PNG")
    person1_encoding = face_recognition.face_encodings(person1_image)[0]

    # Create arrays of known face encodings and their names
    known_face_encodings = [
        person1_encoding
    ]
    known_face_names = [
        "MasterWard"
    ]

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    return name
                print(name)
                face_names.append(name)

        process_this_frame = not process_this_frame

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()

def catFace():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml') 
    cap = cv2.VideoCapture(0) 
    # loop runs if capturing has been initialized. 
    while True: 
            # reads frames from a camera 
            ret, img = cap.read() 

            # convert to gray scale of each frames 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

            # Detects faces of different sizes in the input image 
            faces = face_cascade.detectMultiScale(gray, 1.3, 5) 

            for (x,y,w,h) in faces: 
                    # To draw a rectangle in a face 
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
                    roi_gray = gray[y:y+h, x:x+w] 
                    roi_color = img[y:y+h, x:x+w] 

            # Display an image in a window 
            cv2.imshow('img',img) 

            # Wait for Esc key to stop 
            k = cv2.waitKey(30) & 0xff
            if k == 27: 
                    break

    # Close the window 
    cap.release() 

    # De-allocate any associated memory usage 
    cv2.destroyAllWindows() 



def main():
    print("finding the human face")
    name = humanFace()
    print(name)
    print("Finding cat face")
    # Find the cat here

main()
