import logging
import threading
import time

def thread_func(name):
    logging.info("Sub-Thread: %s: Starting", name)
    time.sleep(3)
    logging.info("Sub-Thread: %s: Finishing", name)


if __name__ == "__main__":
    # Logging 포맷 설정하기 
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: before creating Thread")

    # 함수 인자 확인
    x = threading.Thread(target=thread_func, args=("First", ))

    logging.info("Main-Thread: before running Thread")

    x.start()
    
    x.join()

    logging.info("Main-Thread: Waiting For the Thread To Finish.")

    logging.info("Main-Thread: Now All Finished!")

'''
요점은 부모 스레드가 먼저 끝나도 자식 스레드는 끝까지 맡은 일을 다 하고 종료된다는 거임.
뒤에서 배울 Daemon이랑은 좀 다른데 그건 이따가 보도록 함
'''