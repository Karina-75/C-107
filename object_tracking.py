import cv2
import time
import math

p1 = 530
p2 = 300
xs = []
ys = []
video = cv2.VideoCapture("bb3.mp4")
tracker = cv2.TrackerCSRT_create()
returned, img = video.read()
b_box = cv2.selectROI('tracking', img, False)
tracker.init(img, b_box)
print(b_box)

def drawbox(img, b_box):
    x,y,w,h = int(b_box[0]), int(b_box[1]), int(b_box[2]), int(b_box[3])
    cv2.rectangle(img, (x,y), ((x+w),(y+h)), (255,0,0), 3, 1)

def goal_track(img, b_box):
    x,y,w,h = int(b_box[0]), int(b_box[1]), int(b_box[2]), int(b_box[3])
    c1 = x+int(w/2)
    c2 = y+int(h/2)
    cv2.circle(img, (c1, c2), 2, (0,0,255), 5)
    cv2.circle(img, (int(p1), int (p2)), 2, (0,255,0), 3)
    distance = math.sqrt(((c1-p1)**2) + (c2-p2)**2)
    print(distance)
    xs.append(c1)
    ys.append(c2)
    for i in range(len(xs) -1):
       cv2.circle(img, (xs[i], ys[i]), 2, (0,0,255), 5)

while True:
    check,img = video.read() 
    success, b_box = tracker.update(img)
    if success:
        drawbox(img, b_box)
    else:
        cv2.putText(img, 'lost', (75,90), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (0,0,255), 2)

    goal_track(img, b_box)

    cv2.imshow("result",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break


video.release()
cv2.destroyALLwindows()



