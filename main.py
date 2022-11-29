from rich.console import Console
import requests
import random

from scripts import getListSize
from scripts import roulette
from scripts import getTopPlayers
from scripts import getTopXDemons
from scripts import pointercratecli

console = Console()

def menu():
    console.print("Welcome to the pointercratecli!", style="bold red")
    console.print("1. Main Demonlist CLI", style="bold red")
    console.print("2. Demonlist Roulette", style="bold red")
    console.print("3. Get Demonlist Size", style="bold red")
    console.print("4. Get top X demons", style="bold red")
    console.print("5. Get top players", style="bold red")
    console.print("6. Exit", style="bold red")
    choice = int(input("Enter your choice: "))
    return choice

def main():
    choice = menu()
    if choice == 1:
        pointercratecli.main()
    elif choice == 2:
        roulette.main()
    elif choice == 3:
        getListSize.main()
    elif choice == 4:
        getTopXDemons.main()
    elif choice == 5:
        getTopPlayers.main()
    elif choice == 6:
        exit()
    else:
        console.print("Invalid choice", style="bold red")
        main()

if __name__ == "__main__":
    main()