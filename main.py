import os
import flavor as fl


def new_screen():
    os.system('cls')
    print(fl.logo)


def game_over(ch, choice_i):
    new_screen()
    print(fl.chapters[ch]["texts"][choice_i])
    input("Press Enter to start again!\n")
    return game()


def ask(ch):
    """Asks user for input and returns the index of their choice"""
    active_chapter = fl.chapters[ch]

    player_input = input(f"{active_chapter["texts"][0]}\n").lower()
    while player_input not in active_chapter["choices"]:
        player_input = input(f"\n{fl.invalid_msg}\n\n").lower()
    
    for choice in (chs for chs in active_chapter["choices"] if chs == player_input):
        return active_chapter["choices"].index(choice)


# Game function is here
def game():
    game_lenght = len(fl.chapters)

    for chapter in (ch for ch in range(game_lenght) if ch < game_lenght):
        new_screen()
        choice_index = ask(chapter)
        if choice_index != 0:
            return game_over(chapter, choice_index)

    new_screen()
    print(fl.win)


print(f"{fl.logo}\n{fl.welcome}")
input(fl.prompt)
game()
