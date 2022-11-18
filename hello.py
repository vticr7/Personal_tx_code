import time as t

from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns
import csv
api_key = 'AIzaSyDgqj4wCUTvAh48KvYAvHPgPqKDYM9LS0E'

youtube = build('youtube', 'v3', developerKey=api_key)


def get_video_stats(youtube):
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics", id="_B6T8O15Ohk")
    response = request.execute()
    data = dict(views=response['items'][0]["statistics"]["viewCount"])
    req_data = int(data['views'])
    return req_data








    with open("traddd.csv", 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        current_time = t.strftime("%H:%M:%S")
        csvwriter.writerow([i, current_time, get_video_stats(youtube)])
        print(str(current_time)+"  "+str(get_video_stats(youtube)))
        csvfile.close()
        t.sleep(60*3)
