# speech_bot
The project contains a Telegram bot code that allows you to convert text into an audio message. 
The bot does not know how to work with Cyrillic text, unfortunately.
:(

First, create your Telegram bot via BotFather (ex. Text2Voice) and get its token.
Create virtual environment.
Then create the requirements.txt file with required libraries list: python-telegram-bot and pyttsx3.
Install these libraries with “python pip install requirements.txt” command in Terminal.


Create folder "data/".
Create voice.py script, import there pyttsx3  and subprocess libraries.
Initiate engine by pyttsx3. Set voice and speech rate. 
Define text_to_file function there. Outputs will be saved in data/ folder.
Create bot.py script. Input your bot’s token there (not explicitly). Define help_handler and reply functions.
Run “python bot.py” command in venv. Go to your bot, input any text and enjoy its audio version.
:)


Add the project to git.
Add local ignores data/, *.mp3,  *.ogg  into .gitignore file.
