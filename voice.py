import pyttsx3, subprocess

engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-60)
engine.setProperty("voice", '[] HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')



# ffmpeg -i test.mp3 -c:a libopus test_out.ogg
# ["ffmpeg", '-i', audio_path_wav, '-acodec', 'libopus', audio_path_ogg, '-y']



def text_to_file(text):
    mp3_file = f'data/test.mp3'
    out_file = f'data/test_out.ogg'
    engine.save_to_file(text, mp3_file)
    engine.runAndWait()
    subprocess.run(["ffmpeg", '-i', mp3_file, '-acodec', 'libopus', out_file, '-y'])
    return out_file



# text_to_file('Hi, I\'m a message')
