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