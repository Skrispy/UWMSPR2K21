import tensorflow
import numpy as np
import matplotlib
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Dense, Flatten, MaxPooling2D, Dropout
from matplotlib import pyplot
from tensorflow.keras.datasets import fashion_mnist

outcomes = 10
#load data into test and train sets
(x_train,y_train),(x_test,y_test)= fashion_mnist.load_data()
#normalize images scaled [0,1] range
x_train = x_train.astype('float32')/255
x_test = x_test.astype('float32')/255
x_train = x_train.reshape(x_train.shape[0],28,28,1)
x_test = x_train.reshape(x_train.shape[0],28,28,1)
print(x_train.shape)

#convert class vectors
y_train = tensorflow.keras.utils.to_categorical(y_train,outcomes)
y_test = tensorflow.keras.utils.to_categorical(y_test,outcomes)

#build cnn
m = Sequential()
m.add(Conv2D(32,kernel_size=(4,4), activation="relu", input_shape=(28,28,1)))
m.add(Conv2D(64,(3,3),activation="relu"))
m.add(MaxPooling2D(pool_size=(2,2)))
m.add(Dropout(0.2))
m.add(Flatten())
m.add(Dense(128,activation="relu"))
m.add(Dense(outcomes,activation="softmax"))

m.summary()
#compile cnn
m.compile(loss="categorical_crossentropy",optimizer="Adadelta",metrics=["accuracy"])

#training
m.fit(x_train,y_train,batch_size=128,epochs=5,verbose=1)