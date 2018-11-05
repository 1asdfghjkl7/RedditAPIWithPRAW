import praw

reddit = praw.Reddit(client_id='INSERT_CLIENT_ID',
                     client_secret="INSERT_CLIENT_SECRET", user_agent='INSERT_ANY_NAME')


def grabapi(string=""):
    arrayofarticles = []
    objectofarticles = {
        "hits": arrayofarticles
    }
    keys = ['title', 'url']
    if string:
        for submission in reddit.subreddit("all").search(query=string, sort='relevance', syntax='lucene',
                                                         time_filter='all',
                                                         limit=11):
            boi = [submission.title, "https://reddit.com" + submission.permalink]
            arrayofarticles.append(dict(zip(keys, boi)))

    if not string:
        for submission in reddit.subreddit("programming").hot(limit=11):
            boi = [submission.title, "https://reddit.com" + submission.permalink]
            arrayofarticles.append(dict(zip(keys, boi)))
    return objectofarticles
