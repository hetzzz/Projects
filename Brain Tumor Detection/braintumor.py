

from keras.backend import binary_crossentropy
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras import callbacks
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import Adam
import os
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Conv2D, MaxPool2D, LeakyReLU, BatchNormalization, Dropout, Dense, InputLayer, Flatten
from tensorflow.keras.losses import  BinaryCrossentropy
from tensorflow.keras import utils
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping

#Splitting dataset into train,test,validation
# input_folder = 'brain tumor dataset\Brain Tumor Data Set\Brain Tumor Data Set'
# sf.ratio(input_folder, output="brain tumor dataset\splited dataset",ratio=(.8,.1,.1),group_prefix=None)

#creating a datasets for training, validation and for testing the model

train_inst= ImageDataGenerator(rescale=1./255,dtype=tf.float32)
test_inst= ImageDataGenerator(rescale=1./255,dtype=tf.float32)
val_inst= ImageDataGenerator(rescale=1./255,dtype=tf.float32)

train = train_inst.flow_from_directory(directory='brain tumor dataset/splited dataset/train/' ,
target_size=(224,224),
class_mode="binary",
# classes=['Brain Tumor','Healthy'],
batch_size= 80,
color_mode="rgb",
shuffle=True,
)

test = test_inst.flow_from_directory(directory="brain tumor dataset/splited dataset/test/",
target_size=(224,224),
class_mode="binary",
# classes=["Brain Tumor","Healthy"],
batch_size= 8,
color_mode="rgb",
shuffle=True,
)

val = val_inst.flow_from_directory(directory="brain tumor dataset/splited dataset/val/",
target_size=(224,224),
class_mode="binary",
# classes=["Brain Tumor","Healthy"],
batch_size= 8,
color_mode="rgb",
shuffle=True,
)

#creating a simple CNN model
model = Sequential()
model.add(InputLayer(input_shape=(224,224,3)))
model.add(Conv2D(filters=32,kernel_size=3, activation="relu", padding="same"))
model.add(MaxPool2D())
model.add(Conv2D(filters=64,kernel_size=3, activation="relu", padding="same"))
model.add(MaxPool2D())

model.add(Flatten())

model.add(Dense(128, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(rate=0.3))
model.add(Dense(64, activation="relu"))
model.add(BatchNormalization())
model.add(Dropout(rate=0.3))
model.add(Dense(1, activation="sigmoid"))

model.compile(optimizer=Adam(0.001),loss = BinaryCrossentropy(),metrics=['accuracy'])

model.summary()

#plotting the model to show the details of each layer in png file
utils.plot_model(
    model, to_file='model.png', show_shapes=True,
    show_layer_names=True,
)

#saving model if the value of loss decreases during each epoch
checkpoint =  callbacks.ModelCheckpoint("brain tumor dataset/",monitor='val_loss',verbose=2,save_best_only=True,save_weights_only=False,mode = 'min',save_freq= 'epoch')

#to stop the training early if the loss doesnt decrease.
earlystop = callbacks.EarlyStopping(monitor='val_loss', patience=5, verbose=2, mode='min',restore_best_weights=True)

#fitting the model
history =  model.fit(train,verbose=1,callbacks = [earlystop,checkpoint],epochs=10,validation_data=(val))


#Plotting a Training and Validation Accuracy of the model
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.show()

#Plotting a Training and Validation loss of the model
plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label = 'val_loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.show()

#Saving the trained model.
model.save("brain tumor dataset/models/")

#Evaluating the models accuracy using test dataset
model.evaluate(test)
print(model.evaluate(test))

# model.predict()
# loaded_model = models.load_model("brain tumor dataset/")
# a = loaded_model.predict(val)
# print(a)



