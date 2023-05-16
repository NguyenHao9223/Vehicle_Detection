import cv2

video_path = 'VID9.mp4'
cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

interval = int(fps * 4)
frame_counter = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if frame_counter % interval == 0:
        img_path = 'image_' + str(frame_counter) + '.png'
        cv2.imwrite(img_path, frame)
        print(img_path)

    frame_counter += 1
    if frame_counter >= total_frames:
        break
cap.release()
cv2.destroyAllWindows()