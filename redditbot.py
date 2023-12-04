import praw
import config
import time

def bot_login():
    praw.Reddit(username = config.username, 
                password = config.password, 
                client_id = config.client_id, 
                client_secret = config.client_secret, 
                user_agent = "Nuggets test app v0.1")
    return r

def run_bot(r):
    print ("obtaining comments")

    comments_replied_to = []

    for comment in r.subreddit('test').comments(limit=25):
        if "dog" in comment.body:
            print ("test")
            comment.reply("test response")
            print ("responded")
            comments_replied_to.append(comment.id) 

    time.sleep(10)


r = bot_login()
while True:
    run_bot(r)