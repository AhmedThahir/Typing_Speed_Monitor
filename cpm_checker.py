# 300cpm = 300/60 = 5cps

# allow 20 keys every 5seconds = 2 cps
time_threshold = 5
key_threshold = 10

from pynput.keyboard import Key, Listener
from notifypy import Notify

from time import sleep, time as now

temp_keys = None
start_time = None

def on_press(key):
  pass
  
def on_release(key):
  if key == Key.esc:
    return False

  global temp_keys
  global start_time

  temp_keys.append(key)
  
  if len(temp_keys) == key_threshold:
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
  with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()