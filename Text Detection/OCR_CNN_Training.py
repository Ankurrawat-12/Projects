import numpy as np
import cv2
import os
from sklearn.model_selection import train_test_split
from keras.layers import Dense, Dropout, Flatten
from tensorflow.keras import Adam
from keras.models import Sequential
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from keras.utils.np_utils import to_categorical

# Settings
path = "myData"
test_ratio = 0.2
validation_ratio = 0.2
images = []
classNo = []
imageDimensions = (64, 64, 3)


my_list = os.listdir(path)
print("Total No Of Classes Detected "+str(len(my_list)))
noOfClasses = len(my_list)
print("Importing Classes .....")
for x in range(0, noOfClasses):
    myPicList = os.listdir(path + "/" + str(x))
    for y in myPicList:
        curImg = cv2.imread(path + "/" + str(x) + "/" + y)
        curImg = cv2.resize(curImg, (imageDimensions[0], imageDimensions[1]))
        images.append(curImg)
        classNo.append(x)

    print(x, end=" ")
print()

images = np.array(images)
classNo = np.array(classNo)
print(images.shape)

X_train, X_test, y_train, y_test = train_test_split(images, classNo, test_size=test_ratio)
X_train, X_validation, y_train, y_validation = train_test_split(X_train, y_train, test_size=validation_ratio)

print(X_train.shape)
print(X_test.shape)
print(X_validation.shape)

numberOfSamples = []

for x in range(0, noOfClasses):
    numberOfSamples.append(len(np.where(y_train == x)[0]))

print(numberOfSamples)


plt.figure(figsize=(10, 5))
plt.bar(range(0, noOfClasses), numberOfSamples)
plt.title("No Of Images For Each Class")
plt.xlabel("Class ID")
plt.ylabel("No Of Images")
plt.show()


def preProcessing(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    img = img/255
    return img


# img = X_train[30]
# img = cv2.resize(img, (300, 300))
# cv2.imshow(" PreProcessed", img)
# cv2.waitKey(0)
# print(X_train[30].shape)
# print(X_train[30].shape)

X_train = np.array(list(map(preProcessing, X_train)))
X_test = np.array(list(map(preProcessing, X_test)))
X_validation = np.array(list(map(preProcessing, X_validation)))


X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], X_train.shape[2], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], X_test.shape[2], 1)
X_validation = X_validation.reshape(X_validation.shape[0], X_validation.shape[1], X_validation.shape[2], 1)

dataGen = ImageDataGenerator(width_shift_range=0.1,
                             height_shift_range=0.1,
                             zoom_range=0.2,
                             shear_range=0.1,
                             rotation_range=10)

dataGen.fit(X_train)


y_train = to_categorical(y_train, noOfClasses)
y_test = to_categorical(y_test, noOfClasses)
y_validation = to_categorical(y_validation, noOfClasses)


def myModel():
    noOfFilters = 60
    sizeOfFilter1 = (5, 5)
    sizeOfFilter2 = (3, 3)
    sizeOfPool =(2,2)
    noOfNode = 500

    model = Sequential()
    model.add((Conv2D()))


