import time

def focus_timer(duration):
    start_time = time.time()
    end_time = start_time + duration * 60

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes = remaining_time // 60
        seconds = remaining_time % 60

        print(f"剩余时间: {minutes:02d}:{seconds:02d}", end="\r")
        time.sleep(1)

    print("Time's up！")

# 设置时间为25分钟
focus_timer(25)
