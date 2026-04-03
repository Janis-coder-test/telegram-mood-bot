from storage import load_users, save_user
from reply_buttons import buttons

def register_name(bot, message):
    markup = buttons()
    users = load_users()
    user_id = str(message.chat.id)
    
    
    if user_id not in users:
    	users[user_id] = {}
    	
    	save_user(users)
    
    bot.send_message(message.chat.id, f"Ок, {message.text}. Напиши число от 1 до 10 — твоё настроение.", reply_markup=markup)