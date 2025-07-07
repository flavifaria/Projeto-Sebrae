import sys
import os
import time
import colorama
from colorama import init, Fore, Back
import random
init(autoreset=True)

def clear():
    os.system("cls")

class player:
    def __init__(self, nome):
        self.nome = nome
        self.max_hp = 100 
        self.hp = self.max_hp  
        self.fe = 10
        self.atk = 10
        self.iniventario = []
        self.gold = 0
        self.padre_encontrado = False
        self.crucifixo_coletado = False
        self.espada_coletada = False
        self.faith_uses = 5

    def status(self):
        print('====================')
        print(Fore.MAGENTA + f'Nome:{self.nome}')
        print(Fore.GREEN + f'Fisico:{self.hp}/{self.max_hp}')
        print(Fore.BLUE + f'Fé:{self.fe} (Usos restantes: {self.faith_uses})')
        print(Fore.RED + f'Violencia:{self.atk}')
        print(Fore.WHITE + f'Inventario: {",\n ".join(self.iniventario)}')
        print(Fore.YELLOW + f'Almas:{self.gold}')
        print('====================')

    def menu_pl(self):
        print('====================')
        print(Fore.MAGENTA + f'Nome:{self.nome}')
        print(Fore.GREEN + f'Fisico:{self.hp}/{self.max_hp}') 
        print(Fore.BLUE + f'Fé:{self.fe} (Usos restantes: {self.faith_uses})')
        print(Fore.RED + f'Violencia:{self.atk}')
        print('====================')

class Enemy:
    def __init__(self, name, hp, atk, ascii_art=''):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.ascii = ascii_art

    def status(self):
        print(f"{self.ascii}")
        print(Fore.YELLOW+f"--- {self.name} Status ---")
        print(Fore.RED+f"HP: {self.hp}")
        print(Fore.BLUE+f"ATK: {self.atk}")
        print("--------------------")

def ll():
    print("=#"*24)
    print(f"{Fore.MAGENTA}          Capitulo 2 LUAXURIA ")
    print("=#"*24)

def luxuria(player_character):
    ll()
    platao = f'''{Fore.BLUE}
Platão: Agora estamos no real inferno onde nada mais
ao não ser dor e sofrimento existe estamos no segundo
ciclo luxiria onde todos aqueles se prefiriram o prazer
carnal sofrem eternamente'''
    voce = f'''{Fore.RED}{player_character.nome}
: Meu Deus essas malditas almas penadas estão sofrendo
dessa forma qual é o castigo delas Platão?
'''
    castigo = '''
Platão: O castigo dassas almas é sofrer eternamente
em um grande furacão onde elas estão amuntuadas
porem nunca conseguem fazer oque mais fizeram e
gostavam em vida ou seja uma tentação eterna
esse é o sofrimento deles.
'''
    player_character.status()
    demonio = '''
         .m.                                   ,_
         ' ;M;                                ,;m `
           ;M;.           ,      ,           ;SMM;
          ;;Mm;         ,;  ____  ;,         ;SMM;
         ;;;MM;        ; (.MMMMMM.) ;       ,SSMM;;
       ,;;;mMp'        l  ';mmmm;/  j       SSSMM;;
     .;;;;;MM;         .\,.mmSSSm,,/,      ,SSSMM;;;
    ;;;;;;mMM;        .;MMmSSSSSSSmMm;     ;MSSMM;;;;
   ;;;;;;mMSM;     ,_ ;MMmS;;;;;;mmmM;  -,;MMMMMMm;;;;
  ;;;;;;;MMSMM;     \"*;M;( ( '') );m;*"/ ;MMMMMM;;;;;,
 .;;;;;;mMMSMM;      \(@;! _     _ !;@)/ ;MMMMMMMM;;;;;,
 ;;;;;;;MMSSSM;       ;,;.*o*> <*o*.;m; ;MMMMMMMMM;;;;;;,
.;;;;;;;MMSSSMM;     ;Mm;           ;M;,MMMMMMMMMMm;;;;;;.
;;;;;;;mmMSSSMMMM,   ;Mm;,   '-    ,;M;MMMMMMMSMMMMm;;;;;;;
;;;;;;;MMMSSSMMMMMMMm;Mm;;,  ___  ,;SmM;MMMMMMSSMMMM;;;;;;;;
;;'";;;MMMSSSSMMMMMM;MMmS;;,  "  ,;SmMM;MMMMMMSSMMMM;;;;;;;;.
!   ;;;MMMSSSSSMMMMM;MMMmSS;;._.;;SSmMM;MMMMMMSSMMMM;;;;;;;;;
    ;;;;*MSSSSSSMMMP;Mm*"'q;'   `;p*"*M;MMMMMSSSSMMM;;;;;;;;;
    ';;;  ;SS*SSM*M;M;'     `-.        ;;MMMMSSSSSMM;;;;;;;;;,
     ;;;. ;P  `q; qMM.                 ';MMMMSSSSSMp' ';;;;;;;
     ;;;; ',    ; .mm!     \.   `.   /  ;MMM' `qSS'    ';;;;;;
     ';;;       ' mmS';     ;     ,  `. ;'M'   `S       ';;;;;
      `;;.        mS;;`;    ;     ;    ;M,!     '  luk   ';;;;
       ';;       .mS;;, ;   '. o  ;   oMM;                ;;;;
        ';;      MMmS;; `,   ;._.' -_.'MM;                 ;;;
         `;;     MMmS;;; ;   ;      ;  MM;                 ;;;
           `'.   'MMmS;; `;) ',    .' ,M;'                 ;;;
              \    '' ''; ;   ;    ;  ;'                   ;;
               ;        ; `,  ;    ;  ;                   ;;
                        |. ;  ; (. ;  ;      _.-.         ;;
           .-----..__  /   ;  ;   ;' ;\  _.-" .- `.      ;;
         ;' ___      `*;   `; ';  ;  ; ;'  .-'    :      ;
         ;     """*-.   `.  ;  ;  ;  ; ' ,'      /       |
         ',          `-_    (.--',`--'..'      .'        ',
           `-_          `*-._'.\\\;||\\)     ,'
              `"*-._        "*`-ll_ll'l    ,'
                 ,==;*-._           "-.  .'
              _-'    "*-=`*;-._        ;'
            ."            ;'  ;"*-.    `
            ;   ____      ;//'     "-   `,
            `+   .-/                 ".\\;
              `*" /                    "'

'''

def minos(player_character):
    clear()
    tt()
    MM = f'''{Fore.MAGENTA}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⣴⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡟⣴⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣬⣿⣯⡇⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⢿⣷⣟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⣀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡛⠛⠛⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣿⠼⠳⢯⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣶⢞⣩⣍⠀⠀⠀⢠⠠⠍⢡⣍⢻⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡷⣿⣧⢈⠉⠃⢀⣀⠀⠀⣠⣼⡇⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠹⢿⠿⠷⠓⠈⠛⠷⠻⣿⢟⠡⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡟⠘⣧⣶⠄⠂⠐⠂⠄⠐⢶⠾⢙⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣯⣿⡁⠀⢽⡓⢰⣾⡄⢴⡆⠀⢈⡀⢀⣿⣛⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠾⣿⡉⠛⠀⢸⣿⣦⣴⡶⣦⠤⣾⣿⡁⠺⢿⣿⠿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣮⠧⠀⠀⣿⣿⠅⠀⣂⠽⠃⠙⢿⣇⠀⢾⣷⣾⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⠀⠀⢸⣷⣈⡄⠘⣃⡃⢀⡠⣤⢻⡄⠀⣿⣿⡛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡿⠇⠀⣿⣿⣇⡀⢴⣿⡷⠀⠙⣿⣿⣇⠐⣷⣿⣥⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⡇⠀⠀⡿⣽⣄⢡⣄⠻⠏⣴⢈⣽⣿⡏⠀⠸⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡄⠀⠀⡍⣽⠋⢆⣿⠂⢻⣿⠈⠿⣏⡏⠀⣀⣭⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠀⠀⡏⡽⠀⢾⡟⠀⠸⡿⡔⡈⣿⡇⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠃⢰⠀⠸⠀⠈⠀⡅⠀⡘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢃⡁⠈⠂⠀⠀⠀⡀⠹⡄⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'''
    platão = '''Platão: Estamos no jugamento das almas do inferno
o rei Minus as julga e as joga nos seus definitivos
ciclos uns para baixo outros para o final temos que
pedir para ele nós deixar descer'''
    minos = f'''Minus: Sinto cheiro de mortal isso está errado quem é
o verme que quer passar sendo um mortal vivo no inferno
diga logo mortal'''
    voce= f'''{player_character.nome}: Eu sou aquele que procura o final desse maldito inferno
seu mostro horrendo e maligno irei matalo se não me deixar
avança em minha missão'''
    minos2 = '''Minus: *Uma gargalhada alta e estrondosa é escutada por todos*
ver que se diz homem que tu pensas que é para falar de mim
o rei Minus o juiz das almas pecadoras'''
    minos3 = '''Minos: seu verme como você me derrotol te entrego uma 
embrança para você usar em sua jornada
'''
    escudo = f'''{Fore.LIGHTYELLOW_EX}  |-`-._/\_.-`-|
  |     ||     |
  | ___o()o___ |
  | __((<>))__ |
   \   o\/o   /
    \   ||   /
     \  ||  /
      '.||.'
        ``
'''
    lines = MM.split('\n')
    print(platão)
    print("=#"*24)
    input()
    clear()
    tt()
    print(minos)
    print(voce)
    print("=#"*24)
    input()
    clear()
    tt()
    print(minos2)
    print("=#"*24)
    input("Pressione Enter para iniciar a batalha...")
    minos_enemy = Enemy('Minus', 100, 25, MM)
    combat(player_character, minos_enemy)
    if player_character.hp > 0:
        player_character.gold += 100
        clear()
        print(MM)
        print(minos3)
        print(escudo)
        print("Você recebel um escudo de Minus é um lindo escudo")
        player_character.hp = player_character.max_hp
        player_character.iniventario.append(f"{Fore.YELLOW}Escudo")
        input()
        clear()
        for i in range(len(lines), -5, -5):
            clear()
            for j in range(i):
                print(lines[j])
            time.sleep(0.9)
        print("O corpo de Minos foi devorado pelo inferno.")
        luxuria(player_character)
    else:
        print(f"{Fore.RED}Você foi morto por Minus! Seu corpo é dilacerado.")
        input("Pressione Enter para sair do jogo...")
        sys.exit()

def tt():
    print("=#"*24)
    print(Fore.LIGHTRED_EX+"          Capitulo 1 LIMBO")
    print("=#"*24)

def limbo_p(player_character):
    def mulherops(player_character):
        text3 = f'''{Fore.YELLOW}Desidindo ir para o proximo Ciclo infernal tu sente uma mulher
te puxando e falando altos com os dizires'''
        mulher = f'''{Fore.GREEN}Mulher: Senhor me ajude me tire daqui por favor me mate
não aguento mais eu quero que você me jugue por favor livre me
desse estranho sentimento de culpa'''
        clear()
        tt()
        print('=#'*24)
        print(text3)
        print(mulher)
        print('=#'*24)
        print("O que você faz?")
        print(Fore.BLUE + "1. Orar por ela")
        print(Fore.RED + "2. Matar ela")
        escolha_padre = input("=>").lower()
        if escolha_padre == '1' or escolha_padre == 'orar':
            clear()
            tt()
            print("=#"*24)
            mulherora = f'''{Fore.YELLOW}Você coloca o crucifixo sobe a cabeça da mulher e começa a resar
a mulher começa a subir para o cêu pios ela finalmente te um
contato com Cristo e foi para os braços de Deus '''
            print(mulherora)
            player_character.fe += 5
            print(f"{Fore.BLUE}Sua Fé almentou: {player_character.fe}")
            print("=#"*24)
            input("Pressione Enter para continuar...")
            minos(player_character)
        elif escolha_padre == '2' or escolha_padre == 'matar':
            clear()
            tt()
            print("=#"*24)
            mulhermata = f'''{Fore.YELLOW}Você estrangula a mulher e a mata você relembra da sua matança
de inocentes a alma da mulher é esvaida e você suspira e seus
olha não tem nada alem do horror da guerra'''
            print(mulhermata)
            player_character.atk += 5
            print(f"{Fore.RED}Sua Violencia almentou: {player_character.atk}")
            print("=#"*24)
            input("Pressione Enter para continuar...")
            minos(player_character)
        else:
            clear()
            tt()
            print('você não interfere na alma da Mulher a deixando vagar por ali')
            input()
            minos(player_character)

    def op(player_character):
        ops = f'''{Fore.RED}1. Andar {Fore.BLUE}2. Conversar
{Fore.GREEN}3. Menu {Fore.MAGENTA}4. Descer'''
        clear()
        tt()
        print(text2)
        print('=#'*24)
        print(ops)
        print('=#'*24)
        escolha = input("=>")
        if escolha == '1' or escolha == 'andar':
            clear()
            tt()
            print('=#'*24)
            andar = f'''{Fore.YELLOW}Você descide andar pelo limbo vendo todos os antigos folosofos
como Aristóteles, Sócrates, Epicuro, Sêneca, Virgilho dentre
muito outros filosofos conhecidos além de imperadores e
pessoas comundas da epoca antes de Cristo '''
            print(andar)
            print('=#'*24)
            lembanças = f'''{Fore.YELLOW}Andando tu vê a sombra de Saladino e se lembra da guerra
lembra das sua cruzada em Jerusalem e lembra de cada alma
que você matol cade musumano e inocente mortor então
uma culpa toma seu coração'''
            lembanças2 = f'''{Fore.BLUE}Platão: Não pare continue sua missâo mal comessou e já
está parado vamos rapaz temos que continuar a andar'''
            input()
            print("=#"*24)
            print(lembanças)
            print("=#"*24)
            print(lembanças2)
            print("=#"*24)
            input()
            op(player_character)
        elif escolha == '2' or escolha == 'Conversar':
            conversa = f'''{Fore.BLUE}Platão: Aqui a luz não bate apenas a filosofia de Lucifer por
não conheserem a Cristo eles só tem o pensamento demoniaco
ou seja sem conciencia do pecado cristão'''
            conversa2 = f'''{Fore.BLUE}Platão: Então desça para o proximo ciclo rapaz para você cumprir sua missâo'''
            clear()
            tt()
            print("=#"*24)
            print(conversa)
            print("=#"*24)
            print(conversa2)
            print("=#"*24)
            input()
            op(player_character)
        elif escolha == '3' or escolha == 'menu':
            tt()
            player_character.status()
            input()
            op(player_character)
        elif escolha == '4' or escolha == 'descer':
            mulherops(player_character)

        else:
            clear()
            op(player_character)

    text = f'''{Fore.BLUE}Platão: Estamos na primeira parte do inferno o nome é Limbo
onde os Pagoes virtuosos e pessoas que não conheceram a Cristo
eles não sofrem mas tambem nunca veram a Deus essas almas
são triste e decaidas aqui fica a maioria dos grandes pensadores
ou até bebês sem batismo'''
    text2 = f'''{Fore.RED}Vendo essa cena você se intristese por ter pessoas que nunca
conheseram a Deus ou a Cristo assim você suspira e começa a andar
indo para o segundo ciclo na porta aberta enquanto você anda uma
mulher te agarra na perna e diz te emplorando '''
    clear()
    tt()
    print('=#'*24)
    print(text)
    print('=#'*24)
    input('Precione Enter')
    clear()
    print('=#'*24)
    print(text2)
    print('=#'*24)
    op(player_character)

def limbo(player_character):
    clear()
    tt()
    input("Precione enter para continuar")
    text = f'''{Fore.YELLOW}Adentrando o inferno você persebe um homen ao seu lado
{Fore.YELLOW}parece ser um homem sabio você fala de forma duvidosa
{Fore.RED}{player_character.nome}: Quem é você? senhor por que me olhas tanto sabio?'''
    text1 = f'''{Fore.BLUE}Sabio: Eu sou um velho filosofo grego vocês me conhecem como platão
{Fore.BLUE}Platão: {player_character.nome} eu irei te guiar em direção ao final do inferno
{Fore.BLUE}você deve ir para frente pois uma vez no inferno você só pode sair pelo ultimo circlo'''
    clear()
    tt()
    print(text)
    print("precione enter"),input()
    print(text1)
    print("precione enter"),input()
    print("=#"*24)
    print(f'{Fore.MAGENTA}Platão virou seu guia no inferno vocês desseram todo inferno')
    print("=#"*24)
    input("Precione enter para continuar")
    limbo_p(player_character)

def inferno(player_character):
    texto = '''Você desce para o porão e vê uma
entrada com os dizeres.
Deixai toda esperança, vós que entrais!
Mas nessa porta, contém uma chave com
formato de crucifixo.'''
    def pops(player_character):
        print("=#"*24)
        print(Fore.MAGENTA+'1. se aproximar do altar'+Fore.RED+' 3. sair da capela')
        print(Fore.BLUE+"2. Aproximar-se do crucifixo")
        print("=#"*24)
        escolha = input("=>")
        if escolha == '1' or escolha == 'altar':
            cena_do_padre(player_character)
        elif escolha == '2' or escolha == 'crucifixo':
            cruz(player_character)
        elif escolha == '3' or escolha == 'porão':
            exploracao(player_character)
        else:
            clear()
            pops(player_character)
    clear()
    print("=#"*24)
    print(texto)
    print("=#"*24)
    if f"{Fore.BLUE}Crucifixo" in player_character.iniventario:
        print(Fore.BLUE + "Você possui o Crucifixo e sente uma energia protetora.")
        print(Fore.GREEN + "Você quer abrir a porta? (sim/não)")
        escolha = input("=>").lower()
        if escolha == 'sim' or escolha == 's':
            limbo(player_character)
        else:
            clear()
            print("=#"*24)
            print(Fore.YELLOW+"Você decide não abrir a porta, por enquanto.")
            print("=#"*24)
            pops(player_character)

    else:
        print(Fore.RED + "Você não possui o Crucifixo.\nA porta está selada e uma energia maligna te impede de prosseguir.")
        print("=#"*24)
        input("Pressione Enter para retornar...")
        pops(player_character)

def cena_do_padre(player_character):
    def pops(player_character):
        print("=#"*24)
        print(Fore.MAGENTA+'1. sair da capela'+Fore.RED+' 3.Ir para o porâo')
        print(Fore.BLUE+"2. Aproximar-se do crucifixo")
        print("=#"*24)
        escolha = input("=>")
        if escolha == '1' or escolha == 'sair':
            exploracao(player_character)
        elif escolha == '2' or escolha == 'crucifixo':
            cruz(player_character)
        elif escolha == '3' or escolha == 'porão':
            inferno(player_character)
        else:
            clear()
            pops(player_character)
    clear()
    print("=#"*24)
    print("Você vê um padre quase morto. Ele está podre e cheirando mal.")
    print("Ele pega seu braço e, usando suas últimas forças, sussurra:")
    print(Fore.YELLOW+"Me mate, pelo amor de Deus, Paladino... Termine meu sofrimento.")
    print("=#"*24)
    print("O que você faz?")
    print(Fore.BLUE + "1. Orar por ele")
    print(Fore.RED + "2. Matar ele")
    escolha_padre = input("=>").lower()
    if escolha_padre == '1' or escolha_padre == 'orar':
        clear()
        print("=#"*24)
        print("Você fecha os olhos e começa uma oração fervorosa pelo padre.")
        print("Uma luz azul emana de suas mãos enquanto você recita as palavras sagradas.")
        print("O corpo do padre se contorce por um momento, mas então a podridão começa a recuar,")
        print("e uma expressão de paz se espalha por seu rosto antes que ele expire.")
        print(Fore.BLUE + "Sua fé foi fortalecida por este ato de compaixão!")
        player_character.fe += 5
        print(f"Sua Fé agora é: {player_character.fe}")
        print("=#"*24)
        input("Pressione Enter para continuar...")
        player_character.padre_encontrado = True
        pops(player_character)
    elif escolha_padre == '2' or escolha_padre == 'matar':
        clear()
        print("=#"*24)
        print("Você empunha sua arma e, sem hesitar, desfere um golpe misericordioso no padre.")
        print("O som da lâmina se chocando com o corpo doente ressoa pela capela, e o padre finalmente encontra seu descanso.")
        print(Fore.RED + "Uma parte de você sente a crueldade do ato, mas outra sente um aumento de poder.")
        player_character.atk += 5
        print(f"Seu Ataque agora é: {player_character.atk}")
        print("=#"*24)
        input("Pressione Enter para continuar...")
        player_character.padre_encontrado = True
        pops(player_character)
    else:
        clear()
        cena_do_padre(player_character)

def cruz(player_character):
    cruzs = Fore.YELLOW+Back.BLACK+'''         ___         
        |###|        
        |###|        
 _______|###|_______ 
|###################|
|###################|
        |###|        
        |###|        
        |###|        
        |###|        
        |###|        
        |###|        
        |###|        
                     '''
    def ops(player_character):
        print("=#"*24)
        print(Fore.MAGENTA+'1. sair da capela'+Fore.RED+' 3.Ir para o porâo')
        print(Fore.BLUE+"2. Aproximar-se do padre")
        print("=#"*24)
        escolha = input("=>")
        if escolha == '1' or escolha == 'sair':
            exploracao(player_character)
        elif escolha == '2' or escolha == 'padre':
            cena_do_padre(player_character)
        elif escolha == '3' or escolha == 'porão':
            inferno(player_character)
        else:
            clear()
            ops(player_character)
    clear()
    print(cruzs)
    print("=#"*24)
    text = '''Você se aproxima do crucifixo e o limpa.
Você se machuca um pouco e percebe que há espinhos
no crucifixo, e há uma velha escrita nele
que diz 'Hic crucifixus spinas coronae Christi continet'.
Você reconhece essa língua, e ali fala:
'Este crucifixo contém os espinhos da coroa de Cristo'.'''
    print(text)
    print("=#"*24)
    if not player_character.crucifixo_coletado:
        print(Fore.CYAN + "Você gostaria de pegar o crucifixo? (sim/não)")
        escolha_pegar = input("=>").lower()
        if escolha_pegar == 'sim' or escolha_pegar == 's':
            player_character.iniventario.append(f"{Fore.BLUE}Crucifixo")
            player_character.fe += 10
            player_character.crucifixo_coletado = True
            print(Fore.GREEN + "Você pegou o Crucifixo! Sua Fé aumentou em 10.")
            print(f"Sua Fé agora é: {player_character.fe}")
            ops(player_character)
        elif escolha_pegar == 'n' or escolha_pegar == 'não':
            print("Você decide deixar o crucifixo onde está.")
            ops(player_character)
        else:
            clear()
            cruz(player_character)

def lapedi(player_character):
    espada = Fore.YELLOW+Back.BLACK+ '''         />____________________________________
[########[]____________________________________|
          \>                                  '''
    clear()
    print(espada)
    print("=#"*24)
    print("Você se aproxima de uma lápide antiga. Entre as ervas daninhas,")
    print("você discerne o brilho de metal enferrujado. É a sua velha espada sagrada!")
    print("=#"*24)
    if not player_character.espada_coletada:
        print(Fore.CYAN + "Você gostaria de pegar a espada? (sim/não)")
        escolha_pegar = input("=>").lower()
        if escolha_pegar == 'sim' or escolha_pegar == 's':
            player_character.iniventario.append(f"{Fore.RED}Espada")
            player_character.atk += 10
            player_character.espada_coletada = True
            print(Fore.RED + "Você pegou a sua velha espada!")
            print(Fore.RED + "Sua Violencia aumentou em mais 10!")
            print(f"Sua Violencia agora é: {player_character.atk}")
        else:
            print("Você decide deixar a espada onde está.")
    else:
        print("Você já coletou esta espada.")

    input("Pressione Enter para continuar...")
    exploracao(player_character)

def capela(player_character):
    clear()
    print("=#"*24)
    texto1 = '''Você abre as pesadas portas de madeira da capela,
que rangem como se lamentassem a própria existência.
O ar lá dentro é frio e denso, com o cheiro
inconfundível de poeira, incenso velho e algo mais...
algo que lembra terra úmida e metal. A luz que entra
pelas frestas das janelas empoeiradas mal ilumina
o interior, revelando sombras dançantes que parecem
se contorcer nas paredes.'''
    print(texto1)
    print("=#"*24)
    input("Pressione Enter para continuar...")
    clear()
    print("=#"*24)
    texto2 = '''À medida que seus olhos se ajustam à penumbra,
você distingue os contornos de bancos de madeira
carcomida, um altar coberto por um pano rasgado e,
no centro, o que parece ser uma estátua ou um
crucifixo coberto por um manto. Um silêncio
pesado preenche o lugar, interrompido apenas
pelo eco distante de seus próprios passos.'''
    print(texto2)
    print("=#"*24)
    print(Fore.MAGENTA+'1. Aproximar-se do altar'+Fore.RED+' 3.Ir para o porâo')
    print(Fore.BLUE+"2. Aproximar-se do crucifixo")
    escolha_capela = input("=>").lower()
    if escolha_capela == '1' or escolha_capela == 'altar':
        if not player_character.padre_encontrado:
            cena_do_padre(player_character)
        else:
            clear()
            print("=#"*24)
            print("Você se aproxima do altar novamente. O corpo do padre não está mais lá,")
            print("apenas uma mancha escura no chão e o cheiro persistente de morte.")
            print("Não há mais nada para fazer aqui por enquanto.")
            print("=#"*24)
            input("Pressione Enter para continuar...")
            capela(player_character)
    elif escolha_capela == '2' or escolha_capela == 'crucifixo':
        cruz(player_character)
    elif escolha_capela == '3' or escolha_capela == 'porão':
        inferno(player_character)
    else:
        clear()
        exploracao(player_character)

def exploracao(player_character):
    clear()
    print("=#"*24)
    texto ='''Pelo visto você está em um cemitério.
O céu está preto, não pela noite,
e sim pelo pecado dos seres humanos,
impuros e pecadores. O cheiro é
pútrido e nojento. Você decide andar:'''
    print(texto)
    print("=#"*24)
    print(Fore.LIGHTYELLOW_EX+"1. Capela", Fore.LIGHTBLUE_EX+" 2. Lápide")
    print(Fore.GREEN+ "3. Menu", Fore.RED+" 4. Ir para o Inferno" ) # Changed option 4 for a direct path to inferno test
    print("=#"*24)
    escolha = input("=>").lower()
    if escolha == '1' or escolha == 'capela':
        capela(player_character)
    elif escolha == '2' or escolha == 'lápide':
        lapedi(player_character)
    elif escolha == '3' or escolha == 'menu':
        clear()
        player_character.status()
        input("enter para retornar ao jogo")
        exploracao(player_character)
    elif escolha == '4' or escolha == 'inferno': # Updated choice
        # Check if the player has the crucifix before entering inferno
        if "Crucifixo" in player_character.iniventario:
            inferno(player_character)
        else:
            print(Fore.RED + "Você precisa do Crucifixo para entrar no Inferno!")
            input("Pressione Enter para continuar...")
            exploracao(player_character)
    else:
        clear()
        exploracao(player_character)

def menu():
    clear()
    print("=#" * 24)
    print(Fore.GREEN+"1: Jogar")
    print(Fore.RED+"2: Sair")
    print("=#" * 24)
    escolha = input("=>").lower()

    if escolha == '1' or escolha == 'jogar':
        clear()
        print("=#" * 24)
        texto ="""Você renasceu das cinzas e vê o mundo
totalmente corrompido e destruído. Percebe
sua lápide e seu nome está apagado. Então,
escolha seu nome atual, Cavalheiro."""
        print(texto)
        print("=#" * 24)
        nome = input("=>")
        player_character = player(nome)
        clear()
        player_character.status()
        input(Fore.CYAN+nome+" pressione Enter para continuar:")
        exploracao(player_character)
    elif escolha == '2' or escolha == 'sair':
        exit()
    else:
        clear()
        menu()
def combat(player_char, enemy):
    clear()
    print(f"--- BATALHA CONTRA {enemy.name.upper()} ---")
    player_hit_chance = 75  
    enemy_hit_chance = 50  
    while player_char.hp > 0 and enemy.hp > 0:
        enemy.status()
        player_char.menu_pl()
        print("Escolha sua ação:")
        print(Fore.BLUE + "1. Usar Fé (Dano alto, usos limitados)")
        print(Fore.RED + "2. Usar Violência (Dano normal, usos ilimitados)")
        choice = input("=> ").lower()

        player_damage = 0
        player_roll = random.randint(1, 100)

        if player_roll <= player_hit_chance:
            if choice == '1' or choice == 'fé':
                if player_char.faith_uses > 0:
                    player_damage = player_char.fe * 2
                    player_char.faith_uses -= 1
                    print(f"{Fore.BLUE}Você invoca sua fé e CAUSA {player_damage} de dano a {enemy.name}!")
                else:
                    print(Fore.YELLOW + "Você não tem mais usos de Fé restantes! Escolha outra ação.")
                    continue
            elif choice == '2' or choice == 'violência':
                player_damage = player_char.atk
                print(f"{Fore.RED}Você ataca com violência e CAUSA {player_damage} de dano a {enemy.name}!")
            else:
                clear()
                print(Fore.YELLOW + "Escolha inválida. Tente novamente.")
                continue
        else:
            print(Fore.YELLOW + "Seu ataque ERROU!")
        enemy.hp -= player_damage
        if enemy.hp < 0:
            enemy.hp = 0
        time.sleep(1) 
        if enemy.hp > 0:
            enemy_roll = random.randint(1, 100)
            if enemy_roll <= enemy_hit_chance:
                enemy_damage = enemy.atk
                player_char.hp -= enemy_damage
                if player_char.hp < 0:
                    player_char.hp = 0
                print(f"{Fore.MAGENTA}{enemy.name} ataca você e CAUSA {enemy_damage} de dano!")
            else:
                print(f"{Fore.CYAN}{enemy.name} ERROU o ataque!")
            time.sleep(1)
        clear()
    if player_char.hp <= 0:
        clear()
        print(f"\n{Fore.RED}Você foi derrotado por {enemy.name}!")
        player_char.hp = 0 
        player_char.menu_pl()
        enemy.status()
        input("Pressione Enter para continuar...")
    elif enemy.hp <= 0:
        print(f"\n{Fore.GREEN}Você derrotou {enemy.name}!")
        enemy.status()
        player_char.menu_pl()
        input("Pressione Enter para continuar...")

if __name__ == "__main__":
    menu()