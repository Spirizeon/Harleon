# bot.py
import os
import discord
from discord.ext import commands
import openai

openai.api_key = 'OPENAITOKEN'

completion = openai.Completion()


def Reply(question):
  prompt = f'You: {question}\n Harleon: '
  response = completion.create(prompt=prompt,
                               engine="text-davinci-002",
                               stop=['\You'],
                               max_tokens=200)
  answer = response.choices[0].text.strip()
  return answer


##
client = commands.Bot(command_prefix="hr", intents=discord.Intents.all())


@client.event
async def on_ready():
  print("Harleon has been connected")


@client.command()
async def ping(ctx):
  await ctx.send('pong')


@client.command()
async def l(ctx, *, question):
  await ctx.send(Reply(question))


client.run(
  'BOTTOKEN')
