keys_per_second_threshold = 5 # 60wpm = 300cpm
checking_key_frequency = 10 # check speed every x keys pressed
time_threshold = checking_key_frequency/keys_per_second_threshold

from pynput.keyboard import Key, Listener
from notifypy import Notify

import keyboard

import time

count = None
start_time = None

def block():
  for key in range(150):
    keyboard.block_key(key)

def unblock():
  for key in range(150):
    keyboard.unblock_key(key)

def on_release(key):
  global count
  global start_time

  count += 1
  
  if count == checking_key_frequency:

    duration = time.time() - start_time

    reset()

    if duration < time_threshold:
      notification = Notify()
      notification.title = "Speed Warning"
      notification.message = "You are typing too fast"

      notification.send()

      block()
      time.sleep(5)
      unblock()
  
def reset():
  global count
  global start_time

  count = 0
  start_time = time.time()
    
if __name__ == "__main__":
  reset()
  with Listener(on_release=on_release) as listener:
    listener.join()
