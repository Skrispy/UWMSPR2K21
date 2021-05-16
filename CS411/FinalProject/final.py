import tensorflow
import numpy as np
import matplotlib
import time
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Dense, Flatten, MaxPooling2D, Dropout
from matplotlib import pyplot
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator

data = ImageDataGenerator()
train = data.flow_from_directory('/Data/Train',classes=["Blank","Fist","Five","ThumbsUp","Two","Yo"] class_mode="categorical",target_size=(200,200))
