import discord
from bot_config import TOKEN, INTENTS
import modules.message_reply as message_reply
from discord import Intents, Client, Interaction, app_commands
from discord.app_commands import CommandTree
from modules.commands import Response

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents,) -> None:
        super().__init__(intents=intents)
        self.tree = CommandTree(self)
        self.tree.add_command(Response('response'))

    # 実装されたコマンドをBotが読み込む
    async def setup_hook(self) -> None:
        await self.tree.sync()
    
    async def on_ready(self):
        print('Bot is ready.')

    async def on_message(self, message):
        # ignore messages from bot
        if message.author.bot == True: return
        await message_reply.arm(message)

def main():
    client = MyClient(intents=INTENTS)
    client.run(TOKEN)

if __name__ == '__main__':
    main()
