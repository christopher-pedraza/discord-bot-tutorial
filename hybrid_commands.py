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

		# We need to synchronize the commands with discord when
		# they are hybrid (that can be used with /)
		await bot.tree.sync()

	# To create a hybrid command, we use @bot.hybrid_command
	@bot.hybrid_command()
	async def ping(ctx):
		await ctx.send("pong!")

	# Another way to create a hybrid command
	@bot.tree.command()
	async def ciao(interaction: discord.Interaction):
		# Adding ephemeral makes the message be "Only you can see this. Dismiss message"
		await interaction.response.send_message(f"Ciao {interaction.user.mention}!", ephemeral=True)

	bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
	run()