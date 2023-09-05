import nextcord

from nextcord.ext import commands
from nextcord import slash_command

class ping(commands.Cog):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
	
	@slash_command(name="ping", description="send the latency of the bot")
	async def ping(self, ctx:nextcord.Interaction):
		await ctx.response.send_message(f"pong🏓\nping of bot is: {int(self.bot.latency * 1000)}ms")

def setup(bot:commands.Bot):
	bot.add_cog(ping(bot))
