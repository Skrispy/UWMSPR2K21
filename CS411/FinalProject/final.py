import tensorflow as tf
import numpy as np
import matplotlib
import time
import os
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Dense, Flatten, MaxPool2D, Dropout
from matplotlib import pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from PIL import Image,ImageFilter

train_path = 'Data/Train'
test_path = 'Data/Test'
data = ImageDataGenerator(validation_split=0.2)
data_test = ImageDataGenerator(rescale=1/255)
train = data.flow_from_directory(train_path,classes=["Blank","Fist","Five","ThumbsUp","Two","Yo"],color_mode="grayscale",subset="training",class_mode="categorical",target_size=(200,200))
valid =data.flow_from_directory(train_path,classes=["Blank","Fist","Five","ThumbsUp","Two","Yo"],color_mode="grayscale",subset="validation",class_mode="categorical",target_size=(200,200))
test = data_test.flow_from_directory(test_path,color_mode="grayscale",class_mode="categorical",target_size=(200,200))

def testFold (path):
    for i in os.listdir(path):
        print(i)

#testFold(test_path)
#im = Image.open('Data/Test/Fist/IMG_5306.jpg')
#im.show()
def plotImages(images_arr):
    fig, axes = plt.subplots(1, 10, figsize=(20,20))
    axes = axes.flatten()
    for img, ax in zip( images_arr, axes):
        ax.imshow(img)
        ax.axis('off')
    plt.tight_layout()
    plt.show()

#imgs, labels = next(test)
#plotImages(imgs)
#print(labels)
def trainMod ():
    model = Sequential([
        Conv2D(filters=32, kernel_size=(3, 3), activation='relu', padding = 'same', input_shape=(200,200,1)),
        MaxPool2D(pool_size=(2, 2), strides=2),
        Conv2D(filters=64, kernel_size=(3, 3), activation='relu', padding = 'same'),
        MaxPool2D(pool_size=(2, 2), strides=2),
        Flatten(),
        Dense(units=6, activation='softmax')
    ])

    model.summary()
    model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(x=train,
        steps_per_epoch=len(train),
        validation_data=valid,
        epochs=10,
        verbose=1
    )
    score = model.evaluate(test,verbose=1)
    print(score)
    print("Test Accuracy:", score[1])

trainMod()