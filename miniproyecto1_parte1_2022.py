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
test_cant_Platelets = contador[1]
test_cant_RBC = contador[2]
test_cant_WBC = contador[3]
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
train_cant_Platelets = contador[1]
train_cant_RBC = contador[2]
train_cant_WBC = contador[3]
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
valid_cant_Platelets = contador[1]
valid_cant_RBC = contador[2]
valid_cant_WBC = contador[3]
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

total_celulas_test = test_cant_Platelets + test_cant_RBC + test_cant_WBC
total_celulas_train = train_cant_Platelets + train_cant_RBC + train_cant_WBC
total_celulas_valid =  valid_cant_Platelets + valid_cant_RBC + valid_cant_WBC
total_celulas = total_celulas_test + total_celulas_train + total_celulas_valid

#calcula porcentage de un valor a sobre un 100% dado g
def percent(a, g):
  ret = a * 100 / g
  return ret

p_test_P = percent(test_cant_Platelets, total_celulas_test)
p_test_R = percent(test_cant_RBC, total_celulas_test)
p_test_W = percent(test_cant_WBC, total_celulas_test)
p_test_total_P = percent(test_cant_Platelets, total_celulas)
p_test_total_R = percent(test_cant_RBC, total_celulas)
p_test_total_W = percent(test_cant_WBC, total_celulas)

p_train_P = percent(train_cant_Platelets, total_celulas_test)
p_train_R = percent(train_cant_RBC, total_celulas_test)
p_train_W = percent(train_cant_WBC, total_celulas_test)
p_train_total_P = percent(train_cant_Platelets, total_celulas)
p_train_total_R = percent(train_cant_RBC, total_celulas)
p_train_total_W = percent(train_cant_WBC, total_celulas)

p_valid_P= percent(valid_cant_Platelets, total_celulas_test)
p_valid_R = percent(valid_cant_RBC, total_celulas_test)
p_valid_W = percent(valid_cant_WBC, total_celulas_test)
p_valid_total_P = percent(valid_cant_Platelets, total_celulas)
p_valid_total_R = percent(valid_cant_RBC, total_celulas)
p_valid_total_W = percent(valid_cant_WBC, total_celulas)

print(
  "El total de celulas que hay en el set de test es ", total_celulas_test,"\n"  
  "La cantidad de plaquetas que hay en el set completo de test es ", test_cant_Platelets,
  "representando un",p_test_P,"%"," sobre el total de las celulas que hay en test y un ",p_test_total_P,"%",
  " sobre el total \n",
  "La cantidad de globulos rojos que hay en el set completo de test es ", test_cant_RBC ,
  "representando un",p_test_R,"%"," sobre el total de las celulas que hay en test y un ",p_test_total_R,"%",
  " sobre el total \n",
  "La cantidad de globulos blancos que hay en el set completo de test es ", test_cant_WBC ,
  "representando un",p_test_W,"%"," sobre el total de las celulas que hay en test y un ",p_test_total_W,"%",
  " sobre el total \n \n",

  "El total de celulas que hay en el set de train es ", total_celulas_train,"\n"
  "La cantidad de plaquetas que hay en el set completo de train es ", train_cant_Platelets,
  "representando un",p_train_P,"%"," sobre el total de las celulas que hay en train y un ",p_train_total_P,"%",
  " sobre el total \n",
  "La cantidad de globulos rojos que hay en el set completo de train es ", train_cant_RBC ,
  "representando un",p_train_R,"%"," sobre el total de las celulas que hay en train y un ",p_train_total_R,"%",
  " sobre el total \n",
  "La cantidad de globulos blancos que hay en el set completo de train es ", train_cant_WBC ,
  "representando un",p_train_W,"%"," sobre el total de las celulas que hay en train y un ",p_train_total_W,"%",
  " sobre el total \n \n",

  "El total de celulas que hay en el set de valid es ", total_celulas_valid,"\n"
  "La cantidad de plaquetas que hay en el set completo de valid es ", valid_cant_Platelets,
  "representando un",p_valid_P,"%"," sobre el total de las celulas que hay en train y un ",p_valid_total_P,"%",
  " sobre el total \n",
  "La cantidad de globulos rojos que hay en el set completo de valid es ", valid_cant_RBC ,
  "representando un",p_valid_R,"%"," sobre el total de las celulas que hay en train y un ",p_valid_total_R,"%",
  " sobre el total \n",
  "La cantidad de globulos blancos que hay en el set completo de valid es ", valid_cant_WBC ,
  "representando un",p_valid_W,"%"," sobre el total de las celulas que hay en train y un ",p_valid_total_W,"%",
  " sobre el total \n \n",
  
  "El total de celulas que hay en el total de las imagenes (totoal general) es ", total_celulas,"\n \n"
  
)

p_ima_test = percent(imagenes_en_test, numero_total_imagenes)
p_ima_train = percent(imagenes_en_train, numero_total_imagenes)
p_ima_valid = percent(imagenes_en_valid, numero_total_imagenes)

p_ano_test = percent(anotaciones_en_test, total_anotaciones)
p_ano_train = percent(anotaciones_en_train, total_anotaciones)
p_ano_valid = percent(anotaciones_en_valid, total_anotaciones)

print (
  "Teniendo en cuenta que el total de imagenes es de", numero_total_imagenes, "\n \n",

  "El porcentaje de imagenes en test representa un ", p_ima_test,"%"," sobre el total las imagenes en test. \n",
  "El porcentaje de imagenes en train representa un ", p_ima_train,"%"," sobre el total las imagenes en train. \n",
  "El porcentaje de imagenes en valid representa un ", p_ima_valid,"%"," sobre el total las imagenes en valid. \n \n",

  "Teniendo en cuenta que el total de anotaiones es de", total_anotaciones, "\n \n",

  "El porcentaje de anotaciones en test representa un ",   p_ano_test,"%"," sobre el total lasanotaciones en test. \n",
  "El porcentaje de anotaciones en train representa un ", p_ano_train,"%"," sobre el total las anotaciones en train. \n",
  "El porcentaje de anotaciones en valid representa un ", p_ano_valid,"%"," sobre el total las anotaciones en valid. "
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