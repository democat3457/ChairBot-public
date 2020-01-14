import discord
import os
from discord.ext import commands
import random
from constants import *
import gh
import json
import io
import inspect
import textwrap
import traceback
import aiohttp
from contextlib import redirect_stdout

progressServer4 = {}
prog = gh.readProgress()
print(prog)

progressServer4 = json.loads(prog)
for i in progressServer4.keys():
	progressServer4[int(i)] = progressServer4.pop(i)

# with open('progressServer4.json') as json_file:
# 	progressServer4 = json.load(json_file)

bot = commands.Bot(command_prefix=';')

def is_bot_admin():
	def predicate(ctx):
		return ctx.author.id in botAdmins
	return commands.check(predicate)

def is_me(message):
	return message.author == bot.user

def write_progress(i, value):
	progressServer4[i] = value
# 	with open('progressServer4.json', 'w') as json_file:
	gh.updateProgress(json.dumps(progressServer4, indent=4))

@bot.event
async def on_ready():
	print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
	if message.author.bot:
		return
	
	if type(message.channel) is discord.DMChannel:
		mem1 = bot.get_guild(servers[0]).get_member(message.author.id)
		mem2 = bot.get_guild(servers[1]).get_member(message.author.id)
		mem3 = bot.get_guild(servers[2]).get_member(message.author.id)
		mem4 = bot.get_guild(servers[3]).get_member(message.author.id)
		mem5 = bot.get_guild(servers[4]).get_member(message.author.id)
		mem6 = bot.get_guild(servers[5]).get_member(message.author.id)
		if "hint" in message.content or "solution" in message.content or "clue" in message.content:
			await message.channel.send("||https://cdn.discordapp.com/attachments/543890064506355716/651115429489541140/unknown.gif||")
# 		elif "KN" in message.content and "waX" in message.content:
# 			await message.channel.send("What's Volkswagen's case and shorthand symbol?")
		if mem6 is not None:
			pass
		elif mem5 is not None:
			pass
		elif mem4 is not None:
			server4 = bot.get_guild(servers[3])
			trunk = bot.get_channel(664692183802052619)
			cabinet = bot.get_channel(664692354044919848)
			safeChannel = bot.get_channel(664692430729379860)
			switchChannel = bot.get_channel(664692584056094743)
			secretChannels = [[],[665062320170598401,665062358183575572,665062412218662942,665062383344943124],[665062104428052490],[664844432146694144]]
			try:
				if progressServer4[message.author.id] == 0 and message.content == 'stage1code':
					write_progress(message.author.id, 1)
					await trunk.set_permissions(mem4, read_messages=True, send_messages=False)
					for c in secretChannels[1]:
						await bot.get_channel(c).set_permissions(mem1, read_messages=True, send_messages=False)
					await message.channel.send('Unlocked!')
					print('{0.author} unlocked Server 4 Stage {1}!'.format(message, progressServer4[message.author.id]))
				if progressServer4[message.author.id] == 1 and message.content == 'stage2code':
					write_progress(message.author.id, 2)
					await cabinet.set_permissions(mem4, read_messages=True, send_messages=False)
					for c in secretChannels[2]:
						await bot.get_channel(c).set_permissions(mem3, read_messages=True, send_messages=False)
					await message.channel.send('Unlocked!')
					print('{0.author} unlocked Server 4 Stage {1}!'.format(message, progressServer4[message.author.id]))
				if progressServer4[message.author.id] == 2 and message.content == 'stage3code':
					write_progress(message.author.id, 3)
					await safeChannel.set_permissions(mem4, read_messages=True, send_messages=False)
					for c in secretChannels[3]:
						await bot.get_channel(c).set_permissions(mem2, read_messages=True, send_messages=False)
					await message.channel.send('Unlocked!')
					print('{0.author} unlocked Server 4 Stage {1}!'.format(message, progressServer4[message.author.id]))
				if progressServer4[message.author.id] == 3 and message.content == 'stage4code':
					write_progress(message.author.id, 4)
					await switchChannel.set_permissions(mem4, read_messages=True, send_messages=False)
					await message.channel.send('Unlocked!')
					print('{0.author} unlocked Server 4 Stage {1}!'.format(message, progressServer4[message.author.id]))
			except KeyError:
				write_progress(message.author.id, 0)
				if message.content == '16x16png':
					write_progress(message.author.id, 1)
					await trunk.set_permissions(message.author, read_messages=True, send_messages=False)
					for c in secretChannels[1]:
						await bot.get_channel(c).set_permissions(mem1, read_messages=True, send_messages=False)
					await message.channel.send('Unlocked!')
					print('{0.author} unlocked Server 4 Stage {1}!'.format(message, progressServer4[message.author.id]))
		elif mem3 is not None:
			pass
		elif mem2 is not None:
			pass
		elif mem1 is not None:
			pass
		
		print('@{0.channel.recipient.name}: {0.channel.recipient}: {0.content}'.format(message))
		return
	
	print('{0.channel.guild.name}: #{0.channel.name}: {0.author}: {0.content}'.format(message))
	
	await bot.process_commands(message)

@bot.command()
async def toot(ctx, *args):
	if len(args) != 0 and args[0].startswith('loudly'):
		embed1 = discord.Embed(title="🎺🎺 **`TOOT TOOT`** 🎺🎺", color=discord.Color.from_rgb(235,180,84))
		await ctx.send(embed=embed1)
	else:
		embed1 = discord.Embed(title="🎺🎺 **`toot toot`** 🎺🎺", color=discord.Color.from_rgb(235,180,84))
		await ctx.send(embed=embed1)

@bot.command(name='eval')
@is_bot_admin()
async def _eval(ctx, *, body):
    """Evaluates python code - Originally created by fourjr at fourjr/eval-bot"""
    blocked_words = ['.delete()', 'os', 'subprocess', 'history()', '("token")', "('token')",
                     'aW1wb3J0IG9zCnJldHVybiBvcy5lbnZpcm9uLmdldCgndG9rZW4nKQ==', 'aW1wb3J0IG9zCnByaW50KG9zLmVudmlyb24uZ2V0KCd0b2tlbicpKQ==']
    if ctx.author.id != bot.owner_id:
        for x in blocked_words:
            if x in body:
                return await ctx.send('Your code contains certain blocked words.')
    env = {
        'ctx': ctx,
        'channel': ctx.channel,
        'author': ctx.author,
        'guild': ctx.guild,
        'message': ctx.message,
        'source': inspect.getsource,
        'bot':bot
    }

    env.update(globals())

    body = cleanup_code(body)
    stdout = io.StringIO()
    err = out = None

    to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

    def paginate(text: str):
        '''Simple generator that paginates text.'''
        last = 0
        pages = []
        for curr in range(0, len(text)):
            if curr % 1980 == 0:
                pages.append(text[last:curr])
                last = curr
                appd_index = curr
        if appd_index != len(text)-1:
            pages.append(text[last:curr])
        return list(filter(lambda a: a != '', pages))
    
    try:
        exec(to_compile, env)
    except Exception as e:
        err = await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
        return await ctx.message.add_reaction('\u2049')

    func = env['func']
    try:
        with redirect_stdout(stdout):
            ret = await func()
    except Exception as e:
        value = stdout.getvalue()
        err = await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
    else:
        value = stdout.getvalue()
        if ret is None:
            if value:
                try:
                    
                    out = await ctx.send(f'```py\n{value}\n```')
                except:
                    paginated_text = paginate(value)
                    for page in paginated_text:
                        if page == paginated_text[-1]:
                            out = await ctx.send(f'```py\n{page}\n```')
                            break
                        await ctx.send(f'```py\n{page}\n```')
        else:
            bot._last_result = ret
            try:
                out = await ctx.send(f'```py\n{value}{ret}\n```')
            except:
                paginated_text = paginate(f"{value}{ret}")
                for page in paginated_text:
                    if page == paginated_text[-1]:
                        out = await ctx.send(f'```py\n{page}\n```')
                        break
                    await ctx.send(f'```py\n{page}\n```')

    if out:
        await ctx.message.add_reaction('\u2705')  # tick
    elif err:
        await ctx.message.add_reaction('\u2049')  # x
    else:
        await ctx.message.add_reaction('\u2705')

def cleanup_code(content):
    """Automatically removes code blocks from the code."""
    # remove ```py\n```
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])

    # remove `foo`
    return content.strip('` \n')

def get_syntax_error(e):
    if e.text is None:
        return f'```py\n{e.__class__.__name__}: {e}\n```'
    return f'```py\n{e.text}{"^":>{e.offset}}\n{e.__class__.__name__}: {e}```'
		
@bot.group()
@is_bot_admin()
async def game(ctx):
	if ctx.invoked_subcommand is None:
		if ctx.author.id in botAdmins:
			await ctx.send('setup, purge, rules, send')
			
@game.error
async def game_error(ctx, error):
	if isinstance(error, commands.CheckFailure):
		await ctx.message.add_reaction('\N{THUMBS DOWN SIGN}')
	elif isinstance(error, commands.CommandNotFound):
		pass
			
@game.command()
@is_bot_admin()
async def setup(ctx):
	print('Starting setup...')
	i = 1
	for serverId in servers:
		hasRules = False
		hasHost = False
		hasMod = False
		hasPrev = False
		hostRole = None
		modRole = None
		prevRole = None
		textCategory = None
		server = bot.get_guild(serverId)
		await server.edit(name='{1} #{0}'.format(i, serverName))
		for channel in server.text_channels:
			if channel.name == 'rules':
				hasRules = True
		for role in server.roles:
			if role.name == 'Host':
				hasHost = True
				hostRole = role
			if role.name == 'Moderator':
				hasMod = True
				modRole = role
			if role.name.startswith('Sparkly Solution Solver'):
				hasPrev = True
				prevRole = role
		for category in server.categories:
			if category.name == 'Text Channels':
				textCategory = category
		if hasHost is False:
			hostRole = await server.create_role(name='Host', permissions=discord.Permissions.all(), color=discord.Color.from_rgb(random.randint(10,255), random.randint(10,255), random.randint(10,255)), hoist=True)
			print('Created host role for server {0}'.format(i))
		if hasMod is False:
			modPerms = discord.Permissions.none()
			modPerms.update(view_audit_log=True, manage_roles=True, kick_members=True, change_nickname=True, read_messages=True, send_messages=True, send_tts_messages=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True, add_reactions=True, connect=True, speak=True, mute_members=True, use_voice_activation=True)
			modRole = await server.create_role(name='Moderator',permissions=modPerms,color=discord.Color.from_rgb(random.randint(10,255),random.randint(10,255),random.randint(10,255)),hoist=True)
			print('Created mod role for server {0}'.format(i))
		if hasPrev is True:
			await prevRole.edit(name='{0.user.name}'.format(bot))
			print('Edited bot role name for server {0}'.format(i))
		if hasRules is False:
			overwrites = {
				modRole: discord.PermissionOverwrite(send_messages=True),
				server.default_role: discord.PermissionOverwrite(send_messages=False)
			}
			await server.create_text_channel('rules', overwrites=overwrites, category=textCategory, position=0)
			print('Created rules channel for server {0}'.format(i))
		print('Finished setting up server {0}'.format(i))
		i = i + 1
	await ctx.message.add_reaction('\N{THUMBS UP SIGN}')

@game.command()
@is_bot_admin()
async def purge(ctx):
	ctx.invoke(setup, ctx)
	await ctx.message.add_reaction('\N{THUMBS UP SIGN}')

@game.command()
@is_bot_admin()
async def rules(ctx):
	for channelId in ruleChannels:
		channel = bot.get_channel(channelId)
		embed = discord.Embed(color=discord.Color.from_rgb(78,191,80))
		embed.add_field(name='Rules & Info',value="Welcome to the {0} servers!\n\n1. Each invite has infinite uses, except for the last one, which has 3 uses. This means each invite has 7 characters.\n2. Don't use selfbots. Selfbots are forbidden per Discord's ToS, however we can't and won't track them. Anyone who is proven to use such a script **in order to get an advantage over other players** will be permanently cross-banned in the servers.\n3. Posting the real invite codes/links to the next servers is a grey area. Your message will be deleted and you'll be warned by a mod. Don't repost your message or there will be consequences! Sometimes, a challenge may specify that posting the code in plaintext is prohibited. Please use common sense.\n4. **There is a behavior that is allowed __only in these servers:__**\n - You can spam the **text** channels as long as the content doesn't break the rules.\n5. *The list of rules is* ***not*** *guaranteed to be exhaustive. Again, use common sense.*\n6. Lastly, have fun and keep a positive mental attitude!".format(serverName))
		embed.set_image(url='https://cdn.discordapp.com/attachments/543890064506355716/651115429489541140/unknown.gif')
		await channel.send(embed=embed)
		print('Finished adding rules to {0.guild.name}'.format(channel))
		# await channel.send(value='https://cdn.discordapp.com/attachments/543890064506355716/651115429489541140/unknown.gif')

@game.command()
@is_bot_admin()
async def send(ctx, destination, *, args):
	if destination == 'all':
		for channelId in ruleChannels:
			channel = bot.get_channel(channelId)
			await channel.send(args)
	else:
		channel = bot.get_channel(int(destination))
		await channel.send(args)
	await ctx.message.add_reaction('\N{THUMBS UP SIGN}')

@game.group()
@is_bot_admin()
async def invite(ctx):
	if ctx.invoked_subcommand is None:
		ctx.send('create, revoke')

@invite.command()
@is_bot_admin()
async def create(ctx, *dest):
	print('Creating invites')
	if len(dest) == 0 or dest[0] == "all":
		i = 1
		for channelId in ruleChannels:
			channel = bot.get_channel(channelId)
			if i == 6:
				invite = await channel.create_invite(max_uses=3)
			else:
				invite = await channel.create_invite()
			print('{0.guild.name} invite: {1.code}'.format(channel, invite))
			await ctx.send('{0.guild.name} invite: {1.code}'.format(channel, invite))
			i += 1
	else:
		for i in dest:
			channel = bot.get_channel(ruleChannels[int(i)-1])
			if i == 6:
				invite = await channel.create_invite(max_uses=3)
			else:
				invite = await channel.create_invite()
			print('{0.guild.name} invite: {1.code}'.format(channel, invite))
			await ctx.send('{0.guild.name} invite: {1.code}'.format(channel, invite))
	print('Finished creating invites')

@invite.command()
@is_bot_admin()
async def revoke(ctx, *dest):
	print('Revoking invites')
	if len(dest) == 0 or dest[0] == "all":
		for guildId in servers:
			server = bot.get_guild(guildId)
			invites = await server.invites()
			for invite in invites:
				code = invite.code
				await invite.delete()
				print('{0.name} invite {1} deleted'.format(server, code))
	else:
		if len(dest) == 1 or dest[0] == "code":
			if dest[0] == "code":
				for code in dest[1:]:
					if not code.startswith('discord.gg') and not code.startswith('http'):
						code = 'discord.gg/' + code
					invite = await bot.fetch_invite(code)
					if invite is False:
						await ctx.send('Invalid invite {0}!'.format(code), delete_after=3)
					else:
						await invite.delete()
						print('{0.guild.name} invite {0.code} deleted'.format(invite))
			else:
				code = dest[0]
				if not code.startswith('discord.gg') and not code.startswith('http'):
					code = 'discord.gg/' + code
				invite = await bot.fetch_invite(code)
				if invite is False:
					await ctx.send('Invalid invite {0}!'.format(invite.code), delete_after=3)
				else:
					await invite.delete()
					print('{0.guild.name} invite {0.code} deleted'.format(invite))
		else:
			if dest[0] == "server":
				for i in dest[1:]:
					i = int(i)
					serverId = servers[i-1]
					server = bot.get_guild(serverId)
					invites = await server.invites()
					for invite in invites:
						code = invite.code
						await invite.delete()
						print('{0.name} invite {1} deleted'.format(server, code))
			else:
				for code in dest:
					if not code.startswith('discord.gg') and not code.startswith('http'):
						code = 'discord.gg/' + code
					invite = await bot.fetch_invite(code)
					if invite is False:
						await ctx.send('Invalid invite {0}!'.format(code), delete_after=3)
					else:
						await invite.delete()
						print('{0.guild.name} invite {0.code} deleted'.format(invite))
	print('Finished revoking invites')

@bot.command()
async def pma(ctx):
	await ctx.send('https://cdn.discordapp.com/attachments/543890064506355716/651115429489541140/unknown.gif')

@bot.command()
@is_bot_admin()
async def delete(ctx, num: int):
	await ctx.message.delete()
	messages = await ctx.channel.history(limit=num).flatten()
	await ctx.channel.delete_messages(messages)

@bot.command()
@is_bot_admin()
async def clean(ctx, *channels):
	numDel = 0
	if len(channels) == 0 or channels[0] == "all":
		for serverId in servers:
			server = bot.get_guild(serverId)
			for channelId in channels in server:
				channel = bot.get_channel(channelId)
				deleted = await channel.purge(limit=100, check=is_me)
				numDel += len(deleted)
	elif channels[0] == "rules":
		for channelId in ruleChannels:
			channel = bot.get_channel(channelId)
			deleted = await channel.purge(limit=100, check=is_me)
			numDel += len(deleted)
	else:
		for channelId in channels:
			channel = bot.get_channel(int(channelId))
			deleted = await channel.purge(limit=100, check=is_me)
			numDel += len(deleted)
	await ctx.send('Deleted {} message(s)'.format(numDel), delete_after=3.0)

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
	print('Shutdown initiated.')
	await bot.logout()
	
@bot.command()
@commands.is_owner()
async def restart(ctx):
	print('Restart initiated.')
	await bot.logout()
	subprocess.call(['python', 'main.py'])

bot.run(os.getenv("BOT_TOKEN"))
