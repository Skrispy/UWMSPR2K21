import tensorflow
import numpy as np
import matplotlib
import time
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Dense, Flatten, MaxPooling2D, Dropout
from matplotlib import pyplot
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import load_model

outcomes = 10
#load data into test and train sets
(x_train,y_train),(x_test,y_test)= fashion_mnist.load_data()
#for error analysis
(ox_train, oy_train), (ox_test, oy_test) = fashion_mnist.load_data()
#normalize images scaled [0,1] range
x_train = x_train.astype('float32')/255
x_test = x_test.astype('float32')/255
x_train = x_train.reshape(x_train.shape[0],28,28,1)
x_test = x_test.reshape(x_test.shape[0],28,28,1)


#convert class vectors
y_train = tensorflow.keras.utils.to_categorical(y_train,outcomes)
y_test = tensorflow.keras.utils.to_categorical(y_test,outcomes)

print(x_test.shape)
print(y_test.shape)

def m1 ():
    #build 1st
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
    s=time.time()
    m.fit(x_train,y_train,batch_size=128,epochs=10,verbose=1)
    e = time.time()
    print(e-s,"seconds")
    score = m.evaluate(x_test, y_test, verbose=0)
    print("Test Accuracy:", score[1])
    predictions = m.predict(x_test)
    m.save("model1.h5")

def m2 ():
    #build 2nd no droupout layer
    m = Sequential()
    m.add(Conv2D(64,kernel_size=(5,5), activation="relu", input_shape=(28,28,1)))
    m.add(Conv2D(32,(4,4),activation="relu"))
    m.add(MaxPooling2D(pool_size=(2,2)))
    m.add(Flatten())
    m.add(Dense(50,activation="relu"))
    m.add(Dense(outcomes,activation="softmax"))
    m.summary()
    #compile cnn
    m.compile(loss="categorical_crossentropy",optimizer="Adadelta",metrics=["accuracy"])

    #training
    s=time.time()
    m.fit(x_train,y_train,batch_size=128,epochs=10,verbose=1)
    e=time.time()
    print(e-s,"seconds")
    score = m.evaluate(x_test,y_test,verbose=1)
    print(score)
    print("Test Accuracy:", score[1])
    predictions = m.predict(x_test)
    m.save("model2.h5")

def m3 ():
    #build 1st
    m = Sequential()
    m.add(Conv2D(32,kernel_size=(3,3), activation="relu", input_shape=(28,28,1)))
    m.add(Conv2D(64,(4,4),activation="relu"))
    m.add(Dropout(0.3))
    m.add(Flatten())
    m.add(Dense(200,activation="relu"))
    m.add(Dense(outcomes,activation="softmax"))
    m.summary()
    #compile cnn
    m.compile(loss="categorical_crossentropy",optimizer="Adadelta",metrics=["accuracy"])

    #training
    s=time.time()
    m.fit(x_train,y_train,batch_size=128,epochs=10,verbose=1)
    e=time.time()
    t = e-s
    print(t, "seconds")
    score = m.evaluate(x_test,y_test,verbose=1)
    print(score)
    predictions = m.predict(x_test)
    print("Test Accuracy:", score[1])
    m.save("model3.h5")
    #Error Analysis 
    for i in range(len(predictions)) :
        predicted = np.argmax(predictions[i])
        if (predicted != oy_test[i]) :
            print("Predicted:",predicted," Correct: ",oy_test[i])
            pyplot.imshow(ox_test[i],cmap="gray")
            pyplot.show()
m1()
m2()
