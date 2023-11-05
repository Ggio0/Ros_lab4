# Ros_lab4

# Miembros:
Edgar Giovanny Obregon Espitia

Juan Nicolas Carvajal Useche
# Descripción de la solución planteada
# Modelo cinemático directo del robot
Se creó el modelo cinemático del robot usando la toolbox de Peter Corke. Inicialmente, se midieron los eslabones utilizando un calibrador pie de rey. Las imágenes de las mediciones se pueden observar en las figuras 1 y 2.

![image](https://github.com/Ggio0/Ros_lab4/assets/82681128/e56b815a-ae50-4f35-b21e-6d3771fc8a63)

Figura 1. Mediciones tomadas para el robot.

![image](https://github.com/Ggio0/Ros_lab4/assets/82681128/d53bf454-3270-4775-bda9-6787d546b33a)

 
Figura 2. Medición de la base. 
Los resultados fueron L1=45mm, L2= L3=105mm, L4 = 75mm. Cabe aclarar que L4 va hasta el centro la “base” del gripper, la distancia desde esta base al centro del gripper es de 20mm. Ahora se realiza el esquema del robot para establecer los sistemas coordenados y así los parámetros DH. Este diagrama se observa en la figura 3.

![image](https://github.com/Ggio0/Ros_lab4/assets/82681128/4b0926c3-b1c8-425d-8de0-ddacdfc18eae)


Figura 3. Diagrama del robot. Por comodidad en el documento se poner horizontal.
A estos sistemas coordenados le corresponden los parámetros mostrados en la figura 4.

![image](https://github.com/Ggio0/Ros_lab4/assets/82681128/606fc8a0-6e5e-4184-b7d0-50394a60bd02)


Figura 4. Parámetros DH.
Luego, se crearon las matrices de transformación homogénea para cada eslabón, se realizó el modelo cinemático directo desde la base hasta el centro del gripper multiplicando las matrices de cada eslabón. Dada la extensión de estas matrices, se dejan en el código de Matlab anexo a este repositorio en https://github.com/Ggio0/Ros_lab4/tree/main/Entregables/Matlab .

Este modelo es simulado usando la toolbox de Peter Corke y se simulan las 4 poses dadas por la guía para compararlas con la pose del robot en la implementación física. Los resultados se muestran en las figuras 5, 6, 7, 8, 9.

![image](https://github.com/Ggio0/Ros_lab4/assets/82681128/6a3c328e-57b5-4420-86b3-4c516c9355ec)

Figura 5. Comparación de la simulación con la implementación de la pose 1.

![image](https://github.com/Ggio0/Ros_lab4/assets/82681128/07c658a7-83da-4fd9-aa8c-21d3ace0a2a0)

Figura 6. Comparación de la simulación con la implementación de la pose 2.

![image](https://github.com/Ggio0/Ros_lab4/assets/82681128/d923970b-b1fb-412a-a3a9-ca6796f29a92)

Figura 7. Comparación de la simulación con la implementación de la pose 3.

![image](https://github.com/Ggio0/Ros_lab4/assets/82681128/02fde358-064a-4b1e-a724-efb023f29378)


Figura 8. Comparación de la simulación con la implementación de la pose 4.

![image](https://github.com/Ggio0/Ros_lab4/assets/82681128/e7048911-8bd3-4055-857b-f54b022a4e22)

  
Figura 9. Comparación de la simulación con la implementación de la pose home.

Conexión al phantom

Para la conexión al phantom, se instalaron las librerías de dynamixel para su utilización en Ros, primero se realizó la verificación por la aplicación de Dynamixwl Wizard de las posiciones del robot, los limites articulares y la limitación de torque de cada motor.
Posteriormente se verifica la conexión del puerto y se ejecuta atreves de ROS el archivo pxcontroler.launch para realizar la conexión y nombrar las articulaciones por medio de archivo joints.yaml como se ve en la siguiente Figura 10.

![image](https://github.com/Ggio0/Ros_lab4/assets/82681128/1c20613c-dfe9-4572-af53-aafb9ab68525)

Figura 10. Código Joints.yml.
Código de Python y catkin

Se configura el archivo CmakeList.txt para agregar el script de Python donde esta nuestro código, además de archivos adicionales como las imágenes usadas para la interfaz gráfica, ver figura 11.

![image](https://github.com/Ggio0/Ros_lab4/assets/82681128/6e3d3c9b-ad02-4861-a34e-d8a1329324a5)

Figura 11 código CmakeList.txt.
Una vez creadas las rutas procedemos con la realización del código, donde utilizamos 3 servicios,  publicar, en la función join_publisher, donde tiene como parámetro un vector con la configuración de cada articulación en radianes; suscribirse, en la función listener, el cual se encarga de recibir las posiciones actuales del phantom, y por último el servicio de dynamixel, el cual no permite ajustar diversos parámetros de acuerdo al número id y su valor, en nuestra aplicación se usó para limitar el torque como se muestra en la figura 12.

![image](https://github.com/Ggio0/Ros_lab4/assets/82681128/9298196d-86bb-43d5-9b08-99d95ce2890b)


Figura 12 código en python.

Con estos servicios, se crea la función movTotalPartes, la cual recibe la posición objetivo y la posición presente y se encarga de mover articulación por articulación hasta llegar a la pose requerida.


Interfaz grafica

La interfaz gráfica se llevó a cabo con la librería tkinter, donde se agregaron los nombres de los integrantes del grupo, dos imágenes, en la izquierda la pose pasada del robot, y en la derecha la pose actual, posteriormente se imprimen los valores de la pose anterior y luego los de la pose actual, por último, se configuraron 5 botones, los cuales se encargarían de llevar el robot articulación por articulación hasta la pose objetivo, dicha interfaz se muestra en la siguiente figura 13.

![image](https://github.com/Ggio0/Ros_lab4/assets/82681128/a4586784-dbf4-4d67-ab04-e6fa92027348)


Figura 13 código Interfaz gráfica.

# Codigo en python
Programa en python usado para el desarrollo de la practica.

https://github.com/Ggio0/Ros_lab4/tree/main/Entregables/Python

# Codigo en matkab
Programa en matlab usado para el desarrollo de la practica.

https://github.com/Ggio0/Ros_lab4/tree/main/Entregables/Matlab

# Videos
Video del brazo alcanzando las poses



https://github.com/Ggio0/Ros_lab4/assets/82681128/892067d7-232c-484e-b4e7-d8a8797ffe56



https://github.com/Ggio0/Ros_lab4/assets/82681128/a5c70cd1-92f4-4e4b-8044-1e96def28f25


ver en mejor calidad.

https://github.com/Ggio0/Ros_lab4/tree/main/Entregables/Videos

Video de la interfaz grafica

https://github.com/Ggio0/Ros_lab4/assets/82681128/ac056370-14c5-41d7-b194-ade862aa8eeb









