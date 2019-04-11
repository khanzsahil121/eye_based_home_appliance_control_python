import numpy as np
import cv2
from tkinter import messagebox
 

cap = cv2.VideoCapture("eye_recording.flv")
g=[]
d=0
yy=[]
flag_light=0
flag_fan=0
flag_AC=0
while True:
    ret, frame = cap.read()
    if ret is False:
        break
     
    roi = frame[269: 795, 537: 1416]
    rows, cols, _ = roi.shape
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gray_roi = cv2.GaussianBlur(gray_roi, (7, 7), 0)
 
    _, threshold = cv2.threshold(gray_roi, 3, 255, cv2.THRESH_BINARY_INV)
    _, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
    
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        
        #cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 3)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.line(roi, (x + int(w/2), 0), (x + int(w/2), rows), (0, 255, 0), 2)
        cv2.line(roi, (0, y + int(h/2)), (cols, y + int(h/2)), (0, 255, 0), 2)
        cv2.rectangle(threshold, (x, y), (x + w, y + h), (255, 0, 0), 2)
##        r,c,w,h=269, 795, 537, 1416
##        track_window = (c,r,w,h)
##        roi = frame[r:r+h, c:c+w]
##        hsv_roi =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
##        mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
##        roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
##        term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
##
##
##
##        dst = cv2.calcBackProject([threshold],[0],roi_hist,[0,180],1)
##        ret, track_window = cv2.meanShift(dst, track_window, term_crit)

        # Draw it on image
##        x,y,w,h = track_window
##        img2 = cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)
##        cv2.imshow('img2',img2)







        if x==0 or y==0:
            continue


        g.append(x)
        yy.append(y)
##        print(x)
        print('y',y)
        if len(g)>1:
            change=x-463
            print('mean change in x',change)
            print('current x value',x)
            if change> 110:
                flag_light=flag_light+1
                if flag_light>15:
                    messagebox.showinfo("Title", "user want to flip light1")
                    flag_light=0
                    continue
                    continue
                    continue
                    continue
                    continue
                    continue
                    continue
                    continue
            if change< -110:
                flag_fan=flag_fan+1
                if flag_fan>15:
                    messagebox.showinfo("Title", "user want to flip fan")
                    flag_fan=0
                    continue
                    continue
                    continue
                    continue
                    continue
                    continue
                    continue
                    continue
            
        if len(yy)>1:
            change1=y-253
            
            print('mean change in y',change1)
            print('current y value',y)
            if change1< -200:
                flag_AC=flag_AC+1
                if flag_AC>15:
                    messagebox.showinfo("Title", "user want to flip AC ")
                    flag_AC=0
                    continue
                    continue
                    continue
                    continue
                    continue
                    continue
                    continue
                    continue


##            messagebox.showinfo("Title", "user want to turn on light")
        break
    
    
    d=d+1    
    cv2.imshow("Threshold", threshold)
    cv2.imshow("gray roi", gray_roi)
    cv2.imshow("Roi", roi)
    key = cv2.waitKey(30)
    if key == 27:
        break
     
cv2.destroyAllWindows()
