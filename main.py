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
    def __init__(self, nome: str, max_hp: int, atc: int, max_mana: int, atm: int, gold: int, xp: int):
        self.nome = nome
        self.max_hp = max_hp
        self.hp = self.max_hp
        self.atc = atc
        self.max_mana = max_mana
        self.mana = self.max_mana
        self.inventario = []
        self.gold = gold
        self.xp = xp
        self.hit_chance = 75
        self.atk_mana = atm

    def status(self):
        """Exibe o status detalhado do jogador."""
        clear() 
        table = Table(box=box.HEAVY, style="blue")
        table.add_column(f"Nome: [bold white]{self.nome}[/bold white]")
        table.add_row(f"HP: [#00FF00]{self.hp}[/#00FF00]/[#00FF00]{self.max_hp}[/#00FF00]")
        table.add_row(f"Mana: [#7B68EE]{self.mana}[/#7B68EE]/[#7B68EE]{self.max_mana}[/#7B68EE]")
        table.add_row(f"Ataque: [#FF0000]{self.atc}[/#FF0000]")
        table.add_row(f"Ouro: [#FFFF00]{self.gold}[/#FFFF00]")
        table.add_row(f"XP: [#4B0082]{self.xp}[/#4B0082]")
        console.print(table)
        console.input("\n[bold magenta]Pressione Enter para continuar...[/bold magenta]")


    def batalha_info(self):
        """Exibe informações do jogador específicas para a batalha."""
        table = Table(box=box.HEAVY, style='blue')
        table.add_column(f"Nome: [bold white]{self.nome}[/bold white]")
        table.add_row(f"HP: [#00FF00]{self.hp}[/#00FF00]/[#00FF00]{self.max_hp}[/#00FF00]")
        table.add_row(f"Mana: [#7B68EE]{self.mana}[/#7B68EE]/[#7B68EE]{self.max_mana}[/#7B68EE]")
        table.add_row(f"Ataque: [#FF0000]{self.atc}[/#FF0000]")
        console.print(table)

    def take_damage(self, damage: int):
        """Reduz o HP do jogador pelo dano recebido."""
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        console.print(f"[bold red]{self.nome} recebeu {damage} de dano![/bold red]")

    def attack_enemy(self, enemy):
        """Jogador ataca o inimigo com chance de acerto."""
        roll = random.randint(1, 100)
        if roll <= self.hit_chance:
            damage = random.randint(self.atc - 3, self.atc + 3)
            enemy.take_damage(damage)
            console.print(f"[bold green]{self.nome} atacou {enemy.name} e causou {damage} de dano![/bold green]")
        else:
            console.print(f"[bold yellow]{self.nome} errou o ataque em {enemy.name}![/bold yellow]")

    def attack_mana(self, enemy):
        roll = random.randint(1, 100)
        if roll <= self.hit_chance:
            damage = random.randint(self.atk_mana - 3, self.atk_mana + 3)
            enemy.take_damage(damage)
            console.print(f"[bold green]{self.nome} atacou {enemy.name} e causou {damage} de dano![/bold green]")
        else:
            console.print(f"[bold yellow]{self.nome} errou o ataque em {enemy.name}![/bold yellow]")

class Inimigo:
    """Representa um personagem inimigo."""
    def __init__(self, name: str, hp: int, atk: int, xp: int, gold: int, ascii_art=""):
        self.ascii = ascii_art
        self.name = name
        self.hp = hp
        self.atk = atk
        self.xp = xp
        self.hp_max = hp
        self.hit_chance = 50
        self.gold = gold

    def info(self):
        """Exibe informações detalhadas do inimigo."""
        table = Table(box=box.HEAVY, style='red')
        table.add_column(f'Nome: [bold red]{self.name}[/bold red]')
        table.add_row(f'[red]{self.ascii}[/red]')
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
        """Inimigo ataca o jogador com chance de acerto."""
        roll = random.randint(1, 100)
        if roll <= self.hit_chance:
            damage = random.randint(self.atk - 2, self.atk + 2)
            player.take_damage(damage)
            console.print(f"[bold red]{self.name} atacou {player.nome} e causou {damage} de dano![/bold red]")
        else:
            console.print(f"[bold yellow]{self.name} errou o ataque em {player.nome}![/bold yellow]")
# --- Sistema de Combate ---
def combat(player: Jogador, enemy: Inimigo):
    """Gerencia o combate por turnos entre o jogador e um inimigo."""
    console.print(f"\n--- [bold yellow]Um {enemy.name} selvagem apareceu![/bold yellow] ---")
    time.sleep(2)

    while player.hp > 0 and enemy.hp > 0:
        clear()
        console.print("\n--- [bold cyan]TURNO DE BATALHA[/bold cyan] ---")
        player.batalha_info()
        enemy.info()
        console.print("\n[bold green]Seu Turno![/bold green]")
        console.print("[1] Atacar")
        console.print("[2]Mana")
        choice = console.input("[bold blue]Escolha uma ação: [/bold blue]")
        if choice == '1':
            player.attack_enemy(enemy)
        elif choice == '2':
            player.attack_mana(enemy)
            player.mana -= 10
        else:
            console.print("[bold red]Ação inválida! Você perde seu turno![/bold red]")
        time.sleep(1.5)

        if enemy.hp <= 0:
            break

        if player.hp > 0: 
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
        player.gold += enemy.gold
        console.print(f"[bold yellow]Você encontrou {enemy.gold} ouro![/bold yellow]")
        player.status() 

def menu():
    def gerar_inimigo_aleatorio():
        """Gera um inimigo com atributos aleatórios."""
        nomes = ["Goblin", "Esqueleto", "Morcego Gigante", "Aranha Venenosa", "Lobo Faminto", "Slime Pegajoso", "Orc Selvagem"]
        ascii_arts = [
        '''
  }{
 -==o-
    ''',
        '''
  }O{
  /|\
  ===
    ''',
        '''
  /\\
 (oo)
  \\/
    ''',
        '''
   /\\
  (..)/
   VV
    ''',
        '''
  ^ ^
 (o o)
  /V\\
    ''',
        '''
  .---.
 /     \\
|  ()  |
 \\     /
  `---'
    ''',
        '''
   O O
  / V \\
  \\_U_/
    '''
    ]
        nome_aleatorio = random.choice(nomes)
        ascii_aleatorio = random.choice(ascii_arts)
        hp_aleatorio = random.randint(30, 100)
        atk_aleatorio = random.randint(5, 15)
        xp_aleatorio = random.randint(100, 300)
        gold_aleatorio = random.randint(1, 10)
        return Inimigo(nome_aleatorio, hp_aleatorio, atk_aleatorio, xp_aleatorio, gold_aleatorio, ascii_aleatorio)
    clear()
    
    nome = console.input("[bold blue]Digite o nome do seu jogador: [/bold blue]")
    player1 = Jogador(nome, max_hp=100, atc=15, max_mana=50, atm=25, gold=250, xp=0) 
    while True:
        clear()
        console.print("[bold green]Bem-vindo à Aventura![/bold green]")
        console.print("[1] Iniciar Combate")
        console.print("[2] Status do Jogador")
        console.print("[3] Sair do Jogo")
        escolha = console.input("[bold blue]O que você gostaria de fazer? [/bold blue]")
        if escolha == '1':
            if player1.hp > 0:
                console.print("\n[bold yellow]Você continua sua jornada... e encontra um inimigo![/bold yellow]")
                time.sleep(2)
                inimigo_atual = gerar_inimigo_aleatorio()
                combat(player1, inimigo_atual)
            else:
                console.print("\n[bold red]Sua jornada termina aqui. Você não tem HP para continuar.[/bold red]")
                break
        elif escolha == '2':
            player1.status()
        elif escolha == '3':
            console.print("\n[bold magenta]Obrigado por jogar! Até a próxima![/bold magenta]")
            break 
        else:
            console.print("\n[bold red]Opção inválida. Por favor, escolha novamente.[/bold red]")
            time.sleep(1.5)

if __name__ == "__main__":
    menu()