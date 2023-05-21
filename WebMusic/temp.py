import pandas as pd

df = pd.read_csv("D:/Semester8/Final_Completed/ClassifiedMusicData.csv")

for i in df['id']:
    temp = str("https://open.spotify.com/embed/track/" + i + "?utm_source=generator")
    df['id'] = df['id'].replace(i, temp)

print(df['id'])

df.to_csv("temp.csv")

    