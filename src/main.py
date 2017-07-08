import discord
import logging
import asyncio
import os
import random

client = discord.Client()

@client.event
async def on_ready():
	print("Username: " + client.user.name)
	print("ID: " + client.user.id)
	
@client.event
async def on_message(message): 
	if(message.content.startswith("!img")):
		imgList = os.listdir("./ImgList") 
		imgString = random.choice(imgList)
		path = "./ImgList/" + imgString
		msg = await client.send_file(message.channel, path)

	if(message.content.startswith("!cag")):
		imgList = os.listdir("./ImgList") 
		path = "./ImgList/cag.png"
		msg = await client.send_file(message.channel, path)

	if(message.content.startswith("!doge")):
		imgList = os.listdir("./ImgList") 
		path = "./ImgList/doge.jpg"
		msg = await client.send_file(message.channel, path)
		

	if(message.content.startswith("!nichijou")):
		imgList = os.listdir("./ImgList") 
		path = "./ImgList/nichijou.gif"
		msg = await client.send_file(message.channel, path)
		
	if(message.content.startswith("!Quit")):
		client.logout()

client.run("MzExODg3OTc1NzQ5NTE3MzEz.C_T3qw.Ei3VoUAIkNIK4wW-2RyQiMFcxac")