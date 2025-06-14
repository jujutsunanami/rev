from pyrogram import filters
from bot import app, data, sudo_users
from bot.helper.utils import add_task

video_mimetype = [
  "video/x-flv",
  "video/mp4",
  "application/x-mpegURL",
  "video/MP2T",
  "video/3gpp",
  "video/quicktime",
  "video/x-msvideo",
  "video/x-ms-wmv",
  "video/x-matroska",
  "video/webm",
  "video/x-m4v",
  "video/quicktime",
  "video/mpeg"
  ]

@app.on_message(filters.incoming & filters.command(['start', 'help']))
def help_message(app, message):
    message.reply_text(f"𝗛𝗲𝘆 {message.from_user.mention()}\n🤣𝗕𝗮𝗸𝗮 𝗬𝗼𝘂'𝗿𝗲 𝗕𝗮𝗻𝗻𝗲𝗱 𝗧𝗼 𝗨𝘀𝗲 𝗠𝗲\n📞𝗖𝗼𝗻𝘁𝗮𝗰𝘁 𝗠𝘆 𝗔𝗱𝗺𝗶𝗻 𝗧𝗼 𝗨𝗻𝗯𝗮𝗻\n🤔𝙒𝙖𝙞𝙩 𝙊𝙬𝙣𝙚𝙧 𝘿𝙤𝙚𝙨𝙣'𝙩 𝙃𝙖𝙫𝙚 𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚", quote=True)

@app.on_message(filters.user(sudo_users) & filters.incoming & (filters.video | filters.document))
def encode_video(app, message):
    if message.document:
      if not message.document.mime_type in video_mimetype:
        message.reply_text("```𝙎𝙤𝙢𝙚𝙩𝙝𝙞𝙣𝙜 𝙒𝙚𝙣𝙩 𝙒𝙧𝙤𝙣𝙜 𝘼𝙨 𝙏𝙖𝙩𝙠𝙖𝙡 𝙏𝙞𝙘𝙠𝙚𝙩 𝘽𝙤𝙤𝙠𝙞𝙣𝙜\n𝙇𝙤𝙜𝙨 𝙎𝙚𝙣𝙩 𝙏𝙤 𝘾𝙝𝙖𝙣𝙣𝙚𝙡```", quote=True)
        return
    message.reply_text("```𝙁𝙪𝙘𝙠 𝙎𝙖𝙠𝙚 𝙎𝙤 𝙇𝙤𝙣𝙜```", quote=True)
    data.append(message)
    if len(data) == 1:
      add_task(message)

app.run()