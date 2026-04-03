from logic import get_task_by_mood
from reply_buttons import buttons
from registration import register_name
from storage import load_users

def register_handlers(bot):
    
    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, "Привет! Напиши своё имя:")
        bot.register_next_step_handler(message, lambda msg: register_name(bot, msg))
        
    @bot.message_handler(func=lambda message: True)
    def mood_buttons(message):
    	markup = buttons()
    	
    	if message.text in ["1–3", "4–6", "7–9", "10"]:
    	   mood = {"1–3": 3, "4–6": 5, "7–9": 8, "10": 10}[message.text]
    	   task = get_task_by_mood(mood)
    	   bot.send_message(message.chat.id, f"Твоё задание: {task}", reply_markup=markup)
    	
    	else:
    		bot.send_message(message.chat.id, "Попробуй нажать одну из кнопок", reply_markup=markup)