import telegram
import asyncio

async def send_message():
    token = ""  # 여기에 봇 토큰을 넣으십시오.
    bot = telegram.Bot(token=token)
    public_chat_name = '@abcde' # 여기에 chat_name을 입략하시오.
    message = await bot.sendMessage(chat_id=public_chat_name, text="alarm arrived!")
    print(message)

loop = asyncio.get_event_loop()
loop.run_until_complete(send_message())


'''
token = ""  # 여기에 봇 토큰을 넣으십시오.
#chat_id = "123456"  #여기에 chat_id를 넣으십시오.
bot = telegram.Bot(token = token)
public_chat_name = '@abcde'  # 여기에 chat_name을 입략하시오.
id_channel = bot.sendMessage(chat_id = public_chat_name, text = "alarm arrived!").chat_id
print(id_channel)
'''
