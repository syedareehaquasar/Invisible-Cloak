import cv2
import numpy as np

cap = cv2.VideoCapture(0)
background = cv2.imread('./image.jpg')

while cap.isOpened():
    CamWorking, frame = cap.read()

    if CamWorking:
        #hue(color) Saturation(white + color) Value(black + color); hsv - can see by eyes (color + intensity)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # how do we convert rgb to hsv?
        # cv2.imshow("hsv", hsv) #testing how hsv looks

        # how to get hsv value?
        # lower: hue - 10, 100, 100, higher: h+10, 255, 255
        red = np.uint8([[[0,0,255]]]) # bgr value of red
        hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV) # get hsv value of red from bgr

        # threshold the hsv value to get only red colors #creating a range of reds we need to remove
        l_orange = np.array([0, 100, 50])
        u_orange = np.array([10, 255, 255])

        mask = cv2.inRange(hsv, l_orange, u_orange)
        # cv2.imshow("mask", mask)

        # all things orange
        part1 = cv2.bitwise_and(background, background, mask=mask)
        # cv2.imshow("part1", part1)

        mask = cv2.bitwise_not(mask)

        # part 2 is all things not red
        part2 = cv2.bitwise_and(frame, frame, mask=mask)
        # cv2.imshow("mask", part2)

        cv2.imshow("cloak", part1 + part2)

        if cv2.waitKey(5) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()