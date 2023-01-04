import os, time as t, discord
def embedCreator():
    title,description,colour,thumbnail,fields,footer=input('Title: '),input('Description: '),input('Colour: '),input('Thumnail [Text/N]: '),input('fields [Y/N]: '),input('Footer [Text/N]: ')
    embed=f"discord.Embed(title='{title}',description='{description}',color={colour})"
    author=input('Author: [Y/N]')
    if author.lower()=='n': pass
    else:
        name,iconURL,url=input('Author Name: '),input('Author iconURL: '),input('Author RL [Text/N]: ')
        if url.lower()=='n': url=None
        else: url==f"\"{url}\""
        embed=f'{embed}.set_author(name="{name}",icon_url="{iconURL}",url={url})'
    if thumbnail.lower()=='n': pass
    else: embed=f"{embed}.set_thumbnail(url='{thumbnail}')"
    if fields.lower()=='y':
        while fields.lower()=='y':
            fields=input('Add Field? [Y/N]: ')
            if fields=='n': break
            else:
                name,value,inline=input('Name: '),input('Value: '),input('Inline [True/False]: ')
                embed=f'{embed}.add_field(name="{name}",value="{value}",inline={inline})'
    if footer.lower()=='n': pass
    else: embed=f'{embed}.set_footer(text="{footer}")'
    return embed

print('Welcome to the Discord Bot creator (Python Bot)')
while True:
    sel=input('Starter Menu:\nA) Create a Bot\nB) Instructions/Help\nC) Embed Creator\n')
    if sel.upper()=='A': break
    elif sel.upper()=='B': print("Instructions\n1) You'll want to install discord py onto your Device\nWindows: Open Powershell/Command Prompt and input 'py -3 -m pip install -U discord.py'\nMAC: Open Terminal and input: 'python3 -m pip install -U discord.py'\nWait for it to install and then Create a Bot")
    elif sel.upper()=='C':
        embed=embedCreator()
        print(f'{embed}')
    else: print('Please choose a proper action')
name,prefix,token=input('Bot Name: '),input('Bot Prefix: '),input('Bot Token: ')
file=open(f'{name}.py','a')
if file==f'{name}.py':
    print('File Found')
file.write('import discord\nfrom discord.ext import commands\n')
file.write('intents=discord.Intents.default()\nintents.message_content=True\n')
file.write(f'bot=commands.Bot(command_prefix="{prefix}",intents=intents)\n')
want,arg='y','y'
while want.lower()=='y':
    want=input('Command? [Y/N]: ')
    if want.lower()=='n':break
    cmdName,message,dmorchannel=input('Command Name: '),input('a) Message\nb) Embed\n'),input('A) DM\nB) Channel\n')
    if dmorchannel.upper()=='A': dmorchannel='author.send'
    else: dmorchannel='send'
    if message.lower()=='a':
        message=input('Message: ')
        file.write(f'\n@bot.command()\nasync def {cmdName}(ctx):\nctx.{dmorchannel}("{message}")')
    elif message.lower()=='b':
        embed=embedCreator()
        file.write(f'\n@bot.command()\nasync def {cmdName}(ctx):\nctx.{dmorchannel}(embed={embed})')
    
file.write(f'\nbot.run("{token}")')
file.close()
print('Bot Created')
t.sleep(1)
os.startfile('')
