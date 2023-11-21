import telegram
import asyncio

token = "5965897880:AAHwEJqt5Axjg_TpL3c-fys78nJ7vFRqeF0"
bot = telegram.Bot(token=token)
public_chat_name = '@dvnlb2'
message = asyncio.run(bot.sendMessage(chat_id=public_chat_name, text="alarm arrived!"))
print(message)


'''
async def send_message():
    token = "5965897880:AAHwEJqt5Axjg_TpL3c-fys78nJ7vFRqeF0"
    bot = telegram.Bot(token=token)
    public_chat_name = '@dvnlb2'
    message = await bot.sendMessage(chat_id=public_chat_name, text="alarm arrived!")
    print(message)

loop = asyncio.get_event_loop()
loop.run_until_complete(send_message())
'''

'''
token = "5965897880:AAHwEJqt5Axjg_TpL3c-fys78nJ7vFRqeF0"  # 여기에 봇 토큰을 넣으십시오.
#chat_id = "6507308870"
bot = telegram.Bot(token = token)
public_chat_name = '@dvnlb2'
id_channel = bot.sendMessage(chat_id = public_chat_name, text = "alarm arrived!").chat_id
print(id_channel)
'''