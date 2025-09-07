"""
Bot configuration settings
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Bot settings
BOT_TOKEN = os.getenv("8306300764:AAHW32LignvebTsLcQA4Cuar9sQrX9mnvkc") #(bot token revoke qilingan)

# Moderation settings
FORBIDDEN_WORDS = ["ko't", "ahmoq", "so'z1", "so'z2" "so'kinish2", "yomonso'z"]

# Progressive punishment durations (in seconds)
PUNISHMENT_DURATIONS = {
    1: 300,      # First offense: 5 minutes
    2: 900,      # Second offense: 15 minutes
    3: 3600,     # Third offense: 1 hour
    4: 86400     # Fourth offense: 1 day
}

# Time window for counting violations (24 hours)
VIOLATION_WINDOW = 86400  # 24 hours in seconds

# Message templates
BLOCKED_MESSAGE_TEMPLATE = """❌ Siz taqiqlangan so'z ishlatdingiz!

🚫 Sabab: "{word}" so'zi taqiqlangan
⏱ Blok muddati: {duration}
📊 Bugungi kunlik buzishlar soni: {count}/4

Iltimos, guruh qoidalariga rioya qiling."""

# Group notification template with clickable profile and blue ID
GROUP_NOTIFICATION_TEMPLATE = """🚫 **Foydalanuvchi bloklandi**

👤 Foydalanuvchi: [{user_name}](tg://user?id={user_id}) `#{user_id}`
🚫 Sabab: "{word}" so'zi guruhda taqiqlangan so'z hisoblanadi
⏱ Blok muddati: {duration}
📊 Bu foydalanuvchining {count}-chi marta qoida buzishi

_Bu xabar foydalanuvchi blokdan chiqgach o'chadi._"""

def format_duration(seconds):
    """Format duration in human readable format"""
    if seconds < 60:
        return f"{seconds} soniya"
    elif seconds < 3600:
        minutes = seconds // 60
        return f"{minutes} daqiqa"
    elif seconds < 86400:
        hours = seconds // 3600
        return f"{hours} soat"
    else:
        days = seconds // 86400
        return f"{days} kun"
