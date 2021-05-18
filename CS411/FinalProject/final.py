import tensorflow as tf
import numpy as np
import matplotlib
import time
import os
import itertools
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Dense, Flatten, MaxPool2D, Dropout,BatchNormalization,Activation
from matplotlib import pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from PIL import Image,ImageFilter
from sklearn.metrics import confusion_matrix

#trail one
train_path = 'Data/Train'
test_path = 'Data/Test'
data = ImageDataGenerator(rescale=1/255, validation_split=0.2)
data_test = ImageDataGenerator(rescale=1/255)
train = data.flow_from_directory(train_path,classes=["Blank","Fist","Five","ThumbsUp","Two","Yo"],color_mode="grayscale",subset="training",class_mode="categorical",target_size=(200,200),batch_size=20)
valid =data.flow_from_directory(train_path,classes=["Blank","Fist","Five","ThumbsUp","Two","Yo"],color_mode="grayscale",subset="validation",class_mode="categorical",target_size=(200,200),batch_size=20)
test = data_test.flow_from_directory(test_path,classes=["Blank","Fist","Five","ThumbsUp","Two","Yo"],color_mode="grayscale",class_mode="categorical",target_size=(200,200),batch_size=20)
#build test

#trial 2
unstruct_path = "Data/Combo"
data2 = ImageDataGenerator(rescale=1/255, validation_split=0.1)
train2 = data2.flow_from_directory(unstruct_path,classes=["Blank","Fist","Five","ThumbsUp","Two","Yo"],color_mode="grayscale",subset="training",class_mode="categorical",target_size=(200,200),batch_size=20)
test2 = data2.flow_from_directory(unstruct_path,classes=["Blank","Fist","Five","ThumbsUp","Two","Yo"],color_mode="grayscale",subset="validation",class_mode="categorical",target_size=(200,200),batch_size=20)

#build model -1 for no validation set
def trainMod1 (data,valid,output):
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
    s=time.time()
    if(valid != -1):
        model.fit(x=data,
            steps_per_epoch=len(data),
            validation_data=valid,
            validation_steps=len(valid),
            epochs=10,
            verbose=1
        )
    else :
        model.fit(x=data,
            steps_per_epoch=len(data),
            epochs=10,
            verbose=1
        )

    e=time.time()
    t = e-s
    print(t, "seconds")
    model.save(output+".h5")
    return model

#trainMod(train,valid,"hands")

#build model2 (more advanced cnn) -1 for no validation set
def trainMod2 (data,valid,output):
    model = Sequential()
    model.add(Conv2D(filters = 32, kernel_size = (5,5),padding = 'Same', 
                 activation ='relu', input_shape = (200,200,1)))
    model.add(Conv2D(filters = 32, kernel_size = (5,5),padding = 'Same', 
                 activation ='relu'))
    model.add(MaxPool2D(pool_size=(2,2)))
    model.add(Dropout(0.25))
    model.add(Conv2D(filters = 64, kernel_size = (3,3),padding = 'Same', 
                    activation ='relu'))
    model.add(Conv2D(filters = 64, kernel_size = (3,3),padding = 'Same', 
                    activation ='relu'))
    model.add(MaxPool2D(pool_size=(2,2), strides=(2,2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(256, activation = "relu"))
    model.add(Dropout(0.5))
    model.add(Dense(6, activation = "softmax"))

    model.summary()
    model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])
    s=time.time()
    if(valid != -1):
        model.fit(x=data,
            steps_per_epoch=len(data),
            validation_data=valid,
            validation_steps=len(valid),
            epochs=10,
            verbose=1
        )
    else :
        model.fit(x=data,
            steps_per_epoch=len(data),
            epochs=10,
            verbose=1
        )

    e=time.time()
    t = e-s
    print(t, "seconds")
    model.save(output+".h5")
    return model

#trainMod2(train,valid,"hands3")
#trainMod2(train2,-1,"hands4")

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
            horizontalalignment="center",
            color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


#load in test set and model name
def eval (t,m):
    mod = tf.keras.models.load_model(m)
    score = mod.evaluate(x=t,steps=len(t),verbose=1)
    print(score)
    print("Test Accuracy:", score[1])
    predictions = mod.predict(x=t,steps=len(t),verbose=1)
    rounded = np.round(predictions)
    print(rounded)
    #confusuin matrix
    cm = confusion_matrix(y_true=t.classes,y_pred=np.argmax(predictions,axis=-1))
    cm_plot_labels=['Blank','Fist','Five','ThumbsUp','Two','Yo']
    plot_confusion_matrix(cm=cm, classes=cm_plot_labels, title='Confusion Matrix')
    plt.show()

#eval(test2,"hands4.h5")


#tools used for troubleshooting/building
'''
#indevidual image testing 

for i in range(0,44):
    img = image.load_img(test_path+"/"+str(i)+".jpg" ,target_size=(200,200))
    plt.imshow(img)
    plt.show()

    X= image.img_to_array(img)
    X= np.expand_dims(X,axis=0)
    images = np.vstack([X])
    val = model.predict(images)
    if val == 0:
        print('Blank')
    elif val == 1:
        print('Fist')
    elif val == 2:
        print('Five')
    elif val == 3:
        print("Thumbs Up")
    elif val == 4:
        print("Two")
    elif val == 5:
        print("Yo")
'''

#testing
'''
train_imgs, train_labels = next(train)
valid_imgs, valid_labels = next(valid)
test_imgs, test_labels = next(test)
print(test_labels.shape)
print(train_labels.shape)
print(valid_labels.shape)
print(len(train))
'''
#built np array for test data
test2_arr = []
batch_index = 0

while batch_index <= test2.batch_index:
    data = test2.next()
    test2_arr.append(data[0])
    batch_index = batch_index + 1

# now, data_array is the numeric data of whole images
test2_nparr = np.asarray(test2_arr)


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
