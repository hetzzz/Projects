
from keras.backend import binary_crossentropy
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import Adam
import os
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras import utils
import random

#creating a test dataset
test_inst = ImageDataGenerator(rescale=1./255)

test = test_inst.flow_from_directory(directory="brain tumor dataset/splited dataset/test/",
target_size=(224,224),
class_mode="binary",
# classes=["Brain Tumor","Healthy"],
batch_size= 8,
color_mode="rgb",
shuffle=True,
)

#Loading a pretrained model
model = load_model("brain tumor dataset/models/")

#Evaluating the accuracy of model using test dataset
model.evaluate(test)

#Selecting a Random image from test dataset and predicting whether the MRI image has tumor or not
path = "brain tumor dataset/splited dataset/test_acc/"
# path = "brain tumor dataset/splited dataset/testingdata/"
# path = "brain tumor dataset/splited dataset/test_acc/Cancer (475).jpg"

images = os.listdir(path)

#selecting a random image path
d = random.choice(images)
print(d)
#loading the image using its path
img = image.load_img(path+''+d,target_size=(224,224))
# img = image.load_img(path+''+'Cancer (475).jpg',target_size=(224,224))
plt.imshow(img)
plt.show()
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array,axis = 0)
images = np.vstack([img_array])
val = model.predict(images)
print(val)
val1 = (model.predict(images) > 0.5).astype("int32")
print(val1)
if val1 == 0:
    print("MRI Image shows signs of tumor")
elif val1 == 1:
    print("MRI Image does not show any signs of tumor")
plt.imshow(img)
plt.show()


#Cancer (475).jpg