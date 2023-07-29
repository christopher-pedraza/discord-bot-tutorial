import settings
import random
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

class Slapper(commands.Converter):
	def __init__(self, *, use_nicknames) -> None:
		self.use_nicknames = use_nicknames

	async def convert(self, ctx, argument):
		someone = random.choice(ctx.guild.members).display_name
		
		if self.use_nicknames:
			nickname = ctx.author.display_name
		else:
			nickname = ctx.author

		return f"{nickname} slaps {someone} with {argument}"

def run():
	intents = discord.Intents.default()
	intents.message_content = True

	bot = commands.Bot(command_prefix="!", intents=intents)

	@bot.event
	async def on_ready():
		logger.info(f"User: {bot.user} (ID: {bot.user.id})")

	@bot.command()
	async def joined(ctx, who: discord.Member):
		await ctx.send(who.joined_at)

	@bot.command()
	async def slap(ctx, reason: Slapper(use_nicknames=True)):
		await ctx.send(reason)

	# Starts the bot. You need to supply the discord api secret
	bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
	run()