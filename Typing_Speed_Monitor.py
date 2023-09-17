keys_per_second_threshold = 5 # 60wpm = 300cpm
checking_key_frequency = 10 # check speed every x keys pressed
time_threshold = checking_key_frequency/keys_per_second_threshold

from pynput.keyboard import Key, Listener
from notifypy import Notify

from time import sleep, time as now

count = None
start_time = None

def on_release(key):
  global count
  global start_time

  count += 1
  
  if count == checking_key_frequency:

    duration = round(now() - start_time)

    reset()

    if duration < time_threshold:
      notification = Notify()
      notification.title = "Speed Warning"
      notification.message = "You are typing too fast"

      notification.send()

      sleep(10)
  
def reset():
  global count
  global start_time

  count = 0
  start_time = now()
    
if __name__ == "__main__":
  reset()
  with Listener(on_release=on_release) as listener:
    listener.join()
