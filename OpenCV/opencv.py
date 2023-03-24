# Llamar la libreria
import cv2

#Leer la imagen
path = r"E:\Academico\Universidad\Cursos\Repositorios\Info-2\OpenCV\brain.png"
img=cv2.imread(path)

#Caracteristicas

print (img.shape)
print (img.size)
print (img.dtype)

#Tomar los 3 canales
imgR=img[:,:,0]
imgG=img[:,:,1]
imgB=img[:,:,2]

#Entar a los pixeles de la imagen
print(img[100,100])

#Crear imagen
cv2.imwrite('ImagenX.png',imgR)

#Crear ventana
cv2.namedWindow('Ventana',0)
cv2.namedWindow('VentanaB',0)
cv2.namedWindow('VentanaG',0)
cv2.namedWindow('VentanaR',0)

#Mostrar imagen
cv2.imshow('Ventana',img)
cv2.imshow('VentanaR',imgB)
cv2.imshow('VentanaG',imgG)
cv2.imshow('VentanaB',imgR)

#Detener la imagen
cv2.waitKey(0)
#Cerrar las ventanas
cv2.destroyAllWindows()




