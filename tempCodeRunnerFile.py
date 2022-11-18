if (i != 0):
            f = open("traddd.csv")
            f.writerow([i, current_time, get_video_stats(youtube)])

            f.close()