from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# טוקן הבוט
BOT_TOKEN = "7853970323:AAG78UpqnEBWxtjZ5JHMc4CwYK6YLM4qlI4"  

# מזהה הערוץ
CHANNEL_ID = "-1001403432675"  # מזהה הערוץ שלך

# פקודה שמופעלת כשמשתמש שולח /start
def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id

    try:
        # בדיקת אם המשתמש חבר בערוץ
        member_status = context.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id).status

        if member_status in ["member", "administrator", "creator"]:
            # אם המשתמש חבר בערוץ
            coupon_code = "tele50"  # קוד הקופון
            message = f"ברוך הבא! קוד הקופון שלך הוא: {coupon_code}.\nשים לב: הקוד מוגבל לשימוש אחד בלבד."
            context.bot.send_message(chat_id=chat_id, text=message)
        else:
            # אם המשתמש לא חבר בערוץ
            keyboard = [[InlineKeyboardButton("הצטרף לערוץ", url=f"https://t.me/+RXq1JdXs1hE3NTFk")]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            join_message = "עליך להצטרף לערוץ שלנו לפני שתוכל להשתמש בבוט."
            context.bot.send_message(chat_id=chat_id, text=join_message, reply_markup=reply_markup)

    except Exception as e:
        # טיפול בשגיאות (לדוגמה: אם המשתמש לא נמצא ברשימת החברים)
        keyboard = [[InlineKeyboardButton("הצטרף לערוץ", url=f"https://t.me/+RXq1JdXs1hE3NTFk")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        join_message = "עליך להצטרף לערוץ שלנו לפני שתוכל להשתמש בבוט."
        context.bot.send_message(chat_id=chat_id, text=join_message, reply_markup=reply_markup)

# הגדרת הבוט
def main():
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    # הוספת הפקודה /start לבוט
    dispatcher.add_handler(CommandHandler("start", start))

    # הפעלת הבוט
    print("Bot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
