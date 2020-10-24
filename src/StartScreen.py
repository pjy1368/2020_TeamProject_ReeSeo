import ctypes
import os
import sys

def gotoxy(x,y):
    return ctypes.windll.kernel32.SetConsoleCursorPosition(ctypes.windll.kernel32.GetStdHandle(-11),(((y&0xFFFF)<<0x10)|(x&0xFFFF)))

def startScreen():
    os.system('cls')
    gotoxy(30,5)
    print("<Exercise Objective Setting and Achievement Program>")
    gotoxy(70,16)
    print("201711370  Kang\tYunseok")
    gotoxy(70,17)
    print("201911156  Kim\tByeolchan")
    gotoxy(70,18)
    print("201911175  Park\tJinyoung")
    gotoxy(70,19)
    print("201911192  Yang\tSukjoon")
    gotoxy(70,20)
    print("201910514  Jo\tJaehun")
    input()
    os.system('cls')
    
