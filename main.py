from rich import print
from rich.table import Table, box
from rich.console import Console
import time
import os
import random

console = Console()

def clear():
    """Limpa a tela do console."""
    os.system('cls' if os.name == 'nt' else 'clear')

class Jogador:
    """Representa o personagem do jogador."""
    def __init__(self, nome: str, hpmax: int, atc: int, manamax: int, gold: int, xp: int):
        self.nome = nome
        self.hpmax = hpmax
        self.hp = self.hpmax
        self.atc = atc
        self.manamax = manamax
        self.mana = self.manamax
        self.inventario = []
        self.gold = gold
        self.xp = xp

    def status(self):
        """Exibe o status detalhado do jogador."""
        table = Table(box=box.HEAVY, style="blue")
        table.add_column(f"Nome: [bold white]{self.nome}[/bold white]")
        table.add_row(f"HP: [#00FF00]{self.hp}[/#00FF00]/[#00FF00]{self.hpmax}[/#00FF00]")
        table.add_row(f"Mana: [#7B68EE]{self.mana}[/#7B68EE]/[#7B68EE]{self.manamax}[/#7B68EE]")
        table.add_row(f"Ataque: [#FF0000]{self.atc}[/#FF0000]")
        table.add_row(f"Ouro: [#FFFF00]{self.gold}[/#FFFF00]")
        table.add_row(f"XP: [#4B0082]{self.xp}[/#4B0082]")
        console.print(table)

    def batalha_info(self):
        """Exibe informações do jogador específicas para a batalha."""
        table = Table(box=box.HEAVY, title=f"--- [bold blue]{self.nome}[/bold blue] ---")
        table.add_row("HP", f"[#00FF00]{self.hp}[/#00FF00]/[#00FF00]{self.hpmax}[/#00FF00]")
        table.add_row("Mana", f"[#7B68EE]{self.mana}[/#7B68EE]/[#7B68EE]{self.manamax}[/#7B68EE]")
        table.add_row("Ataque", f"[#FF0000]{self.atc}[/#FF0000]")
        console.print(table)

    def take_damage(self, damage: int):
        """Reduz o HP do jogador pelo dano recebido."""
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        console.print(f"[bold red]{self.nome} recebeu {damage} de dano![/bold red]")

    def attack_enemy(self, enemy):
        """Jogador ataca o inimigo."""
        damage = random.randint(self.atc - 3, self.atc + 3)
        enemy.take_damage(damage)
        console.print(f"[bold green]{self.nome} atacou {enemy.name} e causou {damage} de dano![/bold green]")
        time.sleep(1)

class Inimigo:
    """Representa um personagem inimigo."""
    def __init__(self, name: str, hp: int, atk: int, xp: int, ascii_art=""):
        self.ascii = ascii_art
        self.name = name
        self.hp = hp
        self.atk = atk
        self.xp = xp
        self.hp_max = hp

    def info(self):
        """Exibe informações detalhadas do inimigo."""
        table = Table(box=box.HEAVY, style='red')
        table.add_column(f'Nome: [bold red]{self.name}[/bold red]')
        table.add_row(f'{self.ascii}')
        table.add_row(f"Vida: [#FF0000]{self.hp}[/#FF0000]/[#FF0000]{self.hp_max}[/#FF0000]")
        table.add_row(f'Ataque: {self.atk}')
        print(table)

    def take_damage(self, damage: int):
        """Reduz o HP do inimigo pelo dano recebido."""
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        console.print(f"[bold red]{self.name} recebeu {damage} de dano![/bold red]")

    def attack_player(self, player):
        """Inimigo ataca o jogador."""
        damage = random.randint(self.atk - 2, self.atk + 2)
        player.take_damage(damage)
        console.print(f"[bold red]{self.name} atacou {player.nome} e causou {damage} de dano![/bold red]")
        time.sleep(1)

# --- Sistema de Combate ---
def combat(player: Jogador, enemy: Inimigo):
    """Gerencia o combate por turnos entre o jogador e um inimigo."""
    console.print(f"\n--- [bold yellow]Um {enemy.name} selvagem apareceu![/bold yellow] ---")
    time.sleep(1.5)

    while player.hp > 0 and enemy.hp > 0:
        clear()
        console.print("\n--- [bold cyan]TURNO DE BATALHA[/bold cyan] ---")
        player.batalha_info()
        enemy.info()

        # Turno do Jogador
        console.print("\n[bold green]Seu Turno![/bold green]")
        console.print("[1] Atacar")

        choice = console.input("[bold blue]Escolha uma ação: [/bold blue]")

        if choice == '1':
            player.attack_enemy(enemy)
        else:
            console.print("[bold red]Ação inválida! Você perde seu turno![/bold red]")
            time.sleep(1.5)
        if enemy.hp <= 0:
            break
        console.print(f"\n[bold red]Turno do {enemy.name}![/bold red]")
        enemy.attack_player(player)
        time.sleep(1.5)

    clear()
    if player.hp <= 0:
        console.print("[bold red]Você foi derrotado... Fim de Jogo.[/bold red]")
        player.status()
    else:
        console.print(f"[bold green]Você derrotou o {enemy.name}![/bold green]")
        console.print(f"[bold yellow]Você ganhou {enemy.xp} XP![/bold yellow]")
        player.xp += enemy.xp
        player.gold += random.randint(5, 15)
        console.print(f"[bold yellow]Você encontrou {player.gold} ouro![/bold yellow]")
        player.status() 

    console.input("\n[bold magenta]Pressione Enter para continuar...[/bold magenta]")
def menu():
    clear()
    nome = console.input("[bold blue]Digite o nome do seu jogador: [/bold blue]")
    player1 = Jogador(nome, hpmax=100, atc=15, manamax=50, gold=250, xp=0)
    player1.status()
    time.sleep(2)

    # Definir alguns inimigos
    mosquito_art = '''
  }{    
 -==o-
    '''
    mosquito = Inimigo(ascii_art=mosquito_art, name='Mosquito Gigante', hp=50, atk=8, xp=50)

    goblin_art = '''
 }O{
 /|\
 ===
    '''
    goblin = Inimigo(ascii_art=goblin_art, name='Goblin Selvagem', hp=75, atk=12, xp=75)

    # Iniciar um encontro de combate
    combat(player1, mosquito)
    if player1.hp > 0:
        console.print("\n[bold yellow]Você continua sua jornada... e encontra outro inimigo![/bold yellow]")
        time.sleep(2)
        combat(player1, goblin)
    else:
        console.print("\n[bold red]Sua jornada termina aqui.[/bold red]")


if __name__ == "__main__":
    menu()
