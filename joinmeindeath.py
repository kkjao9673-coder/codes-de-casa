import time
import os
from rich.console import Console
console = Console()


def Lyrics(text, speed, cor="white"):
    linha = ""

    for letra in text:
        linha += letra
        console.print(f"[{cor}]{linha}[/]", end="\r")
        time.sleep(speed)

    console.print(f"[black {cor}]{text}[/]")
    time.sleep(0.6)

def sing():
    Lyrics("death bless me", 0.06,)
    Lyrics("with you", 0.11, )
    Lyrics("Whooaa-oh", 0.30, )
    console.print()
    Lyrics("would  you die tonight for love?", 0.13)
    Lyrics("Baby, join me in death", 0.11)
    console.print()
    Lyrics("So, would you die?????", 0.16,) 
    console.print()
    Lyrics("Baby, join me in death...", 0.15)
    console.print()
  
sing()