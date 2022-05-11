import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs

client = commands.Bot(command_prefix= ":")

@client.command()
async def counter(ctx, *, hero_name):
	hero_name = hero_name.split(" ")
	hero_name = "-".join(hero_name)
	driver = webdriver.Firefox(executable_path="C:\\Users\\rty35\\Documents\\code\\geckodriver.exe")
	driver.get(f"https://ru.dotabuff.com/heroes/{hero_name.lower()}/counters")
	html = driver.page_source
	driver.quit()
	try:
		soup = bs(html, features="html.parser")
		section = soup.find("section", {"class": "counter-outline"})
		heroes = section.find('table').find("tbody")
		send_string = "-------------------------"
		for hero in heroes:
			counter = 0
			for fields in hero:
				if counter == 1:
					send_string += '\n' + fields.text + '\n'
					counter += 1
					continue
				elif counter == 2:
					send_string += "Невыгодное положение " + fields.text + '\n'
					counter += 1
					continue
				elif  counter == 3:
					send_string += "Винрейт персонажа " + fields.text + '\n'
					send_string += "-------------------------"
					break
				counter += 1
	except:
		await ctx.reply("Sorry, no such hero found. Check spelling!", mention_author=False)
		return
	await ctx.reply(send_string, mention_author=False)
	send_string = ""

client.run("your discord token")
	