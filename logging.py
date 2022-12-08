import logging
import logging.handlers
import time

# debug < info < warning < error < critical
logger = logging.getLogger(__name__) # 로거 객체 생성
logger.setLevel(logging.INFO) # 로깅 레벨 설정

formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s') # 포맷팅

stream_handler = logging.StreamHandler() # 콘솔 출력용
stream_handler.setFormatter(formatter)

# 1시간마다 로그를 생성
file_handler = logging.handlers.TimedRotatingFileHandler(filename="log",when = "H", interval=1) # 파일 출력용
file_handler.setFormatter(formatter)

# 로깅을 처리할 객체 추가
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

# while True:
#     logger.info("this is info")
#     time.sleep(10)

# https://docs.python.org/ko/3.7/howto/logging.html
# https://hamait.tistory.com/880?category=79136
