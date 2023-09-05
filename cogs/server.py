import nextcord
import mcstatus
import asyncio

from python_aternos import Client
from mcstatus import BedrockServer
from nextcord.ext import commands
from nextcord import slash_command

aternos_username = ""
aternos_password = ""
ip = "server address"

async def bot_stats(bot:commands.Bot) -> nextcord.Embed:
	server = BedrockServer.lookup(ip)
	stat = server.status()
	stat:mcstatus.status_response.BedrockStatusResponse
	
	embed = nextcord.Embed(title="Server Status", color=nextcord.Color.green())
	
	embed.add_field(inline=False, name="server ping:", value=f"{int(stat.latency)}ms")
	embed.add_field(inline=False, name="server status:", value=stat.description)
	embed.add_field(inline=False, name="server version:", value=stat.version.name)
	embed.add_field(inline=False, name="server players:", value=f"{stat.players.online}/{stat.players.max}")
	
	return embed

class server(commands.Cog):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
	
	@slash_command(name="qoqnus-smp", description="send the latency of the bot")
	async def smp(self, ctx:nextcord.Interaction):
		pass
	
	@smp.subcommand(name="start", description="start Qoqnus SMP server")
	async def start(self, ctx:nextcord.Interaction):
		embed = nextcord.Embed(color=nextcord.Color.yellow())
		embed.add_field(inline=False, name="trying to start server...", value=f"")
		res = await ctx.response.send_message(embed=embed)
		try:
			atclient = Client()
			atclient.login(aternos_username, aternos_password)
			aternos = atclient.account
			serv = aternos.list_servers()[0]
			try:
				serv.start()
			except:
				embed = nextcord.Embed(colour=nextcord.Color.red())
				embed.add_field(inline=False, name="server is already starting or stoping or online", value="")
				await res.edit(embed=embed)
				return 
			for i in range(50):
				await res.edit(content="درحال روشن کردن سرور:", embed=await bot_stats(self.bot))
				await asyncio.sleep(3)
		except Exception as e:
			print(e)
			embed = nextcord.Embed(color=nextcord.Color.red())
			embed.add_field(inline=False, name="failed to start server", value="unexpected eror")
			await res.edit(embed=embed)
		
	@smp.subcommand(name="status", description="send Qoqnus SMP status")
	async def status(self, ctx:nextcord.Interaction):
		await ctx.response.send_message(embed=await bot_stats(self.bot))
	
def setup(bot:commands.Bot):
	bot.add_cog(server(bot))
