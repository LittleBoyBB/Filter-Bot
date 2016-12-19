#coding: utf-8

import telepot, time

TOKEN = ""# Seu token entre aspas
bot = telepot.Bot(TOKEN)
print("Conectado")

def handle(msg):
	tipomsg, tchat, chat_id = telepot.glance(msg)
	print(tipomsg, tchat, chat_id)

	msgid = msg['message_id']
	usermsg = msg['text'].split(' ')

	for palavra in usermsg:
		if palavra == 'palavra':# Se a mensagem for 'palavra' o bot responde
			bot.sendMessage(chat_id, "Você disse palavra!", reply_to_message_id=msgid)# Aqui é a resposta que o bot envia de acordo com a 'palavra'

bot.message_loop(handle)

while 1:
    time.sleep(10)
