import settings
import discord
from discord.ext import commands

def run():
    intents = discord.Intents.default()
    bot = commands.Bot(command_prefix="!", intents=intents)

    # Event that is trigged the moment the bot is ready
    @bot.event
    async def on_ready():
        print(bot.user, bot.user.id)

    # Starts the bot. You need to supply the discord api secret
    bot.run(settings.DISCORD_API_SECRET)

if __name__ == "__main__":
    run()