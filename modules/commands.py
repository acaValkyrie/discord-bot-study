import discord
from app import client

@client.tree.command(name="hello", description="挨拶は大事")
async def test_command_definition(interaction: discord.Interaction):
    await interaction.response.send_message('hello')