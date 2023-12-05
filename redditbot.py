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

def run_bot(r,comments_replied_to):
    print ("obtaining comments")


    for comment in r.subreddit('subreddit').comments(limit=25) and comment.id not in comments_replied_to and comment.author != user.me():
        if "dog" in comment.body:
            print ("test")
            comment.reply("test response")
            print ("responded")
            comments_replied_to.append(comment.id) 

    time.sleep(10)
#file func
def get_saved_comments():
    with open("comments_replied_to.txt",r)as f:
        comments_replied_to = f.read()
        comments_replied_to = comments_replied_to.split("\n")
        
    return comments_replied_to

r = bot_login()

comments_replied_to = []
while True:
    run_bot(r,comments_replied_to)