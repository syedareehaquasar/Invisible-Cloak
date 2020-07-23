import cv2
cap = cv2.VideoCapture(0)

while cap.isOpened():
    camWorking, background = cap.read()
    if camWorking:
        cv2.imshow("image", background)
        if cv2.waitKey(5) == ord('q'): # q is used to capture # 5 of w8 key is taking pictures in interwal of 5 and save it if u press q
            cv2.imwrite('image.jpg', background) #capture image and saving it
            break

cap.release()
cv2.destroyAllWindows()