from discord.ext import commands

#
# Groups
#
@commands.group()
async def math(ctx):
	if ctx.invoked_subcommand is None:
		await ctx.send(f"No, {ctx.subcommand_passed} does not belong to simple")

#
# Commands
#
@math.command()
async def add(ctx, num1:float, num2:float):
	await ctx.send(num1 + num2)

@math.command()
async def substract(ctx, num1:float, num2:float):
	await ctx.send(num1 - num2)

@math.command()
async def divide(ctx, num1:float, num2:float):
	await ctx.send(num1 / num2)

@math.command()
async def multiply(ctx, num1:float, num2:float):
	await ctx.send(num1 * num2)

#
# Setup
#
async def setup(bot):
	# We can add the groups here
	bot.add_command(math)
	# We can also add the individual commands
	bot.add_command(add)