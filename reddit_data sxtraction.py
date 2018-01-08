#Defining the important libraries

import requests
import json
import config
import praw
import csv
import sys
from datetime import datetime
import pandas as pd


#Definig the function for Praw package with required credentials present in config file to make a call to Reddit API 

def reddit_feed():
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "Swappy9 feed")
    return r

r = reddit_feed()

#Defining the Required headers required

header1 = ['Data Source', 'ID', 'User_Id', 'Screen_Name', 'User_Name', 'Original Source', 'Language',
           'Time', 'Date', 'Time_Zone', 'Location', 'City', 'State', 'Country', 'Share_Count', 'Favorite_Count',
           'Comment_Count', 'URL', 'Description', 'Headlines', 'Text']


#Checking the CSV file if it contains the header, if not copying the headers to the csv file otherwise move forward

with open('Reddit1.csv', 'a', newline='', encoding='utf-8') as csvfile:
    #writer = csv.writer(csvfile)
    if csvfile.seek(0) in (None, "", 0):
        writer = csv.writer(csvfile)
        writer.writerows([header1])
                
    else:
        pass

csvfile.close()


#Making the call to the API with "Atlanta" as a keyword and limit of the data to 1000
#Saving the required data into the csv file in respective columns

def run_reddit(r):
    for submission in r.subreddit('Atlanta').new(limit=1000):
        li = []
        parsed_DateTime = datetime.utcfromtimestamp(submission.created_utc)

        li.extend(('Reddit', submission.id, submission.id, submission.author, submission.author, submission.domain,
                  'NA', parsed_DateTime.time(), parsed_DateTime.date(), 'UTC', 'NA',
                   'NA', 'NA', 'NA', 'NA', submission.score, submission.num_comments,
                  submission.url, submission.link_flair_text, 'NA', submission.title, submission.view_count))
        with open('Reddit1.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows([li])

        csvfile.close()

   

run_reddit(r)


