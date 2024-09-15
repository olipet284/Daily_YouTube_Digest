# Daily YouTube Digest


email_search.py was thought as a way of reducing the amount of time spent browsing YouTube, by means of searching for topics in the terminal and then recieving a mail (in order to watch videos on certain topics later on and having all YouTube videos within the mail inbox).

Using <takeout.google.com> you can download a file with all subscriptions, that contains their channelId, and name. This is converted to a list (printed in the terminal) with the code in youtube_takeout.py, in order to insert the code into Pipedream, where a daily trigger can automatically run the entire code. You can use the following template <https://pipedream.com/new?h=tch_Evfb0B>
