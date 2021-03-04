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
- Opens images in sxiv
- Shows description if there is one
- Open comments by pressing C