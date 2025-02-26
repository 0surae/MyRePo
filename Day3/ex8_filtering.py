import cv2
import numpy as np

# 이미지 읽기 (BGR 형식)
image = cv2.imread("mountain.jpg")

# 이미지가 정상적으로 로드되었는지 확인
if image is None:
    print("이미지를 불러올 수 없습니다.")
    exit()

# 1. 평균값 필터 (Blurring, 5x5 커널 적용)
blurred = cv2.blur(image, (5, 5))

# 2. 샤프닝 필터 (Sharpening)
sharpening_kernel = np.array([[ 0, -1,  0],
                               [-1,  5, -1],
                               [ 0, -1,  0]])
sharpened = cv2.filter2D(image, -1, sharpening_kernel)

# 3. 라플라시안 필터 (Laplacian Edge Detection)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 엣지 검출을 위해 그레이스케일 변환
laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)  # 64비트 부동소수점으로 처리
laplacian = cv2.convertScaleAbs(laplacian)  # 절댓값 변환 (양수 값만 남김)

# 결과 이미지 출력
cv2.imshow("Original Image", image)
cv2.imshow("Blurred (Average Filter)", blurred)
cv2.imshow("Sharpened (Sharpening Filter)", sharpened)
cv2.imshow("Laplacian (Edge Detection)", laplacian)

# 키 입력 대기 후 종료
cv2.waitKey(0)
cv2.destroyAllWindows()
