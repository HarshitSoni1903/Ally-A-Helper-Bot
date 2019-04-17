import librosa.display
import librosa
import os
import pandas as pd
import glob 
import keras
from keras.models import model_from_json
import pickle
import numpy as np
import matplotlib.pyplot as plt

json_file = open('speech/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

loaded_model.load_weights("speech/saved_models/Emotion_Voice_Detection_Model.h5")

opt = keras.optimizers.rmsprop(lr=0.00001, decay=1e-6)
loaded_model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

def findemo(aud):
    data, sampling_rate = librosa.load(aud)
    X, sample_rate = librosa.load(aud, res_type='kaiser_fast',duration=2.5,sr=22050*2,offset=0.5)
    sample_rate = np.array(sample_rate)
    mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=13),axis=0)
    featurelive = mfccs
    livedf2 = featurelive
    livedf2= pd.DataFrame(data=livedf2)
    livedf2 = livedf2.stack().to_frame().T
    twodim= np.expand_dims(livedf2, axis=2)
    livepreds = loaded_model.predict(twodim,batch_size=32,verbose=1)
    livepreds1=livepreds.argmax(axis=1)
    liveabc = livepreds1.astype(int).flatten()
    file=open('speech/lbsave.txt','rb')
    lb=pickle.load(file)
    file.close()
    livepredictions = (lb.inverse_transform((liveabc)))
    #print(livepredictions)
    return livepredictions

if __name__=="__main__":
    print(findemo("output1.wav"))