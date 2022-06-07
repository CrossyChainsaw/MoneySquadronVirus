import os
import discord
import random
from discord.ext import commands
from discord.ext import tasks
from keep_alive import keep_alive

links = [
  "https://imgur.com/gqAnr5J", # richkid
  "https://imgur.com/wspnr9q", # side
  "https://imgur.com/NdYxBs1", # monkey big nose 
  "https://imgur.com/OGUaxjP", # happykid
  "https://imgur.com/3Ky4OVq", # happykid2
  "https://imgur.com/nmblXr6", # Harambe
  "https://imgur.com/t8b6PXD", # Gay
  "https://imgur.com/Xbr1fIU", # Hoodie
  "https://imgur.com/6c9wLvf", # Donkey
  "https://imgur.com/7etqmf5", # Mario
  "https://imgur.com/UpxZTY4", # Hop on
  "https://www.youtube.com/watch?v=yQQNZTEnl6o", # Promo
  "https://imgur.com/qNshpko", # Winnie
  "https://imgur.com/mK0nPH0", # Yes papa
  "https://imgur.com/bwHEYmt", # Mr krabs
  "https://imgur.com/p9vkwtj", # berserk skeletons
  "https://imgur.com/uuRAxKB", # beautiful
  "https://imgur.com/acuRkCs", # blue
  "https://imgur.com/1DG8iJK", # squad games
  "https://imgur.com/nJ1Ag2V", # money squat
  "https://imgur.com/akvUGrP", # squid invite
  "https://imgur.com/GiSg7Km", # yugioh card
  "https://imgur.com/CFNMKlg", # spotify
  "https://imgur.com/M56NnIz", # m&m
  "https://imgur.com/gHeXGmA", # crook
  "https://imgur.com/XL8JJCd", # donald
  "https://imgur.com/Q76CDWs", # doggo
  "https://imgur.com/x8Nx0sk", # turkey
  "https://imgur.com/xBx0Mvg", # DOGGO SQUADRO
  "https://imgur.com/pzmwj61", # mike
  "https://imgur.com/MbhDlyp", # Cartman
  "https://imgur.com/mV7MuGr", # cAT
  "https://i.imgur.com/iFdxY99.jpg", # crossy
  "https://imgur.com/n9IebRR" # cordon blue part 2
]

blameMasterMsg = 'you need to be a skyward member for this command sorry blame ma2st4er5'

# COMMANDS
bot = commands.Bot(command_prefix=['ms', 'Ms', 'MS'], help_command=None)


#@commands.has_role('Clan Member')
@bot.command(name='meme', help=blameMasterMsg)
async def meme(ctx):
    memeNew = links[random.randint(0, len(links) - 1)]
    await ctx.send(memeNew)


@commands.has_role('Clan Member')
@bot.command(name='donke', help=blameMasterMsg)
async def donke(ctx):
    await ctx.send("https://imgur.com/6c9wLvf")


@commands.has_role('Clan Member')
@bot.command(name='mike', help=blameMasterMsg)
async def mike(ctx):
    await ctx.send("https://imgur.com/pzmwj61")
  

@bot.command(name='help')
async def help(ctx, args=None):
    help_embed = discord.Embed(title="My Bot's Help!")
    command_names_list = [x.name for x in bot.commands]

    # If there are no arguments, just list the commands:
    if not args:
        help_embed.add_field(
            name="List of supported commands:",
            value="\n".join([str(i+1)+". "+x.name for i,x in enumerate(bot.commands)]),
            inline=False
        )
        help_embed.add_field(
            name="Details",
            value="Type `mshelp <command name>` for more details about each command.",
            inline=False
        )

    # If the argument is a command, get the help text from that command:
    elif args in command_names_list:
        help_embed.add_field(
            name=args,
            value=bot.get_command(args).help
        )

    # If someone is just trolling:
    else:
        help_embed.add_field(
            name="X",
            value="That command does not exist"
        )

    await ctx.send(embed=help_embed)

  

keep_alive()
bot.run(os.environ['BOT_TOKEN'])
