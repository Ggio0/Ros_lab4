import math
import os
import time
import cv2

import numpy
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from dynamixel_workbench_msgs.srv import DynamixelCommand

import tkinter as tk

# Nombres de los integrantes del grupo
integrantes = ["Giovanny", "Nicolas"]

'''Definicion de variables Variables'''
#torque de cada junta en bits
Torques=[500,400,400,400,400]

#Definicion de posicion de home y pose
angd1 = [0, 0, 0, 0, 0]
angd2 = [25, 25, 20, -20, 0]
angd3 = [-35, 35, -30, 30, 0]
angd4 = [85, -20, 55, 25, 0]
angd5 = [80, -35, 55, -45, 0]
# Convierte los ángulos de grados a radianes
ang1 = [math.radians(a) for a in angd1]
ang2 = [math.radians(a) for a in angd2]
ang3 = [math.radians(a) for a in angd3]
ang4 = [math.radians(a) for a in angd4]
ang5 = [math.radians(a) for a in angd5]

angpres=ang1

'''Servicios'''
 
#Publisher para los motores
def joint_publisher(q):
    pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)

    #while not rospy.is_shutdown():
    state = JointTrajectory()
    state.header.stamp = rospy.Time.now()
    state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
    point = JointTrajectoryPoint()
    point.positions = [q[0], q[1],q[2],q[3],q[4]]    
    point.time_from_start = rospy.Duration(0.5)
    state.points.append(point)
    pub.publish(state)
    print('published command')
    rospy.sleep(1)

#Subscriber para la posicion real
def callback(data):
    rospy.loginfo(data.position)
    global angpres
    angpres=data.position

    if data.position[4]>-2:
        print('gripper abierto')
    else:
        print('gripper cerrado')
    
def listener():
    #rospy.init_node('joint_listener', anonymous=True)
    rospy.Subscriber("/dynamixel_workbench/joint_states", JointState, callback)
    #rospy.spin()


#Dynamixel service
def jointCommand(command, id_num, addr_name, value, time):
    #rospy.init_node('joint_node', anonymous=False)
    rospy.wait_for_service('dynamixel_workbench/dynamixel_command')
    try:        
        dynamixel_command = rospy.ServiceProxy(
            '/dynamixel_workbench/dynamixel_command', DynamixelCommand)
        result = dynamixel_command(command,id_num,addr_name,value)
        rospy.sleep(time)
        return result.comm_result
    except rospy.ServiceException as exc:
        print(str(exc))

#Ajustar torque
def ajus_torque(T):
    #Definir los límites de torque de los motores.
    for i in range(5):    
        jointCommand('', (i+1), 'Torque_Limit', T[i], 0)    

#Movimiento de junta por junta
def movTotalPartes(Goal,presnt):
    q=numpy.asarray(presnt)
    for i in range(5):
        q[i]=Goal[i]
        print('Moviento eslabon: '+str(i+1))
        joint_publisher(q)
        rospy.sleep(3)
    print('Finalizada la rutina.')

'''Definicion de las funciones para mover el robot '''

def gohome():
    print('Has elegido llevar a home')
    mostrar_imagen(imagen_poshome, opcion_elegida.get())
    opcion_elegida.set(ang1)
    movTotalPartes(ang1,angpres)

def accion1():
    print('Has elegido la pose 1')
    mostrar_imagen(imagen_pose1, opcion_elegida.get())
    opcion_elegida.set(ang2)
    movTotalPartes(ang2,angpres)


def accion2():
    print('Has elegido la pose 2')
    mostrar_imagen(imagen_pose2, opcion_elegida.get())
    opcion_elegida.set(ang3)
    movTotalPartes(ang3,angpres)

def accion3():
    print('Has elegido la pose 3')
    mostrar_imagen(imagen_pose3, opcion_elegida.get())
    opcion_elegida.set(ang4)
    movTotalPartes(ang4,angpres)

def accion4():
    print('Has elegido la pose 4')
    mostrar_imagen(imagen_pose4, opcion_elegida.get())
    opcion_elegida.set(ang5)
    movTotalPartes(ang5,angpres)

def leer_sensor():
    print('Has elegido leer')
    opcion_elegida.set(angpres)
    listener()

# Función para mostrar imágenes
def mostrar_imagen(imagen, opcion_anterior):
    imagen_label_pasada.config(image=imagen_label_actual.cget("image"))
    imagen_label_actual.config(image=imagen)
    opcion_anterior_label.config(text="Anterior: " + opcion_anterior)


'''Cracion de la interfaz grafica'''
# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Selección de Opciones")

# Etiqueta para mostrar los nombres de los integrantes
nombres_label = tk.Label(ventana, text="Integrantes del grupo: " + ", ".join(integrantes))
nombres_label.pack()

# Cargar imágenes para cada opción

package_dir = os.path.dirname(os.path.abspath(__file__))
imagen_pathhom = os.path.join(package_dir, "figuras/poshome.png")
imagen_pathpose1 = os.path.join(package_dir, "figuras/pose1.png")
imagen_pathpose2 = os.path.join(package_dir, "figuras/pose2.png")
imagen_pathpose3 = os.path.join(package_dir, "figuras/pose3.png")
imagen_pathpose4 = os.path.join(package_dir, "figuras/pose4.png")
imagen_pathdef = os.path.join(package_dir, "figuras/def.png")


# Crear una etiqueta para mostrar la imagen
# Crear una etiqueta grande para mostrar la imagen
imagen_def = tk.PhotoImage(file=imagen_pathdef)
imagen_poshome = tk.PhotoImage(file=imagen_pathhom)
imagen_pose1 = tk.PhotoImage(file=imagen_pathpose1)
imagen_pose2 = tk.PhotoImage(file=imagen_pathpose2)
imagen_pose3 = tk.PhotoImage(file=imagen_pathpose3)
imagen_pose4 = tk.PhotoImage(file=imagen_pathpose4)


imagen_label = tk.Label(ventana, image=imagen_def)
#imagen_label.pack()


# Crear un Frame para contener las imágenes
imagen_frame = tk.Frame(ventana)
imagen_frame.pack()

# Crear etiquetas para mostrar las imágenes actual y pasada
imagen_label_actual = tk.Label(imagen_frame, image=imagen_def)
imagen_label_pasada = tk.Label(imagen_frame, image=imagen_def)
imagen_label_actual.grid(row=0, column=1)
imagen_label_pasada.grid(row=0, column=0)


# Etiqueta para mostrar la opción anterior
opcion_anterior_label = tk.Label(ventana, text="Anterior:")
opcion_anterior_label.pack() 

# Crear una etiqueta para mostrar la opción elegida abajo a la derecha
opcion_elegida = tk.StringVar()
opcion_elegida_label = tk.Label(ventana, textvariable=opcion_elegida)
opcion_elegida_label.pack()

# Crear botones para las 5 opciones
boton1 = tk.Button(ventana, text="pose 1", command=accion1)
boton2 = tk.Button(ventana, text="pose 2", command=accion2)
boton3 = tk.Button(ventana, text="pose 3", command=accion3)
boton4 = tk.Button(ventana, text="pose 4", command=accion4)
boton5 = tk.Button(ventana, text="Home", command=gohome)



# Ubicar los botones en la parte inferior izquierda
boton4.pack(side="right")
boton3.pack(side="right")
boton2.pack(side="right")
boton1.pack(side="right")
boton5.pack(side="left")


'''Funcion principal'''


def run():
    rospy.init_node('joint_listener', anonymous=True)
    listener()
    ajus_torque(Torques)
    #menu_principal()
    
    ventana.mainloop()


if __name__ == '__main__':
    run()