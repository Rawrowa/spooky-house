import os


def game(gm_len):
    """Main game function"""


    def new_screen():
        os.system("cls")
        print(logo)


    def game_over(stg_i, stg_chs_i):
        new_screen()
        print(stages[stg_i]["screens"][stg_chs_i])
        input("\nPress Enter to start again!")
        return game(game_lenght)


    # Each "stage" asks player for input, if index of their choice isn't 0 (correct one) it returns game_over function which starts the game again
    for stage_index in (stg_i for stg_i in range(gm_len) if stg_i < gm_len):
        new_screen()
        active_stage = stages[stage_index]

        player_input = input(f"{active_stage["screens"][0]}\n").lower()
        while player_input not in active_stage["choices"]:
            player_input = input("\nPlease type a valid choice\n").lower()
        
        for stage_choice in (stg_chs for stg_chs in active_stage["choices"] if stg_chs == player_input):
            stage_choice_index = active_stage["choices"].index(stage_choice)
        
        if stage_choice_index != 0:
            return game_over(stage_index, stage_choice_index)

    new_screen()
    print(end_text)


# Generating a table from provided txt files from text folder, last 3 are skipped and used as just variables
text_list = os.listdir("text")[:-3]
game_lenght = int(text_list[-1][:2])

stages = []
for n in range(game_lenght):
    stages.append(
        {
            "screens": [],
            "choices": [],
        },
    )

for filename in text_list:
    with open(os.path.join("text", filename)) as file:
        stage_text = str(file.read())
    
    stage_index = int(filename[:2]) - 1
    stage_choice = str(filename[10:-4])

    stages[stage_index]["screens"].append(stage_text)
    stages[stage_index]["choices"].append(stage_choice)

# The table end up looking something like this...
# --------------------------------------------------------------
# stages = [
#     {
#         "screens": ["question 1", "gameover 1a"],
#         "choices": ["right answer 1", "wrong answer 1a"],
#     },
#     {
#         "screens": ["question 2", "gameover 2a", "gameover 2b"],
#         "choices": ["right answer 2", "wrong answer 2a", "wrong answer 2b"],
#     },
# ]
# --------------------------------------------------------------
# Note that screens and choices placement correspond, first (0) is reserved for questions and answers

# Filling the rest as variables
with open(os.path.join("text", "end.txt")) as file:
    end_text = str(file.read())

with open(os.path.join("text", "logo.txt")) as file:
    logo = str(file.read())
    
with open(os.path.join("text", "welcome.txt")) as file:
    welcome_text = str(file.read())

# Starting the game
print(f"{logo}\n{welcome_text}")
input("\nPress Enter to continue...")
game(game_lenght)
