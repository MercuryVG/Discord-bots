import discord
from selenium import webdriver
from selenium.webdriver.common.by import By
from discord.ext import commands
from bs4 import BeautifulSoup as bs 


client = commands.Bot(command_prefix = ":")

@client.command()
async def counter(ctx, hero1, hero2=''):
	driver = webdriver.Firefox(executable_path="path to your driver")
	if(hero2 == ''):
		driver.get(f"http://dotapicker.com/counterpick#!/E_{hero1}")
	else:
		driver.get(f"http://dotapicker.com/counterpick#!/E_{hero1}_{hero2}")
	html = driver.page_source
	soup = bs(html, features="html.parser")
	center_container = soup.find("div",  {'class':'heroSuggestionContainerScroll'})

	all_hearoes = center_container.find("div",  {'class':'heroSuggestionContainer'})
	carry_container = all_hearoes.find("div", {'class':'heroSuggestionContainerCoreUtil ng-scope'})
	hero_scope = carry_container.find("div", {'class':'ng-scope'})
	heroes_list = ""
	driver.quit()
	for hero in hero_scope.find_all("span",{'class':'inlineBlock vAlignMid ng-binding'})[:5:]:
		heroes_list += hero.text.replace('\t', '').replace('\n', '')
		heroes_list += '\n'
		
	await ctx.send(heroes_list)
	heroes_list = ""



client.run("your discord bot tocken")

