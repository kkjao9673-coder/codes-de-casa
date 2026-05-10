from rich import print
from time import sleep

def printSong():

    lines = [
        ("You were layin' on my chest", 0.10),
        ("I Still remember", 0.14),
        ("I was scared to take a breath, didn't want you to move your head", 0.11),
        ("How can we go back to being friends", 0.10),
        ("When we just shared a bed?", 0.10),
        ("How can you look at me and pretend", 0.11),
        ("I'm someone you've never met?", 0.11),
    ]

    delays = [2.0, 2.6, 1.0, 1.0, 1.5, 1.1, 2.0]

    color = "#999999"

    for i, (line, char_delay) in enumerate(lines):

        for char in line:
            print(
                f"[bold {color}]{char}[/bold {color}]",
                end="",
                flush=True
            )
            sleep(char_delay)

        print()
        sleep(delays[i])

printSong()