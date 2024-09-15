# Daily YouTube Digest

A simple script that searches for new videos among a list of channelIds, and sends an email containing the new videos.

Using [Google Takeout](https://takeout.google.com) you can download a file with all your subscriptions, that contains their channelId and name. This is converted to a list (printed in the terminal) with the code in $\verb|youtube_takeout.py|$.

You can insert the entire code into Pipedream to run the script daily at a given time, using [this template](https://pipedream.com/new?h=tch_Evfb0B).

The additional files $\verb|email_search.py|$ and $\verb|youtube_download.py|$ were created as a means to reducing the amount of time spent browsing YouTube, by means of either searching for topics in the terminal and then recieving a mail, and to download the videos through using the urls, rather than using the web app.
