#!/usr/bin/env python3

"""
A simple Markov chain-powered text generator for Discord.

You can run this code with `python -X utf8 bot.py`.
"""

import argparse
import discord

from markov import Chain

parser = argparse.ArgumentParser(
    description="Discord bot for generating random sentences with a Markov chain."
)
parser.add_argument("token", type=str, help="The Discord token for your bot.")

args = parser.parse_args()

chain = Chain(1)

client = discord.Client()


@client.event
async def on_ready():
    print(f"Logged on as {client.user}.")


@client.event
async def on_message(message):
    # Don't respond to ourself.
    if message.author == client.user:
        return

    if message.content == "ping":
        await message.channel.send("pong")
    elif message.content == f"{client.user.name} give me text":
        await message.channel.send(chain.generate())
    else:
        corpus = message.content.rstrip().split()
        chain.train(corpus)


client.run(args.token)
