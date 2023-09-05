game_data = {
  "money": 0,
  "quit": False
}
while(True):
  player_choice = int(input("""
                      Would you like to...
                      [1] Make 1 money cutting lawns with your teeth?
                      [2] Quit Landscaper
                      """))
  if (player_choice == 1):
    game_data["money"] += 1
    print(f"You now have a total of {game_data['money']} money")

  if (player_choice == 2):
    game_data["quit"] = True

  if (game_data["quit"]) == True:
    print("You quit the game")
    break

  elif (game_data["money"] >= 5):
    player_choice = int(input("""
                        You can...
                        [1] Make 1 money cutting lawns with your teeth?
                        [2] Quit Landscaper?
                        [3] Buy rusty scissors for 5 money?
                        """))

  if (player_choice == 3):
    game_data["money"] -= 5
    print("You bought the rusty scissors")
    player_choice = int(input("""
                          You can...
                          [4] Make 5 money cutting the lawn with your rusty scissors?
                          [2] Quit Landscaper?
                          """))
    
  if (player_choice == 4):
    game_data["money"] += 5
    print(f"You now have a total of {game_data['money']} money")
    player_choice = int(input("""
                          You can...
                          [4] Make 5 money cutting the lawn with your rusty scissors?
                          [2] Quit Landscaper?
                          """))

  if (game_data["money"] >= 10):
    print("You won the game!")
    break