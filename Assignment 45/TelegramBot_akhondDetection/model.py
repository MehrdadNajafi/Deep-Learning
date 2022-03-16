import os
import cv2
import numpy as np
import tensorflow as tf

if not os.path.exists("model"):
    os.mkdir("model")

class Model:
    def __init__(self):
        self.model = tf.keras.models.load_model("model/akhondDetector.h5")
    def predit_type(self, img_path):
        width = height = 299
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (width, height))
        img = img / 255
        img = img.reshape(1, width, height, 3) # 3d ---> 4d
        
        pred = np.argmax(self.model.predict(img))
        
        if pred == 0:
            pred_result = "'Normal Person'"
        if pred == 1:
            pred_result = "'Sheikh'"
        
        return pred_result