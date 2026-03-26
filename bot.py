import logging
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ТВОЙ ТОКЕН (замени)
TOKEN = '8661389421:AAEBgbp0S5XNihx3ySY2zL80l_rBK-KPWfQ'

# Адрес твоего сайта (локально)
SITE_URL = 'http://127.0.0.1:8100'

# Включаем логи
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Приветствие"""
    await update.message.reply_text(
        " Привет! Я бот Хранителя Семени.\n\n"
        "Я умею:\n"
        "/battles — последние битвы\n"
        "/stats — статистика\n"
        "/help — помощь\n\n"
        "Погнали, братишка!"
    )

async def missions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Последние битвы"""
    try:
        response = requests.get(f'{SITE_URL}/api/missions/')
        if response.status_code == 200:
            battles = response.json()[:5]
            if battles:
                text = " *Последние битвы:*\n\n"
                for b in battles:
                    text += f"• {b['title']} — {b['date'][:16]}\n"
                await update.message.reply_text(text, parse_mode='Markdown')
            else:
                await update.message.reply_text("Пока нет битв. Используй способности!")
        else:
            await update.message.reply_text("Ошибка загрузки битв. Попробуй позже.")
    except:
        await update.message.reply_text("Не могу подключиться к сайту.")

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Статистика"""
    try:
        # Получаем силу семени
        response = requests.get(f'{SITE_URL}/api/seed/')
        if response.status_code == 200:
            seed = response.json()['value']
            await update.message.reply_text(f"🌱 Сила Семени: *{seed}*", parse_mode='Markdown')
        else:
            await update.message.reply_text("Ошибка получения статистики.")
    except:
        await update.message.reply_text("Не могу подключиться к сайту.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Помощь"""
    await update.message.reply_text(
        "🤖 *Команды бота:*\n\n"
        "/start — приветствие\n"
        "/battles — последние битвы\n"
        "/stats — сила семени\n"
        "/help — помощь\n\n"
        " Сайт: http://keeper.vercel.app\n"
        " Хранитель Семени — защищает чистый код!"
    )

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("battles", missions))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("help", help_command))
    
    print(" Бот запущен!")
    app.run_polling()

if __name__ == '__main__':
    main()