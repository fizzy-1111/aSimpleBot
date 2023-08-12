import discord
from discord import app_commands
from discord.ext import commands
import os
import math

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
@bot.event
async def on_ready():
    print("Bot is ready")
    try:
        synced=await bot.tree.sync()
        print(f"Synced {len(synced)} commands(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="ping")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message('Pong!')
@bot.command()
async def greet(ctx):
    await ctx.send(f"Hello, {ctx.author.mention}!")

@bot.command()
async def wordcount(ctx):
    # Check if there are attachments in the message
    if not ctx.message.attachments:
        await ctx.send("Please attach a text file.")
        return

    # Get the first attachment (assuming it's a text file)
    attachment = ctx.message.attachments[0]

    # Download the attachment
    file_content = await attachment.read()

    # Decode the file content and count words
    text = file_content.decode('utf-8')
    word_count = len(text.split())

    await ctx.send(f"The number of words in the file is: {word_count}")


@bot.command()
async def factorial(ctx, number: int):
    if number < 0:
        await ctx.send("Factorial is not defined for negative numbers.")
        return
    
    result = 1
    for i in range(1, number + 1):
        result *= i

    # Check if the result is too large to fit in a Discord message
    if len(str(result)) > 1900:  # Adjust the threshold as needed
        file_path = "factorial_result.txt"
        with open(file_path, "w") as file:
            file.write(f"The factorial of {number} is: {result}")
        
        await ctx.send(f"The factorial result is too large for a message. Here is the result in a text file:", file=discord.File(file_path))
        os.remove(file_path)  # Remove the temporary file
    else:
        await ctx.send(f"The factorial of {number} is: {result}")
@bot.command()
async def goodboy(ctx):
    await ctx.send(f"Where are my treats? One Chase is enough.")

@bot.command()
async def markdown_to_renpy(ctx):
    if len(ctx.message.attachments) == 0 or not ctx.message.attachments[0].filename.endswith('.md'):
        await ctx.send("Please upload a Markdown file with the command.")
        return

    attachment = ctx.message.attachments[0]
    markdown_text = await attachment.read()

    markdown_text = markdown_text.decode('utf-8')
    lines = markdown_text.split('\n')
    charlist=[]
    renpy_code = ''
    character = None
    for i, line in enumerate(lines):
        if line.startswith('char:'):
            character = line[len('char:'):].strip()
        elif line.startswith('>'):
            dialogue = line.strip('>').strip()
            renpy_code += f'{character} "\\"{dialogue}\\""\n'
            # while i + 1 < len(lines) and lines[i + 1].strip() != "":
            #     i += 1
            #     renpy_code += f'{character} "\\"{lines[i].strip()}\\""\n'
            #     charlist.append(charlist)
            #     await ctx.send(lines)
        elif not line.startswith('\r')  and line.endswith:
            fullLine=line.strip('\r')
            renpy_code+=f'"{fullLine}"\r'
    if renpy_code:
        renpy_filename = 'renpy_script.txt'

        with open(renpy_filename, 'w') as file:
            file.write(renpy_code)
        
        await ctx.send(file=discord.File(renpy_filename))

        # Clean up the temporary file
        os.remove(renpy_filename)
    else:
        await ctx.send("No valid character-dialogue pairs found in the Markdown input.")

@bot.command()
async def help_markdown(ctx):
    help_message = (
        "A typical use case to write markdown:\n"
        "To write a character dialogue, for example:\n"
        "char:sam\n"
        "\> Hello\n"
        "If you want to make a character says multiple dialogues:\n"
        "char:sam\n"
        "\> Hello\n"
        "\> Second dialogue here\n"
        "if you want to keep what character saying in a single dialogue, just don't make a new line\n"
    )
    await ctx.send(help_message)
@bot.command()
async def help_commands(ctx):
    help_message = (
        "# Here are the available commands:\n"
        "\n"
        "**!markdown_to_renpy** - Convert Markdown to Ren'Py script\n"
        "**!help_commands** - Display this help message\n"
        "**!help_markdown** - tutorial for writing markdown\n"
        "**!factorial** - output the result for the factorial of a natural number\n"
        "**!wordcount** - Just send a txt file, I gonna count words for you\n"
        "**!goodboy** - If you wanna show your gratitude\n"
    )   
    await ctx.send(help_message)

TOKEN = 'MTEzOTI2NjY3ODQyNTkxMTMxNg.G5Fq9C.zY8fSfyZqjXNW9YfDLHmrbpF5g4itXrB8mx3FY'
bot.run(TOKEN)