#Este codigo fue realizado por Carolina López y Camilo Otalora.  # Yo, Carolina López, soy repitente por 3era vez de la materia "Analisis y procesamiento de imagenes" # Por lo tanto se puede encontrar similitud con mis codigos realizados en los semestres 2021-1 y 2021-2 # Esos laboratorios fueron realizados junto a Jaime Andrés Torres - 201815481 y cuento con su  #autorización para utilizar los codigos que ambos implementamos. 

from skimage.draw import disk
import numpy as np
import matplotlib.pyplot as plt
import json
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
import cv2 as cv
from sklearn.metrics import jaccard_score


#Se cargan las imagenes desde las carpetas

fotos_valid = []
for img in glob.glob(os.path.join('data_mp1','BCCD', 'valid', '*.jpg')):
    io_img = io.imread(img)
    fotos_valid.append(io_img)

def Mask2Detection_201814033_201732760(mask, img_id):
    detection =[]
    arregloCuadros = []
    for i in range(len(mask)):             
        for j in range(len(mask[0])):
            if(mask[i][j]==1):
                encontrado = False
                a = 0
                while (encontrado == False and a < len(arregloCuadros)):
                    estaDentro = estaEn(arregloCuadros[a],[j,i])
                    if(estaDentro):
                        encontrado= True
                    a=a+1
                if(encontrado == False):   #procedimiento para tomar punto de abajo
                    y1= i - 1
                    i2= i 
                    j2 =j 
                    while(mask[i2+1][j2]==1): 
                        i2 = i2+1 
                    y2 = i2 + 1  
                    mitad = 0
                    if((y2 - y1)%2 == 0):   #encontrar la mitad para encontrar pontos de izquierda y derecha
                        mitad = (y2 - y1)/2
                    else: 
                        mitad = (y2 - y1 + 1)/2
                    i2 = y1 + int(mitad)
                    while(mask[i2][j2-1] == 1):    #punto esquina izquierda
                        j2 = j2 - 1
                    x1 = j2 - 1  
                    while(mask[i2][j2+1]==1):        #punto esquina derecha
                        j2=j2+1
                    x2 = j2 + 1   
                    arreglo = [x1,y1, x2 - x1, y2 - y1]
                    nuevos_puntos = {'image_id': img_id, 'bbox': arreglo}

                    arregloCuadros.append(arreglo)
                    detection.append(nuevos_puntos)
    return detection

def estaEn(cubix, punto):  #esta funcion mirara si el punto en el que estamos parados pertenece a las coordenadas encontradas en mask2detection o si se trata de un punto nuevo, si se trata de uno nuevo empezara a hacer la cruz de mask2dtection para tener las coordenadas del nuevo circulo
    x1 = cubix[0]
    y1 = cubix[1]
    w = cubix[2]
    h = cubix[3]
    x2= x1+w 
    y2= y1+h 
    estaDentro = False
    if ((x1 <= punto[0] <= x2) and (y1 <= punto[1] <= y2)):
        estaDentro = True
    else: 
        estaDentro = False
    return estaDentro

####imagenes1  de 50 por 50 #el codigo de las 3 imagenes fue tomado de [1]"Module: draw — skimage v0.19.2 docs", Scikit-image.org. [Online]. Available: https://scikit-image.org/docs/stable/api/skimage.draw.html#skimage.draw.disk. [Accessed: 16- Feb- 2022].

imagen_3_circulos = np.zeros((50, 50), dtype=np.uint8)
rr, cc = disk((20, 25 ), 6)
imagen_3_circulos[rr, cc] = 1

rr, cc = disk((7, 9 ), 5)
imagen_3_circulos[rr, cc] = 1

rr, cc = disk((38, 35 ), 8)
imagen_3_circulos[rr, cc] = 1

tres = imagen_3_circulos.copy()

valores_anotaciones_3 =Mask2Detection_201814033_201732760(tres, 3)

#####imagenes2  de 50 por 50
imagen_2_circulos = np.zeros((50, 50), dtype=np.uint8)
rr, cc = disk((11, 36 ), 6)
imagen_2_circulos[rr, cc] = 1

rr, cc = disk((33, 17 ), 9)
imagen_2_circulos[rr, cc] = 1

dos = imagen_2_circulos.copy()


valores_anotaciones_2 =Mask2Detection_201814033_201732760(imagen_2_circulos, 3)

#####imagenes3  de 50 por 50
imagen_1_circulo = np.zeros((50, 50), dtype=np.uint8)
rr, cc = disk((25, 25 ), 10)
imagen_1_circulo[rr, cc] = 1


uno = imagen_1_circulo.copy()

valores_anotaciones_1 =Mask2Detection_201814033_201732760(imagen_1_circulo, 3)

def hacer_recuadros(cuadrados, imagen):

    for k in range(len(cuadrados)):
        cuadrado = cuadrados[k]
        cuadrado = cuadrado["bbox"]
        x1 = cuadrado[0]
        y1 = cuadrado[1]
        w = cuadrado[2]
        h = cuadrado[3]
        x2= x1+w 
        y2= y1+h 

        #Arriba  a la izq, de izq a derecha
        i=y1
        for j in range(x1,x2):
            imagen[i][j] = 1

        #arriba a la izq, de arriba a abajo 
        j=x1
        for i in range(y1,y2):
            imagen[i][j] = 1   

        #abajo a la izq, de izq a derecha 
        i=y2
        for j in range(x1,x2):
            imagen[i][j] = 1    

        #arriba derecha, de arriba a abajo  
        j=x2
        for i in range(y1,y2+1):
            imagen[i][j] = 1  

    return imagen


circulos3_mas_deteccion = hacer_recuadros(valores_anotaciones_3,imagen_3_circulos)

circulos2_mas_deteccion = hacer_recuadros(valores_anotaciones_2,imagen_2_circulos)

circulos1_mas_deteccion = hacer_recuadros(valores_anotaciones_1,imagen_1_circulo)


#Se crea y se llena el subplot
plt.figure(figsize=(13, 10))

plt.subplot(3,2,1)
plt.title('Imagen binaria 1')
plt.axis('off')
plt.imshow(uno, cmap='gray')

plt.subplot(3,2,2)
plt.title('Imagen binaria 1 + recuadros de anotaciones')
plt.axis('off')
plt.imshow(circulos1_mas_deteccion, cmap = 'gray')

plt.subplot(3,2,3)
plt.title('Imagen binaria 2')
plt.axis('off')
plt.imshow(dos, cmap='gray')

plt.subplot(3,2,4)
plt.title('Imagen binaria 2 + recuadros de anotaciones')
plt.axis('off')
plt.imshow(circulos2_mas_deteccion, cmap = 'gray')

plt.subplot(3,2,5)
plt.title('Imagen binaria 3')
plt.axis('off')
plt.imshow(tres, cmap='gray')

plt.subplot(3,2,6)
plt.title('Imagen binaria 3 + recuadros de anotaciones')
plt.axis('off')
plt.imshow(circulos3_mas_deteccion, cmap = 'gray')

plt.savefig('figura 1')
plt.show()

input("Press Enter to continue...")

#8.3

#pred_file = './data_mp1/dummy_predictions.json'
#FALTA direccion archivo de prediciones xxxxxx


#Se abren los archivos json y se cargan en una variable 

annot_file = './data_mp1/BCCD/valid/_annotations.coco.json'
pred_file = './data_mp1/dummy_predictions.json'
def detections_201814033_201732760(conf_thresh, jaccard_thresh, annot_file, pred_file):
  with open (annot_file ) as j:
      anotaciones_reales = json.load(j)    
  with open ( pred_file) as j:
      predicciones_dummy = json.load(j)
  images = {}
  for image in anotaciones_reales["images"]:
    img = io.imread(os.path.join("data_mp1","BCCD","valid",image["file_name"]))
    img[:,:,:] = 0
    images[image["id"]] = img
  TP = 0
  TN = 0 
  FP = 0
  FN = 0
  for pred_annotation in predicciones_dummy:
    xmin_pred, ymin_pred, width_pred, height_pred = pred_annotation['bbox']
    for annotation in anotaciones_reales['annotations']: 
      xmin_real, ymin_real, width_real, height_real= annotation['bbox']      
# Si son de la misma imagen todo bien y clase 3, todo bien 
#   Si el jaccard > umbral y el score > confianza -> TP 
#   Si el jaccard > al umbral y score > confianza pero la clase real !=3 -> FP 
#   No hay  debido a que no se usaran as anotaciones de cosas que no sean globulos blancos-> TN 
#   Categoría 3 pero no se predijo.-> FN 
      if(pred_annotation["image_id"] == annotation["image_id"]):
        img = images[pred_annotation["image_id"]]
        img_pred = cv2.rectangle(img, (int(xmin_pred), int(ymin_pred)), (int(xmin_pred+width_pred), int(ymin_pred+height_pred)), (1,1,1), -1)
        img_act = cv2.rectangle(img, (int(xmin_real), int(ymin_real)), (int(xmin_real+width_real), int(ymin_real+height_real)), (1,1,1), -1)
        jaccard_cond = jaccard_score(img_act.flatten(), img_pred.flatten()) >= jaccard_thresh
        conf_cond = pred_annotation["score"] >= conf_thresh
        if jaccard_cond and conf_cond: 
          if pred_annotation["category_id"] == annotation["category_id"]: 
            TP = TP + 1 
          else: 
            FP = FP + 1 
        elif pred_annotation["category_id"] == annotation["category_id"]: 
          FN = FN +1 

  print("Cantidad de verdaderos positivos: ", TP, "\n",    "Cantidad de falsos positivos: ", FP, "\n", "Cantidad de verdaderos negativos: ", TN, "\n",    "Cantidad de falsos negativos: ", FN, "\n")

  precision = TP / (TP + FP)
  print ('La precision es', precision)

  cobertura = TP / (TP + FN)
  print ('La cobertura es', cobertura)

  fMedida = 2*precision*cobertura/(precision+cobertura)
  print ('La f medida es', fMedida)

  return TP, FP, TN, FN

  
detections_201814033_201732760(0.5, 0.7, annot_file, pred_file)

