import birthdays_functions as bd_fun
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater('5442107621:AAGb62I0emPZZ-b52BeqBVBaq5zjTDRwS5k',
                  use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Hola soy el pombeBOT 💀, escribe /help para listar todo lo que puedo hacer por vos!!'
    )


def help(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Escribe:' +
        '\n💀/add *dni nombre apellido fecha de naciemiento (DD-MM-AAAA) mensaje de saludo* para agregar un nuevo cumpleaños'
        + '\n💀/delete *dni* para borrar un cumpleaños' +
        '\n💀/list para listar todos los cumpleaños registrados')


def add_one_birthday_bot(update: Update, context: CallbackContext):
    if (len(context.args) != 5):
        update.message.reply_text(
            'Entrada no válida: revise la cantidad de parametros ingresados')

    dni = context.args[0]
    name = context.args[1]
    lastname = context.args[2]
    birthday = context.args[3]
    custom_greetings = context.args[4]

    result = bd_fun.add_one_birthday(dni, name, lastname, birthday,
                                     custom_greetings)
    print(result)
    str_response = ""
    if result.inserted_id != None:
        str_response = 'Cumpleaños seteado con éxito 🥳🥳🥳!!!'
    else:
        str_response = 'Ocurrió un error al setear el cumpleaños 💀💀💀!!!'
    
    update.message.reply_text(str_response % update.message.text)


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Perdón, no fui capaz de entender tu mensaje 💀.' % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('add', add_one_birthday_bot))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

updater.start_polling()
