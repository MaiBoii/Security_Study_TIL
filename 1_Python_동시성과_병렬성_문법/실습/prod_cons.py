import concurrent.futures
import queue
import time
import random
import logging
import threading


# 데이터를 만들어내는 쪽 (I/O나 네트워크 작업 스레드)
def producer(queue, event):
    """네트워크 대기 상태라 가정(서버)"""
    while not event.is_set():
        message = random.randint(1,11)
        logging.info('생산자가 메시지를 받았습니다: %s',message)
        queue.put(message)
        
    logging.info('생산자가 이벤트를 보냈습니다.')

# 소비자 (CPU 작업 스레드)
def consumer(queue, event):
    """응답 받고 소비하는 것으로 가정 or DB 저장"""
    while not event.is_set() or not  queue.empty():
        message = queue.get()
        logging.info('소비자가 메시지를 받았습니다: %s (size=%d)',message, queue.qsize())

    logging.info('소비자가 이벤트를 받았습니다.')



if __name__ == "__main__":
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    # 사이즈 설정이 중요함
    pipeline = queue.Queue(maxsize=10)

    #이벤트 플래그 변수 설정하기
    event = threading.Event()

    #With Context
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as excuter:
        # 실행할 함수 producer에 Queue와 event 2개의 매개변수를 집어넣음
        excuter.submit(producer, pipeline, event)
        excuter.submit(consumer, pipeline, event)

        time.sleep(0.1)
        
        logging.info('Main : 이벤트를 Set 하는 중입니다...')

        #프로그램 종료 시점
        event.set()
    



