import token_discord
import discord
from discord.ext import commands

intents=discord.Intents.all()
intents.message_content=True
intents.members=True
intents.typing=True
intents.presences=True

app=commands.Bot(command_prefix='!',intents=discord.Intents.all())

@app.event
async def on_ready():
    print('Done')
    await app.change_presence(status=discord.Status.online,activity=None)

@app.command()
async def hello(ctx):
    await ctx.send('Hello I am a Bot!')

@app.command()
async def pic(ctx):
    with open('./cache.jpg','rb') as f:
        pic=discord.File(f)
        await ctx.send(file=pic)
        await ctx.send('File send checked')

print(token_discord.token_dis)
app.run(token_discord.token_dis)