from rich import print
from rich.table import Table, box
from rich.console import Console
from rich.text import Text 
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
        self.hp_upgrade_cost = 10 
        self.mana_upgrade_cost = 10
        self.atc_upgrade_cost = 10 
        self.atm_upgrade_cost = 10 
        self.equipado = {
            "Arma": None,
            "Cabeça": None,
            "Escudo": None,
            "Peito": None
        }
        self.item_prices = {
            "Poção de HP": 50,
            "Poção de Mana": 50,
            "Cajado": 75,
            "Espada Longa": 75,
            "Capacete": 75,
            "Escudo": 75,
            "Capuz": 75
        }

    def shop(self):
        while True:
            clear()
            table = Table(box=box.HEAVY, style="blue")
            table.add_column(f"[bold #FFD700]Dinheiro: {self.gold}[/bold #FFD700]")
            table.add_row(f"[bold white][1]Comprar\n[2]Vender\n[3]Sair[/bold white]")
            print(table)
            escolha = console.input("O que você quer? ")
            if escolha == '1':
                while True:
                    clear()
                    table = Table(box=box.HEAVY, style="blue")
                    table.add_column(f"[bold #FFD700]Dinheiro: {self.gold}[/bold #FFD700]")
                    table.add_row(f"[bold white]Tipo de itens\n[1]Consumível\n[2]Equipável\n[3]Sair[/bold white]")
                    print(table)
                    escolha_ops = console.input("O que você deseja? ")
                    if escolha_ops == '1':
                        while True:
                            clear()
                            table = Table(box=box.HEAVY, style="blue")
                            table.add_column(f"[bold #FFD700]Dinheiro: {self.gold}[/bold #FFD700]")
                            table.add_row(f"[bold white][1]Poção de HP: 100\n[2]Poção de Mana: 100\n[3]Sair[/bold white]")
                            print(table)
                            escolha_item = console.input("O que você deseja? ")
                            if escolha_item == '1': 
                                cost = 100
                                if self.gold >= cost:
                                    self.inventario.append("Poção de HP")
                                    self.gold -= cost
                                    console.print(f"[bold green]Você comprou uma Poção de HP! Resta {self.gold} ouro.[/bold green]")
                                else:
                                    console.print("[bold red]Você não tem ouro suficiente para comprar uma Poção de HP.[/bold red]")
                                time.sleep(1.5)
                            elif escolha_item == '2':
                                cons = 100
                                if self.gold >= cons:
                                    self.inventario.append('Poção de Mana')
                                    self.gold -= cons
                                    console.print(f"[bold green]Você comprou uma Poção de Mana! Resta {self.gold} ouro.[/bold green]")
                                else:
                                    console.print("[bold red]Você não tem ouro suficiente para comprar uma Poção de Mana.[/bold red]")
                                time.sleep(1.5)
                            elif escolha_item == '3':
                                break
                            else:
                                console.print("[bold red]Opção inválida.[/bold red]")
                                time.sleep(1.5)
                    elif escolha_ops == '2':
                        while True:
                            clear()
                            table = Table(box=box.HEAVY, style="blue")
                            table.add_column(f"[bold #FFD700]Dinheiro: {self.gold}[/bold #FFD700]")
                            table.add_row(f"[bold white][1]Cajado: 150\n[2]Espada Longa: 150\n[3]Capacete: 150\n[4]Escudo: 150\n[5]Capuz: 150\n[6]Sair[/bold white]")
                            print(table)
                            escolha_item1 = console.input("O que você deseja? ")

                            if escolha_item1 == '1':
                                cost = 150
                                if self.gold >= cost:
                                    self.inventario.append('Cajado')
                                    self.gold -= cost
                                    console.print(f"[bold green]Você comprou um Cajado! Resta {self.gold} ouro.[/bold green]")
                                else:
                                    console.print("[bold red]Você não tem ouro suficiente para comprar um Cajado.[/bold red]")
                                time.sleep(1.5)
                            elif escolha_item1 == '2':
                                cost = 150
                                if self.gold >= cost:
                                    self.inventario.append('Espada Longa')
                                    self.gold -= cost
                                    console.print(f"[bold green]Você comprou uma Espada Longa! Resta {self.gold} ouro.[/bold green]")
                                else:
                                    console.print("[bold red]Você não tem ouro suficiente para comprar uma Espada Longa.[/bold red]")
                                time.sleep(1.5)
                            elif escolha_item1 == '3':
                                cost = 150
                                if self.gold >= cost:
                                    self.inventario.append('Capacete')
                                    self.gold -= cost
                                    console.print(f"[bold green]Você comprou um Capacete! Resta {self.gold} ouro.[/bold green]")
                                else:
                                    console.print("[bold red]Você não tem ouro suficiente para comprar um Capacete.[/bold red]")
                                time.sleep(1.5)
                            elif escolha_item1 == '4':
                                cost = 150
                                if self.gold >= cost:
                                    self.inventario.append('Escudo')
                                    self.gold -= cost
                                    console.print(f"[bold green]Você comprou um Escudo! Resta {self.gold} ouro.[/bold green]")
                                else:
                                    console.print("[bold red]Você não tem ouro suficiente para comprar um Escudo.[/bold red]")
                                time.sleep(1.5)
                            elif escolha_item1 == '5':
                                cost = 150
                                if self.gold >= cost:
                                    self.inventario.append('Capuz')
                                    self.gold -= cost
                                    console.print(f"[bold green]Você comprou um Capuz! Resta {self.gold} ouro.[/bold green]")
                                else:
                                    console.print("[bold red]Você não tem ouro suficiente para comprar um Capuz.[/bold red]")
                                time.sleep(1.5)
                            elif escolha_item1 == '6':
                                break
                            else:
                                console.print("[bold red]Opção inválida.[/bold red]")
                                time.sleep(1.5)
                    elif escolha_ops == '3':
                        break
                    else:
                        console.print("[bold red]Opção inválida.[/bold red]")
                        time.sleep(1.5)
            elif escolha == '2':
                if not self.inventario:
                    console.print("[bold yellow]Seu inventário está vazio. Não há nada para vender.[/bold yellow]")
                    time.sleep(1.5)
                    continue
                while True:
                    clear()
                    table = Table(box=box.HEAVY, style="yellow")
                    table.add_column(f"[bold #FFD700]Seu Dinheiro: {self.gold}[/bold #FFD700]")
                    table.add_column("[bold cyan]Itens no Inventário[/bold cyan]", vertical="top")
                    table.add_column("[bold green]Preço de Venda[/bold green]", vertical="top")
                    if not self.inventario:
                        table.add_row("[bold yellow]Inventário Vazio[/bold yellow]", "", "")
                    else:
                        for i, item in enumerate(sorted(set(self.inventario))):  
                            count = self.inventario.count(item)
                            sell_price = self.item_prices.get(item, 0)
                            table.add_row(f"[{i+1}] {item} (x{count})", f"{item}", f"[bold green]{sell_price}[/bold green] ouro")
                    console.print(table)
                    console.print("\n[bold white][0] Voltar[/bold white]")
                    sell_choice = console.input("Qual item você gostaria de vender? (Digite o número) ")
                    if sell_choice == '0':
                        break
                    try:
                        sell_index = int(sell_choice) - 1
                        unique_items = sorted(list(set(self.inventario)))
                        if 0 <= sell_index < len(unique_items):
                            item_to_sell = unique_items[sell_index]
                            if item_to_sell in self.inventario:
                                sell_price = self.item_prices.get(item_to_sell)
                                if sell_price is not None:
                                    self.inventario.remove(item_to_sell)
                                    self.gold += sell_price
                                    console.print(f"[bold green]Você vendeu {item_to_sell} por {sell_price} ouro. Você agora tem {self.gold} ouro.[/bold green]")
                                else:
                                    console.print(f"[bold red]Não é possível vender {item_to_sell}. Preço de venda não definido.[/bold red]")
                            else:
                                console.print("[bold red]Item não encontrado no seu inventário.[/bold red]")
                        else:
                            console.print("[bold red]Escolha inválida de item.[/bold red]")
                        time.sleep(1.5)
                    except ValueError:
                        console.print("[bold red]Entrada inválida. Por favor, digite um número.[/bold red]")
                        time.sleep(1.5)
            elif escolha == '3':
                console.print("[bold white]Saindo da loja.[/bold white]")
                time.sleep(1)
                break
            else:
                console.print("[bold red]Opção inválida. Por favor, escolha 1, 2 ou 3.[/bold red]")
                time.sleep(1.5)

    def up(self):
        if not self.xp:
            console.print("[bold yellow]Você não tem XP para melhoria.[/bold yellow]")
            time.sleep(1.5)
            return
        while True:
            clear()
            table = Table(box=box.HEAVY, style="green")
            table.add_column(f"[bold #EE82EE]Seu XP: {self.xp}[/bold #EE82EE]")
            table.add_row(f"[bold green][1]HP (Custo: {self.hp_upgrade_cost})[/bold green]")
            table.add_row(f"[bold blue][2]Mana (Custo: {self.mana_upgrade_cost})[/bold blue]")
            table.add_row(f"[bold red][3]Ataque (Custo: {self.atc_upgrade_cost})[/bold red]")
            table.add_row(f"[bold #7B68EE][4]Mana/Ataque (Custo: {self.atm_upgrade_cost})[/bold #7B68EE]")
            table.add_row(f'[bold white][5]Sair[/bold white]')
            print(table)
            escolha = console.input("Escolha o que você quer melhorar? ")
            if escolha == '1':
                if self.xp >= self.hp_upgrade_cost:
                    self.xp -= self.hp_upgrade_cost
                    self.max_hp += 10 
                    self.hp = self.max_hp 
                    self.hp_upgrade_cost = int(self.hp_upgrade_cost * 1.5) 
                    console.print("[bold green]HP melhorado com sucesso![/bold green]")
                else:
                    console.print(f"[bold yellow]XP insuficiente! Você precisa de {self.hp_upgrade_cost} XP.[/bold yellow]")
                time.sleep(1.5)
            elif escolha == '2':
                if self.xp >= self.mana_upgrade_cost:
                    self.xp -= self.mana_upgrade_cost
                    self.max_mana += 5
                    self.mana = self.max_mana 
                    self.mana_upgrade_cost = int(self.mana_upgrade_cost * 1.5) 
                    console.print("[bold green]Mana melhorada com sucesso![/bold green]")
                else:
                    console.print(f"[bold yellow]XP insuficiente! Você precisa de {self.mana_upgrade_cost} XP.[/bold yellow]")
                time.sleep(1.5)
            elif escolha == '3': 
                if self.xp >= self.atc_upgrade_cost:
                    self.xp -= self.atc_upgrade_cost
                    self.atc += 2
                    self.atc_upgrade_cost = int(self.atc_upgrade_cost * 1.5)
                    console.print("[bold green]Ataque melhorado com sucesso![/bold green]")
                else:
                    console.print(f"[bold yellow]XP insuficiente! Você precisa de {self.atc_upgrade_cost} XP.[/bold yellow]")
                time.sleep(1.5)
            elif escolha == '4': 
                if self.xp >= self.atm_upgrade_cost:
                    self.xp -= self.atm_upgrade_cost
                    self.atk_mana += 3
                    self.atm_upgrade_cost = int(self.atm_upgrade_cost * 1.5) 
                    console.print("[bold green]Mana/Ataque melhorado com sucesso![/bold green]")
                else:
                    console.print(f"[bold yellow]XP insuficiente! Você precisa de {self.atm_upgrade_cost} XP.[/bold yellow]")
                time.sleep(1.5)
            elif escolha == '5':
                console.print("[bold white]Saindo do menu de melhorias.[/bold white]")
                time.sleep(1)
                break
            else:
                console.print("[bold red]Opção inválida. Por favor, escolha um número de 1 a 5.[/bold red]")
                time.sleep(1.5)
                
    def status(self):
        """Exibe o status detalhado do jogador, incluindo itens equipados."""
        clear()
        table = Table(box=box.HEAVY, style="blue")
        table.add_column(f"Nome: [bold white]{self.nome}[/bold white]")
        table.add_row(f"HP: [#00FF00]{self.hp}[/#00FF00]/[#00FF00]{self.max_hp}[/#00FF00]")
        table.add_row(f"Mana: [#7B68EE]{self.mana}[/#7B68EE]/[#7B68EE]{self.max_mana}[/#7B68EE]")
        table.add_row(f"Ataque: [#FF0000]{self.atc}[/#FF0000]")
        table.add_row(f"Ataque Mágico: [#7B68EE]{self.atk_mana}[/#7B68EE]")
        table.add_row(f"Ouro: [#FFFF00]{self.gold}[/#FFFF00]")
        table.add_row(f"XP: [#4B0082]{self.xp}[/#4B0082]")
        equipped_items_str = ", ".join([f"{slot}: {item if item else 'Nenhum'}" for slot, item in self.equipado.items()])
        table.add_row(f"Equipado: [bold yellow]{equipped_items_str}[/bold yellow]")
        console.print(table)
        console.input("\n[bold magenta]Pressione Enter para continuar...[/bold magenta]")

    def batalha_info(self):
        """Exibe informações do jogador específicas para a batalha."""
        table = Table(box=box.HEAVY, style='blue')
        table.add_column(f"Nome: [bold white]{self.nome}[/bold white]")
        table.add_row(f"HP: [#00FF00]{self.hp}[/#00FF00]/[#00FF00]{self.max_hp}[/#00FF00]")
        table.add_row(f"Mana: [#7B68EE]{self.mana}[/#7B68EE]/[#7B68EE]{self.max_mana}[/#7B68EE]")
        table.add_row(f"Ataque: [#FF0000]{self.atc}[/#FF0000]")
        table.add_row(f"Ataque Mágico: [#7B68EE]{self.atk_mana}[/#7B68EE]") 
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
            console.print(f"[bold green]{self.nome} atacou {enemy.name} e causou {damage} de dano com magia![/bold green]")
        else:
            console.print(f"[bold yellow]{self.nome} errou o ataque mágico em {enemy.name}![/bold yellow]")

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
                if self.equipado["Arma"] is None:
                    self.atk_mana += 5 
                    self.inventario.remove("Cajado")
                    self.equipado["Arma"] = "Cajado"
                    console.print(f"[bold green]Você equipou o Cajado e seu ataque mágico aumentou para {self.atk_mana}![/bold green]")
                else:
                    console.print(f"[bold yellow]Você já tem {self.equipado['Arma']} equipado. Desequipe-o primeiro para equipar o Cajado.[/bold yellow]")
            else:
                console.print("[bold red]Você não tem um Cajado no seu inventário.[/bold red]")
        elif item_nome == "Espada Longa":
            if "Espada Longa" in self.inventario:
                if self.equipado["Arma"] is None:
                    self.atc += 10    
                    self.inventario.remove("Espada Longa")
                    self.equipado["Arma"] = "Espada Longa"
                    console.print("[bold green]Você equipou a Espada Longa e seu ataque aumentou em 10![/bold green]")
                else:
                    console.print(f"[bold yellow]Você já tem {self.equipado['Arma']} equipado. Desequipe-o primeiro para equipar a Espada Longa.[/bold yellow]")
            else:
                console.print("[bold red]Você não tem uma Espada Longa no seu inventário.[/bold red]")
        elif item_nome == 'Capacete':
            if "Capacete" in self.inventario:
                if self.equipado["Cabeça"] is None:
                    self.max_hp += 10 
                    self.hp = self.max_hp 
                    self.inventario.remove("Capacete")
                    self.equipado["Cabeça"] = "Capacete"
                    console.print("[bold green]Você equipou o Capacete e seu HP máximo aumentou em 10![/bold green]")
                else:
                    console.print(f"[bold yellow]Você já tem {self.equipado['Cabeça']} equipado. Desequipe-o primeiro para equipar o Capacete.[/bold yellow]")
            else:
                console.print("[bold red]Você não tem um Capacete no seu inventário.[/bold red]")
        elif item_nome == 'Escudo': 
            if "Escudo" in self.inventario:
                if self.equipado["Escudo"] is None:
                    self.max_hp += 5 
                    self.hp = min(self.hp, self.max_hp) 
                    self.inventario.remove("Escudo")
                    self.equipado["Escudo"] = "Escudo"
                    console.print("[bold green]Você equipou o Escudo e seu HP máximo aumentou em 5![/bold green]")
                else:
                    console.print(f"[bold yellow]Você já tem {self.equipado['Escudo']} equipado. Desequipe-o primeiro para equipar o Escudo.[/bold yellow]")
            else:
                console.print("[bold red]Você não tem um Escudo no seu inventário.[/bold red]")
        elif item_nome == 'Capuz':
            if "Capuz" in self.inventario:
                if self.equipado["Cabeça"] is None:
                    self.max_hp += 5
                    self.max_mana += 5
                    self.hp = self.max_hp 
                    self.inventario.remove("Capuz")
                    self.equipado["Cabeça"] = "Capuz"
                    console.print("[bold green]Você equipou o Capuz e seu HP máximo aumentou em 5 e sua mana máximo aumentou em 5![/bold green]")
                else:
                    console.print(f"[bold yellow]Você já tem {self.equipado['Cabeça']} equipado. Desequipe-o primeiro para equipar o Capuz.[/bold yellow]")
            else:
                console.print("[bold red]Você não tem um Capuz no seu inventário.[/bold red]")
        elif item_nome == 'Peitoral':
            if "Peitoral" in self.inventario:
                if self.equipado["Peito"] is None:
                    self.max_hp += 25
                    self.hp = self.max_hp 
                    self.inventario.remove("Peitoral")
                    self.equipado["Peito"] = "Peitoral"
                    console.print("[bold green]Você equipou o Peitoral e seu HP máximo aumentou em 25![/bold green]")
                else:
                    console.print(f"[bold yellow]Você já tem {self.equipado['Peito']} equipado. Desequipe-o primeiro para equipar o Peitoral.[/bold yellow]")
            else:
                console.print("[bold red]Você não tem um Peitoral no seu inventário.[/bold red]")
        else:
            console.print("[bold red]Item inválido ou não utilizável desta forma.[/bold red]")
        time.sleep(1.5)

    def desequipar_item(self, item_nome: str):
        if item_nome == "Cajado": 
            if self.equipado["Arma"] == "Cajado":
                self.atk_mana -= 5
                self.inventario.append("Cajado")
                self.equipado["Arma"] = None
                console.print(f"[bold green]Você desequipou o Cajado. Seu ataque mágico voltou para {self.atk_mana}[/bold green]")
            else:
                console.print("[bold red]Você não tem um Cajado equipado.[/bold red]")
        elif item_nome == "Espada Longa":
            if self.equipado["Arma"] == "Espada Longa":
                self.atc -= 10
                self.inventario.append("Espada Longa")
                self.equipado["Arma"] = None
                console.print(f"[bold green]Você desequipou a Espada Longa. Seu ataque voltou para {self.atc}[/bold green]")
            else:
                console.print("[bold red]Você não tem uma Espada Longa equipada.[/bold red]")
        elif item_nome == "Capacete":
            if self.equipado["Cabeça"] == "Capacete":
                self.max_hp -= 10
                self.hp = min(self.hp, self.max_hp) 
                self.inventario.append("Capacete")
                self.equipado["Cabeça"] = None
                console.print(f"[bold green]Você desequipou o Capacete. Seu HP máximo voltou para {self.max_hp}[/bold green]")
            else:
                console.print("[bold red]Você não tem um Capacete equipado.[/bold red]")
        elif item_nome == "Escudo":
            if self.equipado["Escudo"] == "Escudo":
                self.max_hp -= 5
                self.hp = min(self.hp, self.max_hp) 
                self.inventario.append("Escudo")
                self.equipado["Escudo"] = None
                console.print(f"[bold green]Você desequipou o Escudo. Seu HP máximo voltou para {self.max_hp}[/bold green]")
            else:
                console.print("[bold red]Você não tem um Escudo equipado.[/bold red]")
        elif item_nome == "Capuz":
            if self.equipado["Cabeça"] == "Capuz":
                self.max_hp -= 5
                self.max_mana -= 5
                self.hp = min(self.hp, self.max_hp) 
                self.inventario.append("Capuz")
                self.equipado["Cabeça"] = None
                console.print(f"[bold green]Você desequipou o Capuz. Seu HP máximo voltou para {self.max_hp} e sua mana máxima voltou para {self.max_mana}[/bold green]")
            else:
                console.print("[bold red]Você não tem um Capuz equipado.[/bold red]")     
        elif item_nome == "Peitoral":
            if self.equipado["Cabeça"] == "Peitoral":
                self.max_hp -= 25
                self.hp = min(self.hp, self.max_hp) 
                self.inventario.append("Peitoral")
                self.equipado["Peito"] = None
                console.print(f"[bold green]Você desequipou o Peitoral. Seu HP máximo voltou para {self.max_hp}[/bold green]")
            else:
                console.print("[bold red]Você não tem um Peitoral equipado.[/bold red]")   
        else:
            console.print("[bold red]Item não pode ser desequipado ou não está equipado neste slot.[/bold red]")
        time.sleep(1.5)

    def mostrar_inventario(self):
        console.clear()
        inventory_empty = not self.inventario
        equipped_empty = all(value is None for value in self.equipado.values())
        if inventory_empty and equipped_empty:
            console.print("[bold yellow]Seu inventário e seus slots de equipamento estão vazios.[/bold yellow]")
            return
        table = Table(box=box.HEAVY, style="cyan", show_header=True)
        table.add_column("[bold cyan]Inventário[/bold cyan]", vertical="top")
        table.add_column("[bold magenta]Itens Equipados[/bold magenta]", vertical="top")

        equipped_list = []
        for slot, item in self.equipado.items():
            if item:
                equipped_list.append(f"{slot}: {item}")
            else:
                equipped_list.append(f"{slot}: [green]Nenhum[/green]")
        max_rows = max(len(self.inventario), len(equipped_list))
        for i in range(max_rows):
            inventory_item = self.inventario[i] if i < len(self.inventario) else Text("")
            equipped_item = equipped_list[i] if i < len(equipped_list) else ""
            table.add_row(inventory_item, equipped_item)

        console.print(table)

    def exibir_menu_inventario(self):
        """Exibe o menu do inventário e permite ao jogador usar ou desequipar um item."""
        while True:
            clear()
            self.mostrar_inventario()
            console.print("\n[bold magenta]O que deseja fazer com seu inventário?[/bold magenta]")
            console.print("[1] Usar Item")
            console.print("[2] Desequipar Item") 
            console.print("[3] Sair do Inventário") 
            choice = console.input("[bold blue]Escolha uma opção: [/bold blue]")
            if choice == '1':
                clear()
                utilizable_items = [item for item in self.inventario if item in ["Poção de HP", "Poção de Mana", "Cajado", "Espada Longa", "Capacete", "Escudo", 'Capuz', 'Peitoral']]
                if not utilizable_items:
                    console.print("[bold yellow]Você não tem itens utilizáveis (poções ou equipamentos não equipados) no seu inventário.[/bold yellow]")
                    time.sleep(1.5)
                    continue
                console.print("[bold magenta]Seu Inventário (Itens Utilizáveis):[/bold magenta]")
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
                equipped_items_list = []
                for slot, item in self.equipado.items():
                    if item:
                        equipped_items_list.append(item)
                if not equipped_items_list:
                    console.print("[bold yellow]Você não tem itens equipados para desequipar.[/bold yellow]")
                    time.sleep(1.5)
                    continue
                console.print("\n[bold magenta]Itens Equipados:[/bold magenta]")
                for i, item in enumerate(equipped_items_list):
                    console.print(f"[{i+1}] {item}")
                item_choice = console.input("[bold blue]Escolha o número do item para desequipar (ou '0' para cancelar): [/bold blue]")
                try:
                    item_index = int(item_choice) - 1
                    if 0 <= item_index < len(equipped_items_list):
                        self.desequipar_item(equipped_items_list[item_index])
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
        console.print("[1] Atacar (Físico)")
        console.print("[2] Atacar (Mágico - Custo: 10 Mana)")
        console.print("[3] Usar Poção")
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
            clear()
            utilizable_items_combat = [item for item in player.inventario if item in ["Poção de HP", "Poção de Mana"]]
            
            if not utilizable_items_combat:
                console.print("[bold yellow]Você não tem poções para usar no momento.[/bold yellow]")
                time.sleep(1.5)
                continue
            console.print("[bold magenta]Seu Inventário (Poções):[/bold magenta]")
            for i, item in enumerate(utilizable_items_combat):
                console.print(f"[{i+1}] {item}")
            item_choice_combat = console.input("[bold blue]Escolha o número da poção para usar (ou '0' para cancelar): [/bold blue]")
            try:
                item_index_combat = int(item_choice_combat) - 1
                if 0 <= item_index_combat < len(utilizable_items_combat):
                    player.usar_item(utilizable_items_combat[item_index_combat])
                    time.sleep(1.5)
                elif item_index_combat == -1:
                    console.print("[bold yellow]Ação cancelada.[/bold yellow]")
                    time.sleep(1.5)
                else:
                    console.print("[bold red]Escolha inválida de item![/bold red]")
                    time.sleep(1.5)
            except ValueError:
                console.print("[bold red]Entrada inválida![/bold red]")
                time.sleep(1.5)

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
 /\
(oo)
 \/
 ''',
        '''
    /\
   (..)/
    VV
 ''',
        '''
 ^ ^
(o o)
 /V\
 ''',
        '''
 .---.
/   \\
|   |
 \ /
  `---'
 ''',
        '''
    O O
   / V \
    \_U_/
 '''
        ]
        nome_aleatorio = random.choice(nomes)
        ascii_aleatorio = random.choice(ascii_arts)
        hp_aleatorio = random.randint(30, 100)
        atk_aleatorio = random.randint(5, 15)
        xp_aleatorio = random.randint(100, 300)
        gold_aleatorio = random.randint(1, 100)
        return Inimigo(nome_aleatorio, hp_aleatorio, atk_aleatorio, xp_aleatorio, gold_aleatorio, ascii_aleatorio)
    clear()
    nome = console.input("[bold blue]Digite o nome do seu jogador: [/bold blue]")
    player1 = Jogador(nome, max_hp=100, atc=15, max_mana=50, atm=25, gold=250, xp=20)
    player1.inventario.append("Poção de HP")
    player1.inventario.append("Poção de Mana")
    player1.inventario.append("Cajado")
    player1.inventario.append("Capacete")
    player1.inventario.append("Espada Longa")
    player1.inventario.append("Escudo")
    player1.inventario.append('Peitoral')

    while True:
        clear()
        console.print("[bold green]Bem-vindo à Aventura![/bold green]")
        console.print("[1] Iniciar Combate")
        console.print("[2] Status do Jogador")
        console.print("[3] Inventário") 
        console.print("[4] Melhorias")
        console.print("[5] Shop")
        console.print("[6] Sair do Jogo")
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
            player1.up()
        elif escolha == '5':
            player1.shop()
        elif escolha == '6':
            console.print("\n[bold magenta]Obrigado por jogar! Até a próxima![/bold magenta]")
            break
        else:
            console.print("\n[bold red]Opção inválida. Por favor, escolha novamente.[/bold red]")
            time.sleep(1.5)

if __name__ == "__main__":
    menu()