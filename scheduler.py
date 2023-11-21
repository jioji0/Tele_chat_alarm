import sys
import io
import schedule
import datetime
import time
import telegram
import asyncio
import pytz

count = 1

def job():
    
    global count
    count += 1
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    if now.hour >= 23 or now.hour <= 6:
        return
    
    sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

    token = "5965897880:AAHwEJqt5Axjg_TpL3c-fys78nJ7vFRqeF0"
    bot = telegram.Bot(token=token)
    public_chat_name = '@dvnlb2'
    asyncio.run(bot.sendMessage(chat_id=public_chat_name, text="schedule"))
    print("current time = ", str(now))

#n분마다 실행
schedule.every(0.1).minutes.do(job)

print("Start App")

#파이썬 스케쥴러
while True:
    schedule.run_pending()
    time.sleep(1)

'''
import schedule
import asyncio
import time
import telegram

async def job():
    now = time.localtime()
    token = "5965897880:AAHwEJqt5Axjg_TpL3c-fys78nJ7vFRqeF0"
    bot = telegram.Bot(token=token)
    public_chat_name = '@dvnlb2'
    await bot.sendMessage(chat_id=public_chat_name, text="hi:)")
    print("current time = ", str(now))

async def main():
    schedule.every(1).minutes.do(job)

    while True:
        await schedule.run_pending()
        await asyncio.sleep(1)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
'''
