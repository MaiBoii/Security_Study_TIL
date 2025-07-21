import logging
from concurrent.futures import ThreadPoolExecutor
import time

class FakeDataStore:
    # 공유 변수 설정 (스택 영역)
    def __init__(self):
        self.value = 0

    # 변수를 업데이트 시키는 함수
    def update(self,n):
        logging.info('Thread %s: 업데이트 시작', n)

        # Mutex (Lock) 등 동기화가 필요한 지점
        local_copy = self.value # local_copy의 스택 영역에 0을 저장
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy

        logging.info('Thread %s: 업데이트 마침', n)

if __name__ == "__main__":
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    # 클래스 인스턴스화
    store = FakeDataStore()

    logging.info("Testing update. Starting value is %d.", store.value)

    # With Context 시작
    with ThreadPoolExecutor(max_workers=2) as executor:
        for n in ['First', 'Second', 'Third']:
            executor.submit(store.update, n)

    logging.info("Testing update. Ending value is %d.", store.value)