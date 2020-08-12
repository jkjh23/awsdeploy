'''
- 서버 환경
  - ubuntu 18.04 or 16.04
  - apache(or nginx) + flask 연동 
  - (파이썬 웹은 apache 등 웹서버와 연동하여 사용하는 것을 권장)
    - wsgi.py는 apache서버가 가장 먼저 찾는 엔트리포인트
  - 가상환경상에서 구동
'''

import sys
import os

# 서버 운영을 위해서 세팅 =============================================================
# 현재 wsgi.py파일의 경로
cur_dir = os.getcwd()
# print(cur_dir)

# 에러 출력
sys.stdout = sys.stderr
# 출력을 현재 디렉토리로 추가
sys.path.insert(0, cur_dir)
# 아파치 서버에서 표준 출력과 에러 출력의 방향을 설정하기 위한 세팅

# 서버 가동
from run import app as application