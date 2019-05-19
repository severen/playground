#!/usr/bin/env python3

"""
A simple Markov chain-powered text generator for Discord.

You can run this code with `python -X utf8 bot.py`.
"""

import os
import asyncio
import argparse
import discord

from markov import Chain
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

parser = argparse.ArgumentParser(
    description="Discord bot for generating random sentences with a Markov chain."
)
parser.add_argument(
    "-t",
    "--token",
    type=str,
    default=os.environ.get("DISCORD_TOKEN"),
    help="The Discord token for your bot.",
)
parser.add_argument(
    "-p",
    "--persist",
    type=Path,
    default=Path("model.json"),
    help="The file path for storing the model persistently.",
)

args = parser.parse_args()

chain = Chain(1)
if args.persist.exists():
    chain.deserialize(args.persist.read_text())
chain_lock = asyncio.Lock()

client = discord.Client()


@client.event
async def on_ready():
    print(f"Logged on as {client.user}.")


@client.event
async def on_message(message):
    async with chain_lock:
        # Don't respond to ourself.
        if message.author == client.user:
            return

        if message.content == f"{client.user.name} give me text":
            await message.channel.send(chain.generate())
        else:
            chain.train(message.content)


loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(client.start(args.token))
except KeyboardInterrupt:
    loop.run_until_complete(client.logout())

    args.persist.write_text(chain.serialize())
finally:
    loop.close()
