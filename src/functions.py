from src.roles import participant_role
from datetime import datetime


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I am here to admin your wedding :D")


def add_group(update, context):
    for member in update.message.new_chat_members:
        update.message.reply_text("Bienvenido a nuestra boda {username}!\n"
                                  "Hasta las 18:30 del 11 de Octubre de 2020 no podrás enviar nada a este grupo!".
                                  format(username=member.username))

        context.bot.restrict_chat_member(update.message.chat.id, member.id, participant_role,
                                         until_date=datetime(2020, 10, 11, 18, 30))

        update.message.reply_text(f" {member.username} you have no power here!!")

