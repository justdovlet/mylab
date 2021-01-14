import time
import discord
from discord.ext import commands
import random

unit_to_multiplier = {
    1: "Подписывайтесь на мой инстаграм: just_pillow",
    2: "Надеюсь никто не обижает Довлетика",
    3: "Уже появились календари на 2021 год. Оптимизм издателей просто зашкаливает",
    4: "Во мне любви столько, сколько хлопка",
    5: "Мне кажется, что Довлет прячет от меня другую подушку. Дайте знать, если увидите",
    6: "*звуки милой подушки*",
    7: "Поприколу можете проскролить замечательные картиночки тута https://vk.com/samephotoeveryday",
    8: "У меня аллергия на негатив... ХАПЧИИИ",
    9: "Если еще не видели, посмотрите анонс Portal 2. Габен оч постарался https://www.youtube.com/watch?v=pBziwcBpO1Q"
}

unit_to_multiplier2 = {
	1: "- Бронежилет",
	2: "играет с пяти лет",
	3: "ест бургер на обед",
	4: "- Омлет",
	5: "любитель конфет",
	6: "влез по уши в интернет",
	7: "- Скелет",
	8: "- Валет",
	9: "- Кастет"
}

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
		print( 'BOT connected ')

@client.command(pass_context = True)
async def say(ctx):
		x=random.randint(1, 9)
		await ctx.send (unit_to_multiplier[x])

@client.command(pass_context = True)
async def dovlet(ctx):
		y=random.randint(1, 9)
		await ctx.send ("Довлет "+unit_to_multiplier2[y])

@client.command(pass_context = True)
async def photo(ctx):
		await ctx.send ("https://cdn.discordapp.com/attachments/717843368561999885/732021762283274240/EO2fwitmqVQ.png")

@client.command(pass_context = True)
async def info(ctx):
		await ctx.send (".say - Фразочки \n.dovlet - Рифмы Довлета \n.photo - Фото Довлета")

@client.command(pass_context = True)
async def speak(ctx):
		while 1==1:
			await ctx.send (input())
			

#client = MyClient()
client.run("PUT YOUR API KEY")