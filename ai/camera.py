from PySide6.QtCore import *
from PySide6.QtGui import QImage, QPixmap
import cv2
import os
from datetime import datetime
import face_recognition
import numpy as np

class Camera:
    def __init__(self, videoBox):
        self.videoBox = videoBox
        self.capture = None
        self.timer = None
        self.output_dir = "src\\data\\captured_faces"
        self.known_faces_dir = "src\\data\\known_faces"
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(self.known_faces_dir, exist_ok=True)
        
        # Face detection attributes
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
        self.current_faces = []  # Stores current face rectangles

        # Face recognition attributes
        self.known_face_encodings = []
        self.known_face_names = []
        self.load_known_faces()

        # Face capture timer
        self.face_detected = False
        self.face_detection_time = None
        self.current_face_location = None
        self.face_timer = QTimer()
        self.face_timer.timeout.connect(self._check_face_timer)

        #Flags
        self.face_recognition_active = False
        self.imgName = "face_captured"

        #Results
        self.faceID = None
        self.similarity = None
        self.recognizied_face = None

    def setup_camera(self):
        """Initialize camera."""
        self.capture = cv2.VideoCapture(0)
        if not self.capture.isOpened():
            raise RuntimeError("Could not open video device")
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.videoBox.width())
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.videoBox.height())

        self.timer = QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(30)  # ~33 fps

    def detect_faces(self, frame):
        """Detect faces in the frame and return annotated frame."""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(100,100))
        if len(faces) > 0:
            if not self.face_detected:
                self.face_detected = True
                self.face_detection_time = datetime.now()
                self.current_faces = faces[0]
                self.face_timer.start(100)
            elif (datetime.now() - self.face_detection_time).total_seconds() >= 2:
                if self.face_recognition_active:
                    self.capture_and_compare()
                else:
                    self.capture_face()
                self.face_detected = False
                self.face_timer.stop()
        else:
            self.face_detected = False
            self.face_timer.stop()

        for (x, y, w, h) in faces:
            elapsed = (datetime.now() - self.face_detection_time).total_seconds()
            countdown = max(0, 2 - elapsed)
            #cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255 ), 2)
            cv2.putText(frame, f"Capturing in: {countdown:.1f}s", 
                        (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 
                        0.5, (255, 255, 255), 2)
        
        return frame

    def display_video_stream(self):
        """Read frame from camera and repaint QLabel widget."""
        ret, frame = self.capture.read()
        if ret:
            frame = self.detect_faces(frame)
            # Convert to RGB for display
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = QImage(
                frame, 
                frame.shape[1], 
                frame.shape[0], 
                frame.strides[0], 
                QImage.Format_RGB888
            )
            self.videoBox.setPixmap(QPixmap.fromImage(image))

    def capture_face(self):
        if not self.capture or not self.capture.isOpened():
            raise RuntimeError("Camera is not initialized")
            
        ret, frame = self.capture.read()
        if not ret:
            raise RuntimeError("Failed to capture frame")
        
        # Get the first detected face
        x, y, w, h = self.current_faces
        
        # Add some padding around the face (50% of face width/height)
        padding = int(0.7 * min(w, h))
        x = max(0, x - padding)
        y = max(0, y - padding)
        w = min(frame.shape[1] - x, w + 2*padding)
        h = min(frame.shape[0] - y, h + 2*padding)
        
        face_roi = frame[y:y+h, x:x+w]
        
        if self.face_recognition_active:
            img_path = self.output_dir
        else:
            img_path = self.known_faces_dir
        imgName = self.imgName + '.png'
        filepath = os.path.join(img_path, imgName)
        success = cv2.imwrite(filepath,face_roi)
        if not self.face_recognition_active:
            self.close_camera()
        if not success:
            raise RuntimeError(f"Failed to save face image to {filepath}")
        self.faceID = imgName
            
        return filepath

    def load_known_faces(self):
        """Load known faces from the known_faces directory"""
        self.known_face_encodings = []
        self.known_face_names = []
        
        for filename in os.listdir(self.known_faces_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(self.known_faces_dir, filename)
                image = face_recognition.load_image_file(image_path)
                
                # Get face encoding (128-dimensional vector)
                encodings = face_recognition.face_encodings(image)
                if len(encodings) > 0:
                    self.known_face_encodings.append(encodings[0])
                    self.known_face_names.append(os.path.splitext(filename)[0])

    def compare_faces(self, face_image):
        """
        Compare a face image with known faces
        Returns: (name, similarity) or (None, 0) if no match
        """
        # Convert to RGB (face_recognition uses RGB)
        rgb_face = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)
        
        # Get face encoding
        face_encodings = face_recognition.face_encodings(rgb_face)
        if len(face_encodings) == 0:
            return None, 0
            
        face_encoding = face_encodings[0]
        
        # Compare with known faces
        if len(self.known_face_encodings) == 0:
            return None, 0
            
        # Calculate face distances
        face_distances = face_recognition.face_distance(
            self.known_face_encodings, face_encoding
        )
        
        # Get best match
        best_match_index = np.argmin(face_distances)
        min_distance = face_distances[best_match_index]
        
        # Convert distance to similarity (0-1 scale)
        similarity = 1 - min_distance
        
        # Threshold for recognition (adjust as needed)
        if min_distance < 0.6:  # Lower is more similar
            return self.known_face_names[best_match_index], similarity
        else:
            return None, similarity

    def capture_and_compare(self):
        """
        Capture face and compare with known faces
        Returns: (filepath, name, similarity) or (None, None, 0) if no face
        """
        face_path = self.capture_face()
        # Load the captured face
        face_image = cv2.imread(face_path)
        name, similarity = self.compare_faces(face_image)
        if name != None:
            self.recognizied_face = name +'.png'
        self.similarity = similarity

    def _check_face_timer(self):
        """Timer callback for face detection."""
        pass  # Just triggers display update

    def close_camera(self):
        """Release camera resources."""
        if self.capture and self.capture.isOpened():
            self.capture.release()
        if self.timer and self.timer.isActive():
            self.timer.stop()
    