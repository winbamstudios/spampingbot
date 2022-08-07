import discord
import os

client = discord.Client()

print("Welcome to SpamPingBot ")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
# Main Bot Features
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$pingaxo'):
        await message.channel.send('@axolotl127#4099 ')
        print("someone used PingAxo")

    if message.content.startswith('$radarwakefield'):
        await message.channel.send('https://radar.weather.gov/ridge/lite/KAKQ_loop.gif')
        print("someone used wakefield radar")

    if message.content.startswith('$stopbot'):
        await message.channel.send('Bot stopped')
        print("someone used bot stop")
        exit();

    if message.content.startswith('$ping'):
        await message.channel.send('ping')
        print("someone used ping")

    if message.content.startswith('@spam ping bot 2.0#9685 '):
        await message.channel.send('yes?')
        print("someone pinged me")

    if message.content.startswith('$fat'):
        await message.channel.send('https://www.youtube.com/watch?v=RvmQyzbOHFQ')
        print("someone is fat")

    if message.content.startswith('$suggest'):
        await message.channel.send('https://strawpoll.com/polls/YVyP2MMXkgN')
        print("someone is suggesting")

    if message.content.startswith('$ban'):
        await message.channel.send('Banned!')
        print("someone is banned")

    if message.content.startswith('what add to '):
        await message.channel.send('did you just ping me')
        print("someone is pinged, me")

    if message.content.startswith('uhhhh'):
        await message.channel.send('im self conscious')
        print("someone is setf conscious-")

    if message.content.startswith('where do you live, spb?'):
        await message.channel.send('in your walls')
        print("someone is in your walls oh god")

    if message.content.startswith('im scared'):
        await message.channel.send('This section has been found to be very scary and removed. Thank you for your service.')
        await message.channel.send('This section is pinging everyone.')
        print("someone is scared")

    if message.content.startswith('$actualspamping'):
        await message.channel.send('@everyone')
        await message.channel.send('@everyone')
        await message.channel.send('@everyone')
        await message.channel.send('@everyone')
        await message.channel.send('@everyone')
        await message.channel.send('@everyone')
        await message.channel.send('@everyone')
        await message.channel.send('@everyone')
        await message.channel.send('@everyone')
        await message.channel.send('@everyone')
        await message.channel.send('@everyone')
        await message.channel.send('@everyone')
        await message.channel.send('@everyone')
        print("someone is ping")

    if message.content.startswith('didnt ask'):
        await message.channel.send('so? im on the other side of the argument btw')
        print("someone is asking")

    if message.content.startswith('$loop'):
        await message.channel.send('$loop')
        print("someone is looping oh god")

    if message.content.startswith('$beans'):
        await message.channel.send('Eat your beans, and your greens!\nhttps://images.heb.com/is/image/HEBGrocery/000120104')
        print("someone is eating b e a n s")

    if message.content.startswith('$scarecommand'):
        await message.channel.send('done >:)')
        os.system('C:\\Windows\\notepad.exe C:\\Users\\willr\\Desktop\\scare.txt')
        print("someone is being scared.")

    if message.content.startswith('$ron'):
        await message.channel.send(file=discord.File(r'C:\Ron.mp3'))
        print("someone likes ron")

client.run("INSERT BOT TOKEN")
