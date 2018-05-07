import numpy as np
import wfdb as wf
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv1D, MaxPooling1D
from keras.utils import np_utils
import pylab as plt
matplotlib.use('Agg')
np.set_printoptions(suppress=True)


# import original_data as dp
import data_preprocessing as dp

tmp = dp.makeData(9, 0.7)
trainD, trainL, testD, testL = tmp.main()
# print(trainD.shape)
# print(trainL.shape)
# print(testD.shape)
# print(testL.shape)

trainData = trainD.reshape((trainD.shape[0], trainD.shape[1], 1))
trainLabel = np_utils.to_categorical(trainL, 4)
testData = testD.reshape((testD.shape[0], testD.shape[1], 1))
testLabel = np_utils.to_categorical(testL, 4)

print(trainData.shape)
print(trainLabel.shape)
print(testData.shape)
print(testLabel.shape)


model = Sequential() 
model.add(Conv1D(filters = 512, kernel_size = 3, input_shape = (trainData.shape[1], 1), activation = "relu"))
model.add(MaxPooling1D(pool_size = 100))
model.add(Flatten())
model.add(Dense(4, activation = "softmax"))
print(model.summary())

model.compile(optimizer ='adam', loss = "categorical_crossentropy", metrics=['accuracy'])
model.fit(x = trainData, y = trainLabel, epochs=10,validation_split=0.2, batch_size=100, verbose=2)
model.evaluate(x = testData, y = testLabel)
