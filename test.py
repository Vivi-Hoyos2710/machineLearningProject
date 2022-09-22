# -*- coding: utf-8 -*-
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
from tensorflow import keras
from PIL import Image
import numpy as np


json_config_path = 'C:\\Users\\vivia\\Desktop\\virtualEnvPip\\ml_model\\model_config.json'
weights_path = 'C:\\Users\\vivia\\Desktop\\virtualEnvPip\\ml_model\\pets_xception_transferlearning.h5'
file_path = 'C:\\Users\\vivia\\Desktop\\virtualEnvPip\\data\\sedita.jpeg'
with open(json_config_path) as json_file:
  json_config = json_file.read()
model = keras.models.model_from_json(json_config)
model.load_weights(weights_path)

image = tf.keras.preprocessing.image.load_img(file_path,target_size =
(150,150,3))
input_arr = tf.keras.preprocessing.image.img_to_array(image)
input_arr = np.array([input_arr]) # Convert single image to a batch.

pred = tf.keras.activations.sigmoid(model.predict(input_arr))
if pred < 0.5:
  label ='cat'
  prob = 1-pred
else:
  label ='dog'
  prob = pred
print(f'The pet is a {label} with probability {prob}')