import re
from typing import AsyncGenerator, List

from pyrogram.types import Message

from keyboards import lucky_jet_inline_keyboard


async def reverse_order_in_history_messages(messages: AsyncGenerator):
    reverse_message = [message async for message in messages]
    return reverse_message[::-1]


async def clone(client, bot, from_channel, to_channel, admin_account='', promocode='', messages_limit=1, ):
    messages: AsyncGenerator[Message, None] = client.get_chat_history(chat_id=from_channel, limit=messages_limit)
    reversed_messages: List[Message] = await reverse_order_in_history_messages(messages)

    for message in reversed_messages:
        if message:
            # Text
            if message.text:
                text = message.text
                text = re.sub(r'(?i)(промокод:).*', r'\1 ' + promocode, text)
                text = re.sub(r'(?i)@([^ ]+)', '@' + admin_account, text)
                if message.reply_markup:
                    await bot.send_message(chat_id=to_channel, text=text, reply_markup=lucky_jet_inline_keyboard)
                else:
                    await bot.send_message(chat_id=to_channel, text=text)
            # Photo
            if message.photo:
                if message.caption:
                    caption = message.caption
                    caption = re.sub(r'(?i)(промокод:).*', r'\1 ' + promocode, caption)
                    caption = re.sub(r'(?i)@([^ ]+)', '@' + admin_account, caption)
                    if message.reply_markup:
                        await bot.send_message(
                            chat_id=to_channel,
                            text=caption,
                            reply_markup=lucky_jet_inline_keyboard
                        )
                    else:
                        await bot.send_message(
                            chat_id=to_channel,
                            text=caption
                        )
                else:
                    photo = await message.download(in_memory=True)
                    if message.reply_markup:
                        await bot.send_photo(chat_id=to_channel, photo=photo, reply_markup=lucky_jet_inline_keyboard)
                    else:
                        await bot.send_photo(chat_id=to_channel, photo=photo)
            # Animation
            if message.animation:
                animation = await message.download(in_memory=True)
                if message.caption:
                    caption = message.caption
                    caption = re.sub(r'(?i)(промокод:).*', r'\1 ' + promocode, caption)
                    caption = re.sub(r'(?i)@([^ ]+)', '@' + admin_account, caption)
                    if message.reply_markup:
                        await bot.send_animation(chat_id=to_channel, animation=animation, caption=caption,
                                                 reply_markup=lucky_jet_inline_keyboard)
                    else:
                        await bot.send_animation(chat_id=to_channel, animation=animation, caption=caption)
                else:
                    if message.reply_markup:
                        await bot.send_animation(chat_id=to_channel, animation=animation,
                                                 reply_markup=lucky_jet_inline_keyboard)
                    else:
                        await bot.send_animation(chat_id=to_channel, animation=animation)
            # Circle
            if message.video_note:
                video_note = await message.download(in_memory=True)
                if message.caption:
                    caption = message.caption
                    caption = re.sub(r'(?i)(промокод:).*', r'\1 ' + promocode, caption)
                    caption = re.sub(r'(?i)@([^ ]+)', '@' + admin_account, caption)
                    if message.reply_markup:
                        await bot.send_video_note(chat_id=to_channel, video_note=video_note, caption=caption,
                                                  reply_markup=lucky_jet_inline_keyboard)
                    else:
                        await bot.send_video_note(chat_id=to_channel, video_note=video_note, caption=caption)
                else:
                    if message.reply_markup:
                        await bot.send_video_note(chat_id=to_channel, video_note=video_note,
                                                  reply_markup=lucky_jet_inline_keyboard)
                    else:
                        await bot.send_video_note(chat_id=to_channel, video_note=video_note)
            # Video
            if message.video:
                if message.caption:
                    caption = message.caption
                    caption = re.sub(r'(?i)(промокод:).*', r'\1 ' + promocode, caption)
                    caption = re.sub(r'(?i)@([^ ]+)', '@' + admin_account, caption)
                    if message.reply_markup:
                        await bot.send_message(
                            chat_id=to_channel,
                            text=caption,
                            reply_markup=lucky_jet_inline_keyboard
                        )
                    else:
                        await bot.send_message(
                            chat_id=to_channel,
                            text=caption
                        )
                else:
                    video = await message.download(in_memory=True)
                    if message.reply_markup:
                        await bot.send_video(chat_id=to_channel, video=video, reply_markup=lucky_jet_inline_keyboard)
                    else:
                        await bot.send_video(chat_id=to_channel, video=video)
            # Audiio
            if message.audio:
                audio = await message.download(in_memory=True)
                await bot.send_audio(chat_id=to_channel, audio=audio)
            # Document
            if message.document:
                document = await message.download(in_memory=True)
                await bot.send_document(chat_id=to_channel, document=document)
            # Poll
            if message.poll:
                poll = message.poll
                await bot.send_poll(chat_id=to_channel, poll=poll)
        else:
            pass
