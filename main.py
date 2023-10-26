import cv2
import numpy as np 
import time




while True:
    #This is to check whether to break the first loop
    isclosed=0
    cap = cv2.VideoCapture('robot_blink.mp4')
    while (True):

        ret, frame = cap.read()
        # It should only show the frame when the ret is true
        if ret == True:

            cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
            cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) == 27:
                # When esc is pressed isclosed is 1
                isclosed=1
                break
        else:
            break
    # To break the loop if it is closed manually
    if isclosed:
        break
    time.sleep(5)



cap.release()
cv2.destroyAllWindows()