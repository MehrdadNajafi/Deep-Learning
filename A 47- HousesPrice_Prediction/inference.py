import os
import argparse
import cv2
import tensorflow as tf
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--input-path", type=str, required=True,
                    help="Path of input images")
args = parser.parse_args()

if not os.path.exists("model/"):
    os.makedirs("model/")

model = tf.keras.models.load_model("model\housesPrice_Model.h5")

inputImages = []
outputImage = np.zeros((64, 64, 3), dtype="uint8")

for img_path in os.listdir(args.input_path):
    image = cv2.imread(os.path.join(args.input_path, img_path))
    image = cv2.resize(image, (32, 32))
    inputImages.append(image)

outputImage[0:32, 0:32] = inputImages[0]
outputImage[0:32, 32:64] = inputImages[1]
outputImage[32:64, 32:64] = inputImages[2]
outputImage[32:64, 0:32] = inputImages[3]

outputImage = np.array(outputImage)
outputImage = outputImage / 255.0
outputImage = outputImage.reshape(1, 64, 64, 3)

pred = model.predict([outputImage])
pred = pred[0][0]
print(f"[INFO] The estimated price for this house is $ {pred} ")