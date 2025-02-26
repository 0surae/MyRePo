import cv2
import numpy as np

# 이미지 읽기 (OpenCV는 기본적으로 BGR 순서로 이미지를 로드함)
image = cv2.imread("Lenna.png")

# 이미지가 정상적으로 로드되었는지 확인
if image is None:
    print("이미지를 불러올 수 없습니다.")
    exit()

# BGR -> RGB 변환 (OpenCV는 BGR 형식이므로 변환)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# RGB 채널 분리
r, g, b = cv2.split(image_rgb)

# 개별 채널을 색상으로 표현하기 위해 빈 채널 생성
zeros = np.zeros_like(r)

# R, G, B 채널만 포함된 이미지 생성
red_image = cv2.merge([r, zeros, zeros])  # 빨간색만 강조
green_image = cv2.merge([zeros, g, zeros])  # 초록색만 강조
blue_image = cv2.merge([zeros, zeros, b])  # 파란색만 강조

# 원본 및 분리된 색상 이미지 표시
cv2.imshow("Original RGB Image", image_rgb)
cv2.imshow("Red Channel", red_image)
cv2.imshow("Green Channel", green_image)
cv2.imshow("Blue Channel", blue_image)

# 키 입력 대기 후 창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()
