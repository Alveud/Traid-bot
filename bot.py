from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "7719551438:AAEZPE00zzdQPxZSjt5pypne0q1YGY6qrFU"

keyboard = [
    ["🟢 Long", "🔴 Short"],
    ["📊 BTC", "⚙️ Настройки"]
]
markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет, старик! 🤖 Выбирай команду:",
        reply_markup=markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "🟢 Long":
        await update.message.reply_text("Открываем Long 🚀")
    elif text == "🔴 Short":
        await update.message.reply_text("Шортим рынок 🛑")
    elif text == "📊 BTC":
        await update.message.reply_text("Скоро будет цена BTC 💸")
    elif text == "⚙️ Настройки":
        await update.message.reply_text("Настроек пока нет 🛠️")
    else:
        await update.message.reply_text("Не понял тебя 🤔")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🚀 Бот запущен с кнопками")
    app.run_polling()
