# pybotgram
Telegram bot template in python-telegram-bot

## Start from here
* Clone this repo
* Edit bot_token in configs.telegram
* Install python-telegram-bot
```pip install python-telegram-bot```
* run your bot
```python run.py```

## Add new commands
* create new file with your command name in commands directory with start or say as template
* add to commands/__init__
* add to run with dp.add_handler(..)

## Add new dialog
* create new file in dialogs directory with hello as template
* add to dialogs/__init__
* add to dialogs/handler

## Utils?
In utils there are commonly used functions, mainly tools and dummy functions.  

### Dummy functions?
The dummy functions are functions that facilitate other functions.  
For example user.get_name(..) facilitates the taking of the name and surname if the username is not present.

## Add new utils
Each util should be part of the file that closes a set of functions.  
For example get_name is an executable function on the user so it is present in the user file. A function that takes the id of a chat is part of the up (update) file.
