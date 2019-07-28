import cv2
import numpy as np
#=========================点击鼠标按钮发出响应=============================================
#鼠标的回调函数   #点击鼠标左键，打印出此时的坐标位置
#回调函数的参数格式是固定的
# def mouse_event(event,x,y,flags,param):
#     if event ==cv2.EVENT_LBUTTONDOWN:  #点击鼠标左键发出响应
#     # if event == cv2.EVENT_RBUTTONDOWN:  #点击鼠标右键发出响应
#         print(x,y)
#
# img = np.zeros((512,512,3),np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image',mouse_event)
#
# while(True):
#     cv2.imshow('image',img)
#     if cv2.waitKey(20) == 27:
#         break
#=================================================================================

#打印出所有的事件
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

#=============================用鼠标来进行画图===============================
# import cv2
# import numpy as np
# drawing = False
# mode = True
# start = (-1,-1)
#
# def mouse_event(event,x,y,flags,param):
#     global start,drawing,mode
#
#     if event ==cv2.EVENT_LBUTTONDOWN:
#         drawing =True
#         start = (x,y)
#
#     elif event == cv2.EVENT_MOUSEMOVE:
#         if drawing:
#             if mode:
#                 cv2.rectangle(img,start,(x,y),(0,255,0),1)
#             else:
#                 cv2.circle(img,(x,y),5,(0,0,255),-1)
#     elif event == cv2.EVENT_LBUTTONUP:
#         drawing =False
#         if mode:
#             cv2.rectangle(img,start,(x,y),(0,255,0),1)
#         else:
#             cv2.circle(img,(x,y),5,(0,0,255),-1)
# img = np.zeros((512,512,3),np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image',mouse_event)
#
# while(True):
#     cv2.imshow('image',img)
#     if cv2.waitKey(1) == ord('m'):
#         mode = not mode
#     elif cv2.waitKey(1) == 27:
#         break
#

#========================实现目标检测中用鼠标将目标圈出来的功能===========================
import cv2
start,end =(0,0),(0,0)
drawing = False

img = cv2.imread('lena.jpg')
def mouse_event(event,x,y,flags,param):
    global start,drawing,end,temp

    if event ==cv2.EVENT_LBUTTONDOWN:
        drawing =True
        start = (x,y)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
           end = (x,y)
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        cv2.rectangle(img,start,(x,y),(255,0,0),2)
        start=end=(0,0)
cv2.namedWindow('image')
cv2.setMouseCallback('image',mouse_event)

while(True):
    # 下面这句话很关键，拷贝出原图，这样才可以实时画一个矩形
    temp = np.copy(img)
    if (drawing and end!=(0,0)):
        cv2.rectangle(temp,start,end,(0,0,255),2)
    cv2.imshow('image',temp)
    if cv2.waitKey(20) == 27:
        break