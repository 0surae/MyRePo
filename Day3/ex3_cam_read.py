import cv2

# 웹캠 열기 (0은 기본 카메라, 다른 번호를 입력하면 추가 카메라 선택 가능)
cap = cv2.VideoCapture(0)

# 카메라가 정상적으로 열렸는지 확인
if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

# 실시간 영상 출력 루프
while True:
    ret, frame = cap.read()  # 프레임 읽기

    # 프레임이 정상적으로 읽히지 않으면 종료
    if not ret:
        print("프레임을 가져올 수 없습니다.")
        break

    cv2.imshow("Webcam Live", frame)  # 프레임 화면에 표시

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()
