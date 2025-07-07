from rich import print
from rich.table import Table, box
from rich.console import Console
from rich.text import Text 
import time
import os
import random
from ascii import art_ascii, art_ascii2
from progeto_completo import Jogador, Inimigo, combat
from amusicas import parar_musica, cidade01, rotasmm, batalhas, cidade02, labirinto_music, cidade03, music_boss, cidade04
console = Console()
itens_coletados_casa01 = set()
itens_coletados_labirinto = set()
itens_coletados_escola = set()
itens_coletados_labirinto01 = set()
boss = False
lago1 = False
ponte = False
aa = art_ascii2()
art = art_ascii()
def clear():
    """Limpa a tela do console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def gerar_inimigo_aleatorio():
    """Gera um inimigo com atributos aleatórios."""
    nomes = ["Goblin", "Esqueleto", "Morcego Gigante", "Aranha Venenosa", "Lobo Faminto", "Slime Pegajoso", "Orc Selvagem"]
    ascii_arts = [
        '''
 }{
-==o-
 ''',
    ]
    nome_aleatorio = random.choice(nomes)
    ascii_aleatorio = random.choice(ascii_arts)
    hp_aleatorio = random.randint(1, 100)
    atk_aleatorio = random.randint(5, 10)
    xp_aleatorio = random.randint(100, 300)
    gold_aleatorio = random.randint(0, 100)
    return Inimigo(nome_aleatorio, hp_aleatorio, atk_aleatorio, xp_aleatorio, gold_aleatorio, ascii_aleatorio)

def gerar_inimigo_aleatorio1():
    """Gera um inimigo com atributos aleatórios."""
    nomes = ["Goblin", "Esqueleto", "Morcego Gigante", "Aranha Venenosa", "Lobo Faminto", "Slime Pegajoso", "Orc Selvagem"]
    ascii_arts = [
        '''
 }{
-==o-
 ''',
    ]
    nome_aleatorio = random.choice(nomes)
    ascii_aleatorio = random.choice(ascii_arts)
    hp_aleatorio = random.randint(100, 200)
    atk_aleatorio = random.randint(15, 30)
    xp_aleatorio = random.randint(300, 600)
    gold_aleatorio = random.randint(10, 120)
    return Inimigo(nome_aleatorio, hp_aleatorio, atk_aleatorio, xp_aleatorio, gold_aleatorio, ascii_aleatorio)


b = """
      .--.    W    .--.    
    .'    ', {_} ,'    '.  
   <       =( X )=       > 
    '.    .`/'''\`.    .'  
      '--'  '--'   '--'    """
def c1(player):
    chaves = False
    def rota01():
        def encounter_rotas(player):
            if random.random() < 0.5: 
                enemy = gerar_inimigo_aleatorio()
                combat(player, enemy)
                if player.hp <= 0:
                    exit()
                elif player.hp > 0: 
                    parar_musica()
                    rotasmm()
        parar_musica()
        rotasmm()
        nonlocal player
        while True:
            clear()
            table = Table(style='blue',box=box.HEAVY)
            table.add_column("Rota:01")
            table.add_column("ANDAR:")
            table.add_row(f'[bold]{art.rota01}[/bold]',f'[bold yellow]{art.rota01_ops}[/bold yellow]')
            print(table)
            rot = console.input()
            if rot == '1':
                encounter_rotas(player)
            elif rot == '2':
                clear()
                table = Table(style='blue',box=box.HEAVY)
                table.add_column("Rota:01")
                table.add_column("ANDAR:")
                table.add_row(f'[bold]{art.rota01}[/bold]',f'[bold yellow]PELO VISTO NÃO TEM NADA:[/bold yellow]')
                print(table)
                console.input('[bold yellow]PRECIONE ENTER:[/bold yellow]')
            elif rot == '3':
                encounter_rotas(player)
                cidade1()
            elif rot == '4':
                encounter_rotas(player)
                cidade2()
            elif rot == '5':
                player.menu()

    def cidade1():
        def casa00():
            while True:
                clear()
                table = Table(style='blue',box=box.HEAVY)
                table.add_column("Sua Casa:")
                table.add_column("ANDAR:")
                table.add_row(f'[bold]{art.casa}[/bold]',f'[bold yellow]{art.c00}[/bold yellow]')
                print(table)
                andar = console.input()
                if andar == '1':
                    player.visitar_hospital()
                elif andar == '2':
                    cidade1()
        def casa01():
            while True:
                clear()
                table = Table(style='blue',box=box.HEAVY)
                table.add_column("[yellow]Casa: 01[/yellow]")
                table.add_column("ANDAR:")
                table.add_row(f'[bold]{art.casa}[/bold]',f'[bold yellow]{art.escolha1}[/bold yellow]')
                print(table)
                andar = console.input()
                if andar == '1':
                    item_na_casa = "Refrigerante" 
                    if item_na_casa not in itens_coletados_casa01:
                        player.adicionar_item_inventario(item_na_casa)
                        itens_coletados_casa01.add(item_na_casa) 
                        console.print(f"[bold green]Você ganhou um {item_na_casa} na Casa 01![/bold green]")
                        time.sleep(1)
                    else:
                        console.print(f"[bold yellow]Você já coletou o {item_na_casa} desta casa. Não há mais nada aqui.[/bold yellow]")
                        time.sleep(1.5)
                elif andar == '2':
                    cidade1()
        def escola():
            while True:
                clear()
                table = Table(style='blue',box=box.HEAVY)
                table.add_column("[yellow]Casa: 01[/yellow]")
                table.add_column("ANDAR:")
                table.add_row(f'[bold]{art.escola}[/bold]',f'[bold yellow]{art.escolha1}[/bold yellow]')
                print(table)
                andar = console.input()
                if andar == '1':
                    item_na_esc = "Livro" 
                    if item_na_esc not in itens_coletados_escola:
                        player.adicionar_item_inventario(item_na_esc)
                        itens_coletados_escola.add(item_na_esc) 
                        console.print(f"[bold green]Você recebeu um {item_na_esc} do Professor![/bold green]")
                        time.sleep(1)
                    else:
                        console.print(f"[bold yellow]Você já coletou o {item_na_esc} desta escola. Não há mais nada aqui.[/bold yellow]")
                        time.sleep(1)
                elif andar == '2':
                    cidade1()
        def casa24():
            while True:
                clear()
                table = Table(style='blue',box=box.HEAVY)
                table.add_column("Casa:24")
                table.add_column("ANDAR:")
                table.add_row(f'[bold]{art.casa}[/bold]',f'[bold yellow]{art.escolha1}[/bold yellow]')
                print(table)
                andar = console.input()
                if andar == '1':
                    clear()
                    table = Table(style='blue',box=box.HEAVY)
                    table.add_column("Casa:24")
                    table.add_column("ANDAR:")
                    table.add_row(f'[bold]{art.casa}[/bold]',f'[bold yellow]{art.dialogo1}[/bold yellow]')
                    print(table)
                    console.input()
                    cidade1()
                elif andar == '2':
                    cidade1()
        nonlocal player
        parar_musica()
        cidade01()
        while True:
            clear()
            table = Table(style='blue',box=box.HEAVY)
            table.add_column("[yellow]Cidade Inicial:[/yellow]")
            table.add_column("ANDAR:")
            table.add_row(f'[bold]{art.cidade1}[/bold]',f'[bold yellow]{art.c1}[/bold yellow]')
            print(table)
            andar = console.input()
            if andar == '1':  
                casa00()  
            elif andar == '2':
                casa01() 
            elif andar == '3':
                rota01()
            elif andar == '4':
                escola()
            elif andar == '5':
                casa24()
            elif andar == '6':
                player.menu()

    def cidade2():
        parar_musica()
        cidade02()
        def casa():
            while True:
                clear()
                table = Table(style='red',box=box.HEAVY)
                table.add_column("Casa:21")
                table.add_column("ANDAR:")
                table.add_row(f'[bold]{art.casa}[/bold]',f'[bold yellow]{art.escolha1}[/bold yellow]')
                print(table)
                rot = console.input()
                if rot == '1':
                    if chaves == True:
                        ##cidade final
                        pass
                    elif chaves == False:
                        clear()
                        table = Table(style='red',box=box.HEAVY)
                        table.add_column("Casa:21")
                        table.add_column("ANDAR:")
                        table.add_row(f'[bold]{art.casa}[/bold]',f'[bold yellow]{art.chaves}[/bold yellow]')
                        print(table)
                        console.input()
                elif rot == '2':
                    cidade2()
        nonlocal player
        while True:
            clear()
            table = Table(style='blue',box=box.HEAVY)
            table.add_column("Cidade Harley:")
            table.add_column("ANDAR:")
            table.add_row(f'[bold]{art.cidade2}[/bold]',f'[bold yellow]{art.c2}[/bold yellow]')
            print(table)
            rot = console.input()
            if rot == '1':
                rota01()
            elif rot == '2':
                player.shop()
            elif rot == '3':
                player.visitar_hospital()
                cidade2()
            elif rot == '4':
                labirinto()
            elif rot == '5':
                casa()
            elif rot == '6': 
                player.menu()
    
    def labirinto02():
        def encounter_chance1(player):
            if random.random() < 0.5: 
                enemy = gerar_inimigo_aleatorio1()
                combat(player, enemy)
                if player.hp <= 0:
                    exit()
                elif player.hp > 0:
                    parar_musica()
                    labirinto_music()
        def encounter(player):
            if random.random() < 1: 
                enemy = gerar_inimigo_aleatorio1()
                combat(player, enemy)
                if player.hp <= 0:
                    exit()
                elif player.hp > 0:
                    parar_musica()
                    labirinto_music()
        parar_musica()
        labirinto_music()
        nonlocal player
        global boss
        while True:
            clear()
            table = Table(style='blue',box=box.HEAVY)
            table.add_column("Labirinto")
            table.add_column("ANDAR:")
            table.add_row(f'[bold]{art.labirinto}[/bold]',f'[bold yellow]{art.labirinto_ops}[/bold yellow]')
            print(table)
            labirinto0 = console.input()
            if labirinto0 == '1':
                encounter_chance1(player)
                labirinto()
            elif labirinto0 == '2':
                encounter_chance1(player)
                cidade3()
            elif labirinto0 == '3':
                while True:
                    clear()
                    table = Table(style='blue',box=box.HEAVY)
                    table.add_column("[bold yellow]Labirinto[/bold yellow]")
                    table.add_column("[bold red]ANDAR[/bold red]:")
                    table.add_row(f'[bold]{art.interrogação}[/bold]',f'[bold yellow]{art.ex}[/bold yellow]')
                    print(table)
                    andar = console.input()
                    if andar == '1':
                        console.print('[bold yellow]Não há nada por aqui[/bold yellow]')
                        time.sleep(2)
                        break
                    elif andar == '3':
                        item_no_lab1 = "Livro" 
                        if item_no_lab1 not in itens_coletados_labirinto01:
                            player.adicionar_item_inventario(item_no_lab1)
                            itens_coletados_labirinto01.add(item_no_lab1) 
                            console.print(f"[bold green]Você achou uma {item_no_lab1} no labirinto![/bold green]")
                            time.sleep(1)
                        else:
                            console.print(f"[bold yellow]Você já coletou o {item_no_lab1} no labirinto. Não há mais nada aqui.[/bold yellow]")
                            time.sleep(1)
                    elif andar == '2':
                        break
                    elif andar == '4':
                        player.menu()
            elif labirinto0 == '4':
                encounter(player)
            elif labirinto0== '5':
                player.menu()

    def labirinto():
        def encounter_chance1(player):
            if random.random() < 0.5: 
                enemy = gerar_inimigo_aleatorio1()
                combat(player, enemy)
                if player.hp <= 0:
                    exit()
                elif player.hp > 0:
                    parar_musica()
                    labirinto_music()
        def encounter(player):
            if random.random() < 1: 
                enemy = gerar_inimigo_aleatorio1()
                combat(player, enemy)
                if player.hp <= 0:
                    exit()
                elif player.hp > 0:
                    parar_musica()
                    labirinto_music()
        nonlocal player
        global boss
        while True:
            clear()
            table = Table(style='blue',box=box.HEAVY)
            table.add_column("Labirinto")
            table.add_column("ANDAR:")
            table.add_row(f'[bold]{art.labirinto1}[/bold]',f'[bold yellow]{art.labirinto1_ops}[/bold yellow]')
            print(table)
            rota = console.input()
            if rota =='1':
                encounter(player)
                labirinto02()
            elif rota == '2':
                cidade2()
            elif rota == '3':
                encounter_chance1(player)
                while True:
                    clear()
                    table = Table(style='blue',box=box.HEAVY)
                    table.add_column("[bold yellow]Labirinto[/bold yellow]")
                    table.add_column("[bold red]ANDAR[/bold red]:")
                    table.add_row(f'[bold]{art.interrogação}[/bold]',f'[bold yellow]{art.ex}[/bold yellow]')
                    print(table)
                    rota1 = console.input()
                    if rota1 == '1':
                        clear()
                        table = Table(style='blue',box=box.HEAVY)
                        table.add_column("[bold yellow]Labirinto[/bold yellow]")
                        table.add_column("[bold red]ANDAR[/bold red]:")
                        table.add_row(f'[bold]{art.interrogação}[/bold]',f'[bold yellow]{art.explorar}[/bold yellow]')
                        print(table)
                        explorar = console.input()
                        if explorar == '1':
                            item_no_lab = "Refrigerante" 
                            if item_no_lab not in itens_coletados_labirinto:
                                player.adicionar_item_inventario(item_no_lab)
                                itens_coletados_labirinto.add(item_no_lab) 
                                console.print(f"[bold green]Você encontrou uma {item_no_lab} no labirinto![/bold green]")
                                time.sleep(1)
                            else:
                                console.print(f"[bold yellow]Você já coletou a {item_no_lab} do Labirinto. Não há mais nada aqui.[/bold yellow]")
                                time.sleep(1)
                        elif explorar == '2':
                            break
                        elif explorar == '3':
                            player.menu()
                    elif rota1 == '2':
                            encounter_chance1(player)
                            break
                    elif rota1 == '3':
                        if boss == False:
                            ee = Inimigo(name='Grande Moaquito', hp=500, atk=35, xp=1000, gold=350, ascii_art=b)
                            combat(player, ee)
                            if player.hp <=0:
                                console.print('[bold yellow]Você foi derrotado[/bold yellow]')
                                time.sleep(2)
                                exit()
                            elif player.hp > 0:
                                boss = True
                                console.print('[bold yellow]Você Ganho[/bold yellow]')
                                time.sleep(2)
                        elif boss == True:
                            console.print('[bold yellow]Você já Ganho[/bold yellow]')
                            time.sleep(2)
                    elif rota1 == '4':
                        player.menu()
            elif rota == '4':
                encounter_chance1(player)
            elif rota == '5':
                player.menu()

    def cidade3():
        nonlocal player
        global lago1
        global ponte
        parar_musica()
        cidade03()
        while True:
            clear()
            table = Table(style='blue',box=box.HEAVY)
            table.add_column("Cidade: West")
            table.add_column("ANDAR:")
            table.add_row(f'[bold]{art.cidade3}[/bold]',f'[bold yellow]{art.ops_c3}[/bold yellow]')
            print(table)
            ops = console.input()
            if ops == '1':
                while True:
                    clear()
                    table = Table(style='blue',box=box.HEAVY)
                    table.add_column("Cidade:3")
                    table.add_column("ANDAR:")
                    table.add_row(f'[bold]{art.casa}[/bold]',f'[bold yellow]{art.casa11}[/bold yellow]')
                    print(table)
                    console.input()
                    break
            elif ops == '2':
                while True:
                    clear()
                    table = Table(style='blue',box=box.HEAVY)
                    table.add_column("Cidade:3")
                    table.add_column("ANDAR:")
                    table.add_row(f'[bold]{art.casa24}[/bold]',f'[bold yellow]{art.casa13}[/bold yellow]')
                    print(table)
                    console.input()
                    break
            elif ops == '3':
                player.shop()
            elif ops == '4':
                player.visitar_hospital()
            elif ops == '5':
                parar_musica()
                music_boss()
                while True:
                    clear()
                    table = Table(style='blue',box=box.HEAVY)
                    table.add_column("Grande Lago:")
                    table.add_column("Ações:")
                    table.add_row(f'[bold]{art.lagos}[/bold]',f'[bold yellow]{art.lago_ops1}[/bold yellow]')
                    print(table)
                    boss_bat = input("")
                    if boss_bat == '1':
                        if lago1 == False:
                            console.print("[bold red]Você se aproxima do Chefe e ele sai\nda água e vai te atacar se prepare[/bold red]")
                            time.sleep(3)
                            mos = Inimigo(name='Aedes Aegypti', hp=600, atk=50, xp=5000, gold=2500, ascii_art=b)
                            combat(player, mos)
                            if player.hp <= 0:
                                exit()
                            elif player.hp > 0:
                                lago1 = True
                                ponte = True
                                console.print("[bold yellow]Você derrotol o Aedes Aegypti[/bold yellow]")
                                console.print("[bold yellow]HÁ PONTE FOI LIBRERADA[/bold yellow]")
                                music_boss()
                        elif lago1 == True:
                            console.print("[bold yellow]Você já derrotol o Aedes Aegypti[/bold yellow]")
                            time.sleep(3)
                    elif boss_bat == '2':
                        cidade3()
            elif ops == '6':
                if ponte == False:
                    console.print("[bold yellow]Você não pode passar daqui derrote\no Grande Chefe da cidade[/bold yellow]")
                    time.sleep(3)
                elif ponte == True:
                    clear()
                    table = Table(style='blue',box=box.HEAVY)
                    table.add_column("Ponte:Lest")
                    table.add_column("ANDAR:")
                    table.add_row(f'[bold]{aa.ponte}[/bold]',f'[bold yellow]{aa.ponte_ops}[/bold yellow]')
                    print(table)
                    po = console.input('')
                    if po == '1':
                        cidade3()
                    elif po == '2':
                        c2()
            elif ops == '7':
                labirinto02()
            elif ops == '8':
                player.menu()
    cidade1()

def c2(player):
    def cidade4():
        parar_musica()
        cidade04()
        nonlocal player
        table = Table(style='blue',box=box.HEAVY)
        table.add_column("Cidade Pelicanos")
        table.add_column("ANDAR:")
        table.add_row(f'[bold]{aa.cidade4}[/bold]',f'[bold yellow]{aa.cidade4_ops}[/bold yellow]')
        print(table)
    cidade4()

