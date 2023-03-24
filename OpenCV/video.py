import cv2
#import numpy as np

#video=cv2.VideoCapture("Sin título 1.avi")
video=cv2.VideoCapture(0)

W=video.get(cv2.CAP_PROP_FRAME_WIDTH)#Ancho del video
H=video.get(cv2.CAP_PROP_FRAME_HEIGHT)#Alto del video
F=video.get(cv2.CAP_PROP_FRAME_COUNT)#Cantidad de fotogramas
FPS=video.get(cv2.CAP_PROP_FPS)#Velocidad de fotogramas, fotogramas por segundo
print('Ancho: ',W)
print('Alto: ',H)
print('Fotogramas: ',F)
print('Velocidad: ',FPS)
size = (W, H)
fourcc = cv2.VideoWriter_fourcc(*'WMV1')
path =r'E:\Academico\Universidad\Pregrado\GIBIC\path.avi'
result = cv2.VideoWriter(path,apiPreference = 0,fourcc = fourcc, fps = 30,frameSize = (640,480) )

while True:
    state, frame=video.read()#Funciona mientras las imagenes se muestran
    result.write(frame)
    
    if state==False:#cuando se dejan de mostrar las imagenes state se vuelve falso
        print('Fin de video')
        break
    
    frameR=frame[:,:,2]
    frameG=frame[:,:,1]
    frameB=frame[:,:,0]
    
    cv2.imshow('ventana',frame)
#    cv2.imshow('ventanaR',frameR)
#    cv2.imshow('ventanaG',frameG)
#    cv2.imshow('ventanaB',frameB)
    k=cv2.waitKey(24)
    
    
    if k==27: 
        break


video.release()

cv2.destroyAllWindows()
        
