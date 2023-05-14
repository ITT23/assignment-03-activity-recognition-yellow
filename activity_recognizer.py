import os
import pandas as pd
import re
import numpy as np
from sklearn import svm
from sklearn.preprocessing import scale, StandardScaler, MinMaxScaler

class Recognizer():

    def __init__(self):
        self.jumping_data = []
        self.lying_data = []
        self.waving_data = []
        self.classifier = None
        
    # reads all files named jumping, waving or lying and trains the classifier with them
    def train_classifier(self):
        
        files = os.listdir('data')

        # get jumping data
        for file in files:
            if(len(re.findall('jumping', file)) != 0):
                self.jumping_data.append(pd.read_csv(f'data/{file}'))

        # get waving data
        for file in files:
            if(len(re.findall('waving', file)) != 0):
                self.waving_data.append(pd.read_csv(f'data/{file}'))

        # get lying data
        for file in files:
            if(len(re.findall('lying', file)) != 0):
                self.lying_data.append(pd.read_csv(f'data/{file}'))

        # transforms the data in frequency domain
        jumping_frequencies =  get_frequencies(self.jumping_data)
        waving_frequencies =  get_frequencies(self.waving_data)
        lying_frequencies = get_frequencies(self.lying_data)

        # trains the classifier
        classifier =  train_model(jumping_frequencies, waving_frequencies, lying_frequencies)
        self.classifier = classifier
    
    # classifies the new data and returns a prediction
    def classify(self, data_x, data_y, data_z):
        # finds the dominant frequency for all three axis
        x = get_frequency(data_x)
        y = get_frequency(data_y)
        z = get_frequency(data_z)

        # transforms the data in a dataframe
        data_set = [x, y, z]
        columns = ['acc_x', 'acc_y', 'acc_z']
        dataframe = pd.DataFrame(data_set, index=columns)
        dataframe = dataframe.T

        # normalizes the data
        scaled = scaler.transform(dataframe[['acc_x', 'acc_y', 'acc_z']])
        
        # predicts the new motion
        predicted_motion = self.classifier.predict(scaled)

        return predicted_motion[0]
  
# extracts the frequencies of a given data frame
def get_frequencies(df):
        frequencies_x = []
        frequencies_y = []
        frequencies_z = []
        for data in df:
            frequencies_x.append(get_frequency(data.loc[:,'acc_x']))
            frequencies_y.append(get_frequency(data.loc[:, 'acc_y']))
            frequencies_z.append(get_frequency(data.loc[:, 'acc_z']))

        combined_data = [frequencies_x, frequencies_y, frequencies_z]
        columns = ['acc_x', 'acc_y', 'acc_z']
        transformed_data = pd.DataFrame(combined_data, index=columns)
        transformed_data = transformed_data.T
        transformed_data['class'] = df[0].loc[:, 'activity_label']
        return transformed_data

# transforms the data in frequency domain and finds the main frequency
def get_frequency(data):
    spectrum = np.abs(np.fft.fft(data))
    main_frequency = get_main_frequency(spectrum)
    main_frequency = main_frequency[0][-1]
    return main_frequency

# returns the position of the dominant frequency
def get_main_frequency(spectrum):
    highest_frequency = max(spectrum)
    return np.where(spectrum == highest_frequency)

# normalizes the data for training
def pre_process_data(data):
    global scaler
    scaler = MinMaxScaler()
    scaler.fit(data[['acc_x', 'acc_y', 'acc_z']])
    scaled_sample = scaler.transform(data[['acc_x', 'acc_y', 'acc_z']])
    data_scaled = data.copy()
    data_scaled[['acc_x', 'acc_y', 'acc_z']] = scaled_sample
    return data_scaled

# trains the SVM after normalizing the data
def train_model(jumping_frequencies, shaking_frequencies, lying_frequencies):
    frames = pd.concat([jumping_frequencies, shaking_frequencies, lying_frequencies], ignore_index=True)
    normalized_frames =  pre_process_data(frames)
    classifier = svm.SVC(kernel='rbf')
    classifier.fit(normalized_frames[['acc_x', 'acc_y', 'acc_z']], normalized_frames['class'])
    return classifier