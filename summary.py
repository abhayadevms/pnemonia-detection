import sys
import os
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
from keras.models import Sequential
from keras.layers import Dropout, Flatten, Dense, Activation

from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras import callbacks
from keras.layers import BatchNormalization
from keras.layers import Conv2D, MaxPooling2D
import numpy as np
from keras.preprocessing import image
from keras.optimizers import RMSprop, adam
from keras.callbacks import EarlyStopping
from keras.regularizers import l2
#from sklearn import svm
from keras.optimizers import SGD
#from imutils import paths






model = Sequential()
model.add(Conv2D(16, (3, 3), activation='relu', padding="same", input_shape=(240, 240,3)))
model.add(Conv2D(16, (3, 3), padding="same", activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2),dim_ordering='th'))

model.add(Conv2D(32, (3, 3), padding="same", activation='relu'))
model.add(Conv2D(32, (3, 3), padding="same", activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2),dim_ordering='th'))

model.add(Conv2D(64, (3, 3), activation='relu', padding="same"))
model.add(Conv2D(64, (3, 3), padding="same", activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2),dim_ordering='th'))

model.add(Conv2D(96, (3, 3), dilation_rate=(2, 2), activation='relu', padding="same"))
model.add(Conv2D(96, (3, 3), padding="valid", activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2),dim_ordering='th'))

model.add(Conv2D(128, (3, 3), dilation_rate=(2, 2), activation='relu', padding="same"))
model.add(Conv2D(128, (3, 3), padding="valid", activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2),dim_ordering='th'))

model.add(Flatten())

model.add(Dense(64, activation='relu'))
model.add(Dropout(0.4))
#model.add(Dense(2, activation='softmax'))
model.add(Dense(2, W_regularizer=l2(0.01)))
model.add(Activation('linear'))

model.compile(loss = "hinge",
                    optimizer = SGD(lr=0.0001, momentum=0.9),
                    metrics=["accuracy"])
model.summary()