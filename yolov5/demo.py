import torch
import cv2
import numpy as np
def POINTS(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = [x, y]
        print(colorsBGR)

cv2.namedWindow('ROI')
cv2.setMouseCallback('ROI', POINTS)
path = 'F:/HK6 2022-2023/AI/YoloV5/yolov5-20230505T112404Z-001/yolov5/runs/train/exp/weights/best.pt'
model = torch.hub.load('ultralytics/yolov5', 'custom', path, force_reload=True)
count = 0
cap = cv2.VideoCapture('F:/HK6 2022-2023/AI/YoloV5/yolov5-20230505T112404Z-001/yolov5/data/demo1.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    count += 1
    if count % 2 != 0:
        continue

    frame = cv2.resize(frame, (1080, 1080))
    results = model(frame)
    for index, row in results.pandas().xyxy[0].iterrows():
        x1 = int(row['xmin'])
        y1 = int(row['ymin'])
        x2 = int(row['xmax'])
        y2 = int(row['ymax'])
        d = (row['name'])
        print(d)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, str(d), (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 2)
    frame = np.squeeze(results.render())
    print(frame)
    cv2.imshow("ROI", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
# stream.release()
cv2.destroyAllWindows()