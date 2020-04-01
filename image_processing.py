import cv2, time, pandas

##read the image
##img=cv2.imread("C:\\Users\\syeda fatima\\Documents\\data\\nikkah\\me2.jpeg", 1)
#show type of image
#print(img.show)
#print(type(img))
##sizing the image
#resize_img=cv2.resize(img, (400,500))
##resize_img=cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
##resize_img=cv2.resize(img, (int(img.shape[1]*2), int(img.shape[0]*2)))
#cv2.imshow("rida", img)
##cv2.imshow("rida", resize_img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()
##face detection with rectagular box
##https://github.com/opencv/opencv/tree/master/data/haarcascades ""for xml files""
'''face_cascade = cv2.CascadeClassifier("C:\\Users\\syeda fatima\\Pictures\\haarcascade_frontalface_default.xml")
img=cv2.imread("C:\\Users\\syeda fatima\\Downloads\\WhatsApp Image 2020-02-19 at 2.30.56 PM (1).jpeg", 1)
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#SEARCH CO-ORDINATES OF FACE
faces = face_cascade.detectMultiScale(grey_img, scaleFactor=1.05, minNeighbors=5)
for x,y,w,h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

resize_img = cv2.resize(img, (int(img.shape[1]), int(img.shape[0])))
cv2.imshow("Gray", resize_img)'''

### make a video by using self camera
video = cv2.VideoCapture(0)
a = 1
while True:
    a = a + 1
    check, frame = video.read()
    print(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capture", gray)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
print(a)
#time.sleep(3)
video.release()
cv2.destroyAllWindows()
##print(type(faces))
##print(faces)
