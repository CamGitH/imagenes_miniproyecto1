import os 
import shutil
from tkinter import image_names 
import matplotlib.pyplot as plt
import glob 
import cv2
from numpy import TooHardError
from skimage import io
import os
import json


fotos_test = []
for img in glob.glob(os.path.join('data_mp1','BCCD', 'test', '*.jpg')):
    io_img = io.imread(img)
    fotos_test.append(io_img)

#plt.imshow(fotos[0])

fotos_train = []
for img in glob.glob(os.path.join('data_mp1','BCCD', 'train', '*.jpg')):
    io_img = io.imread(img)
    fotos_train.append(io_img)


fotos_valid = []
for img in glob.glob(os.path.join('data_mp1','BCCD', 'valid', '*.jpg')):
    io_img = io.imread(img)
    fotos_valid.append(io_img)

#7.2.1

#Se crea y se llena el subplot
plt.figure(figsize=(13, 10))

plt.subplot(2,4,1)
plt.axis('off')
plt.imshow(fotos_test[0])

plt.subplot(2,4,2)
plt.axis('off')
plt.imshow(fotos_train[1])

plt.subplot(2,4,3)
plt.axis('off')
plt.imshow(fotos_valid[2])

plt.subplot(2,4,4)
plt.axis('off')
plt.imshow(fotos_test[3])

plt.subplot(2,4,5)
plt.axis('off')
plt.imshow(fotos_train[4])

plt.subplot(2,4,6)
plt.axis('off')
plt.imshow(fotos_valid[5])

plt.subplot(2,4,7)
plt.axis('off')
plt.imshow(fotos_test[6])

plt.subplot(2,4,8)
plt.axis('off')
plt.imshow(fotos_train[7])

plt.savefig('figura 1')
plt.show()

input("Press Enter to continue...")


#7.2.2

#Se abren los archivos json y se cargan en una variable 
with open ( './data_mp1/BCCD/test/_annotations.coco.json') as j:
    datos_test = json.load(j)
    
with open ( './data_mp1/BCCD/train/_annotations.coco.json') as j:
    datos_train = json.load(j)

with open ( './data_mp1/BCCD/train/_annotations.coco.json') as j:
    datos_valid = json.load(j)

#para test:
#numero de imagenes en test
imagenes_en_test = len(datos_test['images'])
print("Cantidad de imagenes en test:", imagenes_en_test) 

#Realizar contador para ver cuantas anotaciones hay por categoria hay por diccionario en test
contador = dict()
for anotacion in datos_test['annotations']:
  categoria = anotacion["category_id"] 
  contador[categoria] = contador.get(categoria,0) + 1
print(contador) #anotaciones en cada categoria de test

#cuantas anotaciones hay en total en el json de test
anotaciones_en_test = len(datos_test['annotations'])
print('cantidad de anotaciones de detección que hay en test', anotaciones_en_test)

#Promedio de anotaciones por imagen en la carpeta test, se hace dividiendo el numero de anotaciones sobre el numero de imagenes 
print('El promedio de anotaciones por imagen para test', anotaciones_en_test/imagenes_en_test)


#Para train 
#numero de imagenes en train
imagenes_en_train = len(datos_train['images'])
print("Cantidad de imagenes en train", imagenes_en_train) 

#Realizar contador para ver cuantas anotaciones hay por categoria hay por diccionario en train
contador = dict()
for anotacion in datos_train['annotations']:
  categoria = anotacion["category_id"] 
  contador[categoria] = contador.get(categoria,0) + 1
print(contador) #anotaciones en cada categoria de train

#cuantas anotaciones hay en total en el json de test
anotaciones_en_train = len(datos_train['annotations'])
print('cantidad de anotaciones de detección que hay en train',anotaciones_en_train)

#Promedio de anotaciones por imagen en la carpeta test, se hace dividiendo el numero de anotaciones sobre el numero de imagenes 
print('El promedio de anotaciones por imagen para train', anotaciones_en_train/imagenes_en_train)


#Para valid 
#numero de imagenes en valid
imagenes_en_valid=len(datos_valid['images'])
print("Cantidad de imagenes en valid:", imagenes_en_valid) 

#Realizar contador para ver cuantas anotaciones hay por categoria hay por diccionario en valid
contador = dict()
for anotacion in datos_valid['annotations']:
  categoria = anotacion["category_id"] 
  contador[categoria] = contador.get(categoria,0) + 1
print(contador) #anotaciones en cada categoria de valid

#cuantas anotaciones hay en total en el json de test
anotaciones_en_valid = len(datos_valid['annotations'])
print('El promedio de anotaciones por imagen para valid', anotaciones_en_valid)

#Promedio de anotaciones por imagen en la carpeta valid, se hace dividiendo el numero de anotaciones sobre el numero de imagenes 
print('el numero de anotaciones promedio por imagen es', anotaciones_en_valid/imagenes_en_valid)

#total de anotaciones
total_anotaciones = anotaciones_en_test + anotaciones_en_train + anotaciones_en_valid
print('la cantidad total de anotaciones es', total_anotaciones)

#promedio de anotaciones para cada imagen en total
numero_total_imagenes = imagenes_en_test + imagenes_en_train + imagenes_en_valid
promedio_anotaciones_total = (total_anotaciones / numero_total_imagenes)
print('El promedio de anotaciones por imagen en total es', promedio_anotaciones_total)

#7.2.3

p_ima_test = imagenes_en_test * 100 / numero_total_imagenes
p_ima_train = imagenes_en_train * 100 / numero_total_imagenes
p_ima_valid = imagenes_en_valid * 100 / numero_total_imagenes

p_ano_test = anotaciones_en_test * 100 / total_anotaciones
p_ano_train = anotaciones_en_train * 100 / total_anotaciones
p_ano_valid = anotaciones_en_valid * 100 / total_anotaciones

print (
"En las imagenes, \n",
"El porcentaje de imagenes en test sobre el total es del: ", p_ima_test,"% \n",
"El porcentaje de imagenes en train sobre el total es del: ", p_ima_train,"% \n",
"El porcentaje de imagenes en valid sobre el total es del: ", p_ima_valid,"% \n \n",
"Mientras que en las anotaciones, \n",
"El porcentaje de anotaciones en test sobre el total es del: ", p_ano_test,"% \n",
"El porcentaje de anotaciones en train sobre el total es del: ", p_ano_train,"% \n",
"El porcentaje de anotaciones en valid sobre el total es del: ", p_ano_valid,"%"
)

#7.3

#Se crea y se llena el subplot
plt.figure(figsize=(13, 10))

plt.subplot(4,4,1)
plt.axis('off')
plt.imshow()

plt.subplot(4,4,2)
plt.axis('off')
plt.imshow()

plt.subplot(4,4,3)
plt.axis('off')
plt.imshow()

plt.subplot(4,4,4)
plt.axis('off')
plt.imshow()

plt.subplot(4,4,5)
plt.axis('off')
plt.imshow()

plt.subplot(4,4,6)
plt.axis('off')
plt.imshow()

plt.subplot(4,4,7)
plt.axis('off')
plt.imshow()

plt.subplot(4,4,8)
plt.axis('off')
plt.imshow()

plt.subplot(4,4,9)
plt.axis('off')
plt.imshow()
 
plt.subplot(4,4,10)
plt.axis('off')
plt.imshow()

plt.subplot(4,4,11)
plt.axis('off')
plt.imshow()

plt.subplot(4,4,12)
plt.axis('off')
plt.imshow()

plt.subplot(4,4,13)
plt.axis('off')
plt.imshow()

plt.subplot(4,4,14)
plt.axis('off')
plt.imshow()

plt.subplot(4,4,15)
plt.axis('off')
plt.imshow()

plt.subplot(4,4,16)
plt.axis('off')
plt.imshow()

plt.savefig('figura 2')
plt.show()

input("Press Enter to continue...")