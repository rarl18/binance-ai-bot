
import schedule
import time
from bot.signal_generator import generate_signal

def job():
    signal = generate_signal()
    print(f"🟢 Signal: {signal}")

schedule.every(15).minutes.do(job)

print("✅ Binance AI Bot is running...")
while True:
    schedule.run_pending()
    time.sleep(1)
