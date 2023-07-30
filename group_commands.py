import settings
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

	# Main group
	@bot.group()
	async def math(ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send(f"No, {ctx.subcommand_passed} does not belong to math")

	# Subgroup inside math
	@math.group()
	async def simple(ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send(f"No, {ctx.subcommand_passed} does not belong to simple")
	
	# Commands inside simple, which is inside math
	@simple.command()
	async def add(ctx, num1:float, num2:float):
		await ctx.send(num1 + num2)
	@simple.command()
	async def substract(ctx, num1:float, num2:float):
		await ctx.send(num1 - num2)
	@simple.command()
	async def divide(ctx, num1:float, num2:float):
		await ctx.send(num1 / num2)
	@simple.command()
	async def multiply(ctx, num1:float, num2:float):
		await ctx.send(num1 * num2)


	bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
	run()