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

		# Gets the files from the CMDS_DIR (declared in settings.py) and
		# iterate over them
		for cmd_file in settings.CMDS_DIR.glob("*.py"):
			# If the file is not __init__.py, which is not a commands file
			if cmd_file.name != "__init__.py":
				# Add the files remove the `.py` from their names
				await bot.load_extension(f"cmds.{cmd_file.name[:-3]}")


	bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
	run()