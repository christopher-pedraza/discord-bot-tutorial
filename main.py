import settings
import random
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    # Event that is trigged the moment the bot is ready
    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

    @bot.command(
        aliases = ["p"],
        # Description of the command when using `!help ping`
        description = "This is description",
        # Help of the command when using `!help ping`
        help = "This is help",
        # Brief description of the command when you just use help
        brief = "This is brief",
        # Lets you enable/disable the command
        enabled = True,
        # Lets you hide the command from the help list without disabling it
        hidden = True
    )
    # ctx: context
    # ctx contains information such as the message, channel, guild, etc.
    async def ping(ctx):
        """ Answers with pong """
        await ctx.send("pong")

    # Chooses a random option from the list supplied
    @bot.command()
    async def choose(ctx, *options):
        await ctx.send(random.choice(options))

    # Adds 2 numbers together
    @bot.command()
    async def add(ctx, num1:float, num2:float):
        await ctx.send(num1 + num2)

    @bot.command()
    # Each separate word is a parameter, so for example with:
    # !say Hello World
    # If we only have the parameters ctx and user_input, we would only be
    # getting Hello in the user_input. Thus, we are declaring that we'll
    # receive multiple parameters with *, and joining them with a space
    async def say(ctx, *user_input):
        await ctx.send(" ".join(user_input))

    # Starts the bot. You need to supply the discord api secret
    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()