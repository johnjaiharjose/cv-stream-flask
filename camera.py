# camera class for app streaming
import cv2
import cv2 as cv
import numpy as np

class VideoCamera1(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0) #camobjectsource
        #self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        #self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        #self._fourcc = cv2.VideoWriter_fourcc(*'XVID')
        #self._out = cv2.VideoWriter('output-loading.avi',self._fourcc, 25.0, (640,480))
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        ret, frame = self.video.read(1)
        frame = cv2.resize(frame,None,fx=1.0,fy=1.0,interpolation=cv2.INTER_AREA)
        #self._out.write(frame)
        img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        img_rgb = frame

        ret, jpeg = cv2.imencode('.jpg',frame)
        return jpeg.tobytes()