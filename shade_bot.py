import discord
import discord.utils

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
    
    #when a user reacts give them the correct role
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        #if they reacted to the right message give them the role
        if message_id == 748108697229590608:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
            
            #give them a role bassed on their reaction
            if payload.emoji.name == 'justStarted':
                role = discord.utils.get(guild.roles, name="just started")
            if payload.emoji.name == 'ten':
                role = discord.utils.get(guild.roles, name="10 days")
            if payload.emoji.name == 'twentyFive':
                role = discord.utils.get(guild.roles, name="25 days")
            if payload.emoji.name == 'fifty':
                role = discord.utils.get(guild.roles, name="50 days")
            if payload.emoji.name == 'seventyFive':
                role = discord.utils.get(guild.roles, name="75 days")
            if payload.emoji.name == 'oneHundred':
                role = discord.utils.get(guild.roles, name="100 days")
            if payload.emoji.name == 'oneHundredFifty':
                role = discord.utils.get(guild.roles, name="150 days")
            if payload.emoji.name == 'twoHundred':
                role = discord.utils.get(guild.roles, name="200 days")
            if payload.emoji.name == 'twoHundredFifty':
                role = discord.utils.get(guild.roles, name="250 days")
            if payload.emoji.name == 'threeHundred':
                role = discord.utils.get(guild.roles, name="300 days")
            if payload.emoji.name == 'fourHundred':
                role = discord.utils.get(guild.roles, name="400 club")
            if payload.emoji.name == 'king':
                role = discord.utils.get(guild.roles, name="completion")
            if payload.emoji.name == 'blackLouse':
                role = discord.utils.get(guild.roles, name="art expert")
            if payload.emoji.name == 'crystal':
                role = discord.utils.get(guild.roles, name="crystal collector")
            if payload.emoji.name == 'coal':
                role = discord.utils.get(guild.roles, name="coal hoarder")
            if payload.emoji.name == 'bookB':
                role = discord.utils.get(guild.roles, name="I like books")
            if payload.emoji.name == 'path':
                role = discord.utils.get(guild.roles, name="my feet hurt")
            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
    #does the same as above, but removes a role if it is deselected
    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id
        if message_id == 748108697229590608:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
            
            if payload.emoji.name == 'justStarted':
                role = discord.utils.get(guild.roles, name="just started")
            if payload.emoji.name == 'ten':
                role = discord.utils.get(guild.roles, name="10 days")
            if payload.emoji.name == 'twentyFive':
                role = discord.utils.get(guild.roles, name="25 days")
            if payload.emoji.name == 'fifty':
                role = discord.utils.get(guild.roles, name="50 days")
            if payload.emoji.name == 'seventyFive':
                role = discord.utils.get(guild.roles, name="75 days")
            if payload.emoji.name == 'oneHundred':
                role = discord.utils.get(guild.roles, name="100 days")
            if payload.emoji.name == 'oneHundredFifty':
                role = discord.utils.get(guild.roles, name="150 days")
            if payload.emoji.name == 'twoHundred':
                role = discord.utils.get(guild.roles, name="200 days")
            if payload.emoji.name == 'twoHundredFifty':
                role = discord.utils.get(guild.roles, name="250 days")
            if payload.emoji.name == 'threeHundred':
                role = discord.utils.get(guild.roles, name="300 days")
            if payload.emoji.name == 'fourHundred':
                role = discord.utils.get(guild.roles, name="400 club")
            if payload.emoji.name == 'king':
                role = discord.utils.get(guild.roles, name="completion")
            if payload.emoji.name == 'blackLouse':
                role = discord.utils.get(guild.roles, name="art expert")
            if payload.emoji.name == 'crystal':
                role = discord.utils.get(guild.roles, name="crystal collector")
            if payload.emoji.name == 'coal':
                role = discord.utils.get(guild.roles, name="coal hoarder")
            if payload.emoji.name == 'bookB':
                role = discord.utils.get(guild.roles, name="I like books")
            if payload.emoji.name == 'path':
                role = discord.utils.get(guild.roles, name="my feet hurt")
            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
    #say hello if the user types "hello shade"
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        if message.content.startswith('hello shade'):
            #await message.channel.send('Hello {0.author.mention}'.format(message))
            await message.channel.send('Oh, hello friend :hearts:'.format(message))
client = MyClient()
client.run('INSERT TOKEN HERE')