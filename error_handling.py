import settings
import random
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
	intents = discord.Intents.default()
	intents.message_content = True

	bot = commands.Bot(command_prefix="!", intents=intents)

	@bot.event
	async def on_ready():
		logger.info(f"User: {bot.user} (ID: {bot.user.id})")

	# To handle errors globally
	@bot.event
	async def on_command_error(ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send("handled error globally")

	# Adds 2 numbers together
	@bot.command()
	async def add(ctx, num1:float, num2:float):
		await ctx.send(num1 + num2)

	# # To handle errors locally
	# @add.error
	# async def add_error(ctx, error):
	# 	if isinstance(error, commands.MissingRequiredArgument):
	# 		await ctx.send("handled error locally")

	bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
	run()