import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

# Function to check if the user is allowed to call certain command
# Basically, it's a custom check
# async def is_owner(ctx):
# 	return ctx.author.id == ctx.guild.owner_id

class NotOwner(commands.CheckFailure):
	pass

def is_owner():
	async def predicate(ctx):
		if ctx.author.id != ctx.guild.owner_id:
			raise NotOwner("Hey you are not the owner")
		return True
	return commands.check(predicate)

def run():
	intents = discord.Intents.default()
	intents.message_content = True

	bot = commands.Bot(command_prefix="!", intents=intents)

	@bot.event
	async def on_ready():
		logger.info(f"User: {bot.user} (ID: {bot.user.id})")

	# Check uses a function as a parameter that returns true or false
	# if the person that calls the command is accepted or not
	# @bot.command()
	# @commands.check(is_owner)
	# async def say(ctx, what="WHAT"):
	# 	await ctx.send(what)

	# @bot.command()
	# # We could use a custom check, or in this case, use a default one
	# # Some examples are:
	# # commands.has_role()
	# # commands.has_permissions()
	# # commands.cooldown()
	# # commands.guild_only()
	# # commands.dm_only()
	# @commands.is_owner
	# async def say(ctx, what="WHAT"):
	# 	await ctx.send(what)

	@bot.command()
	@is_owner()
	async def say(ctx, what="WHAT"):
		await ctx.send(what)

	# Handle the error when a user that is not the owner of the server
	# tries to call the command say
	@say.error
	async def say_error(ctx, error):
		# Check if it's an instance of the custom class NotOwner we
		# created
		if isinstance(error, NotOwner):
			await ctx.send("Permission denied.")


	bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
	run()