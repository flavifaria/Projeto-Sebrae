import progeto_completo 
from progeto_completo import Jogador
from progeto_completo import Inimigo
from progeto_completo import combat
from ascii import art_ascii
from rich import print
from rich.table import Table, box
from rich.console import Console
from rich.text import Text 
import time
import os
import random
console = Console()
mosquito = '''  }{
 -==o-'''


def clear():
    """Limpa a tela do console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def Iniciu():
    clear()
    console.print("[green][1]Jogar[/green]\n[red][2]Sair[/red]]")
    esc = console.input('=>')
    if esc == '1':
        clear()
        nome = console.input("[bold blue]Digite o nome do seu jogador: [/bold blue]")
        clear()
        play = art_ascii()
        nimigo = Inimigo(name='Mosqui',hp= 25, atk=5, xp=100, gold=0, ascii_art=mosquito)
        player = Jogador(nome, max_hp=50, atc=100, max_mana=25, atm=15, gold=0, xp=0)
        table = Table(box=box.HEAVY, style="white")
        table.add_column("[bold green]Seu Quarto: [/bold green]")
        table.add_column("[bold red]COMPUTADOR: [/bold red]")
        table.add_row(f'[bold green]{play.art1}[/bold green]',f'[bold blue]{play.pc}[/bold blue]')
        print(table)
        console.input()
        clear()
        table = Table(box=box.HEAVY, style="white")
        table.add_column("[bold green]Seu Quarto:: [/bold green]")
        table.add_column("[bold red]COMPUTADOR: [/bold red]")
        table.add_row(f'[bold green]{play.art1}[/bold green]',f'[bold blue]{play.pc1}[/bold blue]')
        print(table)
        console.input()
        clear()
        table = Table(box=box.HEAVY, style="white")
        table.add_column("[bold green]Fora de Casa: [/bold green]")
        table.add_column("[bold red]PENSAMENTOS: [/bold red]")
        table.add_row(f'[bold green]{play.sair}[/bold green]',f'[bold blue]{play.andar}[/bold blue]')
        print(table)
        console.input()
        if player.hp > 0:
            time.sleep(2)
            combat(player, nimigo)
            player.inventario.append('Pomada de Regeneração')
            clear()
            table = Table(box=box.HEAVY, style="white")
            table.add_column("[bold green]Fora de Casa: [/bold green]")
            table.add_column("[bold red]AÇÕES: [/bold red]")
            table.add_row(f'[bold green]{play.sair}[/bold green]',f'[bold blue]{play.andar2}[/bold blue]')
            print(table)
            console.input()
            while True:
                clear()
                table = Table(box=box.HEAVY, style="white")
                table.add_column("[bold green]Fora de Casa: [/bold green]")
                table.add_column("[bold red]AÇÕES: [/bold red]")
                table.add_row(f'[bold green]{play.sair}[/bold green]',f'[bold blue]{play.ops}[/bold blue]')
                print(table)
                ops = console.input('AÇÕES:')
                if ops == '1':
                    clear()
                    table = Table(box=box.HEAVY, style="white")
                    table.add_column("[bold green]Fora de Casa: [/bold green]")
                    table.add_column("[bold red]AÇÕES: [/bold red]")
                    table.add_row(f'[bold green]{play.sair}[/bold green]',f'[bold blue]{play.ops1}[/bold blue]')
                    print(table)
                    ops1 = console.input('ANDAR:')
                elif ops == '2':
                    clear()
                    table = Table(box=box.HEAVY, style="white")
                    table.add_column("[bold green]Fora de Casa: [/bold green]")
                    table.add_column("[bold red]AÇÕES: [/bold red]")
                    table.add_row(f'[bold green]{play.sair}[/bold green]',f'[bold blue]{play.ops2}[/bold blue]')
                    print(table)
                    ops2 = console.input('ESCOLHAS:')
                    while True:
                        if ops2 == '1':
                            player.status()
                            console.input("Pressione Enter para continuar...")
                            break
                        elif ops2 == '2':
                            player.exibir_menu_inventario()
                            break
                        elif ops2 == '3':
                            player.up()
                            break
                        elif ops2 == '4':
                            break

                elif ops == '3':
                    break
        else:
            console.print("\n[bold red]Sua jornada termina aqui. Você não tem HP para continuar.[/bold red]")
            exit()
    elif esc == '2':
        exit()
        
Iniciu()