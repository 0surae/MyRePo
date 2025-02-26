import cv2
import numpy as np

# 이미지 읽기 (BGR 형식으로 로드됨)
image = cv2.imread("Lenna.png")

# 이미지가 정상적으로 로드되었는지 확인
if image is None:
    print("이미지를 불러올 수 없습니다.")
    exit()

# BGR -> HSV 변환
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# HSV 채널 분리
h, s, v = cv2.split(image_hsv)


# 원본 및 HSV 채널 이미지 표시
cv2.imshow("Original Image", image)
cv2.imshow("Hue Channel", h)
cv2.imshow("Saturation Channel", s)
cv2.imshow("Value Channel", v)

# 키 입력 대기 후 창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()
