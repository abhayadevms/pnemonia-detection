#from __future__ import absolute_import, division, print_function, unicode_literals
import os
import shutil
import tempfile
import sys
from time import sleep
import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
IMAGE_SIDE = 450  # We have to resize the dataset images to reduce memory consumption

# get the current working directory
current_dir = os.getcwd()

#MODEL_PATH = os.path.join(current_dir, "/home/dev/Desktop/project/phenomia_toch/pneumonia_classifier_model.h5")
MODEL_PATH ="/home/dev/Desktop/project/phenomia_toch/pneumonia_classifier_model.h5"

def trained_model(download_anyway=False):
    model = tf.keras.models.load_model(MODEL_PATH, custom_objects=None, compile=True)
    print("Model loaded.")
    return model


# create an image generator for the uploaded images
def create_image_generator(dir_name):
    print("Creating image generator for images in directory: ", dir_name)
    image_generator = ImageDataGenerator(rescale=1. / 255)
    data_gen = image_generator.flow_from_directory(
        directory=str(dir_name),
        target_size=(IMAGE_SIDE, IMAGE_SIDE),
        color_mode="grayscale")#,
        #class_mode=None)  # class_mode has to be None to indicate there are no data labels
    return data_gen


# Round the prediction to a human-readable interpretation
def interpret_prediction(prediction):
    print("Prediction is:  {}".format(prediction))
    pred_list = prediction[0].tolist()
    max_index = pred_list.index(max(pred_list))
    if max_index == 0:
        print("NORMAL")
    else:
        print("PNEUMONIA")


# # print usage
# def print_usage():
#     print("predict_xray.py chest_xray_image")
#
#
# # get the full path to the image file argument
# def get_arg_path(image_file):
#     if not os.path.exists(image_file):
#         return os.path.join(current_dir, image_file)


model = trained_model()
temp_dir_name = "/home/dev/Desktop/project/phenomia_toch/chest-xray-pneumonia/chest_xray/train/NORMAL/IM-0115-0001.jpeg"
# # preprocess uploaded images
image_gen = create_image_generator(temp_dir_name)
prediction = model.predict(image_gen)
interpret_prediction(prediction)
