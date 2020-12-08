import time
from PIL import ImageGrab

# 자동 스크린 캡처 및 파일저장

time.sleep(5) # 사용자가 준비하는시간 5초

for i in range(1,11): # 2 초간격으로 10개 이미지 저장
    img = ImageGrab.grab() # 현재 스크린의 이미지를 가지고옴
    img.save("image{}.png".format(i)) # 파일로 저장 image 1~10png
    time.sleep(2) # 2초 단위위