from discord.ext import commands
from discord.ext import tasks
import os
import traceback
import discord
from datetime import datetime 

token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID =698653628176531478  #チャンネルID

# 接続に必要なオブジェクトを生成
client = discord.Client()

@client.event
async def on_ready():
    """起動時に通知してくれる処理"""
    print('ログインしました')
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')


# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    
    if now == '02:59':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:jhlo:700932650944299098>') 
    
    if now == '05:26':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:hello:699779689127870514> ') 
        
    if now == '07:26':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':sparkling_heart:')      
    
    if now == '09:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:ge:699792780725059664> ') 
        
    if now == '11:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':balloon::balloon::balloon: ') 

    if now == '13:11':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:gn:699792795363311676>  ')
    
    if now == '12:40':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:heart02:699580174911668225> <:gn:699792795363311676>  ')
          
    if now == '13:48':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('🥳')
        
    if now == '16:48':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('i am Dva:rabbit:')
        
    if now == '19:48':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('🥳:gift_heart:')
        
    if now == '22:48':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(':heartpulse:I :sparkling_heart: handsome:heartpulse:')
        
    if now == '23:59':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('🥳 💝')

  
#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(token)
