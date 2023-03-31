# import random
# print(random.randint(0,9))

from playsound import playsound 



import time

myseconds=int(input("Enter the time in seconds "))

def countdown(seconds):
    while seconds>0:
        min=int(seconds/60)
        sec=int(seconds%60)
        timer=f"{min}:{sec}"

        print(timer)
        time.sleep(1)
        seconds-=1
    print("timer")
    playsound("mixkit-sound.wav")



countdown(myseconds)