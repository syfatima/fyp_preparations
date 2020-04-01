import numpy as np
import cv2
hand_cascade = cv2.CascadeClassifier("C:\\Users\\syeda fatima\\PycharmProjects\\untitled\\haar_cascades\\hand.xml")
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hands = hand_cascade.detectMultiScale(gray, scaleFactor=1.03, minNeighbors=3)
    for (x, y, w, h) in hands:
        print(x, y, w, h)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        roi_gray = gray[y:y+h, x:x+w]
        img_item = '‪my-image.png'
        cv2.imwrite(img_item, roi_gray)

    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()