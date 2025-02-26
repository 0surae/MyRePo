import cv2

# 이미지 읽기
image = cv2.imread("Lenna.png", cv2.IMREAD_GRAYSCALE)

# 이미지가 제대로 로드되었는지 확인
if image is None:
    print("이미지를 불러올 수 없습니다.")
else:
    # 이미지 표시
    cv2.imshow("Lenna", image)

    # 아무 키나 누르면 창 닫기
    cv2.waitKey(0)
    cv2.destroyAllWindows()