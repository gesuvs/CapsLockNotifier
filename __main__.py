import time
from app.notifier import CapsLockNotifier

if __name__ == "__main__":
    print("START")
    notifier = CapsLockNotifier()
    notifier.run()
    
    try:
      while True:
        time.sleep(1)
    except KeyboardInterrupt:
      print("FINISH...")