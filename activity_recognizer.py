import os
import pandas as pd
import re
import numpy as np
# install scikit-learn
from sklearn import svm
from sklearn.preprocessing import scale, StandardScaler, MinMaxScaler

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

def get_frequency(data):
    spectrum = np.abs(np.fft.fft(data))
    main_frequency = get_main_frequency(spectrum)
    main_frequency = main_frequency[0][0]
    return main_frequency

def get_main_frequency(spectrum):
    highest_frequency = max(spectrum)
    return np.where(spectrum == highest_frequency)

def pre_process_data(data):
    global scaler
    scaler = MinMaxScaler()
    scaler.fit(data[['acc_x', 'acc_y', 'acc_z']])
    scaled_sample = scaler.transform(data[['acc_x', 'acc_y', 'acc_z']])
    data_scaled = data.copy()
    data_scaled[['acc_x', 'acc_y', 'acc_z']] = scaled_sample
    return data_scaled

def train_model(jumping_frequencies, shaking_frequencies, lying_frequencies):
    frames = pd.concat([jumping_frequencies, shaking_frequencies, lying_frequencies], ignore_index=True)
    normalized_frames =  pre_process_data(frames)
    classifier = svm.SVC(kernel='rbf')
    classifier.fit(normalized_frames[['acc_x', 'acc_y', 'acc_z']], normalized_frames['class'])
    return classifier



class Recognizer():

    def __init__(self):
        self.jumping_data = []
        self.lying_data = []
        self.waving_data = []
        self.classifier = None
        

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

        try:
            jumping_frequencies =  get_frequencies(self.jumping_data)
            waving_frequencies =  get_frequencies(self.waving_data)
            lying_frequencies = get_frequencies(self.lying_data)
            classifier =  train_model(jumping_frequencies, waving_frequencies, lying_frequencies)
            self.classifier = classifier
        except:
            print('data folder is empty')
        
    def classify(self, data_x, data_y, data_z):
        x = get_frequency(data_x)
        y = get_frequency(data_y)
        z = get_frequency(data_z)

        data_set = [x, y, z]
        columns = ['acc_x', 'acc_y', 'acc_z']
        dataframe = pd.DataFrame(data_set, index=columns)
        dataframe = dataframe.T

        scaled = scaler.transform(dataframe[['acc_x', 'acc_y', 'acc_z']])
        
        predicted_motion = self.classifier.predict(scaled)

        return predicted_motion[0]

    
