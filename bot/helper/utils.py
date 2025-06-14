import os
from bot import data, download_dir
from pyrogram.types import Message
from pyrogram.errors.exceptions.bad_request_400 import MessageNotModified
from .ffmpeg_utils import encode, get_thumbnail, get_duration, get_width_height

def on_task_complete():
    del data[0]
    if len(data) > 0:
      add_task(data[0])

def add_task(message: Message):
    try:
      msg = message.reply_text("```📥𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙𝙞𝙣𝙜 𝙏𝙝𝙞𝙨 𝙑𝙞𝙙𝙚𝙤 𝙁𝙪𝙘𝙠 𝙎𝙖𝙠𝙚 𝙎𝙤 𝙇𝙤𝙣𝙜```", quote=True)
      filepath = message.download(file_name=download_dir)
      msg.edit("```🗜️𝙃𝙖 𝙍𝙚𝙡𝙖𝙭 𝙁𝙞𝙣𝙖𝙡𝙡𝙮 𝙄 𝙎𝙩𝙖𝙧𝙩𝙚𝙙 𝙀𝙣𝙘𝙤𝙙𝙞𝙣𝙜🗜️```")
      new_file = encode(filepath)
      if new_file:
        msg.edit("```🧐𝗜 𝗧𝗵𝗶𝗻𝗸 𝗡𝗼𝘄 𝗜𝘁'𝘀 𝗙𝗶𝗻𝗶𝘀𝗵𝗲𝗱 𝗟𝗲𝘁 𝗠𝗲 𝗖𝗵𝗲𝗰𝗸```")
        duration = get_duration(new_file)
        thumb = get_thumbnail(new_file, download_dir, duration / 4)
        width, height = get_width_height(new_file)
        msg.edit("```⬆️𝙁𝙞𝙣𝙖𝙡𝙡𝙮 𝙎𝙩𝙖𝙧𝙩𝙚𝙙 𝙐𝙥𝙡𝙤𝙖𝙙𝙞𝙣𝙜 𝙁𝙪𝙘𝙠 𝙎𝙖𝙠𝙚 𝙏𝙝𝙞𝙨 𝙎𝙚𝙧𝙫𝙚𝙧 𝙎𝙝𝙞𝙩⬆️```")
        message.reply_video(new_file, quote=True, supports_streaming=True, thumb=thumb, duration=duration, width=width, height=height)
        os.remove(new_file)
        os.remove(thumb)
        msg.edit("```𝗜 𝗱𝗼𝗻'𝘁 𝗵𝗮𝘃𝗲 𝘁𝗵𝗲 𝘁𝗶𝗺𝗲 𝘁𝗼 𝘁𝗵𝗶𝗻𝗸 𝗮𝗯𝗼𝘂𝘁 𝘄𝗵𝗮𝘁 𝘀𝗼𝗺𝗲𝗼𝗻𝗲 𝗲𝗹𝘀𝗲 𝘁𝗵𝗶𝗻𝗸𝘀 𝗼𝗳 𝗺𝗲```")
      else:
        msg.edit("```𝙎𝙤𝙢𝙚𝙩𝙝𝙞𝙣𝙜 𝙒𝙚𝙣𝙩 𝙒𝙧𝙤𝙣𝙜 𝘼𝙨 𝙏𝙖𝙩𝙠𝙖𝙡 𝙏𝙞𝙘𝙠𝙚𝙩 𝘽𝙤𝙤𝙠𝙞𝙣𝙜```")
        os.remove(filepath)
    except MessageNotModified:
      pass
    except Exception as e:
      msg.edit(f"```{e}```")
    on_task_complete()
