    player_choice = int(input("""
                            You can...
                            [2] Quit Lanscaper
                            [4] Make $5 using your rusty scissors to cut the lawn?
                          """))
    if (player_choice == 4):
      game_data["money"] += 5
      print(f"You now have a total of {game_data['money']} money")