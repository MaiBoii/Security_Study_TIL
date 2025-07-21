import logging
from concurrent.futures import ThreadPoolExecutor
import time

# 스레드 실행 함수
def task(name):
    logging.info("Sub-Thread %s: starting", name)

    result = 0
    for i in range(10001):
        result = result + i

    logging.info("Sub-Thread %s: finishing result: %d", name, result)

    return result

def main():
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main-Thread : before creating and running thread")

    # 실행 방법1
    # max_workers : 작업의 개수가 남어가면 직접 설정이 유리
    executor = ThreadPoolExecutor(max_workers=3) 
    
    task1 = executor.submit(task, ('First',))
    task2 = executor.submit(task, ('Second',))
    task3 = executor.submit(task, ('Third',))


    #결과 값 있을 경우
    print(task1.result())
    print(task2.result())
    print(task3.result())

    

    # # 실행 방법2
    # # with context 구문 사용

    # with ThreadPoolExecutor(max_workers=3) as executor:
    #     tasks = executor.map(task, ['First', 'Second'])
        
    #     # 결과 확인
    #     # print(list(tasks))

    # logging.info("Main-Thread : all done")

if __name__ == '__main__':
    main()