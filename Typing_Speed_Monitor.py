keys_per_second_threshold = 5 # 60wpm = 300cpm
checking_key_frequency = 10 # check speed every x keys pressed
time_threshold = checking_key_frequency/keys_per_second_threshold

from pynput.keyboard import Key, Listener
from notifypy import Notify

from time import sleep, time as now

temp_keys = None
start_time = None

def on_release(key):
  global temp_keys
  global start_time

  temp_keys.append(key)
  
  if len(temp_keys) == checking_key_frequency:
    duration = now() - start_time

    if duration < time_threshold:
      notification = Notify()
      notification.title = "Speed Warning"
      notification.message = "You are typing too fast"

      notification.send()

      sleep(10)
    reset()
  
def reset():
  global temp_keys
  global start_time

  temp_keys = []
  start_time = now()
    
if __name__ == "__main__":
  reset()
  with Listener(on_release=on_release) as listener:
    listener.join()
