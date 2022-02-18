#Este codigo fue realizado por Carolina López y Camilo Otalora.  # Yo, Carolina López, soy repitente por 3era vez de la materia "Analisis y procesamiento de imagenes" # Por lo tanto se puede encontrar similitud con mis codigos realizados en los semestres 2021-1 y 2021-2 # Esos laboratorios fueron realizados junto a Jaime Andrés Torres - 201815481 y cuento con su  #autorización para utilizar los codigos que ambos implementamos. 

from skimage.draw import disk
import numpy as np



def Mask2Detection_201814033_201732760(mask, img_id):
    detection = []
    for i in range(len(mask)):
        for j in range(len(mask[0])):
            if(mask[i][j]==1):
                encontrado = False
                a = 0
                while (encontrado == False and a < len(detection)):
                    estaDentro = estaEn(detection[a],[j,i])
                    if(estaDentro):
                        encontrado= True
                    a=a+1

                if(encontrado == False):
                    y1= i
                    i2= i
                    j2 =j
                    while(mask[i2+1][j2]==1):
                        i2 = i2+1
                    y2 = i2

                    mitad = 0
                    if((y1 + y2)%2 == 0):
                        mitad = (y1 + y2)/2


                    else: 
                        mitad = (y1 + y2 + 1)/2

                    i2 = int(mitad)
                    
                    while(mask[i2][j2-1] == 1):
                        j2 = j2 - 1
                    x1 = j2

                    while(mask[i2][j2+1]==1):
                        j2=j2+1
                    x2 = j2
                    
                    arreglo = [x1,y1, x2 - x1, y2 - y1]

                    detection.append(arreglo)
                
    print(detection)
    return detection

def estaEn(cubix, punto):
    x1 = cubix[0]
    y1 = cubix[1]
    w = cubix[2]
    h = cubix[3]
    x2= x1+w
    y2= y1+h
    estaDentro = False
    if ((x1 < punto[0] < x2) and (y1 < punto[1]) < y2 ):
        estaDentro = True
    else: 
        estaDentro = False 
        
    return estaDentro                           






#imagenes de 50 por 50

img = np.zeros((50, 50), dtype=np.uint8)
rr, cc = disk((15, 15), 7)
img[rr, cc] = 1
img   


Mask2Detection_201814033_201732760(img, 3)