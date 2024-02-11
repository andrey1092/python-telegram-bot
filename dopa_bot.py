from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
import logging
import threading
import time

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = 'seu_token_aqui'

GRUPO_DESTINO_ID = 'id_do_grupo_destino'

MENSAGEM_AUTOMATICA = 'Sua mensagem automática aqui.'

def extrair_e_adicionar(update, context):
    try:
        grupo_origem_id = update.message.chat_id
        membros = context.bot.get_chat_members(chat_id=grupo_origem_id)
        for member in membros:
            context.bot.add_chat_members(chat_id=GRUPO_DESTINO_ID, user_ids=member.user.id)
        update.message.reply_text('Membros extraídos e adicionados ao grupo de destino com sucesso.')
    except Exception as e:
        logging.error(f'Erro ao extrair e adicionar membros: {e}')
        update.message.reply_text('Ocorreu um erro ao extrair e adicionar membros.')

def procurar_e_enviar_mensagem(bot):
    try:
        while True:
            time.sleep(600)  # Espera 10 minutos
    except Exception as e:
        logging.error(f'Erro ao procurar e enviar mensagem: {e}')

def controle_grupo(update, context):
    try:
        pass
    except Exception as e:
        logging.error(f'Erro ao controlar o grupo: {e}')
        update.message.reply_text('Ocorreu um erro ao controlar o grupo.')

def enviar_mensagem_automatica(bot):
    try:
        while True:
            bot.send_message(chat_id=GRUPO_DESTINO_ID, text=MENSAGEM_AUTOMATICA)
            time.sleep(600)  # Espera 10 minutos
    except Exception as e:
        logging.error(f'Erro ao enviar mensagem automática: {e}')

def main():
    try:
        updater = Updater(token=TOKEN, use_context=True)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("extrair", extrair_e_adicionar))
        dispatcher.add_handler(CommandHandler("controlargrupo", controle_grupo))
        updater.start_polling()
        updater.idle()
        threading.Thread(target=enviar_mensagem_automatica, args=(updater.bot,)).start()
        threading.Thread(target=procurar_e_enviar_mensagem, args=(updater.bot,)).start()
    except Exception as e:
        logging.error(f'Erro ao iniciar o bot: {e}')

if __name__ == '__main__':
    main()
