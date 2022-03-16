import os
import telebot
from model import Model

model = Model()

mybot = telebot.TeleBot(token="5241854696:AAE2IhD5_g0LbaBDUl442M59aqzrfu0KBtE")

if not os.path.exists("images"):
    os.mkdir("images")

@mybot.message_handler(commands=["start"])
def send_welcome(message):
    mybot.reply_to(message, f"Hi {message.from_user.first_name}, Welcome\n/help- for commands")

@mybot.message_handler(commands=["sheikh_detector"])
def sheikh_Detector(message):
    answer = mybot.reply_to(message, "Send me a photo of a Normal person or a Sheikh and i Recognize that a sheikh is in the picture or an ordinary person.\nNote: The dimensions of the photo should be more than 299 * 299")
    mybot.register_next_step_handler(answer, get_image)
    
def get_image(message):
    try:
        raw = message.photo[2].file_id
        path = raw + ".jpg"
        file_info = mybot.get_file(raw)
        downloaded_file = mybot.download_file(file_info.file_path)
        with open(f"images/{path}",'wb') as new_file:
            new_file.write(downloaded_file)
        
        result_pred = model.predit_type(f"images/{path}")
        mybot.reply_to(message, f"He/She is a {result_pred}")
    except:
        mybot.reply_to(message, f"Somthing went wrong, Please try again\nNote: The dimensions of the photo should be more than 299 * 299")
        
@mybot.message_handler(commands=['help'])
def help_func(message):
    mybot.reply_to(message, "Here's the commands:\n/sheikh_detector- Recognize that a sheikh is in the picture or an ordinary person")
    
@mybot.message_handler(func=lambda message: True)
def help(message):
    mybot.reply_to(message, "Please first select a command\n/help- for more information")    

mybot.polling()