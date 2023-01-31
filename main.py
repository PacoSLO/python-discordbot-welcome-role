from discord.ext import commands
import discord
intents = discord.Intents.default()
intents.members = True
from discord.utils import get

# Just add your desired prefix there.
bot = commands.Bot(command_prefix='!', intents=intents)
ROLE = "YOUR SERVER ROLE"

#Bot status
@bot.event
async def on_ready():  # This function is run upon the bots startup completing
    # os.system('cls')
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    print("Status: Running")
    print("########################################")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="CHANGE THIS TO YOU LIKING"))

#Role assign and welcome msg     
@bot.event
async def on_member_join(member):
    role = get(member.guild.roles, name=ROLE)
    await member.add_roles(role)
    print(f"{member} was given {role} and send a welcome msg")
    await member.send(' YOUR WELCOME MESSAGE GOES HERE')  

#Leave channel msg
#@bot.event
#async def on_member_leave(member):
#   channel = discord.utils.get(member.guild.channels, name='CHANNEL NAME')
#   await channel.send(f'{member.mention} Just left, Bye Bye!')

#BOT TOKEN
bot.run('YOUR TOKEN HERE')

