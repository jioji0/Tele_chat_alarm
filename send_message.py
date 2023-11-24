
import telegram
import asyncio

'''
#최종 해결한 코드
token =""  # 여기에 봇 토큰을 넣으십시오.
chat_id = ""  # 여기에 채팅 ID를 넣으십시오.
text = 'test'

bot = telegram.Bot(token=token)
asyncio.run(bot.send_message(chat_id=chat_id, text=text))
'''



#처음 시도한 코드
token =""  # 여기에 봇 토큰을 넣으십시오.
chat_id = ""  # 여기에 채팅 ID를 넣으십시오.
text = 'test'
    
bot = telegram.Bot(token=token)
bot.send_message(chat_id=chat_id, text=text)

#gpt 제안 코드
'''
async def send_message():
    token =""  # 여기에 봇 토큰을 넣으십시오.
    chat_id = ""  # 여기에 채팅 ID를 넣으십시오.
    text = 'test'
    
    bot = telegram.Bot(token=token)
    await bot.send_message(chat_id=chat_id, text=text)

# 비동기 함수 실행
loop = asyncio.get_event_loop()
loop.run_until_complete(send_message())
'''
