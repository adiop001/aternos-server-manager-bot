import nextcord
import keys

from pathlib import Path
from nextcord.ext import commands

bot = commands.Bot(
	command_prefix="$",
	intents= nextcord.Intents.all()
)

@bot.event
async def on_ready():
	print("bot is ready")

if __name__ == "__main__":
	for cog in Path("cogs").glob("*.py"):
		cog_name = cog.name.split(".")[0]
		bot.load_extension(f"cogs.{cog_name}")
		print("Loaded Extension:", cog_name)
	bot.run(keys.token)
