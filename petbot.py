import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio

TOKEN = '7599796662:AAGw8KTnOa_hOq5cMOs_MBPRi8IWmX5gwao'

# Configura el logging
logging.basicConfig(level=logging.INFO)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    commands = """
    Aquí tienes los comandos disponibles:
    /start - Inicia la conversación
    /help - Muestra este mensaje de ayuda
    /feed - Alimenta a tu mascota
    /play - Juega con tu mascota
    """
    await update.message.reply_text(commands)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('¡Hola! Soy tu mascota virtual. ¿Qué te gustaría hacer? Escribe /help para saber más.')

async def feed_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('¡Gracias por alimentar a tu mascota! 🥗')

async def play_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('¡Vamos a jugar! 🎾')

def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()
    app.update_queue.timeout = 30
    
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("feed", feed_command))
    app.add_handler(CommandHandler("play", play_command))

    app.run_polling(allowed_updates=Update.ALL_TYPES)

# Este bloque maneja el caso del bucle de eventos ya en ejecución
if __name__ == '__main__':
    main()
