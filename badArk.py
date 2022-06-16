# Author:    Rogers Kelamen
# Fork from: https://github.com/CallMeToProgram/Bad-Apple
# Bilibili:  https://www.bilibili.com/video/BV1pT411G71A
# GitHub:    https://github.com/Rogerskelamen/Bad-Ark
# Mail:      1368180921@qq.com

import pygame
import time
import curses
from pathlib import Path
import convert

# video and bgm path
VIDEO_PATH = "data/bad-ark.mp4"
BGM_PATH = "data/bgm.mp3"

# frame rate of video
FRAME_RATE = 1 / 30


if Path("video_data.py").exists():
    from video_data import video_data
else:
    if not Path(VIDEO_PATH).exists():
        print("视频不存在: ", VIDEO_PATH)
    video_data = convert.write(VIDEO_PATH)
    input("\n转换完成, 按任意键继续...")

if not Path(BGM_PATH).exists():
    print("音乐不存在: ", BGM_PATH)

count = 0

stdsrc = curses.initscr()
curses.start_color()
stdsrc.resize(50, 150)

pygame.mixer.init()
track = pygame.mixer.music.load(BGM_PATH)
pygame.mixer.music.play()
time.sleep(0.4)
now = time.time()

for frame_data in video_data:
    for i in range(len(frame_data)):
        stdsrc.addstr(i, 0, frame_data[i], curses.COLOR_WHITE)
    while time.time() - now < count * FRAME_RATE:
        time.sleep(count * FRAME_RATE - time.time() + now)
    stdsrc.refresh()
    count += 1

curses.endwin()
