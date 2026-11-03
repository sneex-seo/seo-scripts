from google.cloud import translate
import os
import time
import csv

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "yourfilecredentials.json"

with open('translate.txt', 'r+', encoding='utf-8') as f:
    keywords = [line.strip() for line in f]


for words in keywords:
    time.sleep(0.1)
    print("Original word: " + words)

    try:
        translate_client = translate.Client()
        target = 'en' #choose language where you need to translate
        output = translate_client.translate(words, target_language=target)
        perevod = output['translatedText']
        print("Translated word: " + str(perevod))
        with open('translate_en.txt', 'a', encoding='utf-8') as result_file:
            result_file.write(perevod + '\n')
        
    except:
        print("No Translate")
        with open('translate_en.txt', 'a', encoding='utf-8') as result_file:
            result_file.write(perevod + '\n')