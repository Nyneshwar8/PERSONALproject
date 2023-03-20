import speech_recognition as sr
from gtts import gTTS
import playsound
import translators as ts
import os


# convert speech to text - English
def melania_listen_en():
    # create recognizer
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # use the listen function so the recognizer can catch the source (our microphone)
        audio = r.listen(source)
        text = r.recognize_google(audio, language='en')

    text = text.lower()
    return text


# convert speech to text - German
def melania_listen_de():
    # create recognizer
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # use the listen function so the recognizer can catch the source (our microphone)
        audio = r.listen(source)
        text = r.recognize_google(audio, language='de')

    text = text.lower()
    return text


# convert text to speech - English
def melania_talk_en(text):
    # create audio
    file_name = 'audio_data.mp3'
    # convert text to speech
    tts = gTTS(text=text, lang='en')
    # save file
    tts.save(file_name)
    # play file
    playsound.playsound(file_name)
    # remove file
    os.remove(file_name)


# convert text to speech - Hindi
def melania_talk_hi(text):
    # create audio
    file_name = 'audio_data.mp3'
    # convert text to speech
    tts = gTTS(text=text, lang='hi')
    # save file
    tts.save(file_name)
    # play file
    playsound.playsound(file_name)
    # remove file
    os.remove(file_name)


# convert text to speech - Russian
def melania_talk_ru(text):
    # create audio
    file_name = 'audio_data.mp3'
    # convert text to speech
    tts = gTTS(text=text, lang='ru')
    # save file
    tts.save(file_name)
    # play file
    playsound.playsound(file_name)
    # remove file
    os.remove(file_name)


# convert text to speech - Spanish
def melania_talk_es(text):
    # create audio
    file_name = 'audio_data.mp3'
    # convert text to speech
    tts = gTTS(text=text, lang='es')
    # save file
    tts.save(file_name)
    # play file
    playsound.playsound(file_name)
    # remove file
    os.remove(file_name)


# translator english-spanish
def translator_en_es(text):
    melania_talk_es(ts.google(text, from_language='en', to_language='es'))


# translator english-hindi
def translator_en_hi(text):
    melania_talk_hi(ts.google(text, from_language='en', to_language='hi'))


# translator german-russian
def translator_de_ru(text):
    melania_talk_ru(ts.google(text, from_language='de', to_language='ru'))


# create a function which will give us back a reply based on the input text
def melania_reply(text):
    # translator
    global melania_run
    if 'translate' in text:

        while True:

            melania_talk_en(
                'I will choose the right translator for you. Let me know the source language and the target language.')
            source_target_lang = melania_listen_en()
            print(source_target_lang)

            # english - spanish
            if 'english to spanish' in source_target_lang:
                melania_talk_en('Got it, you need a translator from English to Spanish. What can I translate for you?')
                while True:
                    text_to_translate = melania_listen_en()
                    print(text_to_translate)

                    if text_to_translate != 'switch translator':
                        translator_en_es(text_to_translate)
                    else:
                        break

            # german - russian
            elif 'german to russian' in source_target_lang:
                melania_talk_en('Got it, you need a translator from German to Russian. What can I translate for you?')
                while True:
                    text_to_translate = melania_listen_de()
                    print(text_to_translate)

                    if text_to_translate != 'übersetzer wechseln':
                        translator_de_ru(text_to_translate)
                    else:
                        break

            # english - hindi
            elif 'english to hindi' in source_target_lang:
                melania_talk_en('Got it, you need a translator from English to Hindi. What can I translate for you?')
                while True:
                    text_to_translate = melania_listen_en()
                    print(text_to_translate)

                    if text_to_translate != 'switch translator':
                        translator_en_hi(text_to_translate)
                    else:
                        break

            elif 'turn off translator':
                melania_talk_en('It was a pleasure to do the translation job. Wish you a great day!')
                break

            # else:
            #     melania_talk_en('Sorry, I did not get what you said')


    else:
        melania_talk_en('Sorry, I can not support you with that.')

        def melania_run():
            melania_talk_en('Hi there. Nice to meet you. I am Melania, your personal translator. What is your name?')
            listen_name = melania_listen_en()
            melania_talk_en('Hi ' + listen_name + ' how can I help you?')

            listen_assistant = melania_listen_en()
            print(listen_assistant)
            melania_reply(listen_assistant)

    melania_run()


aa = melania_listen_de()
print(aa)

translator_de_ru('Ich machete in den Supermarket gehen')
