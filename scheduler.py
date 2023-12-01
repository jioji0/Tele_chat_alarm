'''비동기로 해결한 코드
import schedule
import asyncio
import time
import telegram

async def job():
    now = time.localtime()
    token = ""  # 여기에 봇 토큰을 넣으십시오.
    bot = telegram.Bot(token=token)
    public_chat_name = '@abcde' # 여기에 chat_name을 입략하시오.
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

import sys
import io
import datetime
import pytz
import schedule
import time
import telegram

count = 1

#버전을 다운그레이드해서 사용한 코드드
def job():
    global count
    count += 1
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    if now.hour >= 23 or now.hour <= 6:
        return

    sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

    token = ""  # 여기에 봇 토큰을 넣으십시오.
    bot = telegram.Bot(token=token)
    public_chat_name = '@abcde' # 여기에 chat_name을 입략하시오.
    bot.sendMessage(chat_id=public_chat_name, text="schedule alert")
    print("current time = ", str(now))


schedule.every(30).minutes.do(job)

print('Start app')

while True:
    schedule.run_pending()
    time.sleep(1)



