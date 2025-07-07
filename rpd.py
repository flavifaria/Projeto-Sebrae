import progeto_completo 
from progeto_completo import Jogador
from progeto_completo import Inimigo
from progeto_completo import combat
from ascii import art_ascii
from mapa import c1
from rich import print
from rich.table import Table, box
from rich.console import Console
from rich.text import Text 
import time
import os
import random
import threading
import amusicas
console = Console()

musicas = amusicas.ini()
mosquito = '''  }{
 -==o-''' 


def clear():
    """Limpa a tela do console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def demo():
    musicas
    play = art_ascii()
    clear()
    table = Table(box=box.HEAVY, style="white")
    table.add_column("[bold green]DEMO[/bold green]")
    table.add_row("[bold green][1]Jogar[/bold green]\n[bold red][2]sair[/bold red]")
    print(table)
    ops = console.input()
    if ops.lower() == '1':
        nome = console.input("[bold blue]Digite o nome do seu jogador:[/bold blue]")
        player = Jogador(nome, max_hp=50, atc=10, max_mana=25, atm=20, gold=100, xp=0)
        c1(player)
    elif ops == '2':
        exit()
demo()
