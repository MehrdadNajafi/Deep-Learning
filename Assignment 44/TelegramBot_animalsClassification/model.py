import cv2
import numpy as np
import tensorflow as tf
from PIL import ImageFile

class Model:
    def __init__(self):
        self.model = tf.keras.models.load_model("model/animalsClassification.h5")
    def predit_animal(self, img_path):
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        width = height = 224
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (width, height))
        img = img / 255
        img = img.reshape(1, width, height, 3) # 3d ---> 4d
        
        pred = np.argmax(self.model.predict(img))
        
        if pred == 0:
            pred_animal = "Elephant"
        if pred == 1:
            pred_animal = "Koala"
        if pred == 2:
            pred_animal = "Lion"
        if pred == 3:
            pred_animal = "Wolf"
        
        return pred_animal