import requests
import telebot
import time

import schedule
tg_token='7150684276:AAEvn7yP-aSJACmdigyczeswZMkd0fS-h3E'
bot=telebot.TeleBot(tg_token)
def  get_schedule (period, id):
    def get_photo():
        url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'
        response = requests.get(url)
        url= response.json()['hdurl']
        response_image=requests.get(url)
        text=response.json()["explanation"]
        with open ('space.jpg','wb') as image:
            image.write(response_image.content)
        bot.send_photo(id,open('space.jpg','rb'),caption=text)
    if period =='everyday':
        schedule.every().days.at('20:50').do(get_photo)
    while True:
        print ('start')
        schedule.run_pending()
        time.sleep(1)
@bot.message_handler(commands=['start'])
def start_message(message):
    id=message.chat.id
    print(id)
    get_schedule('everyday',id)
bot.infinity_polling()