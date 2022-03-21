import RPi.GPIO as GPIO
import time
import MOVIMIENTOS
from VARIABLES import *


###################################################################
#####################FUNCIóN AMBOS#################################
###################################################################
def BOTH(velR,numR,velL,numL):
    if (numR>0):
        GPIO.output(IN1,GPIO.HIGH)
        GPIO.output(IN2,GPIO.LOW)
    else:
        numR=-numR
        GPIO.output(IN1,GPIO.LOW)
        GPIO.output(IN2,GPIO.HIGH)
    if (numL>0):
         GPIO.output(IN4,GPIO.HIGH)
         GPIO.output(IN3,GPIO.LOW)
    else:
        numL=-numL
        GPIO.output(IN4,GPIO.LOW)
        GPIO.output(IN3,GPIO.HIGH)
    contadorR=0
    contadorL=0
    while ((contadorR<numR)or(contadorL<numL)):
        if (contadorR<numR):
            PWMA.start(velR)
        else:
            GPIO.output(IN1,GPIO.LOW)
            GPIO.output(IN2,GPIO.LOW)
        if (contadorL<numL):
            PWMB.start(velL)
        else:
            GPIO.output(IN3,GPIO.LOW)
            GPIO.output(IN4,GPIO.LOW)
        if (GPIO.input(DataMotorR) == 1) and (GPIO.input(DataMotorR) == 0):
            contadorR += 1
            print ('contador derecha = ',contadorR)
        if (GPIO.input(DataMotorL) == 1) and (GPIO.input(DataMotorL) == 0):
            contadorL += 1
            print ('contador izquierda = ',contadorL)
    MOVIMIENTOS.STOP()
#############################################
###########################FUNCION PASO DERECHA#######################
def RIGHT(vel,num):
    if (num>0):
        GPIO.output(IN1,GPIO.HIGH)
        GPIO.output(IN2,GPIO.LOW)
    else:
        num=-num
        GPIO.output(IN1,GPIO.LOW)
        GPIO.output(IN2,GPIO.HIGH)
    contador=0
    while (contador<num):
        PWMA.start(vel)
        if (GPIO.input(DataMotorR) == 1) and (GPIO.input(DataMotorR) == 0):
            contador += 1
            print ('contador derecha = ',contador)
    MOVIMIENTOS.STOP()
#########################FUNCION PASO IZQUIERDA#############################   
def LEFT(vel,num):
    if (num>0):
        GPIO.output(IN4,GPIO.HIGH)
        GPIO.output(IN3,GPIO.LOW)
    else:
        num=-num
        GPIO.output(IN4,GPIO.LOW)
        GPIO.output(IN3,GPIO.HIGH)
    contador=0
    while (contador<num):
        PWMB.start(vel)
        if (GPIO.input(DataMotorL) == 1) and (GPIO.input(DataMotorL) == 0):
            contador += 1
            print ('contador izquierda = ',contador)
    MOVIMIENTOS.STOP()
