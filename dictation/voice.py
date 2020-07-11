import speech_recognition as sr
import pprint

r = sr.Recognizer()

mic = sr.Microphone(device_index=1)
# pprint.pprint(sr.Microphone.list_microphone_names())
with mic as source:
    print('say something')
    audio = r.listen(source)
    print('recording finished')

recorded = r.recognize_google(audio, language="ko-KR")

print(recorded.replace(" ", ""))

