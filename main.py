import random
import os
import json
import sys
import time
import colorama
from colorama import init, Fore, Back
init(autoreset=True)
SAVE_FILE = "savegame.json"
def clear():
    os.system("cls")
def carregar():
    clear()
    barra = Fore.LIGHTGREEN_EX + Back.BLACK + "#"
    bar = Fore.LIGHTRED_EX + Back.BLACK + "="
    for i in range(0, 21, 5):
        print(barra * i + bar * (20 - i) + f"{i*5}%")
        time.sleep(1)
        clear()

def salvar_jogo(dados):
    with open(SAVE_FILE, "w") as arquivo:
        json.dump(dados, arquivo)
    print("Jogo salvo com sucesso!")

def carregar_jogo():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as arquivo:
            dados = json.load(arquivo)
        print("Save carregado com sucesso!")
        time.sleep(1)
        return dados
    else:
        print("Nenhum save encontrado.")
        time.sleep(2)
        return None

def novo_jogo():
    nome = input("Digite o nome do seu personagem: ")
    personagem = {
        "nome": nome,
        "fisico": 100,
        "sanidade": 100
    }
    salvar_jogo(personagem)
    return personagem

def pescaodor():
    clear()
    barco = Fore.BLUE + '''    ==================================================
    |}                   /|___                      {|
    |}                 ///|   ))                    {|
    |}               /////|   )))                   {|
    |}             ///////|    )))                  {|
    |}           /////////|     )))                 {|
    |}         ///////////|     ))))                {|
    |}       /////////////|     )))                 {|
    |}      //////////////|    )))                  {|
    |}    ////////////////|___)))                   {|
    |}      ______________|________                 {|
    |}      \                    /                  {|
    |}    ~~~~~~~~~~~~~~~~~~~~~~~~~~                {|
    =================================================='''
    print(barco)
    pescaodr = """
    Você decide entrar dentro do barco do velho pescador
    While o senhor que fuma cachinbo e gosta de pescar
    ele pesca de tudo peixes, moluscos e tubaroes
    While: *está dormindo em sua rede do seu barco*
    While: oque você quer garoto? se quiser pescar fale logo 
    quero dormir hoje só acordo com um pescador bom 
    você quer pescar com o velho While?
"""
    for caractere in pescaodr:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(0)
    print(Fore.GREEN+"  SIM", Fore.RED+"NÃO")
    print(Fore.RED + "=#" * 25)
    ops = input("=>")
    if ops == "s":
        clear()
        while True:
            input(Fore.LIGHTMAGENTA_EX + "Pressione Enter para lançar sua linha...")
            print(Fore.LIGHTRED_EX +"Lançando a linha...")
            print("=#" * 25)
            chance_de_peixe = random.randint(1, 100)
            if chance_de_peixe <= 75:
                tipo_de_peixe = random.choice(["Tilápia", "Robalo", "Carpa", "Salmão", "Dourado"])
                tamanho_do_peixe = round(random.uniform(1.0, 10.0), 2)
                print(f"While:Boa rapaz pescou um(a) {tipo_de_peixe} de {tamanho_do_peixe} kg!")
                print("While: foi bom para um iniciante")
                clear()
                print(barco)
            elif chance_de_peixe <=25:
                tipo_de_molusco = random.choice(["Lagosta", "Carangueijo", "Camaram"])
                tamanho_do_molusco = round(random.uniform(0.1, 2.5), 2)
                print(f"While:Boa rapaz pescou um(a) {tipo_de_molusco} de {tamanho_do_molusco} kg!")
                print("While: foi bom para um iniciante")
                clear()
                print(barco)
            else:
                print("Sua linha voltou vazia. Mais sorte na próxima vez!")
                input()
                clear()

def praia():
    clear()
    praia_ascii = Fore.YELLOW +"""           |
         \ _ /
       -= (_) =-
         /   \         _\/_
           |           //o\  _\/_
    _____ _ __ __ ____ _ | __/o\\ _
=- =-=-_-__=_-= _=_=-=_,-'|"'""|-,_
=- =- _=-=- -_=-=_,-";;..'.'.'.'|
=-   =- =- -=.--"''''''''''''''               """
    print(praia_ascii)
    descrição ='''Local:Praia
DESCRIÇÃO:andando na praia você vê as palmeiras e o
sol e sente a areia quente nos seus pés e escuta o
som forte do oceano azul e uma brisa boa.
'''
    for caractere in descrição:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(0.05)
    print(Fore.BLUE+ "#=" * 25)
    print("escolha uma das açoes a baixo")
    print(Fore.BLUE+ "pescador", Fore.GREEN + "professora")
    ops = input("conversar com:").lower()
    while ops not in ["pescador", "professora"]:
        clear()
        print(praia_ascii)
        print(descrição)
        print(Fore.BLUE+ "#=" * 25)
        print("escolha uma das açoes a baixo")
        print(Fore.BLUE+ "pescador", Fore.GREEN + "professora")
        ops = input("conversar com:").lower()
    if ops == "pescador":
        pescaodor()
    elif ops == "professora":
        pass

    

demo = '''      ▄▄▄▄▄▄  ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄    
    █      ██       █  █▄█  █       █    
    █  ▄    █    ▄▄▄█       █   ▄   █    
    █ █ █   █   █▄▄▄█       █  █ █  █    
    █ █▄█   █    ▄▄▄█       █  █▄█  █    
    █       █   █▄▄▄█ ██▄██ █       █    
    █▄▄▄▄▄▄██▄▄▄▄▄▄▄█▄█   █▄█▄▄▄▄▄▄▄█    
        ========================         
        |}      --JOGAR--     {|         
        |}      --LOAD--      {|         
        |}      --SAIR--      {|         
        ========================         '''


def play(personagem,):
    clear()
    farol= Fore.RED + """==================================================
|} . _  .    .__  .  .  __,--'                  {|
|}  (_)    ' /__\\ __,--'                        {|
|}'  .  ' . '| o|'                              {|
|}          [IIII]`--.__                        {|
|}           |  |       `--.__                  {| 
|}           | :|             `--.__            {|
|}           |  |                   `--.__      {|
|}.,,.-,.__.'__.___.,.,.-..,.,.,.,-._..--..     {| 
=================================================="""
    texto ="""Local: Farol
DESCRIÇÃO: Você está na parte de fora do seu 
farol e está um belo dia como sempre na praia 
pelicano você está vendo algumas coisas na praia
"""
    print(farol)
    for caractere in texto:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(0.05)
    print(Fore.CYAN +'=#' * 25)
    print("Digite alguma ação")
    print(Fore.YELLOW + "Ir a praia", Fore.BLUE + "entrar no farol")
    print(Fore.LIGHTMAGENTA_EX + "MENU      ", Fore.RED + "Sair")
    ops = input(Fore.GREEN + "=>")
    if ops == "praia":
        praia()
    elif ops == "oceano":
        pass
    elif ops == "menu":
        pass
    elif ops == "sair":
        clear()
        exit()


def menu():
    clear()
    print(Fore.LIGHTMAGENTA_EX + demo)
    ops = input("=>").lower()
    while ops not in ["jogar", "load", "sair"]:
        clear()
        print(Fore.LIGHTMAGENTA_EX + demo)
        ops = input("=>").lower()
    if ops == "jogar":
        personagem = novo_jogo()
        play(personagem)
    elif ops == "load":
        personagem = carregar_jogo()
        if personagem:
            play(personagem)
        else:
            menu()
    elif ops == "sair":
        clear()
        sys.exit()
menu()
