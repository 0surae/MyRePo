import cv2

# 비디오 파일 열기
video_path = "test_video.mp4"
cap = cv2.VideoCapture(video_path)

# 비디오가 정상적으로 열렸는지 확인
if not cap.isOpened():
    print("비디오를 열 수 없습니다.")
    exit()

# 프레임을 하나씩 읽어와서 표시
while True:
    ret, frame = cap.read()

    # 더 이상 프레임이 없으면 종료
    if not ret:
        break

    # 프레임 표시
    cv2.imshow("Video Playback", frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()
