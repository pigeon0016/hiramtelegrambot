from telegram.ext import Updater, CommandHandler #Se importa la libreria Telegram , y un modulo Ext, se importa updater y commandhadnler



        # la funcion q se va a ejecutar cuando entre un comando o una accion de un usuario /start 
def start(Update, context):   
      Update.message.reply_text("q pdo")


#blque de ejecucion principal
if __name__ == '__main__':
    # aqui se ejecuta el programa principal
    
    
    #conectate con telegram por medio de este token
    #Updater = Se usa para saber las peticiones q el usuario manda
    # se pasa como true la variable de use context
    Updater = Updater(token='1553521009:AAGWTWsnlmiWMpk-Ti-nzWWcFx-XHFZivdI', use_context=True)
    
    #Crear el dispacher llamado dp se encarga de enviar las acciones, maneja los comandos
    dp = Updater.dispatcher
    
    
    #un manjeador de commando /start y cuando entre ese comando se va a ejecutar ese comando start
    #Un handler , q es una funcion q se ejecuta cuando entra uncomando o una accio del usuario
    #cuando ejecutes start vas a ejecutar el def START y devuelve el mesnaje q pdo y 
    dp.add_handler(CommandHandler('start',start)) # cuando entre el comando 'start' se va a ejecutar start
    
    
    #crea un cicli infinito
    #quedate escychando eternamente
    Updater.start_polling()
    Updater.idle()   