# **NASA APOD Telegram Bot Documentation**

## **Overview**
This Telegram bot fetches images from NASA's *Astronomy Picture of the Day (APOD)* API and sends them along with descriptions to users at a scheduled time.

## **Features**
- Retrieves daily space images from NASA's APOD API.
- Sends the image and its description to users.
- Automatically schedules messages at a predefined time.
- Uses `schedule` for automated task execution.

---

## **Installation & Setup**

### **Prerequisites**
Ensure you have the following installed:
- Python 3.x
- Required Python libraries:
  ```sh
  pip install requests pyTelegramBotAPI schedule
A Telegram Bot Token (created via BotFather).
Configuration
Replace tg_token with your actual Telegram Bot Token:
python
Copy
Edit
tg_token = 'YOUR_TELEGRAM_BOT_TOKEN'
Replace DEMO_KEY in the NASA API URL with your own NASA API key from NASA API.
How It Works
Bot Initialization
The bot starts with /start, which triggers the function get_schedule().
It fetches NASA's APOD image and explanation.
Fetching NASA APOD Image
The get_photo() function:

Makes a request to NASA's APOD API.
Extracts the high-definition image URL (hdurl).
Downloads the image and saves it as space.jpg.
Reads the explanation text.
Sends the image and text to the user via Telegram.
Scheduling
The bot schedules the image delivery every day at 20:50 (8:50 PM).
The schedule module ensures the bot runs continuously and sends messages at the set time.
Code Breakdown
1. Importing Required Libraries
python
Copy
Edit
import requests
import telebot
import time
import schedule
requests: Fetches data from the NASA API.
telebot: Handles Telegram bot communication.
time: Provides delays for scheduling.
schedule: Runs the image-fetching task at a fixed time.
2. Setting Up the Bot
python
Copy
Edit
tg_token = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telebot.TeleBot(tg_token)
Initializes the bot with the provided token.
3. Fetching & Sending Images
python
Copy
Edit
def get_photo():
    url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'
    response = requests.get(url)
    url = response.json()['hdurl']
    response_image = requests.get(url)
    text = response.json()["explanation"]
    
    with open('space.jpg', 'wb') as image:
        image.write(response_image.content)
    
    bot.send_photo(id, open('space.jpg', 'rb'), caption=text)
Sends a NASA APOD image and its description to the user.
4. Scheduling the Task
python
Copy
Edit
def get_schedule(period, id):
    if period == 'everyday':
        schedule.every().day.at('20:50').do(get_photo)
    
    while True:
        print('start')
        schedule.run_pending()
        time.sleep(1)
Sets the schedule to run the get_photo() function daily at 20:50.
5. Handling User Commands
python
Copy
Edit
@bot.message_handler(commands=['start'])
def start_message(message):
    id = message.chat.id
    print(id)
    get_schedule('everyday', id)
When a user sends /start, their chat ID is retrieved and stored.
The bot begins scheduling daily messages for that user.
6. Running the Bot
python
Copy
Edit
bot.infinity_polling()
The bot continuously listens for messages and executes scheduled tasks.
Potential Issues & Fixes
Issue	Solution
schedule.every().days throws an error	Change schedule.every().days.at('20:50') to schedule.every().day.at('20:50')
id is not defined inside get_photo()	Pass id as an argument inside get_photo() or store it globally
Image URL not found	Ensure hdurl exists in the API response and handle missing keys with .get()
Improvements & Enhancements
Add an option for users to set their preferred image delivery time.
Store chat IDs in a database for multiple user support.
Use environment variables for secure API key storage.
Implement error handling for API failures.
Conclusion
This Telegram bot automates the delivery of NASA’s daily space images to users via the APOD API. The bot is built using Python, telebot, and schedule, allowing it to fetch and send images at a scheduled time. Future improvements can enhance user customization and scalability.
