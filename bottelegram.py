import telebot

KEY_API = '7369650345:AAGhR-_wsrhbdcJ6UtmEcilj4y6GpZWOypQ'

bot = telebot.TeleBot(token=KEY_API)


@bot.message_handler(commands=['pizza'])
def pizza(message: str):
    bot.send_message(
        chat_id=message.chat.id,
        text='Sua pizza está a caminho!'
    )

@bot.message_handler(commands=['hamburguer'])
def hamburguer(message: str):
    bot.send_message(
        chat_id=message.chat.id,
        text='Seu hamburguer está a caminho!'
    )

@bot.message_handler(commands=['salada'])
def salada(message: str):
    bot.send_message(
        chat_id=message.chat.id,
        text='Não tem salada, Sorry! Clique aqui para iniciar: /iniciar'
    )

@bot.message_handler(commands=['option1'])
def option1(message: str):
    text = """
        O que você vai querer?(Clique em uma das opções)
        /pizza Pizza
        /hamburguer Hamburguer
        /salada Salada
    """
    bot.reply_to(
        message=message,
        text=text
    )

@bot.message_handler(commands=['option2'])
def option2(message: str):
    bot.send_message(
        chat_id=message.chat.id,
        text='Para reclamações, entre em contato no email: reclame_aqui@blabla.com'
    )

@bot.message_handler(commands=['option3'])
def option3(message: str):
    bot.send_message(
        chat_id=message.chat.id,
        text='Valeu! O Lucas mandou um abraço de volta! ;)'
    )

def verificar(message: str) -> bool:
    return True

@bot.message_handler(func=verificar)
def response(message: str):
    text = """
        Escolha uma opção para continuar(Clique no item):
        /option1: Fazer um pedido
        /option2: Reclamar de um pedido
        /option3: Mandar um abraço para o Lucas
        * Responder qualquer outra coisa não vai funtionar! Clique em uma das opções.
    """
    bot.reply_to(
        message=message,
        text=text
    )
    
bot.polling()