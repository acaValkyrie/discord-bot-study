import discord
from bot_config import TOKEN, INTENTS
import modules.message_reply as message_reply
from discord import Intents, Client, Interaction
from discord.app_commands import CommandTree

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents,) -> None:
        super().__init__(intents=intents)
        self.tree = CommandTree(self)

    async def setup_hook(self) -> None:
        await self.tree.sync()
    
    async def on_ready(self):
        print('logged in')

    async def on_message(self, message):
        # ignore messages from bot
        if message.author.bot == True: return
        await message_reply.arm(message)

client = MyClient(intents=INTENTS)

@client.tree.command(name="hello", description="挨拶は大事")
async def test_command_definition(interaction: discord.Interaction):
    await interaction.response.send_message('hello')

def main():
    client.run(TOKEN)

if __name__ == '__main__':
    main()
