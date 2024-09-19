import os
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
import sys

START_MSG = "Hi {},\nThis is a simple bot to forward all messages from one channel to other.\n\n⚠️Warning: Your account may get banned if you forward more files from private channels. Use at your own risk!"
HELP_MSG = "Available commands:\n\n/index - To index a channel\n/forward - To start forwarding\n/total - Count total messages in DB\n/status - Check current status\n/help - Help data\n/stop - To stop all running processes."

buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("✨ Hᴇʟᴘ ✨", callback_data="help"),
            InlineKeyboardButton("⚠️ Hᴏᴡ Dᴏᴇs I Wᴏʀᴋ? ⚠️", callback_data="abt")
        ],
        [
            InlineKeyboardButton("🪄 Sᴏᴜʀᴄᴇ Cᴏᴅᴇ 🪄", url="https://t.me/CT_Arena/135"),
            InlineKeyboardButton("💫 Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ 💫", url="https://t.me/CT_Arena")
        ]
    ]
)

@Client.on_message(filters.private & filters.command('start'))
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=START_MSG.format(message.from_user.first_name),
        reply_markup=buttons,
        parse_mode="markdown_v2"
    )

@Client.on_message(filters.command("stop"))
async def stop_button(bot, message):
    if str(message.from_user.id) not in Config.OWNER_ID:
        return
    msg = await bot.send_message(
        text="Stopping all processes...",
        chat_id=message.chat.id
    )
    await asyncio.sleep(1)
    await msg.edit("All Processes Stopped and Restarted")
    os.execl(sys.executable, sys.executable, *sys.argv)

@Client.on_message(filters.private & filters.command('help'))
async def help(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=HELP_MSG,
        parse_mode="markdown_v2"
    )

@Client.on_callback_query(filters.regex(r'^help$'))
async def cb_help(bot, cb):
    await cb.message.edit_text(HELP_MSG)

@Client.on_callback_query(filters.regex(r'^abt$'))
async def cb_abt(bot, cb):
    await cb.message.edit_text("Talking is cheap, read code.",
    reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🔥 Source 🔥", url="https://t.me/CT_Arena/135"),
            ]
        ]
    ))
