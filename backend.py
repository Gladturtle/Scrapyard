import psutil
import random
import time
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

def randomize(minx,miny,maxx,maxy):
    x = random.randint(minx,maxx)
    y = random.randint(miny,maxy)
    return (x,y,y+50)









