# Emoji-Based Music Recommendation Using Convolutional Neural Networks
AbstractThe human face is an important organ of the human body, and it is especially important in determining an individual's behaviour and emotional state. Music is an excellent medium for self-expression as well as a source of entertainment for music fans and listeners. Developing a system by considering the above two factors that are capable  of  identifying  the  emotion  and  recommending  music improves user retention and performance.
 The software uses convolutional neural network approaches to collect information from the user's face in an attempt to identify the emotion  they  are  attempting  to  convey.  Based  on  the  emojis captured, clustering techniques are used to forecast the music and suggest it to the user.

<q>
To recommend a song that will never let you down or ruin your mood, and that will make your time as valuable as possible
</q>

## Objectives
1. In order to retain users and engage new ones.
2. Enhance  the  performance  of  the  music recommendation systems
3. Obtain the user's intentions without any input from the  user
4. Instant music recommendation.
5. Using  cutting-edge  approaches  to  determine the emotional state of the user
6. Aids  in  the  advancement  of  human  mental health (research)

## Proposed System
![image](https://github.com/SomuTech/Emotion-based-Music-Recommendation-ML/assets/77001358/d58ce033-58e1-4290-92f7-5f73c3f4f3d7)

## Project Modules
### Emotion  Extraction  Module :
The    image    of    the    user    is    captured    with    the    help    of    acamera/webcam.    Once    the    picture    captured,    the    frame    of    thecaptured  image  from  webcam feed is  converted to a grayscale image  toimprove  the performance of the  classifier, which is used to identify theface emotion present in the picture.
### Song Classification Module :
A list a songs are collected using Spotify API, these songs are clusteredbased on different attributes such as soundability, intensity, pitch, rhythmetc, and classified as sad, energetic, happy, romantic etc.
### Emotion-Audio Integration Module :
The  emotions  which  are  extracted  for the  songs  are stored, and thesongs based on the emotion are displayed on the web page built usingDjango framework.  For  example,  if  the  emotion  or  the  facial  feature  iscategorized    under    happy,    then  songs  from  the  happy  database  aredisplayed to the user.

## Result
![image](https://github.com/SomuTech/Emotion-based-Music-Recommendation-ML/assets/77001358/2126c9e3-cf5a-4866-a960-a648126685be)

## Video
https://youtu.be/LovDYBhr888?si=NSV0OvSEeEvGKl0d







