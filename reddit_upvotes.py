import praw
import csv


def main():
    r = praw.Reddit(user_agent='',
                    client_id='', client_secret='',
                    username='', password='')

    write_upvoted_to_csv(get_upvoted_posts(r))


def get_upvoted_posts(r):
    return r.user.me().upvoted(limit=None)

def write_upvoted_to_csv(upvoted_posts):
    with open('upvoted_posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
        field_names = ["Title", "Upvotes", "Subreddit", "URL"]
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()

        not_allowed_subreddits = ["funny", "Drugs", "tattoos", "generative", "aww", "memes", "nextfuckinglevel",
                                  "Damnthatsinteresting", "mildlyinteresting", "proceduralgeneration", "tookjustenough", "oddlysatisfying"]

        for l in upvoted_posts:
            if l.subreddit.display_name not in not_allowed_subreddits:
                try:
                    writer.writerow({field_names[0]: l.title, field_names[1]: l.ups,
                                     field_names[2]: l.subreddit.display_name, field_names[3]: f'www.reddit.com/{l.permalink}'})
                except Exception as e:
                    print(e)

if __name__ == '__main__':
    main()
