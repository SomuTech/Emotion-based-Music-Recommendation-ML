from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

import cv2
import os
from time import sleep
import numpy as np
import pandas as pd
# import seaborn as sns

from keras.models import load_model 
# import matplotlib.pyplot as plt
# from tensorflow.keras.preprocessing.image import load_img



emotion_model = load_model("app/face_emotion.h5")   
mood_music = pd.read_csv("app/musicData.csv")
mood_music = mood_music.drop(['danceability',  'acousticness',  'liveness',  'loudness',  'speechiness'],axis=1)
# for i in range(len(mood_music['id'])):
#     mood_music.at[i,'id']= str("https://open.spotify.com/track/"+ mood_music['id'][i])
#     print(mood_music.at[i,'id'])
def music_results(n):
    if(n==0 or n==1 or n==2 ):
        #for angery,disgust,fear
        filter1=mood_music['mood']=='Chill'
        f1=mood_music.where(filter1)
        f1=f1.dropna()
        f2 =f1.sample(n=10)
        f2.reset_index(inplace=True)
        return f2
    if(n==3 or n==4):
        #for happy, neutral
        filter1=mood_music['mood']=='energetic'
        f1=mood_music.where(filter1)
        f1=f1.dropna()
        f2 =f1.sample(n=10)
        f2.reset_index(inplace=True)
        return f2
    if(n==5):
           #for Sad
        filter1=mood_music['mood']=='cheerful'
        f1=mood_music.where(filter1)
        f1=f1.dropna()
        f2 =f1.sample(n=10)
        f2.reset_index(inplace=True)
        return f2
    if(n==6):
         #for surprise
        filter1=mood_music['mood']=='romantic'
        f1=mood_music.where(filter1)
        f1=f1.dropna()
        f2 =f1.sample(n=10)
        f2.reset_index(inplace=True)
        return f2

def index(request):

    emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}
    emoji_dist={0:"app/emojis/angry.png",2:"app/emojis/disgusted.png",2:"app/emojis/fearful.png",3:"app/emojis/happy.png",4:"app/emojis/neutral.png",5:"app/emojis/sad.png",6:"app/emojis/surpriced.png"}

    key = cv2.waitKey(1)
    webcam = cv2.VideoCapture(0)
    sleep(2)

    while True:
        try:
            check, image = webcam.read()

            cv2.imshow("Capturing", image)
            key = cv2.waitKey(1)
            if key == ord('s'):
                print("cap===============================")
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                faceCascade = cv2.CascadeClassifier("C:/Users/somas/AppData/Local/Programs/Python/Python310/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
                faces = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.3,
                    minNeighbors=3,
                    minSize=(30, 30)
                )
            
                for (x, y, w, h) in faces:
                    print("loop-====================================")
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    roi_color = image[y:y + h, x:x + w]
                    gray = cv2.cvtColor(roi_color, cv2.COLOR_BGR2GRAY)
                    img_ = cv2.resize(gray,(48,48))
                    cv2.imwrite('static/req_img.jpg', img_)
            
                    # image = cv2.imread('static/req_img.jpg',cv2.IMREAD_GRAYSCALE)

                    # plt.imshow(img_,cmap='gray')
                    # plt.show()
                    
                    image = cv2.resize(img_,(48,48))
                    img=np.array(image)
                    img=img.reshape(1,48,48,1)
                    predict_x=emotion_model.predict(img)
                    result=np.argmax(predict_x,axis=1)
                    print(emotion_dict[result[0]])
                    
                    emoji=cv2.imread(emoji_dist[result[0]])
                    # plt.imshow(emoji)
                    # plt.show()
                    
                    info = music_results(result[0])
                    
                    print(info)
                    # print(info['id'])
                    
                    json_records = info.reset_index().to_json(orient ='records')
                    data = []
                    data = json.loads(json_records)
                    
            elif key == ord('q'):
                webcam.release()
                cv2.destroyAllWindows()
                break
                           
        except(KeyboardInterrupt):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break
    context = {
        "data" : data,
        "mood" :  emotion_dict[result[0]]
    }
    # https://open.spotify.com/track/1y1dgeOmBEjdaU5Quj9rOS
    
    # https://open.spotify.com/track/1y1dgeOmBEjdaU5Quj9rOS
    return render(request, 'index.html',context)