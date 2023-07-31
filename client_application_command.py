import settings
import discord
from discord.ext import commands
from discord import app_commands

logger = settings.logging.getLogger("bot")

def run():
	intents = discord.Intents.default()
	intents.message_content = True
	intents.members = True

	bot = commands.Bot(command_prefix="!", intents=intents)

	@bot.event
	async def on_ready():
		logger.info(f"User: {bot.user} (ID: {bot.user.id})")
		logger.info(f"Guild ID: {bot.guilds[0].id}")

		# To copy all the command tree into the server faster
		bot.tree.copy_global_to(guild=settings.GUILD_ID)
		await bot.tree.sync(guild=settings.GUILD_ID)

	# Specifying a name lets us call the commands with that name instead of the
	# function name
	@bot.tree.command(description="Welcomes user", name="greetings")
	async def ciao(interaction: discord.Interaction):
		await interaction.response.send_message(f"Ciao {interaction.user.mention}!", ephemeral=True)

	bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
	run()