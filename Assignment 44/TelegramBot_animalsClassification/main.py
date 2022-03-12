import telebot
from model import Model

model = Model()

mybot = telebot.TeleBot(token="Token")

@mybot.message_handler(commands=["start"])
def send_welcome(message):
    mybot.reply_to(message, f"Hi {message.from_user.first_name}, Welcome\n/help- for commands")

@mybot.message_handler(commands=["animal_detector"])
def animal_Detector(message):
    answer = mybot.reply_to(message, "Ok. now i can say you what animal is in the image\nSend me a phono of these animals:\n1-Elephant\n2-Koala\n3-Lion\n4-Wolf")
    mybot.register_next_step_handler(answer, get_image)
    
def get_image(message):
    try:
        raw = message.photo[2].file_id
        path = raw + ".jpg"
        file_info = mybot.get_file(raw)
        downloaded_file = mybot.download_file(file_info.file_path)
        with open(f"images/{path}",'wb') as new_file:
            new_file.write(downloaded_file)
        
        animal_pred = model.predit_animal(f"images/{path}")
        mybot.reply_to(message, f"This is a {animal_pred}")
    except:
        mybot.reply_to(message, f"Somthing went wrong, Please try again")
        
@mybot.message_handler(commands=['help'])
def help_func(message):
    mybot.reply_to(message, "Here's the commands:\n/animal_detector- To detect animal in the image")
    
@mybot.message_handler(func=lambda message: True)
def help(message):
    mybot.reply_to(message, "Please first select a command\n/help- for more information")    

mybot.polling()