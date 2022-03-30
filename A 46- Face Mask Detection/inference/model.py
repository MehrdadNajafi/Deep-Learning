import tensorflow as tf
import numpy as np
import cv2
from mtcnn import MTCNN

class Model:
    def __init__(self):
        self.model = tf.keras.models.load_model("model/faceMask_detection.h5")
        self.width = self.height = 224
        self.face_detector = MTCNN()
    
    def with_Or_Without_Mask(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = self.face_detector.detect_faces(frame_rgb)
        if faces:
            for face in faces:
                x, y, w, h = face["box"]
                
                face_pic = frame_rgb[y:y+h, x:x+w]
                face_pic = cv2.resize(face_pic, (self.width, self.height))
                face_pic = face_pic.reshape(1, self.width, self.height, 3)
                face_pic = face_pic / 255.0
                y_pred = np.argmax(self.model.predict(face_pic))
                
                if y_pred == 0:
                    result = "With Mask"
                    color = (0, 255, 0)
                elif y_pred == 1:
                    result = "Without Mask"
                    color = (0, 0, 255)
                
                cv2.rectangle(frame, (x, y), (x+w, y+h), color, 4)
                cv2.putText(frame, result, (x, y-15), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
            return frame, "Face detected ✅"
        else:
            return frame, "Face not detected ❌"