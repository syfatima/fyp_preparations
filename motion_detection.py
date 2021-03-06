import cv2, time, pandas
first_frame = None
video = cv2.VideoCapture(0)
while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    if first_frame is None:
        first_frame = gray
        continue
    delta_frame = cv2.absdiff(first_frame, gray)
    tresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    tresh_frame = cv2.dilate(tresh_frame, None, iterations=0)
    (cnts,_) = cv2.findContours(tresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contours in cnts:
        if cv2.contourArea(contours) < 10000:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contours)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
    cv2.imshow('frame', frame)
    cv2.imshow('capturing', gray)
    cv2.imshow('delta', delta_frame)
    cv2.imshow('threshold', tresh_frame)
    key = cv2.waitKey(0)
    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows()


