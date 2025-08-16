import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# 載入 .env 裡的 TOKEN
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# 設定機器人
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} 已上線！")

# 測試指令
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(TOKEN)
