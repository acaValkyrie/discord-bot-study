import discord
from discord import app_commands

class Response(app_commands.Group):
    def __init__(self, name: str):
        super().__init__(name=name)
    
    @app_commands.command(name="hello", description="挨拶は大事")
    async def hello_command(self, interaction: discord.Interaction):
        await interaction.response.send_message('hello')

    @app_commands.command(name="call_shanks", description="シャンクスを呼びます")
    async def sanx_command(self, interaction: discord.Interaction):
        await interaction.response.send_message('この戦争を終わらせに来た!!!')