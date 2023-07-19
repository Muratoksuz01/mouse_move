import pyautogui
import GPUtil
from time import sleep
import random
def get_gpu_temperature():
    gpus = GPUtil.getGPUs()
    gpu_temperature = gpus[0].temperature
    return gpu_temperature
def move_mouse(x,y):
    pyautogui.moveTo(x,y)

temp=get_gpu_temperature()
while  temp <50:
    x,y=random.randint(500,750),random.randint(600,800)
    move_mouse(x,y)
    sleep(5)
    temp=get_gpu_temperature()
    print(temp)
