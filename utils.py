import re

from typing import AsyncGenerator, List

from pyrogram.types import Message

from keyboards import ye_kazik_inline_keyboard


async def reverse_order_in_history_messages(messages: AsyncGenerator):
    reverse_message = [message async for message in messages]
    return reverse_message[::-1]



async def clone(client, bot, from_channel, to_channel, admin_account='', promocode='',reviews_channel='', mines_bot='', brawl_bot='', coin_bot='', live_channel='', messages_limit=1):
    messages: AsyncGenerator[Message, None] = client.get_chat_history(chat_id=from_channel, limit=messages_limit)
    reversed_messages: List[Message] = await reverse_order_in_history_messages(messages)

    for message in reversed_messages:
        if message:
            # Text
            if message.text:
                text = message.text
                text = re.sub(r'(?i)промокод\s*:\s*.*', 'промокод: ' + promocode, text, flags=re.IGNORECASE)
                text = re.sub(r'(?i)промо\s*:\s*.*', 'промо: ' + promocode, text, flags=re.IGNORECASE)
                text = re.sub(r'@nego\s*[^ ]*', '@' + admin_account, text, flags=re.IGNORECASE)
                text = re.sub(r'отзывами\s*-\s*.*', 'отзывами - ' + reviews_channel, text, flags=re.IGNORECASE)
                text = re.sub(r'@mines\s*[^ ]*', '@' + mines_bot, text, flags=re.IGNORECASE)
                text = re.sub(r'@brawl\s*[^ ]*', '@' + brawl_bot, text, flags=re.IGNORECASE)
                text = re.sub(r'@coin\s*[^ ]*', '@' + coin_bot, text, flags=re.IGNORECASE)
                text = re.sub(r'https://t\.me/\+NXf405S5gPM2YzFi[^ ]*', live_channel, text, flags=re.IGNORECASE)
                if message.reply_markup or ('https' in text) or ('@' in text):
                    bot.send_message(chat_id=to_channel, text=text, reply_markup=ye_kazik_inline_keyboard)
                else:
                    bot.send_message(chat_id=to_channel, text=text)
            # Photo
            if message.photo:
                ph = await client.download_media(message.photo.file_id)
                if message.caption:
                    caption = message.caption
                    caption = re.sub(r'(?i)промокод\s*:\s*.*', 'промокод: ' + promocode, caption, flags=re.IGNORECASE)
                    caption = re.sub(r'(?i)промо\s*:\s*.*', 'промо: ' + promocode, caption, flags=re.IGNORECASE)
                    caption = re.sub(r'@nego\s*[^ ]*', '@' + admin_account, caption, flags=re.IGNORECASE)
                    caption = re.sub(r'отзывами\s*-\s*.*', 'отзывами - ' + reviews_channel, caption,
                                     flags=re.IGNORECASE)
                    caption = re.sub(r'@mines\s*[^ ]*', '@' + mines_bot, caption, flags=re.IGNORECASE)
                    caption = re.sub(r'@brawl\s*[^ ]*', '@' + brawl_bot, caption, flags=re.IGNORECASE)
                    caption = re.sub(r'@coin\s*[^ ]*', '@' + coin_bot, caption, flags=re.IGNORECASE)
                    caption = re.sub(r'https://t\.me/\+NXf405S5gPM2YzFi[^ ]*', live_channel, caption,
                                     flags=re.IGNORECASE)
                    if message.reply_markup or ('https' in caption) or ('@' in caption):
                        bot.send_photo(chat_id=to_channel, photo=open(ph, 'rb'), caption=caption, reply_markup=ye_kazik_inline_keyboard)
                    else:
                        bot.send_photo(chat_id=to_channel, photo=open(ph, 'rb'), caption=caption)
                else:
                    bot.send_photo(chat_id=to_channel, photo=open(ph, 'rb'))
            # Animation
            if message.animation:
                animation = await client.download_media(message.animation.file_id)
                if message.caption:
                    caption = message.caption
                    caption = re.sub(r'(?i)промокод\s*:\s*.*', 'промокод: ' + promocode, caption, flags=re.IGNORECASE)
                    caption = re.sub(r'(?i)промо\s*:\s*.*', 'промо: ' + promocode, caption, flags=re.IGNORECASE)
                    caption = re.sub(r'@nego\s*[^ ]*', '@' + admin_account, caption, flags=re.IGNORECASE)
                    caption = re.sub(r'отзывами\s*-\s*.*', 'отзывами - ' + reviews_channel, caption, flags=re.IGNORECASE)
                    caption = re.sub(r'@mines\s*[^ ]*', '@' + mines_bot, caption, flags=re.IGNORECASE)
                    caption = re.sub(r'@brawl\s*[^ ]*', '@' + brawl_bot, caption, flags=re.IGNORECASE)
                    caption = re.sub(r'@coin\s*[^ ]*', '@' + coin_bot, caption, flags=re.IGNORECASE)
                    caption = re.sub(r'https://t\.me/\+NXf405S5gPM2YzFi[^ ]*', live_channel, caption,
                                     flags=re.IGNORECASE)
                    if message.reply_markup or ('https' in caption) or ('@' in caption):
                        bot.send_animation(chat_id=to_channel, animation=open(animation, 'rb'), caption=caption,
                                           reply_markup=ye_kazik_inline_keyboard)
                    else:
                        bot.send_animation(chat_id=to_channel, animation=open(animation, 'rb'), caption=caption)
                else:
                    if message.reply_markup:
                        bot.send_animation(chat_id=to_channel, animation=open(animation, 'rb'),
                                           reply_markup=ye_kazik_inline_keyboard)
                    else:
                        bot.send_animation(chat_id=to_channel, animation=open(animation, 'rb'))
            # Circle
            if message.video_note:
                video_note = await client.download_media(message.video_note.file_id)
                if message.caption:
                    caption = message.caption
                    caption = re.sub(r'(?i)промокод\s*:\s*.*', 'промокод: ' + promocode, caption, flags=re.IGNORECASE)
                    caption = re.sub(r'(?i)промо\s*:\s*.*', 'промо: ' + promocode, caption, flags=re.IGNORECASE)
                    caption = re.sub(r'@nego\s*[^ ]*', '@' + admin_account, caption, flags=re.IGNORECASE)
                    caption = re.sub(r'отзывами\s*-\s*.*', 'отзывами - ' + reviews_channel, caption, flags=re.IGNORECASE)
                    caption = re.sub(r'@mines\s*[^ ]*', '@' + mines_bot, caption, flags=re.IGNORECASE)
                    caption = re.sub(r'@brawl\s*[^ ]*', '@' + brawl_bot, caption, flags=re.IGNORECASE)
                    caption = re.sub(r'@coin\s*[^ ]*', '@' + coin_bot, caption, flags=re.IGNORECASE)
                    caption = re.sub(r'https://t\.me/\+NXf405S5gPM2YzFi[^ ]*', live_channel, caption, flags=re.IGNORECASE)
                    if message.reply_markup or ('https' in caption) or ('@' in caption):
                        bot.send_video_note(to_channel, open(video_note, 'rb'), caption=caption,
                                            reply_markup=ye_kazik_inline_keyboard)
                    else:
                        bot.send_video_note(to_channel, open(video_note, 'rb'), caption=caption)
                else:
                    if message.reply_markup:
                        bot.send_video_note(to_channel, open(video_note, 'rb'),
                                            reply_markup=ye_kazik_inline_keyboard)
                    else:
                        bot.send_video_note(to_channel, open(video_note, 'rb'))
            # Video
            if message.video:
                video = await client.download_media(message.video.file_id)
                if message.caption:
                    caption = message.caption
                    caption = re.sub(r'(?i)промокод\s*:\s*.*', 'промокод: ' + promocode, caption, flags=re.IGNORECASE)
                    caption = re.sub(r'(?i)промо\s*:\s*.*', 'промо: ' + promocode, caption, flags=re.IGNORECASE)
                    caption = re.sub(r'@nego\s*[^ ]*', '@' + admin_account, caption, flags=re.IGNORECASE)
                    caption = re.sub(r'отзывами\s*-\s*.*', 'отзывами - ' + reviews_channel, caption, flags=re.IGNORECASE)
                    caption = re.sub(r'@mines\s*[^ ]*', '@' + mines_bot, caption, flags=re.IGNORECASE)
                    caption = re.sub(r'@brawl\s*[^ ]*', '@' + brawl_bot, caption, flags=re.IGNORECASE)
                    caption = re.sub(r'@coin\s*[^ ]*', '@' + coin_bot, caption, flags=re.IGNORECASE)
                    caption = re.sub(r'https://t\.me/\+NXf405S5gPM2YzFi[^ ]*', live_channel, caption, flags=re.IGNORECASE)
                    if message.reply_markup or ('https' in caption) or ('@' in caption):
                        bot.send_video(
                            chat_id=to_channel,
                            video=open(video, 'rb'),
                            caption=caption,
                            reply_markup=ye_kazik_inline_keyboard
                        )
                    else:
                        bot.send_video(
                            chat_id=to_channel,
                            video=open(video, 'rb'),
                            caption=caption
                        )
                else:
                    if message.reply_markup:
                        bot.send_video(chat_id=to_channel, video=open(video, 'rb'), reply_markup=ye_kazik_inline_keyboard)
                    else:
                        bot.send_video(chat_id=to_channel, video=open(video, 'rb'))
            # Audiio
            if message.audio:
                audio = await client.download_media(message.audio.file_id)
                bot.send_audio(chat_id=to_channel, audio=open(audio, 'rb'))
            # Voice
            if message.voice:
                voice = await client.download_media(message.voice.file_id)
                bot.send_voice(chat_id=to_channel, voice=open(voice, 'rb'))
            # Document
            if message.document:
                document = await client.download_media(message.document.file_id)
                bot.send_document(chat_id=to_channel, document=open(document, 'rb'))
            # Poll
            if message.poll:
                question = message.poll.question
                options = []
                for option in message.poll.options:
                    options.append(option.text)
                bot.send_poll(chat_id=to_channel, question=question, options=options)
        else:
            pass
