# bot/config.py
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot Configuration
OWNER_ID: int = 1042929958286266540

# Discord
DISCORD_TOKEN: str = os.getenv("DISCORD_TOKEN", "")

# Roblox
ROBLOX_API_KEY: str = os.getenv("ROBLOX_API_KEY", "")
API_URL: str = os.getenv("API_URL", "https://api.roblox.com")  # Ajusta según tu endpoint real

# Database
DATABASE_PATH: str = "database/bot.db"

# Logging
LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

# Permissions
ALLOWED_ROLES: list[int] = [
    # Agrega IDs de roles de staff aquí
    123456789012345678,  # Ejemplo
]

# Cooldowns (in seconds)
COMMAND_COOLDOWN: int = 5
BAN_COOLDOWN: int = 30

# Validation
if not DISCORD_TOKEN:
    raise ValueError("DISCORD_TOKEN no está configurado en las variables de entorno")

if not ROBLOX_API_KEY:
    print("⚠️  ADVERTENCIA: ROBLOX_API_KEY no configurada")
