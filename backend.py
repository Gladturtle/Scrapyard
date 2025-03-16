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
        time.sleep(random.randint(0,3))
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

def play_music():
    
    player = vlc.MediaPlayer("sus_music.mp3")
    player.play()
def instatiate_model():
    ollama.pull(model='deepseek-r1')
    client = ollama.Client()
    client.create(model='Response_Gen',from_ = 'deepseek-r1', messages=[{'role':'system','content':'You are a response generator for a meme cat that randomly pops up. You can give nice and slightly snarky comments regarding the user\'s code.'}])

def generate_response():
    response_type = ['snarky','nice','funny']
    response = ollama.generate(model='Response_Gen',prompt=f"Generate a {response_type[random.randint(0,2)]} response")
    message = response['message']['content'][message.index('</think>')+10:]
    return message


  









