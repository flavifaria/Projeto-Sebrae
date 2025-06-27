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
        """Ataca o inimigo usando mana."""
        roll = random.randint(1, 100)
        if roll <= self.hit_chance:
            damage = random.randint(self.atk_mana - 3, self.atk_mana + 3)
            enemy.take_damage(damage)
            console.print(f"[bold green]{self.nome} atacou {enemy.name} e causou {damage} de dano![/bold green]")
        else:
            console.print(f"[bold yellow]{self.nome} errou o ataque em {enemy.name}![/bold yellow]")

    def usar_item(self, item_nome: str):
        if item_nome == "Poção de HP":
            if "Poção de HP" in self.inventario:
                self.hp = min(self.max_hp, self.hp + 30) 
                self.inventario.remove("Poção de HP")
                console.print("[bold green]Você usou uma Poção de HP e recuperou HP![/bold green]")
            else:
                console.print("[bold red]Você não tem Poções de HP no seu inventário.[/bold red]")
        elif item_nome == 'Poção de Mana':
            if 'Poção de Mana' in self.inventario:
                self.mana = min(self.max_mana, self.mana + 30)
                self.inventario.remove('Poção de Mana')
                console.print('[bold blue]Você usou uma Poção de Mana e recuperou Mana![/bold blue]')
            else:
                console.print("[bold red]Você não tem Poções de Mana no seu inventário.[/bold red]")
        elif item_nome == "Cajado":
            if "Cajado" in self.inventario:
                if "Cajado Equipado" not in self.inventario:
                    self.atk_mana += 5 
                    self.inventario.remove("Cajado")
                    self.inventario.append("Cajado Equipado")  
                    console.print(f"[bold green]Você equipou o Cajado e seu ataque magico em {self.atk_mana}[/bold green]")
                else:
                    console.print("[bold yellow]Você já tem uma arma equipada.[/bold yellow]")
            else:
                console.print("[bold red]Você não tem um Cajado no seu inventário.[/bold red]")
        elif item_nome == "Espada Longa":
            if "Espada Longa" in self.inventario:
                if "Espada Equipada" not in self.inventario:
                    self.atc += 10  
                    self.inventario.remove("Espada Longa")
                    self.inventario.append("Espada Equipada")
                    console.print("[bold green]Você equipou a Espada Longa e seu ataque aumentou em 10![/bold green]")
                else:
                    console.print("[bold yellow]Você já tem uma arma equipada.[/bold yellow]")
            else:
                console.print("[bold red]Você não tem uma Espada Longa no seu inventário.[/bold red]")
        elif item_nome == 'Capacete':
            if "Capacete" in self.inventario:
                if "Capacete Equipado" not in self.inventario:
                    self.max_hp += 10 
                    self.inventario.remove("Capacete")
                    self.inventario.append("Capacete Equipado")
                    console.print("[bold green]Você equipou o Capacete e seu Hp aumentou em 10![/bold green]")
                else:
                    console.print("[bold yellow]Você já tem uma armadura equipada.[/bold yellow]")
            else:
                console.print("[bold red]Você não tem um Capacete no seu inventário.[/bold red]")
        else:
            console.print("[bold red]Item inválido.[/bold red]")
        time.sleep(1.5)

    def desequipar_item(self, item_nome: str):
        """Desequipa um item do jogador."""
        if item_nome == "Cajado Equipado":
            if "Cajado Equipado" in self.inventario:
                self.atk_mana -= 5
                self.inventario.remove("Cajado Equipado")
                self.inventario.append("Cajado")
                console.print(f"[bold green]Você desequipou o Cajado. Seu ataque mágico voltou para {self.atk_mana}[/bold green]")
            else:
                console.print("[bold red]Você não tem um Cajado equipado.[/bold red]")
        elif item_nome == "Espada Equipada":
            if "Espada Equipada" in self.inventario:
                self.atc -= 10
                self.inventario.remove("Espada Equipada")
                self.inventario.append("Espada Longa")
                console.print(f"[bold green]Você desequipou a Espada Longa. Seu ataque voltou para {self.atc}[/bold green]")
            else:
                console.print("[bold red]Você não tem uma Espada Longa equipada.[/bold red]")
        elif item_nome == "Capacete Equipado":
            if "Capacete Equipado" in self.inventario:
                self.max_hp -= 10
                self.hp = min(self.hp, self.max_hp)
                self.inventario.remove("Capacete Equipado")
                self.inventario.append("Capacete")
                console.print(f"[bold green]Você desequipou o Capacete. Seu HP máximo voltou para {self.max_hp}[/bold green]")
            else:
                console.print("[bold red]Você não tem um Capacete equipado.[/bold red]")
        else:
            console.print("[bold red]Item não pode ser desequipado ou não está equipado.[/bold red]")
        time.sleep(1.5)

    def mostrar_inventario(self):
        clear()
        if not self.inventario:
            console.print("[bold yellow]Seu inventário está vazio.[/bold yellow]")
        else:
            table = Table(box=box.HEAVY, style="cyan")
            table.add_column("[bold cyan]Inventário[/bold cyan]")
            for item in self.inventario:
                table.add_row(item)
            console.print(table)

    def exibir_menu_inventario(self):
        """Exibe o menu do inventário e permite ao jogador usar ou desequipar um item."""
        clear()
        if not self.inventario:
            console.print("[bold yellow]Seu inventário está vazio.[/bold yellow]")
            time.sleep(1.5)
            return
        while True:
            clear()
            self.mostrar_inventario()
            console.print("[bold magenta]O que deseja fazer com seu inventário?[/bold magenta]")
            console.print("[1] Usar Item")
            console.print("[2] Desequipar Item") 
            console.print("[3] Sair do Inventário") 
            choice = console.input("[bold blue]Escolha uma opção: [/bold blue]")
            if choice == '1':
                clear()
                if not any(item in ["Poção de HP", "Poção de Mana", "Cajado", "Espada Longa", "Capacete"] for item in self.inventario):
                    console.print("[bold yellow]Você não tem itens utilizáveis (poções ou equipamentos não equipados) no seu inventário.[/bold yellow]")
                    time.sleep(1.5)
                    continue
                console.print("[bold magenta]Seu Inventário:[/bold magenta]")
                utilizable_items = [item for item in self.inventario if item in ["Poção de HP", "Poção de Mana", "Cajado", "Espada Longa", "Capacete"]]
                if not utilizable_items:
                    console.print("[bold yellow]Não há itens para usar no momento.[/bold yellow]")
                    time.sleep(1.5)
                    continue
                for i, item in enumerate(utilizable_items):
                    console.print(f"[{i+1}] {item}")
                item_choice = console.input("[bold blue]Escolha o número do item para usar (ou '0' para cancelar): [/bold blue]")
                try:
                    item_index = int(item_choice) - 1
                    if 0 <= item_index < len(utilizable_items):
                        self.usar_item(utilizable_items[item_index])
                        time.sleep(1.5)
                    elif item_index == -1:
                        console.print("[bold yellow]Ação cancelada.[/bold yellow]")
                        time.sleep(1.5)
                    else:
                        console.print("[bold red]Escolha inválida de item![/bold red]")
                        time.sleep(1.5)
                except ValueError:
                    console.print("[bold red]Entrada inválida![/bold red]")
                    time.sleep(1.5)
            elif choice == '2': 
                clear()
                equipped_items = [item for item in self.inventario if "Equipado" in item]
                if not equipped_items:
                    console.print("[bold yellow]Você não tem itens equipados para desequipar.[/bold yellow]")
                    time.sleep(1.5)
                    continue
                console.print("\n[bold magenta]Itens Equipados:[/bold magenta]")
                for i, item in enumerate(equipped_items):
                    console.print(f"[{i+1}] {item}")
                item_choice = console.input("[bold blue]Escolha o número do item para desequipar (ou '0' para cancelar): [/bold blue]")
                try:
                    item_index = int(item_choice) - 1
                    if 0 <= item_index < len(equipped_items):
                        self.desequipar_item(equipped_items[item_index])
                        time.sleep(1.5)
                    elif item_index == -1:
                        console.print("[bold yellow]Ação cancelada.[/bold yellow]")
                        time.sleep(1.5)
                    else:
                        console.print("[bold red]Escolha inválida de item![/bold red]")
                        time.sleep(1.5)
                except ValueError:
                    console.print("[bold red]Entrada inválida![/bold red]")
                    time.sleep(1.5)

            elif choice == '3':
                console.print("[bold yellow]Saindo do Inventário...[/bold yellow]")
                time.sleep(1)
                break
            else:
                console.print("[bold red]Opção inválida. Por favor, escolha novamente.[/bold red]")
                time.sleep(1.5)

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
        console.print("[2] Mana")
        console.print("[3] Usar Item")
        choice = console.input("[bold blue]Escolha uma ação: [/bold blue]")
        if choice == '1':
            player.attack_enemy(enemy)
        elif choice == '2':
            if player.mana >= 10:
                player.attack_mana(enemy)
                player.mana -= 10
            else:
                console.print("[bold red]Mana insuficiente![/bold red]")
        elif choice == '3':
            player.exibir_menu_inventario()
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
 / \\
| () |
 \\ /
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
    player1.inventario.append("Poção de HP")
    player1.inventario.append("Espada Longa")
    player1.inventario.append("Cajado")

    while True:
        clear()
        console.print("[bold green]Bem-vindo à Aventura![/bold green]")
        console.print("[1] Iniciar Combate")
        console.print("[2] Status do Jogador")
        console.print("[3] Inventário") 
        console.print("[4] Sair do Jogo")
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
            player1.exibir_menu_inventario()
        elif escolha == '4':
            console.print("\n[bold magenta]Obrigado por jogar! Até a próxima![/bold magenta]")
            break
        else:
            console.print("\n[bold red]Opção inválida. Por favor, escolha novamente.[/bold red]")
            time.sleep(1.5)

if __name__ == "__main__":
    menu()
