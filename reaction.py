import discord
import pyjokes
import random

TOKEN = 'Token goes here'
client = discord.Client()


@client.event
async def on_ready():
    print('{0.user} is now online'.format(client))


@client.event
async def on_message(message):
    if message.content == 'Hello':
        await message.channel.send('Welcome and goodbye')

    if message.content == 'cool':
        await message.add_reaction('\U0001F60E')

    if message.content == 'hello':
        await message.channel.send('Hello there!')

    if message.content == 'roll':
        await message.channel.send(str(random.randint(1, 6)))

    if message.content == 'test':
        await message.channel.send('👎')

    if message.content == 'annoy':
        await message.channel.send('Booo💀')

    if message.content == 'joke':
        joke = pyjokes.get_joke()
        await message.channel.send(joke)

    if message.content.startswith('fuck'):
        await message.channel.send('Thats not allowed')
        with open(r'C:\Users\David.Entonu\Downloads\captain.jpg', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)
        await message.channel.send(file=discord.File('captain.jpg'))


async def msg(ctx, userid: str, *, msg1):
    user = ctx.message.server.get_member(userid)
    await client.send_message(user, msg1)


@client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author} edit a message. \n'
        f'Before: {before.content}\n'
        f'After: {after.content}'
    )


@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')


client.run(TOKEN)
