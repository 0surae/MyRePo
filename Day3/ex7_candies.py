import cv2

# 이미지 읽기 (BGR 형식으로 로드됨)
image = cv2.imread("Candies.png")

# 이미지가 정상적으로 로드되었는지 확인
if image is None:
    print("이미지를 불러올 수 없습니다.")
    exit()

# BGR -> HSV 변환 (OpenCV 함수 사용)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 빨간색 범위 정의 (HSV에서 빨간색은 두 개의 범위로 나뉨)
lower_red1 = (0, 100, 100)    # 첫 번째 빨간색 범위
upper_red1 = (10, 255, 255)

lower_red2 = (170, 100, 100)  # 두 번째 빨간색 범위
upper_red2 = (180, 255, 255)

# 빨간색 범위에 해당하는 마스크 생성
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = cv2.bitwise_or(mask1, mask2)  # 두 개의 마스크를 합침

# 마스크를 적용하여 붉은색 부분만 추출
result = cv2.bitwise_and(image, image, mask=mask)

# 결과 출력
cv2.imshow("Original Image", image)
cv2.imshow("Red Only", result)

# 키 입력 대기 후 종료
cv2.waitKey(0)
cv2.destroyAllWindows()
