import argparse
import cv2
import numpy as np
from model import MyModel

parser = argparse.ArgumentParser()
parser.add_argument("--inputPath", type=str, required=True,
                    help="Input Path")
parser.add_argument("--weightsPath", type=str, required=True,
                    help="Weights path")
args = parser.parse_args()

width = height = 224

model = MyModel()
model(np.zeros((1, width, height, 3)))
model.load_weights(args.weightsPath)

labels = ['Ali_Khamenei', 'Angelina_Jolie', 'Barak_Obama', 'Behnam_Bani', 'Donald_Trump', 'Emma_Watson', 'Han_Hye_Jin',
          'Kim_Jong_Un', 'Leyla_Hatami', 'Lionel_Messi', 'Michelle_Obama', 'Morgan_Freeman', 'Queen_Elizabeth', 'Scarlett_Johansson']

labels.sort()

img = cv2.imread(args.inputPath)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (width, height))
img = img[np.newaxis, ...]
img = img / 255.0

pred = np.argmax(model(img))
print(f"The person is: {labels[pred]}")