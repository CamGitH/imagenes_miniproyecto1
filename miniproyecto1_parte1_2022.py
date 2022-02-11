#Este codigo fue realizado por Carolina López y Camilo Otalora.  # Yo, Carolina López, soy repitente por 3era vez de la materia "Analisis y procesamiento de imagenes" # Por lo tanto se puede encontrar similitud con mis codigos realizados en los semestres 2021-1 y 2021-2 # Esos laboratorios fueron realizados junto a Jaime Andrés Torres - 201815481 y cuento con su  #autorización para utilizar los codigos que ambos implementamos. 

import os
from skimage import color
from skimage import io
from re import sub 
import shutil 
import matplotlib.pyplot as plt
import glob 
import cv2
from skimage import io
import os
import json
import numpy as np
import sys

#Se cargan las imagenes desde las carpetas
fotos_test = []
for img in glob.glob(os.path.join('data_mp1','BCCD', 'test', '*.jpg')):
    io_img = io.imread(img)
    fotos_test.append(io_img)

fotos_train = []
for img in glob.glob(os.path.join('data_mp1','BCCD', 'train', '*.jpg')):
    io_img = io.imread(img)
    fotos_train.append(io_img)

fotos_valid = []
for img in glob.glob(os.path.join('data_mp1','BCCD', 'valid', '*.jpg')):
    io_img = io.imread(img)
    fotos_valid.append(io_img)

####7.2.1

#Se crea y se llena el subplot
plt.figure(figsize=(13, 10))

plt.subplot(2,4,1)
plt.title('Imagen test 0')
plt.axis('off')
plt.imshow(fotos_test[0], cmap='gray')

plt.subplot(2,4,2)
plt.title('Imagen train 1')
plt.axis('off')
plt.imshow(fotos_train[1], cmap='gray')

plt.subplot(2,4,3)
plt.title('Imagen valid 2')
plt.axis('off')
plt.imshow(fotos_valid[2], cmap='gray')

plt.subplot(2,4,4)
plt.title('Imagen test 3')
plt.axis('off')
plt.imshow(fotos_test[3], cmap='gray')

plt.subplot(2,4,5)
plt.title('Imagen train 4')
plt.axis('off')
plt.imshow(fotos_train[4], cmap='gray')

plt.subplot(2,4,6)
plt.title('Imagen valid 5')
plt.axis('off')
plt.imshow(fotos_valid[5], cmap='gray')

plt.subplot(2,4,7)
plt.title('Imagen test 6')
plt.axis('off')
plt.imshow(fotos_test[6], cmap='gray')

plt.subplot(2,4,8)
plt.title('Imagen train 7')
plt.axis('off')
plt.imshow(fotos_train[7], cmap='gray')

plt.savefig('figura 1')
plt.show()

input("Press Enter to continue...")


######7.2.2

#Se abren los archivos json y se cargan en una variable 
with open ( './data_mp1/BCCD/test/_annotations.coco.json') as j:
    datos_test = json.load(j)
    
with open ( './data_mp1/BCCD/train/_annotations.coco.json') as j:
    datos_train = json.load(j)

with open ( './data_mp1/BCCD/train/_annotations.coco.json') as j:
    datos_valid = json.load(j)

#para test:
#numero de imagenes en test
imagenes_en_test = len(datos_test['images'])   #numero de imagenes en test
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
print('El promedio de anotaciones por imagen para test', len(datos_test['annotations'])/len(datos_test['images']))


#Para train 
imagenes_en_train = len(datos_train['images'])  #numero de imagenes en train
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
print('El promedio de anotaciones por imagen para train', len(datos_train['annotations'])/len(datos_train['images']))


#Para valid 
imagenes_en_valid=len(datos_valid['images'])  #numero de imagenes en valid
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

#cuantas anotaciones en promedio hay en total en el json de test
print('El promedio de anotaciones por imagen para valid', len(datos_valid['annotations'])/len(datos_valid['images']))

#total de anotaciones
total_anotaciones = (len(datos_test['annotations']) + len(datos_train['annotations']) + len(datos_valid['annotations']))
print('La cantidad total de anotaciones es', total_anotaciones)

#Promedio de anotaciones por imagen en la carpeta valid, se hace dividiendo el numero de anotaciones sobre el numero de imagenes 
print('El numero de anotaciones promedio por imagen en valid es:', len(datos_valid['annotations'])/len(datos_valid['images']))


#promedio de anotaciones para cada imagen en total
numero_total_imagenes = (len(datos_valid['images']) + len(datos_train['images']) + len(datos_test['images']))
promedio_anotaciones_total = (total_anotaciones / numero_total_imagenes)
print('El promedio de anotaciones por imagen en total es', promedio_anotaciones_total)

#####7.2.2

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

print("El total de celulas que hay en el set de test es ", total_celulas_test,"\n"  
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



#####7.3.1

def visualize_annotations(fold, img_name, annotations_json_name='_annotations.coco.json', interest_class=-1):  #Codigo tomado del archivo utils
    '''
    Parameters
    ----------
    fold : 'train', 'valid' or 'test' depending on the source fold the image comes from.
    img_name : image of interest from the 'fold' folder name (including the extension).
    annotations_json_name : name of the json located into the 'fold' folder.
    interest_class : Class of interest label to draw only those annotations. If -1 all the annotations are shown.

    Returns
    -------
    img : img_name image content overwritten with the corresponding annotations.

    '''
    # Classes of the Aquarium Dataset
    CLASSES = ['cells', 'platelet', 'red blood cell', 'white blood cell',]   #Codigo tomado del archivo utils

    # Colors for visualization (one per class)
    COLORS = [[0,0,0], [0, 255, 0], [255, 0, 0], [0, 0, 255]]     #Codigo tomado del archivo utils
    
    # Obtaining the images and annotations from de json file
    json_data = json.load(open(os.path.join('data_mp1','BCCD', fold, annotations_json_name), 'r'))    #Codigo tomado del archivo utils
    images = json_data['images']      #Codigo tomado del archivo utils
    annotations = json_data['annotations']      #Codigo tomado del archivo utils
    
    # Importing the image of interest
    img = cv2.imread(os.path.join('data_mp1','BCCD', fold, img_name))       #Codigo tomado del archivo utils
    for i in images:       #Codigo tomado del archivo utils
        # Selection of the id of the image of interest
        if i['file_name'] == img_name:    #Codigo tomado del archivo utils
            train_id = i['id']      #Codigo tomado del archivo utils
            
            # Variables where each annotation, its class type and repsective color to use are added.
            boxes = []      #Codigo tomado del archivo utils
            classes = []      #Codigo tomado del archivo utils
            colors = []     #Codigo tomado del archivo utils
            
            for i in annotations:     #Codigo tomado del archivo utils
                # Adding all the annotations that correspond to the desired image.
                if i['image_id'] == train_id and interest_class != -1:      #Codigo tomado del archivo utils
                    if i['category_id'] == interest_class:      #Codigo tomado del archivo utils
                        boxes.append(i['bbox'])      #Codigo tomado del archivo utils
                        classes.append(CLASSES[i['category_id']])     #Codigo tomado del archivo utils
                        colors.append(COLORS[i['category_id']])     #Codigo tomado del archivo utils
                elif i['image_id'] == train_id:     #Codigo tomado del archivo utils
                    boxes.append(i['bbox'])     #Codigo tomado del archivo utils
                    classes.append(CLASSES[i['category_id']])     #Codigo tomado del archivo utils
                    colors.append(COLORS[i['category_id']])     #Codigo tomado del archivo utils
            # Visualization of the annotations
            size=2     #Codigo tomado del archivo utils
            for cl, (xmin, ymin, width, height), c in zip(classes, boxes, colors):    #Codigo tomado del archivo utils
                cv2.rectangle(img, (int(xmin), int(ymin)), (int(xmin+width), int(ymin+height)), c, size)     #Codigo tomado del archivo utils
                text = f'{cl}'    #Codigo tomado del archivo utils
                cv2.putText(img=img, text=text, org=(xmin, ymin-5), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1.2, color=c,thickness=size-1)     #Codigo tomado del archivo utils

    return img     #Codigo tomado del archivo utils

img = visualize_annotations("test", "BloodImage_00038_jpg.rf.03231bab33fddc4fabbb488a9d458343.jpg","_annotations.coco.json",0)
plaqueta = visualize_annotations("test", "BloodImage_00038_jpg.rf.03231bab33fddc4fabbb488a9d458343.jpg","_annotations.coco.json",3)
gRojo = visualize_annotations("test", "BloodImage_00038_jpg.rf.03231bab33fddc4fabbb488a9d458343.jpg","_annotations.coco.json",2)
gBlanco = visualize_annotations("test", "BloodImage_00038_jpg.rf.03231bab33fddc4fabbb488a9d458343.jpg","_annotations.coco.json",1)

img2 = visualize_annotations("test", "BloodImage_00062_jpg.rf.b00505af820be7ec5988bbd808744c76.jpg","_annotations.coco.json",0)
plaqueta2 = visualize_annotations("test", "BloodImage_00062_jpg.rf.b00505af820be7ec5988bbd808744c76.jpg","_annotations.coco.json",3)
gRojo2 = visualize_annotations("test", "BloodImage_00062_jpg.rf.b00505af820be7ec5988bbd808744c76.jpg","_annotations.coco.json",2)
gBlanco2 = visualize_annotations("test", "BloodImage_00062_jpg.rf.b00505af820be7ec5988bbd808744c76.jpg","_annotations.coco.json",1)

img3 = visualize_annotations("test", "BloodImage_00099_jpg.rf.e3dbcb7c512ca1c50501f5a02fdab561.jpg","_annotations.coco.json",0)
plaqueta3 = visualize_annotations("test", "BloodImage_00099_jpg.rf.e3dbcb7c512ca1c50501f5a02fdab561.jpg","_annotations.coco.json",3)
gRojo3 = visualize_annotations("test", "BloodImage_00099_jpg.rf.e3dbcb7c512ca1c50501f5a02fdab561.jpg","_annotations.coco.json",2)
gBlanco3 = visualize_annotations("test", "BloodImage_00099_jpg.rf.e3dbcb7c512ca1c50501f5a02fdab561.jpg","_annotations.coco.json",1)

img4 = visualize_annotations("test", "BloodImage_00112_jpg.rf.f973440f804c0e587b2f02d2b17164b3.jpg","_annotations.coco.json",0)
plaqueta4 = visualize_annotations("test", "BloodImage_00112_jpg.rf.f973440f804c0e587b2f02d2b17164b3.jpg","_annotations.coco.json",3)
gRojo4 = visualize_annotations("test", "BloodImage_00112_jpg.rf.f973440f804c0e587b2f02d2b17164b3.jpg","_annotations.coco.json",2)
gBlanco4 = visualize_annotations("test", "BloodImage_00112_jpg.rf.f973440f804c0e587b2f02d2b17164b3.jpg","_annotations.coco.json",1)

plt.figure(figsize=(13, 10))

plt.subplot(4,4,1)
plt.axis('off')
# Original
plt.imshow(img, cmap='gray')

plt.subplot(4,4,2)
plt.axis('off')
# Original
plt.imshow(plaqueta, cmap='gray')

plt.subplot(4,4,3)
plt.axis('off')
# Original
plt.imshow(gRojo, cmap='gray')

plt.subplot(4,4,4)
plt.axis('off')
# Original
plt.imshow(gBlanco, cmap='gray')

plt.subplot(4,4,5)
plt.axis('off')
# Original
plt.imshow(img2, cmap='gray')

plt.subplot(4,4,6)
plt.axis('off')
# Original
plt.imshow(plaqueta2, cmap='gray')

plt.subplot(4,4,7)
plt.axis('off')
# Original
plt.imshow(gRojo2, cmap='gray')

plt.subplot(4,4,8)
plt.axis('off')
# Original
plt.imshow(gBlanco3, cmap='gray')

plt.subplot(4,4,9)
plt.axis('off')
# Original
plt.imshow(img3, cmap='gray')

plt.subplot(4,4,10)
plt.axis('off')
# Original
plt.imshow(plaqueta3, cmap='gray')

plt.subplot(4,4,11)
plt.axis('off')
# Original
plt.imshow(gRojo3, cmap='gray')

plt.subplot(4,4,12)
plt.axis('off')
# Original
plt.imshow(gBlanco3, cmap='gray')

plt.subplot(4,4,13)
plt.axis('off')
# Original
plt.imshow(img4, cmap='gray')

plt.subplot(4,4,14)
plt.axis('off')
# Original
plt.imshow(plaqueta4, cmap='gray')

plt.subplot(4,4,15)
plt.axis('off')
# Original
plt.imshow(gRojo4, cmap='gray')

plt.subplot(4,4,16)
plt.axis('off')
# Original
plt.imshow(gBlanco4, cmap='gray')
  
plt.show()

input("Press Enter to continue...")



#####7.3.2

plt.figure(figsize=(13, 10))
for x in range(4):
      
  image = fotos_test[x]

  n = image.copy()
  n= color.rgb2gray(n)
    

  b = image.copy()   #refrencia [1]
  # set green and red channels to 0  #refrencia [1]
  b[:, :, 1] = 0   #refrencia [1]
  b[:, :, 2] = 0   #refrencia [1]
  b= color.rgb2gray(b)
      
  g = image.copy()   #refrencia [1]
  # set blue and red channels to 0
  g[:, :, 0] = 0    #refrencia [1]
  g[:, :, 2] = 0    #refrencia [1]
  g= color.rgb2gray(g)

  r = image.copy()
  # set blue and green channels to 0
  r[:, :, 0] = 0   #refrencia [1]
  r[:, :, 1] = 0   #refrencia [1]
  r= color.rgb2gray(r)

  plt.subplot(4,4,(1 + x*4))
  plt.title('Imagen original')
  plt.axis('off')
  # Original
  plt.imshow(n, cmap='gray')

  plt.subplot(4,4, (2 + x*4))
  plt.title('Imagen canal R')
  plt.axis('off')
  # RGB - RED
  plt.imshow(r, cmap='gray')
    
  plt.subplot(4,4, (3 + x*4))
  plt.title('Imagen canal G')
  plt.axis('off')
  # RGB - Green
  plt.imshow(g, cmap='gray')

  plt.subplot(4,4, (4 + x*4))  
  plt.title('Imagen canal B')
  plt.axis('off')
  # RGB - BLUE
  plt.imshow(b, cmap='gray')
    
  cv2.waitKey(0)   #refrencia [1]
  plt.savefig('figura 3')
  
plt.show()

input("Press Enter to continue...")





#Referencias

#[1]"python: ¿solo quieres mostrar el canal rojo en opencv? - programador clic", Programmerclick.com.
#[Online]. Available: https://programmerclick.com/article/36551588535/. [Accessed: 10- Feb- 2022].
