import token_discord
import discord
import time
from check_face import *
from discord.ext import commands
from discord.ext import tasks
import face_recognition
import cv2
import os
import numpy as np
global checking_end
checking_end=0

app=commands.Bot(command_prefix='!',intents=discord.Intents.all())

@app.event
async def on_ready():
    print('Done')
    await app.change_presence(status=discord.Status.online,activity=None)

async def check_face(ctx):
    global checking_end
    face_recog = FaceRecog()
    await ctx.send('Watchdog is online')
    print(face_recog.known_face_names)
    prev = time.time()

    while True:
        print(checking_end)
        if checking_end == 1:
            checking_end = 0
            break
        frame, count = face_recog.get_frame()
        if count == 1:  # if face is found, save as "cache.jpg"
            now = time.time()
            print(now - prev)
            if int(now - prev) > 10:
                if os.path.exists('./cache.jpg'):
                    os.remove('./cache.jpg')

                cv2.imwrite('./cache.jpg', frame)
                with open('./cache.jpg', 'rb') as f:
                    pic = discord.File(f)
                    await ctx.send(file=pic)
                    await ctx.send('Safety Alert!')
                prev = now
                os.remove('./cache.jpg')
    await ctx.send('Watchdog is now offline.')

@app.command()
async def start(ctx):
    global checking_end
    app.loop.create_task(check_face(ctx))

@app.command()
async def end(ctx):
    global checking_end
    checking_end=1
    print('finish')

app.run(token_discord.token_dis)