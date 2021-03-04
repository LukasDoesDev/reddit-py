from PyInquirer import prompt
import sys
from functions import wait_key, openImage, getComments, get_post_with_id, create_post_string, post_is_image, getSubredditPosts

subreddits = ['linuxmemes', 'memes', 'funny', 'teenagers', 'engrish']

subredditQuestion = {
    'type': 'list',
    'name': 'subreddit',
    'message': 'Subreddit',
    'choices': subreddits,
}

posts = getSubredditPosts(subredditQuestion)

while True:
    posts_strings = list(map(create_post_string, posts))
    post_select = {
        'type': 'list',
        'name': 'list',
        'message': 'Do you want images only',
        'choices': posts_strings,
    }

    post_answer = prompt([post_select])
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
        imageKey = "Press E to exit, S to select a subreddit, P to go back to selecting posts, C for comments and I for image"
    else:
        imageKey = "Press E to exit, S to select a subreddit, P to go back to selecting posts and C for comments"

    while True:
        print(imageKey)

        key = wait_key()

        if key == "e":
            sys.exit(0)
        elif post_is_image(post) and key == "i":
            openImage(post)
        elif key == "p":
            break
        elif key == "s":
            posts = getSubredditPosts(subredditQuestion)
            break
        elif key == "c":
            print ('NOT READY YET')
