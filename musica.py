# salve salve
"""
import sys
from rich import print
from time import sleep
import time
def printLyrics():
    lines = [
        ("I wanna da-", 0.06),
        ("I wanna dance in the lights", 0.05),
        ("I wanna ro-", 0.07),
        ("I wanna rock your body", 0.08),
        ("I wanna go", 0.08),
        ("I wanna go for a ride", 0.068),
        ("Hop in the music and", 0.07),
        ("Rock your body", 0.08),
        ("Rock that body", 0.069),
        ("come on, come on", 0.035),
        ("Rock that body", 0.05),
        ("(Rock your body)", 0.03),
        ("Rock that body", 0.049),
        ("come on, come on", 0.035),
        ("Rock that body", 0.08),
    ]

















    delays = [0.2, 1, 0.2, 2, 0.2, 0.8, 0.2, 0.5, 0.18, 0.1, 0.15, 0.3, 0.3, 0.1, 5]

    for i, (text, char_delay) in enumerate(lines):
        for char in text:
            if text in ("Rock your body", "Rock that body"):
                print(f"[orange4]{char}[/orange4]", end='')
            else:
                print(f"[bold][gold3]{char}[/gold3][/bold]", end='')
            sys.stdout.flush()
            sleep(char_delay)
        print()
        sleep(delays[i])

printLyrics()
""" 



































"""
from rich.console import Console
import time

console = Console()

def typewriter(lines, default_char_delay=0.08, default_line_delay=0.5):
    
    for line in lines:
        if isinstance(line, list):  
            line_delay = default_line_delay
            for segment in line:
                if len(segment) == 2:
                    text, color = segment
                    char_delay = default_char_delay
                elif len(segment) == 3:
                    text, color, char_delay = segment
                else:
                    raise ValueError()

                for ch in text:
                    console.print(ch, style=color, end="")
                    console.file.flush()
                    time.sleep(char_delay)
            console.print()
            time.sleep(line_delay)
        else:  
            text, char_delay, line_delay, color = line
            for ch in text:
                console.print(ch, style=color, end="")
                console.file.flush()
                time.sleep(char_delay)
            console.print()
            time.sleep(line_delay)


if __name__ == "__main__":
 linhas = [
        ("Eu sabia, ia ser nossa última dança", 0.06, 0.06, "#454545"),
        ("(Nossa última dança)",  0.07, 0.03, "#454545"),
        ("Foi embora seu eu ver", 0.09, 0.06, "#454545"),

        [
            ("Igual a minha ", "#454545", 0.05),
            ("infância", "white", 0.05),
        ],

        ("Só me liga, quando ela quer transa", 0.05, 0.05, "#454545"),
        ("Deu saudade, então ela me chama", 0.06, 0.06, "#454545"),
        ("deve ser tão triste", 0.09, 0.07, "#454545"),
        
        [
            ("dançar nos braços de quem ", "#454545", 0.07),
            ("não te A M A", "bold italic red", 0.05),
        ],

        ("Dormir em outros lugares", 0.06, 0.11, "#454545"),
        ("e lembrar da minha cama", 0.06, 0.13, "#454545"),
        ("Pedir meu último pedaço", 0.06, 0.15, "#454545"),
    
        [
            ("E eu te disse: ", "#454545", 0.09),
            ("T o m a", "bold italic white", 0.09),
        ],

        ("Garota, cê ta em pedaço", 0.07, 0.13, "#454545"),
        ("Por que ainda se apaixona?", 0.06, 0.06, "#454545"),
        ("O amor exige muito", 0.09, 0.10, "#454545"),
        
        [
            ("E você não tem ", "#454545", 0.09),
            ("n a d a", "bold italic strike white", 0.11),
        ],

        ("__", 5, 2, "#454545"),
    ]
typewriter(linhas)
"""
















from rich.console import Console
import time

console = Console()

def typewriter(lines, default_char_delay=0.08, default_line_delay=0.5):
    
    for line in lines:
        if isinstance(line, list):  
            line_delay = default_line_delay
            for segment in line:
                if len(segment) == 2:
                    text, color = segment
                    char_delay = default_char_delay
                elif len(segment) == 3:
                    text, color, char_delay = segment
                else:
                    raise ValueError()

                for ch in text:
                    console.print(ch, style=color, end="")
                    console.file.flush()
                    time.sleep(char_delay)
            console.print()
            time.sleep(line_delay)
        else:  
            text, char_delay, line_delay, color = line
            for ch in text:
                console.print(ch, style=color, end="")
                console.file.flush()
                time.sleep(char_delay)
            console.print()
            time.sleep(line_delay)


if __name__ == "__main__":
 linhas = [
        ("Acima de todo ódio e rancor que sinto pelo mundo", 0.04, 0.06, "#454545"),
        ("E acima de todo amor",  0.05, 0.03, "#454545"),
        ("Que eu já senti por cada ser humano vivo", 0.03, 0.06, "#454545"),
        
        [
            ("E u  m e  o d e i o", "bold italic strike white", 0.07),
        ],

        ("Tive a existência mais fútil de todas", 0.03, 0.04, "#454545"),
        
        [
            ("E tive medo de existir com as minhas ", "#454545", 0.04),
            ("individualidades", "bold italic #A0EFFF", 0.03),
        ],

        ("Mas amanhã o Sol nasce de novo", 0.04, 0.05, "#454545"),
        ("comigo aqui ou não", 0.04, 0.05, "#454545"),
        ("Os pássaros vão cantar de manhã", 0.04, 0.05, "#454545"),
        ("E no fim do dia o Sol vai se pôr", 0.04, 0.05, "#454545"),
        
        [
            ("Como sempre.", "bold italic white", 0.04),
        ],

        ("Então não se apegue tanto a isso", 0.025, 0.04, "#454545"),
        ("As coisas começam e acabam", 0.06, 0.06, "#454545"),
        
        [
            ("vivem ", "bold italic #CCE8BD", 0.04),
            ("e ", "italic black ", 0.04),
            ("morrem", "bold italic #E6A4A4", 0.04),
        ],
        
        ("E existir é aceitar o inicio", 0.05, 0.04, "#454545"),
        ("mas aceitar ainda mais", 0.06, 0.10, "#454545"),

        [
            ("O fim.", "bold italic underline white", 0.11),
        ],

        ("___", 5, 2, "#1F1F1F"),
    ]
typewriter(linhas)