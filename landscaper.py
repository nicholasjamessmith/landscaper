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