import discord
from codes import token


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        my_list = ['Коля', 'Саня', 'Дима']

        if message.content in my_list or message.content:
            await message.channel.send(
                f'Возврат сообщения: {message.content}')


client = MyClient()
client.run(token)
