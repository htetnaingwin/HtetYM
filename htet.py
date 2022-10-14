import os
import sys
import time
import cookielib

wd = "\033[90;1m" # dark
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan

def runntxt(s):
        for noobs in s + '\n':
                sys.stdout.write(noobs)
                sys.stdout.flush()
                time.sleep(30. / 2100)

def runtxt(s):
        for noobs in s + '\n':
                sys.stdout.write(noobs)
                sys.stdout.flush()
                time.sleep(120. / 2000)
                
def pil():
                print GG+" "
                g = str(raw_input("[?] fb hack yan thint acc ayin win ya pr mal..\033[93;1m[y/n]: "))
                if g == 'y' or g == 'Y':
                    os.system('python2 brute.py')
                elif g == 'n' or g == 'N':
                    print R+"Keluar dari program..."
                    sys.exit()
                else:
                    print RR+"Pilih yang bener cuk..."
                    pil()


def banner():
    os.system('clear')
    runntxt(GL+"........................................................")
    runntxt(YY+"########################################################")
    runntxt(YY+"#\033[31m......................................................\033[33;1m#")  
    runntxt(YY+"#\033[31m....................\033[32mHtet Naing Win\033[31m....................\033[33;1m#")  
    runntxt(YY+"#\033[31m..............\033[32mMy Fb Acc Htet Naing Win\033[31m..................\033[33;1m#")
    runntxt(YY+"#\033[31m......................................................\033[33;1m#")  
    runntxt(YY+"########################################################")
    runntxt(GL+"........................................................\033[0;1m")
    runtxt(W+"                      min ga lar pr ")
    pil()
    
    
banner()

