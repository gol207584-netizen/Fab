from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from ai import ask_ai
from database import chat_history

TOKEN = "PUT_TELEGRAM_TOKEN"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💊 Drug AI Bot جاهز!")

async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_history[update.effective_user.id] = []
    await update.message.reply_text("🧹 تم المسح")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text

    msg = await update.message.reply_text("🧠 جاري التحليل...")

    answer = ask_ai(user_id, text)

    await msg.delete()
    await update.message.reply_text(answer)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("clear", clear))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
