import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
	intents = discord.Intents.default()
	intents.message_content = True
	# Needed to search for the user that calls the command
	intents.members = True

	bot = commands.Bot(command_prefix="!", intents=intents)

	@bot.event
	async def on_ready():
		logger.info(f"User: {bot.user} (ID: {bot.user.id})")

	
	@bot.command()
	async def ping(ctx):
		# If we have the user in the context, we can send a dm like this:
		# await ctx.message.author.send("Pong")
		
		# This is another method, in which we get from the list of members of the 
		# server the user with the display name "Gabalix", and sends to that user
		# the dm
		user = discord.utils.get(bot.guilds[0].members, display_name="Gabalix")
		if user:
			await user.send("Pong")

	bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
	run()