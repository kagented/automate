import speech_recognition as sr
import pprint
import os
import sys
import time

r = sr.Recognizer()

mic = sr.Microphone(device_index=1)
# pprint.pprint(sr.Microphone.list_microphone_names())

while True:
    with mic as source:
        print('찬양 제목을 말해주세요.')
        audio = r.listen(source)

    try:
        recorded = r.recognize_google(audio, language="ko-KR")

        text = recorded.replace(" ", "")

        if text == '완료':
            break

        else:

            #불러온 제목 검색

            dirname = r'C:\Users\USER\Desktop\예배곡ppt'

            dirlist = []


            for root, dirs, files in os.walk(dirname):
                for file in files:
                    if file.startswith(text):
                        dirlist.append(os.path.join(root, file))

            os.system('start "" "'+dirlist[0]+'""')
    except:
        print('잘 못 들었습니다.')
