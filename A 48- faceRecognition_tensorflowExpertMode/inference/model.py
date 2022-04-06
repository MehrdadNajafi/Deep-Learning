import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D

width = height = 224

class MyModel(Model):
    def __init__(self):
        super().__init__()
        
        self.conv2d_1 = Conv2D(32, (3, 3), activation="relu", input_shape=(width, height, 3))
        self.conv2d_2 = Conv2D(32, (3, 3), activation="relu")
        self.maxpoll_1 = MaxPooling2D()
        self.conv2d_3 = Conv2D(64, (3, 3), activation="relu")
        self.conv2d_4 = Conv2D(64, (5, 5), activation="relu")
        self.maxpoll_2 = MaxPooling2D()

        self.dropout_1 = Dropout(0.5)
        self.dropout_2 = Dropout(0.3)
        
        self.flatten = Flatten()
        self.dense_1 = Dense(512, activation="relu")
        self.dense_2 = Dense(256, activation="relu")
        self.dense_3 = Dense(14, activation="softmax")

    def call(self, x):
        y = self.conv2d_1(x)
        y = self.conv2d_2(y)
        y = self.maxpoll_1(y)
        y = self.conv2d_3(y)
        y = self.conv2d_4(y)
        y = self.maxpoll_2(y)

        y = self.flatten(y)
        y = self.dense_1(y)
        y = self.dropout_1(y)
        y = self.dense_2(y)
        y = self.dropout_2(y)
        out_final = self.dense_3(y)

        return out_final