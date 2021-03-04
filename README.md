# reddit-py

> Browse Reddit on the command line!

## Installation:
```sh
# Install virtualenv globally
pip install virtualenv

# Create a new virtual enviroment
virtualenv venv

# Activate the virtual enviroment
# You should see "(venv)" appear before your prompt
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```
## Usage:

### How to get back to the venv to update requirements, run script, etc:
- Type `source venv/bin/activate` in the terminal.

### How to run reddit-py:
- Make sure you're in the virtual enviroment
- Type `python main.py` in the terminal.
- If you want to only get posts with images, add the `--images-only` flag to the end of the command

### How to exit venv:
- Type `deactivate` in the terminal.

## Features:
- Opens images in sxiv if you press I in the console window (if there is an image)
- Shows description if there is one
- Go back to select a new post without restarting the program by pressing P
- Go back to select a new subreddit without restarting the program by pressing S
- Open comments by pressing C (TODO)
