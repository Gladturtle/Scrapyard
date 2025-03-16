import psutil
import random
import time
import os
import vlc 
import ollama

def detection():
    while True:
        while True:
            running = "Code.exe" in [p.name() for p in psutil.process_iter()]
            if running == True:
                break
        time.sleep(random.randint(0,300))
        running = "Code.exe" in [p.name() for p in psutil.process_iter()]
        if running == True:
            return True
        else:
            continue

def randomize_cood(minx,miny,maxx,maxy):
    x = random.randint(minx,maxx)
    y = random.randint(miny,maxy)
    return (x,y,y+50)

def randomize_deg():
    return random.randint(-80,80)
def randomize_img():
    return os.listdir('./data/')[random.randint(0,4)]
def randomize_song():
    return os.listdir('./music/')[random.randint(0,3)]

def play_music():
    
    player = vlc.MediaPlayer(f"./music/{randomize_song()}")
    player.play()
def instatiate_model():
    ollama.pull(model='deepseek-r1')
    client = ollama.Client()
    client.create(model='Response_Gen',from_ = 'deepseek-r1', messages=[{'role':'system','content':'You are a meme that randomly pops up. You give snarky comments regarding the user\'s code and the user themselves.'}])

def generate_response():
    response_type = ['snarky','diabolical','fun']
    response = ollama.generate(model='Response_Gen',prompt=f"Generate a personal,hard-hitting {response_type[random.randint(0,2)]} roast in English only. Strictly under 20-25 words. Do not introduce yourself,do not start sentences with 'Sure! Here's a roast for you' or any other introductory line. The user is a human writing code on his/her laptop. You are a meme cat that randomly appears and roasts them.")
    message = response['response']
    message = response['response'][message.index('</think>')+10:]
    return message


  








