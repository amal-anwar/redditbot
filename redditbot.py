import praw
import time

reddit = praw.Reddit(
    client_id='clientid',
    client_secret = 'secretykey',
    user_agent='console:nicobot:1.0',
    username='username',
    password='password')


subreddit = reddit.subreddit("formuladank")

nico_quote = ["NIIIICOOOOOOOO HUUUUUUUULKENBERRRRGGGGGG"]

for submission in subreddit.hot(limit=10):
    for comment in submission.comments:
        if hasattr(comment,"body"):
            comment_lower = comment.body.lower()
            if " hulkenberg " in comment_lower:
                print("----------")
                print(comment.body)
                comment.reply(nico_quote)
                time.sleep(660)
