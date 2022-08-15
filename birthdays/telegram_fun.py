import birthdays_functions as bd_fun
from models.response import Status
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater('5442107621:AAGb62I0emPZZ-b52BeqBVBaq5zjTDRwS5k',
                  use_context=True)


def start_bot(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Hola soy el pombeBOT 💀, escribe /help para listar todo lo que puedo hacer por vos!!'
    )


def help_bot(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Escribe:' +
        '\n💀/add *dni nombre apellido fecha de naciemiento (DD-MM-AAAA) mensaje de saludo* '
        + 'para agregar un nuevo cumpleaños'
        + '\n💀/delete *dni* para borrar un cumpleaños' +
        '\n💀/list para listar todos los cumpleaños registrados')


def add_one_birthday_bot(update: Update, context: CallbackContext):
    if len(context.args) != 5:
        return update.message.reply_text(
            'Entrada no válida: revise la cantidad de parametros ingresados')
    
    dni = context.args[0]
    name = context.args[1]
    lastname = context.args[2]
    birthday = context.args[3]
    custom_greetings = context.args[4]

    result = bd_fun.add_one_birthday(dni, name, lastname, birthday,
                                     custom_greetings)

    return update.message.reply_text(result.get_msg)


def unknown(update: Update, context: CallbackContext):
    error_msg = f'Perdón, no fui capaz de entender tu mensaje {update.message.text}💀.'
    update.message.reply_text(error_msg)


updater.dispatcher.add_handler(CommandHandler('start', start_bot))
updater.dispatcher.add_handler(CommandHandler('help', help_bot))
updater.dispatcher.add_handler(CommandHandler('add', add_one_birthday_bot))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))

updater.start_polling()
