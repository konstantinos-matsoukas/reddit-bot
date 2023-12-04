import praw
import config

praw.Reddit(username = config.username, 
            password = config.password, 
            client_id = config.client_id, 
            client_secret = config.client_secret, 
            user_agent = "Nuggets test app v0.1")