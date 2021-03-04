import sys, os, subprocess, json
import requests
from PyInquirer import prompt

def wait_key():
    ''' Wait for a key press on the console and return it. '''
    result = None
    if os.name == 'nt':
        import msvcrt
        result = msvcrt.getch()
    else:
        import termios
        fd = sys.stdin.fileno()

        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)

        try:
            result = sys.stdin.read(1)
        except IOError:
            pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

    return result

def openImage(post):
    imgRes = requests.get(post['url'])
    filename = post['url'].split('/')[-1]

    temp_location = '/tmp/'
    file_location = temp_location + filename

    with open(file_location, 'wb') as output_file:
        output_file.write(imgRes.content)
    
    subprocess.run(['sxiv', file_location])
    os.remove(file_location)

def getComments(post):
    url = f'https://www.reddit.com{post["permalink"]}.json'

    res = requests.get(url, headers={'User-agent': 'your bot 0.1'})

    if res.status_code != 200:
        print(f'There was an error getting {url} {res.status_code}')
        if res.status_code == 404:
            print('404 Not Found')
        elif res.status_code == 429:
            print('429 Too Many Requests')
        sys.exit(1)

    data = res.json()

    comments = data[1]['data']['children']

    return comments


def get_post_with_id(id, posts):
    def post_id_eq(post):
        return post['name'] == 't3_' + id
    return list(filter(post_id_eq, posts))[0]


def create_post_string(post):
    text = f'{post["title"]} by u/{post["author"]}'
    if post['archived']:
        text += ' (ARCHIVED)'
    if post['pinned']:
        text += ' (PINNED)'
    if post['spoiler']:
        text += ' (SPOILER)'
    if post['over_18']:
        text += ' (NSFW)'
    return text + f' (id: {post["name"]})'

def post_is_image(post):
    if 'post_hint' in post:
        return post['post_hint'] == 'image'
    else:
        return False

def getSubredditPosts(subredditQuestion):
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

    return posts
