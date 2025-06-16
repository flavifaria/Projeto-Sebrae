import random
import os
import textwrap
import sys
import time
import colorama
from colorama import init, Fore, Back, deinit

def clear():
    os.system("clear")
demo = '''
    ▄▄▄▄▄▄  ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄      
    █      ██       █  █▄█  █       █    
    █  ▄    █    ▄▄▄█       █   ▄   █    
    █ █ █   █   █▄▄▄█       █  █ █  █    
    █ █▄█   █    ▄▄▄█       █  █▄█  █    
    █       █   █▄▄▄█ ██▄██ █       █    
    █▄▄▄▄▄▄██▄▄▄▄▄▄▄█▄█   █▄█▄▄▄▄▄▄▄█    
        ========================        
        |}      --JOGAR--     {|        
        |}      --OPIS--      {|        
        |}      --SAIR--      {|        
        ========================        
'''
farol = """=================================================================================================
|} . _  .    .__  .  .  __,--'                  {||}'FAROL'                                    {|
|}  (_)    ' /__\ __,--'                        {||}DESCRIÇÃO:Ilumina para os barcor da costa. {|
|}'  .  ' . '| o|'                              {||}Você está em seu farol antigo e enferrujado{|
|}          [IIII]`--.__                        {||}alguns barcos e navios está passando por   {|
|}           |  |       `--.__                  {||}perto da costa do seu farol todoas os dias {|
|}           | :|             `--.__            {||}isso acontece e você está se cansando disso{|
|}           |  |                   `--.__      {||}OPÇÕES: Fumar(-~)  Cochilar(zzz..)         {|
|}._,,.-,.__.'__`.___.,.,.-..,_.,.,.,-._..`--.. {||}        Olhar(o_o) Ler([|])                {|
================================================================================================="""
def carregar():
    clear()
    p1 = '      ===============0%       '
    p2 = '      ***============25%      '
    p3 = '      ******=========50%      '
    p4 = '      *********======70%      '
    p5 = '      ************===85%      '
    p6 = '      ***************100%     '
    print(Fore.LIGHTGREEN_EX+Back.BLACK+p1)
    time.sleep(2)
    clear()
    print(Fore.LIGHTGREEN_EX+Back.BLACK+p2)
    time.sleep(2)
    clear()
    print(Fore.LIGHTGREEN_EX+Back.BLACK+p3)
    time.sleep(2)
    clear()
    print(Fore.LIGHTGREEN_EX+Back.BLACK+p4)
    time.sleep(2)
    clear()
    print(Fore.LIGHTGREEN_EX+Back.BLACK+p5)
    time.sleep(2)
    clear()
    print(Fore.LIGHTGREEN_EX+Back.BLACK+p6)

def play():
    clear()
    print(Fore.LIGHTMAGENTA_EX+ Back.BLACK + farol)
    print("Qual seu nome?")
    input("=>")
def menu():
    carregar()
    clear()
    print(Fore.LIGHTMAGENTA_EX+ Back.BLACK + demo)
    ops = input("=>")
    if ops == "jogar":
        play()
    elif ops == "opis":
        print("HELP")
    elif ops == "sair":
        exit()
    while ops.lower() not in [ "jogar", "opis", "sair"]:
        clear()
        print(Fore.LIGHTMAGENTA_EX+ Back.BLACK + demo)
        ops = input("=>")
        if ops == "jogar":
            clear()
            play()
        elif ops == "opis":
            print("HELP")
        elif ops == "sair":
            clear()
            exit()
           
menu()