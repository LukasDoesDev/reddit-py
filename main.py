from PyInquirer import prompt
import requests
import sys, json
from functions import wait_key, openImage, getComments, get_post_with_id, create_post_string, post_is_image

subreddits = ['linuxmemes', 'memes', 'funny', 'teenagers', 'engrish']

subredditQuestion = {
    'type': 'list',
    'name': 'subreddit',
    'message': 'Subreddit',
    'choices': subreddits,
}

answers = prompt([subredditQuestion])
if answers == {}:
    sys.exit(1)

subreddit = answers['subreddit']
url = f'https://www.reddit.com/r/{subreddit}.json'

res = requests.get(url, headers={'User-agent': 'your bot 0.1'})

if res.status_code != 200:
    print(f'There was an error getting {url} {res.status_code}')
    if res.status_code == 404:
        print('404 Not Found')
    elif res.status_code == 429:
        print('429 Too Many Requests')
    sys.exit(1)


data = res.json()
posts = data['data']['children']
posts = list(map(lambda post: post['data'], posts))

if '--images-only' in sys.argv:
    posts = list(filter(post_is_image, posts))


# Only show 10 posts
del posts[10:]


posts_strings = list(map(create_post_string, posts))
post_answer = prompt([{
    'type': 'list',
    'name': 'list',
    'message': 'Do you want images only',
    'choices': posts_strings,
}])
if post_answer == {}:
    sys.exit(1)


post_id = post_answer['list'].split(' (id: t3_')[-1].split(')')[0]
post = get_post_with_id(post_id, posts)


print('post_id: ' + post_id)
print('Selected post: ' + post['title'])

if 'selftext' in post:
    content = post['selftext']
    content = content.replace('&amp;', '&')
    print('Selftext:')
    print(content)

if post_is_image(post):
    imageKey = "Press E to exit, C for comments and I for image"
else:
    imageKey = "Press E to exit and C for comments"

while True:
    print(imageKey)

    key = wait_key()

    if key == "e":
        sys.exit(0)
    elif post_is_image(post) and key == "i":
        openImage(post)
    elif key == "c":
        print ('NOT READY YET')
