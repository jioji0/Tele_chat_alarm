import schedule
import time
import telegram
import asyncio

def job():
    now = time.localtime()
    token = "5965897880:AAHwEJqt5Axjg_TpL3c-fys78nJ7vFRqeF0"
    bot = telegram.Bot(token=token)
    public_chat_name = '@dvnlb2'
    asyncio.run(bot.sendMessage(chat_id=public_chat_name, text="hi:)"))
    print("current time = ", str(now))

schedule.every(1).minutes.do(job)

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
