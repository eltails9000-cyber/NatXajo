# bot/main.py
import asyncio
import os
import sys
from pathlib import Path

import discord
from dotenv import load_dotenv

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from core.client import CustomBot
from core.logger import setup_logger
from config import DISCORD_TOKEN


async def main():
    # Setup logging
    logger = setup_logger()
    logger.info("Iniciando el bot de Discord...")

    # Create bot instance
    bot = CustomBot()

    @bot.event
    async def on_ready():
        logger.info(f"Bot conectado como {bot.user} (ID: {bot.user.id})")
        logger.info(f"Conectado a {len(bot.guilds)} servidores")
        try:
            synced = await bot.tree.sync()
            logger.info(f"Comandos slash sincronizados: {len(synced)}")
        except Exception as e:
            logger.error(f"Error al sincronizar comandos: {e}")

    # Load cogs
    cogs = [
        "cogs.events",
        "cogs.roblox",
        "cogs.owner",
    ]

    for cog in cogs:
        try:
            await bot.load_extension(cog)
            logger.info(f"Cog cargado: {cog}")
        except Exception as e:
            logger.error(f"Error al cargar {cog}: {e}")

    # Run the bot
    try:
        async with bot:
            await bot.start(DISCORD_TOKEN)
    except KeyboardInterrupt:
        logger.info("Bot detenido manualmente")
    except Exception as e:
        logger.critical(f"Error crítico al iniciar el bot: {e}")


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
