import time
import threading

def task(stop_thread_flg):
    while True:
        if "run" == stop_thread_flg["status"]:
            print("线程:",stop_thread_flg["status"])
            time.sleep(2)
        else:
            print("线程:",stop_thread_flg["status"])
            break
