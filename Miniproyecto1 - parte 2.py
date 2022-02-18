#Este codigo fue realizado por Carolina López y Camilo Otalora.  # Yo, Carolina López, soy repitente por 3era vez de la materia "Analisis y procesamiento de imagenes" # Por lo tanto se puede encontrar similitud con mis codigos realizados en los semestres 2021-1 y 2021-2 # Esos laboratorios fueron realizados junto a Jaime Andrés Torres - 201815481 y cuento con su  #autorización para utilizar los codigos que ambos implementamos. 

from skimage.draw import disk
import numpy as np
import matplotlib.pyplot as plt


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
                if(encontrado == False):
                    y1= i - 1
                    i2= i 
                    j2 =j 
                    while(mask[i2+1][j2]==1): 
                        i2 = i2+1 
                    y2 = i2 + 1  
                    mitad = 0
                    if((y2 - y1)%2 == 0):
                        mitad = (y2 - y1)/2
                    else: 
                        mitad = (y2 - y1 + 1)/2
                    i2 = y1 + int(mitad)
                    while(mask[i2][j2-1] == 1): 
                        j2 = j2 - 1
                    x1 = j2 - 1  
                    while(mask[i2][j2+1]==1):
                        j2=j2+1
                    x2 = j2 + 1   
                    arreglo = [x1,y1, x2 - x1, y2 - y1]
                    nuevos_puntos = {'image_id': img_id, 'bbox': arreglo}

                    arregloCuadros.append(arreglo)
                    detection.append(nuevos_puntos)
    return detection

def estaEn(cubix, punto):
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



####imagenes1  de 50 por 50

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


#8.3

#pred_file = './data_mp1/dummy_predictions.json'
#FALTA direccion archivo de prediciones xxxxxx

def detections_201814033_201732760(conf_thresh, jaccard_thresh, annot_file, pred_file):
    
    #lee archivo de predicciones 
    with open (pred_file) as j:
        pred = json.load(j)  
    #lee archivo de anotaciones
    with open (annot_file) as j:
        annot = json.load(j)  

    #Guarda todas las predicciones en 'pre'
    for predicion in pred:
       pre = predicion["bbox"] 
    #Guarda todas las anotaciones en 'ano'
    for antotacion in annot:
        ano = antotacion["bbox"] 

    #"Cantidad de verdaderos positivos."
    TP = 0
    #"Cantidad de falsos positivos."
    FP = 0
    #"Cantidad de verdaderos negativos."
    TN = 0
    #"Cantidad de falsos negativos." 
    FN = 0    
        
    #teniendo en cuenta las anotaciones y las predicciones deberian estar en el mismo orden
    #y deberian tener la misma cantidad de anotaciones y de predicciones
    i = 0 
    for each in ano:
        #no encontre la formula pero aca se usaria lo de Jccard y conf thresh xxxxxx
        r = each - pre[i]
        #si es un verdadero positivo la resta deberia dar 0 
        if (r == 0):
            TP = TP +1
        #si es un falso positivo xxxxxx
        elif (r < 0):
            FP = FP +1
         #si es un falso negativo 
        elif (r>0):
            FN = FN +1
        #si es un verdadero negativo 
        else:
            TN = TN +1
            
       
        i= i+1    

    print("Cantidad de verdaderos positivos: ", TP, "\n",    "Cantidad de falsos positivos: ", FP, "\n", "Cantidad de verdaderos negativos: ", TN, "\n",    "CCantidad de falsos negativos: ", FN, "\n")


#8.4

def PRCurve_201814033_201732760(jaccard_thresh, annot_file, pred_file, save_route):

    print("El área por debajo de la curva de precisión y cobertura")



