import openai
import telebot

with open('OpenAI API.txt', 'r') as file:
  openai.api_key=file.read()

with open('Telegram Bot API.txt', 'r') as file:
  bot=telebot.TeleBot(file.read())

@bot.message_handler(func=lambda _: True)
def handle_message(message):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.5,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0,
    # stop=["You:"]
  )
  bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'].replace("\n\n", "\n"))

bot.polling()


