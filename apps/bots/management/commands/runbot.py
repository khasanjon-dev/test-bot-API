import asyncio
import logging

from aiogram.fsm.storage.memory import MemoryStorage
from django.core.management.base import BaseCommand

from bots.root.dispatcher import get_dispatcher
from bots.utils.set_bot_commands import set_default_commands
from loader import bot


async def start_bot():
    dp = get_dispatcher(storage=MemoryStorage())
    await set_default_commands(bot)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


class Command(BaseCommand):
    help = 'RUN COMMAND: python manage.py runbot'

    def handle(self, *args, **options):
        logging.basicConfig(level=0)
        asyncio.run(start_bot())
