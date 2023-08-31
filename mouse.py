import cv2
import mediapipe as mp
import pyautogui as pg
cam=cv2.VideoCapture(0)
face_mesh=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w,screen_h=pg.size()
while(True):
    _,frame=cam.read()
    frame=cv2.flip(frame,1)
    rgb_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output=face_mesh.process(rgb_frame)
    landmark_points=output.multi_face_landmarks
    #print(landmark_points)
    frame_h,frame_w,_=frame.shape
    if landmark_points:
        landmarks=landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x=int(landmark.x*frame_w)
            y=int(landmark.y*frame_h)
            cv2.circle(frame,(x,y),2,(0,255,0))
            #print(x,y)
            if id==1:
                screen_x=screen_w/frame_w*x
                screen_y=screen_h/frame_h*y
                pg.moveTo(screen_x,screen_y)
        left=[landmarks[145],landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 1, (0, 255, 0))
        if(left[0].y-left[1].x)<0.004:
            pg.click()
            pg.sleep(1)




    cv2.imshow('Eye Controlled Mouse',frame)
    cv2.waitKey(1)
0