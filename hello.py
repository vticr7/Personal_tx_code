import time as t
import numpy as np
from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns
import csv
import matplotlib.pyplot as pylot
import statistics as st
api_key = 'AIzaSyDgqj4wCUTvAh48KvYAvHPgPqKDYM9LS0E'

youtube = build('youtube', 'v3', developerKey=api_key)


def get_video_stats(youtube):
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics", id="_B6T8O15Ohk")
    response = request.execute()
    data = dict(views=response['items'][0]["statistics"]["viewCount"])
    req_data = int(data['views'])
    return req_data


# for i in range(100):
#     with open("traddd.csv", 'a') as csvfile:
#         csvwriter = csv.writer(csvfile)
#         current_time = t.strftime("%H:%M:%S")
#         csvwriter.writerow([i, current_time, get_video_stats(youtube)])
#         print(str(current_time)+"  "+str(get_video_stats(youtube)))
#         csvfile.close()
#         t.sleep(60*3)


data = pd.read_csv("traddd.csv", error_bad_lines=False)
print(data.shape)
print(data.head())

y = data["Views"].values
x = data["Index"].values
mean_views_y = float(0)
mean_Index_x = 0

for i in range(len(x)-1):
    mean_views_y += y[i]/len(x)
    mean_Index_x += x[i]/len(x)


numer = 0
denom = 0
for i in range(len(x)-1):

    numer = numer+(x[i]-mean_Index_x)*(y[i]-mean_views_y)
    denom += (x[i]-mean_Index_x)**2
