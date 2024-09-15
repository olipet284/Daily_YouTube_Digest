from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime, timedelta
import smtplib
import ssl
from html import unescape
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

y_day = str(datetime.now() - timedelta(days=2))
yesterday = y_day[:10] + 'T' + y_day[11:19] + 'Z'

body = ''

youtube = build('youtube', 'v3', developerKey=os.getenv('api_key'))

new_vid = False
stop = False
for channel in channels:
  if stop:
    break
  for duration in ["medium", "long"]:
    # 4min <= medium <= 20min
    # long >20min
    request = youtube.search().list(part="snippet",
                                    channelId=channel,
                                    order="date",
                                    publishedAfter=yesterday,
                                    type="video",
                                    videoDuration=duration)
    try:
      response = request.execute()
    except HttpError:
      stop = True
      print('Quota Exceeded')
      print('The following is the result thus far:')
      break

    for item in response['items']:
      new_vid = True
      channel_name = item['snippet']['channelTitle']
      video_title = unescape(item['snippet']['title'])
      video_id = item['id']['videoId']
      video_url = 'youtube.com/watch?v=' + video_id
      add_to_body = f'{channel_name}\n{video_title}\n{video_url}\n\n'
      print(add_to_body)
      body += add_to_body

if new_vid:
  msg = EmailMessage()
  msg['From'] = os.getenv['mail_from']
  msg['To'] = os.getenv['mail_to']
  msg['Subject'] = "Daily YouTube Digest"
  msg.set_content(body)
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(os.getenv['mail_from'], os.getenv['mail_key'])
    smtp.send_message(msg)
    smtp.quit()
  print('New videos have been sent to your email')
else:
  print('No new videos available')
