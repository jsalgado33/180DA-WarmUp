import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Create a color range  HSV: 136 96 33
    loweryellow = np.array([162, 100, 100])
    upperyellow = np.array([180, 255, 255])

    #Threshold images 
    mask = cv2.inRange(HSV,loweryellow,upperyellow)
    x,y,w,h = cv2.boundingRect(mask)

    #draw rect 
    cv2.rectangle(HSV,(x,y),(x+w, y+h),(220,0,255),2)
    # Display the resulting frame
    cv2.imshow('frame',HSV)
    cv2.imshow('schlong', mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
	
	


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()