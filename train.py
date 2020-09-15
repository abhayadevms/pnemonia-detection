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
#from sklearn import  svm
from keras.optimizers import SGD
from imutils import paths
from keras.callbacks import ModelCheckpoint



DEV = False
argvs = sys.argv
argc = len(argvs)

if argc > 1 and (argvs[1] == "--development" or argvs[1] == "-d"):
  DEV = True

if DEV:
  epochs = 2
else:
  epochs = 20


img_width, img_height = 240, 240
batch_size =8
samples_per_epoch =25
validation_steps = 100
nb_filters1 = 32
nb_filters2 = 64
conv1_size = 2
conv2_size = 2
pool_size = 2
classes_num = 2
BS = 8
img_width, img_height = 240, 240
train_data_dir ="/home/dev/Desktop/project/phenomia_toch/chest-xray-pneumonia/chest_xray/chest_xray/train"
validation_data_dir = "/home/dev/Desktop/project/phenomia_toch/chest-xray-pneumonia/chest_xray/chest_xray/val"
test_data_dir = "/home/dev/Desktop/project/phenomia_toch/chest-xray-pneumonia/chest_xray/chest_xray/test"
NB = 2
BS = 16
optimizer = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)

TRAIN = len(list(paths.list_images(train_data_dir)))
VAL = len(list(paths.list_images(validation_data_dir)))
TEST = len(list(paths.list_images(test_data_dir)))

model = Sequential()
model.add(Conv2D(16, (3, 3), activation='relu', padding="same", input_shape=(240, 240,3))) ### feature  extr
model.add(Conv2D(16, (3, 3), padding="same", activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2),dim_ordering='th'))

model.add(Conv2D(32, (3, 3), activation='relu', padding="same", input_shape=(240, 240,3)))
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

model.add(Dense(64, activation='relu'))                                                        ###feature extr
model.add(Dropout(0.4))
#model.add(Dense(2, activation='softmax'))                                                    ##svm
model.add(Dense(2, W_regularizer=l2(0.01)))
model.add(Activation('linear'))

#model.add(Dense(classes_num, W_regularizer=l2(0.01)))
#model.add(Activation('linear'))

##model.compile(loss='categorical_crossentropy',
#              optimizer=adam(0.0004),
 #             metrics=['accuracy'])    ###RMSprop(lr=lr)

early = EarlyStopping(monitor = 'val_acc', min_delta = 0,
                      patience = 10, verbose= 1 , mode = 'auto')
model.compile(loss = "hinge",
                    optimizer = SGD(lr=0.0001, momentum=0.9),
                    metrics=["accuracy"])                                              ###svm

# checkpoint


trainAug = ImageDataGenerator(rescale = 1./255,
                    fill_mode = "nearest")

valAug = ImageDataGenerator(rescale = 1./255,
                            fill_mode = "nearest")

trainGen = trainAug.flow_from_directory(
                    train_data_dir,
                    target_size = (img_height, img_width),
                    batch_size = BS,
                    shuffle = True,
                    class_mode = "categorical")

valGen = valAug.flow_from_directory(
                    validation_data_dir,
                    target_size = (img_height, img_width),
                    batch_size = BS,
                    shuffle = False,
                    class_mode = "categorical")

testGen = valAug.flow_from_directory(
                    test_data_dir,
                    target_size = (img_height, img_width),
                    batch_size = BS,
                    shuffle = False,
                    class_mode = "categorical")

#model.compile(loss = "categorical_crossentropy",
 # #                  optimizer = SGD(lr=0.0001, momentum=0.9),
   #                 metrics=["accuracy"])
filepath="/home/abhayadev/Desktop/phenomia_toch/model_wgt/weights-improvement-{epoch:02d}-{val_acc:.2f}.h5"
checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
callbacks_list = [checkpoint]

H = model.fit_generator(
        trainGen,
        epochs = 100,
        steps_per_epoch = TRAIN // BS,
        validation_data = valGen,
        validation_steps = VAL // BS,
        callbacks=callbacks_list)#verbose=1)
        #callbacks = [early])
#################################################################################################################################


