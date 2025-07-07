from rich import print
from rich.table import Table, box
from rich.console import Console
from rich.text import Text
import os
def clear():
    """Limpa a tela do console."""
    os.system('cls' if os.name == 'nt' else 'clear')

console = Console()
class art_ascii:
    def __init__(self):
        m = '[bold green]#[/bold green]'
        a = '[bold #2F4F4F]*[/bold #2F4F4F]'
        c = '[bold magenta]CASA[/bold magenta]'
        s = '[bold blue]SHOP[/bold blue]'
        h = '[bold red]Hospital[/bold red]'
        t = '[bold #8B4513]![/bold #8B4513]'
        u = '[bold red]^[/bold red]'
        b = '[bold red]>[/bold red]'
        d = '[bold #7CFC00]:[/bold #7CFC00]'
        w = '[bold blue]=[/bold blue]'
        p = '[bold #FFA500]-=[/bold #FFA500]'
        r = '[bold yellow]*[/bold yellow]'
        q = '[bold #00FFFF]-[/bold #00FFFF]'
        y = '[bold blue]=[/bold blue]'
        x = '[bold white]_[/bold white]'
        f = '[bold #2F4F4F]/\ '
        z = '[bold #8B4513]|| [/bold #8B4513]'
        self.casa = f'''        `'::.
    _________H ,%%&%,
   /\     _   \%&&%%&%
  /  \___/^\___\%&%%&&
  |  | []   [] |%\Y&%'
  |  |   .-.   | ||  
~~@._|@@_|||_@@|~||~~~~~~~~~~~~~
     `""") )"""`'''
        self.c00 = '''[1]Descansar [2]Andar
Faça sua escolha:'''
        self.dialogo = f'''Olá Jovem rapaz vi sua nobre ação
e lhe darei uma ajuda com um pouco
de Refrigetante para te ajudar 
a pecuperar sua istamina
Precione Enter:'''
        self.art1 = '''                .----.
    .---------. | == | 
    |.-"""""-.| |----| 
    ||       || | == | 
    ||       || |----| 
    |'-.....-'| |::::| 
    `"")---(""` |___.| 
  /:::::::::::\" _  " 
 /:::=======:::\`\`\ 
`"""""""""""""`  '-' 
'''
        self.escola= '''    \_/
  --(_)--  .
    / \   /_\ 
          |Q| 
    .-----' '-----.             __
   /____[Escola]___\           ()))
    | [] .-.-. [] |           (((())
  ..|____|_|_|____|.............)(... '''
        self.escolha1= '''[1]Conversar [2]Andar
Faça sua escolha:'''
        self.professor = '''Você pode Levar um livro Jovem
ira te ajudar muito em sua 
Jornada para nos ajudar
Precione Enter: '''
        self.casa24 = '''    `'::::.
     _____A_  
    /      /\          
 __/__/\__/  \___      
/__|" '' "| /___/\   
|''|"'||'"| |' '||      
   `""`""))""`"`""""`'''
        self.dialogo1 = '''[yellow]NÃO TEM NINGUEM EM CASA:
Precione enter:[/yellow]'''
        self.pc = f'''URGENTE!! Uma nova variante dos 
mosquitos da dengue vem surgundo
dos lugares mais remotos do Brasil
Uma grande lago que foi poluido
pelas grades corpoorações e popolação
Você lendo isso nem se preocupa com
isso e decide continuar sentado
PRECIONE ENTER:'''
        self.pc1= f'''Essa Variante de mosquitos são maiores
mais fortes e estão se reproduzindo 
mais rapido e cada dia estão mais 
agrecivos e estão invadindo as cidades
do Brasil todo e em alguns mês podem
dominar o Brasil depois o mundo
PRECIONE ENTER:'''
        self.sair = '''  __                   ___       
 |""|  ___    _   __  |"""|  __  
 |""| |"""|  |"| |""| |"""| |""| 
 |""| |"""|  |"| |""| |"""| |""| 
 |""| |"""|  |"| |""| |"""| |""| 
 """"""""""""""""""""""""""""""""" '''     
        self.andar = '''
Você decide sair um pouco de casa para 
tentar sequeser os problemas de sua 
vida e do mundo atual e suspira e 
você vê um  desses tais mosquitos  
geneticamente modificados atacando 
uma senhoria e você deside agir'''
        self.andar2 = '''Após derrotar o Mosquito a senhora
te agradesse te dando uma pomada
de regeneração para te ajudar 
não sua missão que você agora 
está sem mesmo nem ter persebido
PRECIONE ENTER:'''
        self.ops = '''
Você Agradece e começa ver sua 
cidade oque você vai fazer agora?
Digito de Açôes do perssonagem
[1]Andar [2]Menu [3]Sair'''
        self.ops2 = '''
[1]Status   [2]Inventario
[3]Melorias [4]Sair
'''
        self.cidade1 = f'''⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿[blue][Rota:[/blue][white] 01][/white]⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿[#FFFF00]++++++++++++++++[/#FFFF00][green]##[#7CFC00]::[/#7CFC00]#####[/green][#8B4513]!!!!!!!!!!!!!![/#8B4513]⣿
⣿[red]++++++++++++++++[/red][green]##[#7CFC00]::[/#7CFC00]#############[/green][#00BFFF]-=-=-=[/#00BFFF]⣿
⣿[#00BFFF]=-=-=-=-=-[/#00BFFF][magenta][CASA:00][/magenta][#7CFC00]::[/#7CFC00][green]#####[/green][blue][ESCOLA][/blue][green]##[/green][blue]-=-[/blue]⣿
⣿[#00BFFF]=-=-=-=-[/#00BFFF][green]####[#7CFC00]::[/#7CFC00]####[/green][#7CFC00]:::::::::::::::::[/#7CFC00][green]#[/green][#00BFFF]=-=[/#00BFFF]⣿
⣿[#8B4513]!!!!!!!!!!!![/#8B4513][#7CFC00]::::::::[/#7CFC00][green]#############[/green][#7CFC00]::[/#7CFC00][#8B4513]!!!![/#8B4513]⣿
⣿[#FFFF00][Casa:24][/#FFFF00][#7CFC00]::::::::[/#7CFC00][green]###################[#7CFC00]::[/#7CFC00]#[/green]⣿
⣿[#8B4513]!!!!!!!!!!!!!!!!!!!!!!!![/#8B4513][green]###[magenta][CASA:01][/magenta]###[/green]⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿'''
        self.c1 = '''[1]Casa:00 [2]Casa:01
[3]Rota:01 [4]Escola
[5]Casa:24 [6]Menu
Faça sua escolha:'''
        self.rota01 = '''[bold]⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿[bold #4B0082][Cidade2:][/bold #4B0082]⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿[/bold]
[bold]⣿[green]######[#7CFC00]:::::::::>>>^::::::::::[/#7CFC00]##########[/green]⣿⣿[/bold]
[bold]⣿[green]#####[#7CFC00]::::::::::^:::::[/#7CFC00]#####[#7CFC00]:::[/#7CFC00][#00008B]=-=-=-=-=[/#00008B]#[/green]⣿⣿[/bold]
[bold]⣿[green]###[ROTA: 05][#7CFC00]::^[ROTA: 01]:::[/#7CFC00][#00008B]=-=-=-=-[/#00008B]##[/green]⣿⣿[/bold]
[bold]⣿[green]####[#00008B]=-=-=-=-=-[/#00008B]#^[#7CFC00]:::::[/#7CFC00]#####[#7CFC00]:::[/#7CFC00][ROTA: 02][/green]⣿⣿[/bold]
[bold]⣿[green]#####[#00008B]=-=-=-=-=[/#00008B]#^#######################[/green]⣿⣿[/bold]
[bold]⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿[bold #4B0082][Cidade1:][/bold #4B0082]⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿[/bold]'''
        self.rota01_ops = '''[1]Batalhar [2]Explorar
[3]Cidade:1 [4]Cidade:2
[5]Menu
Faça sua escolha:'''
        self.cidade2= f'''[bold]⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿[#00FFFF][Labirinto:][/#00FFFF]⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿[green]########################################[/green]⣿
⣿[green]#############[#2F4F4F]*************[/#2F4F4F]##############[/green]⣿
⣿[bold blue][SHOP][/bold blue][#7CFC00]::::::::[/#7CFC00][#8B4513]!!!!!!!!!![/#8B4513][#2F4F4F]***********[/#2F4F4F][green]#####[/green]⣿
⣿[#7CFC00]::::::::[/#7CFC00][#2F4F4F]*****[/#2F4F4F][#7CFC00]:::::::::::::[/#7CFC00][bold red][HOSPITAL][/bold red][green]####[/green]⣿
⣿[green]########################[/green][#7CFC00]::::::[/#7CFC00][#8B4513]!!!!!!!!!![/#8B4513]⣿
⣿[green]#######################[/green][bold magenta][CASA:21][/bold magenta][#7CFC00]::::::::[/#7CFC00]⣿
⣿[bold blue]=-=-=-=-=-=-=-[/bold blue][#8B4513]!!!!!!!!!!!!!!!!!!!!!!!!!![/#8B4513]⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿[#00FFFF][Rota: 01][/#00FFFF]⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿[/bold]'''
        self.c2 = '''[1]Rota:01  [2]Shop
[3]Hospital [4]Labirinto
[5]Casa     [6]Menu
Faça sua escolha:'''
        self.pers = '''  o
 /|\ 
 / \ '''
        self.menu = '''[1]Status     [2]UP
[3]Inventario [4]Sair
Faça sua escolha:'''
        self.chaves = '''Está trancada pelo visto preciso
de uma chave para abrir
Precione enter:'''
        self.labirinto= f'''⣿[magenta][Cidade:3][/magenta]⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿[green]#[red]^^[/red]#######################################[/green]⣿
⣿[#8B4513]![red]^^[/red]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!![/#8B4513]⣿
⣿#[red]<<<<<<<<<<<<<<<<<<<<<<<<^^>>>>>>>>>>>>>>?[/red]⣿
⣿[#2F4F4F]*************************[red]^^[/red]***************[/#2F4F4F]⣿
⣿[#2F4F4F]*************************[red]^^[/red]***************[/#2F4F4F]⣿
⣿[#8B4513]!!!!!!!!!!!!!!!!!!!!!!!!![red]^^[/red]!!!!!!!!!!!!!!![/#8B4513]⣿
⣿[green]#########################[red]^^[/red]###############[/green]⣿
⣿[#7CFC00]?::::::::::::::::::::::[/#7CFC00]====[green]###############[/green]⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿[magenta][Baixo][/magenta]⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿'''
        self.labirinto1 = f'''⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿[Cima]⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿[green]##############^^##########################[/green]⣿
⣿[#2F4F4F]**************[/#2F4F4F][red]^^[/red][green]#############[/green][#2F4F4F]*************[/#2F4F4F]⣿
⣿[#2F4F4F]**************[/#2F4F4F][red]^^[/red][green]#############[/green][#2F4F4F]*************[/#2F4F4F]⣿
⣿[#8B4513]!!!!!!!!!!!!!![red]^^<<<<<<<<<<<<<[/red]!!!!!!!!!!!!![/#8B4513]⣿
⣿[#7CFC00]?::::::::::::::::::::::::::[/#7CFC00][red]^^[/red][#7CFC00]::[/#7CFC00][green]###########[/green]⣿
⣿[#2F4F4F]************[/#2F4F4F][#7CFC00]::[/#7CFC00][green]######[/green][red]>>>>>>>^^[/red][#7CFC00]:::::::::[/#7CFC00][#2F4F4F]****[/#2F4F4F]⣿
⣿[#2F4F4F]************[/#2F4F4F][#7CFC00]::[/#7CFC00][green]######[/green][red]^^[/red][#2F4F4F]**************[#7CFC00]::[/#7CFC00]****[/#2F4F4F]⣿
⣿[#8B4513]!!!!!!!!!!!![#7CFC00]::::::::[/#7CFC00][red]^^[/red]!!!!!!!!!!!!!![#7CFC00]:?[/#7CFC00]!!!![/#8B4513]⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿[Cidade:02]⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿'''
        self.labirinto1_ops ='''[1]Cima     [2]Cidade:02
[3]Explorar [4]Batalhar
[5]Menu'''
        self.labirinto_ops= '''[1]Baixo    [2]Cidade:03
[3]Explorar [4]Batalhar
[5]Menu'''
        self.ex = '''[1]? [2]Andar
[3]? [4]Menu
Faça sua escolha:'''
        self.interrogação = '''    ______    
   / _ __ `. 
  |_/____) |  
    /  ___.'  
    |_|       
    (_)     '''
        self.explorar = '''[1]Explorar [2]Andar
[3]Menu
Faça sua escolha:'''
        self.cidade3 = f'''⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}⣿
⣿{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}{t}⣿
⣿{a}{a}{c}:11{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}⣿
⣿{t}{t}{d}{d}{d}{d}{d}{d}{d}{d}{d}{w}{q}{w}{q}{w}{q}{w}{q}{w}{q}{w}{q}{w}{q}{w}{q}{w}{q}{w}{q}{w}{q}{w}{q}{w}{q}{m}{m}{m}{m}{m}⣿
⣿{m}{m}{d}{d}{b}{b}{b}{b}{b}{b}{b}{b}{b}{w}{q}{w}{q}{w}{q}{w}{q}Lago:{w}{q}{w}{q}{w}{q}{w}{q}{w}{m}{m}{m}{m}{m}{m}{m}⣿
⣿{m}{m}{d}{d}{s}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{h}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}⣿
⣿{m}{m}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{d}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}⣿
⣿{m}{m}{d}{d}{c}:13{m}{m}Ponte:{p}{p}{p}{p}{p}{p}{p}{p}{p}{p}{p}{m}⣿
⣿⣿[red]Labirinto[/red]⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿'''
        self.ops_c3 = '''[1]Casa:11   [2]Casa:13
[3]SHOP      [4]Hospital
[5]Lago      [6]Ponte
[7]Labirinto [8]Menu
Faça sua escolha:'''
        self.casa11 = '''[bold yellom]wOlha Rapaz! Bem os Lagos no mapa
indica onde ficam os Grandes 
Chefes Mosquitos derrote os
8 e volte para a cidade Harley
e entre na casa da cidade
para desbloquear o final[/bold yellom]'''
        self.casa13 = '''Não tem ninguem em casa '''
        self.lagos = f''' {f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}
 {f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}
 {z}{z}{z}{z}{z}{z}{z}{z}{z}{z}{z}{z}{z}{z}
{m}{r}{r}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{r}{r}{m}
{m}{r}{r}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{r}{r}{m}
{m}{r}{r}{r}{y}{x}{y}{x}{y}{x}{y}{y}{x}{y}{x}{y}{x}{y}{y}{x}{y}{x}{y}{x}{y}{y}{x}{y}{x}{y}{x}{y}{y}{x}{y}{x}{y}{x}{y}{r}{r}{r}{m}
{m}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{m}
{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}{m}'''
        self.lago_ops1 = '''Aqui fica o primeito grande 
Chefe dos Moquitos o nome 
dele é Aedes Aegypti
Você quer batalhar contra
[1]SIM     [2]NÃO'''
art = art_ascii()
class art_ascii2:
    def __init__(self):
        t = '[bold #FFA500]⣿[/bold #FFA500]'
        u = '[bold black]⣿[/bold black]'
        y = '[bold blue]=[/bold blue]'
        x = '[bold white]_[/bold white]'
        w = '[bold white]-[/bold white]'
        r = '[bold yellow]*[/bold yellow]'
        e = '[bold #8B4513]|[/bold #8B4513]'
        f = '[bold #2F4F4F]/\ '
        z = '[bold #8B4513]|| [/bold #8B4513]'
        hospital = '[bold red]Hospital[/bold red]'
        shop = '[bold blue]SHOP[/bold blue]'
        self.ponte = f''' {f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}
 {f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}{f}
 {z}{z}{z}{z}{z}{z}{z}{z}{z}{z}{z}{z}{z}{z}
{e}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{w}{e}
{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}
{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}{t}{u}
{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}'''
        self.ponte_ops = '''[1]Cidade:03 [2]Cidade:04
Faça sua escolha:'''
        self.cidade4 = f'''
⣿Ponte⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}Pequeno Ginasio{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}⣿
⣿{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}⣿
⣿{r}{r}{hospital}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}⣿
⣿{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}⣿
⣿{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}⣿
⣿{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}Barco{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}⣿
⣿{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{shop}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}{x}{y}⣿
⣿{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}{r}⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
'''
        self.cidade4_ops = '''[1]Pequeno Ginasio [2]Barco
[3]Hospital        [4]Shop
[5]Lago            [6]Ponte
[7]Menu'''
aa = art_ascii2()
clear()
table = Table(style='blue',box=box.HEAVY)
table.add_column("Sua Casa:")
table.add_column("ANDAR:")
table.add_row(f'[bold]{aa.cidade4}[/bold]',f'[bold yellow]{art.lago_ops1}[/bold yellow]')
print(table)