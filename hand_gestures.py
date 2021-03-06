import cv2
import numpy as np
import math
#capture data from webcam
capture = cv2.VideoCapture(0)
while capture.isOpened():
    ret, frame = capture.read()

    cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 0)
    crop_image = frame[100:300, 100:300]
    blur = cv2.GuassianBlur(crop_image, (3, 3), 0)
    #convert image bgr to hsv
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    #create a image where white will skin color and rest are black
    mask2 = cv2.inRange(hsv, np.array([2, 0, 0]), np.array([20, 255, 255]))
    #calling kernal for morphological transformation
    kernal1 = np.ones((5, 5))
    #apply dilation to filter out morphological transformation
    dilation = cv2.dilate(mask2, kernal1, iterations=1)
    erosion = cv2.erode(dilation, kernal1, iterations=1)
    #applying guassianblur and threshold
    filtered = cv2.GuassianBlur(erosion, (3, 3), 0)
    ret, thresh = cv2.threshold(filtered, 127, 255, 0)
    cv2.imshow("threshold", thresh)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    try:
        # finding contours with max area
        con = max(contours, key=lambda x: cv2.contourArea(x))
        #creating bounded area around contour
        x, y, w, h = cv2.boundingRect(con)
        cv2.rectangle(crop_image, (x, y), (x + w, y + h), (0, 0, 255), 0)
        hull = cv2.convexHull(con)
        #draw contour
        drawing = np.zeros(crop_image.shape, np.uint8)
        cv2.drawContours(drawing, [con], -1, (0, 255, 0), 0)
        cv2.drawContours(drawing, [hull], -1, (0, 255, 0), 0)
        #finding convexity defects
        hull = cv2.convexHull(con, returnPoints= False)
        defects = cv2.convexityDefects(con, hull)
        # Use cosine rule to find angle of the far point from the start and end point i.e. the convex points (the finger
        # tips) for all defects
        count_defects = 0
        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            start = tuple(contour[s][0])
            end = tuple(contour[e][0])
            far = tuple(contour[f][0])

            a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
            b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
            c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
            angle = (math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 180) / 3.14

            # if angle > 90 draw a circle at the far point
            if angle <= 90:
                count_defects += 1
                cv2.circle(crop_image, far, 1, [0, 0, 255], -1)

            cv2.line(crop_image, start, end, [0, 255, 0], 2)
            # Print number of fingers
        if count_defects == 0:
            cv2.putText(frame, "ONE", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        elif count_defects == 1:
            cv2.putText(frame, "TWO", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        elif count_defects == 2:
            cv2.putText(frame, "THREE", (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        elif count_defects == 3:
            cv2.putText(frame, "FOUR", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        elif count_defects == 4:
            cv2.putText(frame, "FIVE", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        else:
            pass
    except:
        pass
    # Show required images
    cv2.imshow("Gesture", frame)
    all_image = np.hstack((drawing, crop_image))
    cv2.imshow('Contours', all_image)

    # Close the camera if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()





