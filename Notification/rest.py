from plyer import notification 
import time 

if __name__ == '__main__':
    notification.notify(
        title ="*** Take Rest ***",
        message="Rest is vital for better mental",
        app_icon="D:notification/try.ico",
        timeout=5)
    time.sleep(20)