import discord

async def arm(message):
    if '腕' in message.content:
        await message.channel.send('安いもんだ')