import smtplib
import ssl
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from html import unescape
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

search_input = str(input('What do you want to see?\n'))

body = ''

youtube = build('youtube', 'v3', developerKey=os.path['api_key'])

no_issues = True
for duration in ["medium", "long"]:
  # 4min <= medium <= 20min
  # long >20min
  request = youtube.search().list(
      part="snippet",
      q=search_input,
      maxResults=2,
      order="relevance",  # Alternative: "viewCount" # "rating"
      type="video",
      videoDuration=duration)
  try:
    response = request.execute()
  except HttpError:
    print('Quota Exceeded')
    no_issues = False
    break

  for item in response['items']:
    new_vid = True
    channel_name = item['snippet']['channelTitle']
    video_title = unescape(item['snippet']['title'])
    video_id = item['id']['videoId']
    video_url = 'youtube.com/watch?v=' + video_id
    body += f'{channel_name}\n{video_title}\n{video_url}\n\n'

if no_issues:
  msg = EmailMessage()
  msg['From'] = os.getenv['mail_from']
  msg['To'] = os.getenv['mail_to']
  msg['Subject'] = "YouTube Search Request"
  msg.set_content(body)
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(os.getenv['mail_from'], os.getenv['mail_key'])
    smtp.send_message(msg)
    smtp.quit()
  print('Videos have been sent to your email')
