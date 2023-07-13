from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from voice import text_to_file
import sys


TOKEN = r"C:\Users\dshylko\Documents\new_4.txt"
with open(TOKEN) as f:
    token = f.read()

async def hello(update, context):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help_handler(update, context):
    help_text = """Для того, чтобы преобразовать текст в аудио, используйте наш бот. Пришлите любой текст обычным сообщением и он превратится в аудио-сообщение."""
    await update.message.reply_text(help_text)

async def reply(update, context):
    file_name = text_to_file(update.message.text)
    # await update.message.reply_text("Проговорим текст: " + update.message.text)
    await update.message.reply_voice(voice=open(file_name, 'rb'))


app = ApplicationBuilder().token(token).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", help_handler))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()