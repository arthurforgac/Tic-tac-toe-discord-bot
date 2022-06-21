import discord
from discord.ext import commands
from tictac import tictac

bot = commands.Bot(command_prefix="!", help_command=None) #initialize the bot with no default help command
botInstances = {} #dict for all the running instances of the game

@bot.command()
async def tictactoe(cxt, *args):
    #initializes the game, randomizes whether the player starts or the computer
    botInstances[cxt.author.id] = tictac() #adds a new instance with player id as key to the dict

    if botInstances[cxt.author.id].currentTurn == "O":
        embed = discord.Embed(
            title=f"Welcome, {cxt.author}! Place your move.",
            color=discord.Colour.green(),
            description=botInstances[cxt.author.id].getBoard()
        )
    else:
        botInstances[cxt.author.id].cpuInput()
        embed = discord.Embed(
            title=f"Welcome, {cxt.author}! I've made my turn, now you make yours.",
            color=discord.Colour.green(),
            description=botInstances[cxt.author.id].getBoard()
        )

    await cxt.send(embed=embed) #sends the created embed

@bot.command()
async def place(cxt, arg, *args):
    #takes a number 1-9 as arg, places the player symbol to the corresponding square
    if cxt.author.id in botInstances:
        #try/except to catch invalid args
        try:
            botInstances[cxt.author.id].board[int(arg)]
        except:
            await cxt.send(embed=discord.Embed(description="Try a valid number next time!", color=discord.Colour.green()))

        #uses the .isFree method to chech whether the selected square is available
        if botInstances[cxt.author.id].isFree(int(arg)):
            #checks whether the player has met the wincon
            if not botInstances[cxt.author.id].winCheck(botInstances[cxt.author.id].board, botInstances[cxt.author.id].playerTurn):
                botInstances[cxt.author.id].move(arg) #call the .move method to place the player input as well as signal the ai to move

                #checks whether the ai has met the wincon
                if not botInstances[cxt.author.id].winCheck(botInstances[cxt.author.id].board, botInstances[cxt.author.id].cpuTurn):
                    #checks whether there is space on the board after the turn
                    if not botInstances[cxt.author.id].isBoardFull():
                        embed = discord.Embed(
                            title=f"Nice move, {cxt.author}! Now it's my turn.",
                            color=discord.Colour.green(),
                            description=botInstances[cxt.author.id].getBoard()
                        )
                    else:
                        embed = discord.Embed(
                            title=f"Looks like we have a tie on our hands!",
                            color=discord.Colour.green(),
                            description=botInstances[cxt.author.id].getBoard()
                        )
                        del botInstances[cxt.author.id] #deletes the game instance in case of a tie

                #ai win case
                else:
                    embed = discord.Embed(
                        title=f"Hahaha! Another one bites the dust!",
                        color=discord.Colour.green(),
                        description=botInstances[cxt.author.id].getBoard()
                    )
                    del botInstances[cxt.author.id]

            #player win case
            else:
                embed = discord.Embed(
                    title=f"Uh-oh! Looks like you've won this time!",
                    color=discord.Colour.green(),
                    description=botInstances[cxt.author.id].getBoard()
                )
                del botInstances[cxt.author.id]

            await cxt.send(embed=embed)

        #case if player chooses an occuppied space
        else:
            await cxt.send(embed=discord.Embed(description="Try a FREE space!", color=discord.Colour.green()))

    #case if the game instance was not found
    else:
        await cxt.send(embed=discord.Embed(description="Please, start a game first.", color=discord.Colour.green()))

@bot.command()
async def quit(cxt, *args):
    #quits and deletes the current game instance
    if cxt.author.id in botInstances:
        await cxt.send(embed=discord.Embed(description="I'll see you next time...", color=discord.Colour.green()))
        del botInstances[cxt.author.id]
    else:
        await cxt.send(embed=discord.Embed(description="You can't quit a game you haven't started!", color=discord.Colour.green()))

@bot.command()
async def help(cxt, *args):
    #shows the possible commands and their description
    embed = discord.Embed(title="Now you see what I can do",
                          color=discord.Colour.green()
                          )
    embed.add_field(name="!tictactoe",
                    value="This command initiates a fun game of tic-tac-toe.",
                    inline=False)
    embed.add_field(name="!place",
                    value="Use this command followed by a number 1-9 to place your symbol in the corresponding field.",
                    inline=False)
    embed.add_field(name="!quit",
                    value="You can use this command to quit the ongoing game, if you are scared.",
                    inline=False)
    embed.add_field(name="!help",
                    value="This command shows you what I'm capable of.")
    await cxt.send(embed=embed)

bot.run("TOKEN_GOES_HERE") #sets the unique token generated by discord