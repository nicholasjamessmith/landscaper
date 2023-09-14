# Pseudocode: What I want the game to do:
## Option to make $1  with user input [1] 
## Option to quit at any time with user input [2] or [q]
## New message with user input response at $5, $25, $250, $500; user input allows you to buy upgrade tool
## Include tool(s) as items in a list within game data upon purchase
## If upgraded tool purchases, new message with user input option to make $__ using (new) tool to cut lawns
## Print message 'You Win!' and break game loop if tool = team of starving students AND $ >= $1,000

# Questions / challenges:
## I only want the prompt to cut the grass with teeth for $1 to display until the user upgrades tools. The way I have it programmed seems to default back to that point in the script under circumstances, and I haven't written any logic to prevent that.

# bugs: after reaching 5 points, need to press 1 twice to earn another point; after 5 points need to press 2 twice to quit; game reverts back to first player_choice prompt after using the rusty scissors; all player_choice input buttons available on each turn
game_data = {
  "money": 0,
  "quit": False,
  "tool": ""
}

while(True):
# Win conditions
  if (game_data["money"] >= 1000 and game_data["tool"] == "starving students"):
    print("You won the game!")
    break

  if (game_data["quit"]) == True:
    print("You quit the game")
    break

# User inputs
  if (game_data["money"] < 5 and game_data["tool"] == ""):
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

  if (game_data["money"] >= 5 and game_data['tool'] == ""):
    player_choice = int(input("""
                        You can...
                        [1] Make 1 money cutting lawns with your teeth?
                        [2] Quit Landscaper?
                        [3] Buy rusty scissors for 5 money?
                        """))
    if (player_choice == 1):
      game_data["money"] += 1
      print(f"You now have a total of {game_data['money']} money")

    if (player_choice == 2):
      game_data["quit"] = True

    if (player_choice == 3):
      game_data["money"] -= 5
      game_data["tool"] = "rusty scissors"
      print(f"You bought and equipped {game_data['tool']} you currently have {game_data['money']} money")

  if (game_data["tool"] == "rusty scissors"):
    player_choice = int(input("""
                          You can...
                          [1] Make 5 money cutting the lawn with your rusty scissors?
                          [2] Quit Landscaper?
                          [3] Do you want to spend 25 money to buy an old timey push lawnmower?
                          """))
    if (player_choice == 1):
      game_data["money"] += 5
      print(f"You now have a total of {game_data['money']} money")

    elif (player_choice == 2):
      game_data["quit"] = True

    elif (player_choice == 3 and game_data["money"] >= 25):
      game_data["money"] -= 25
      game_data["tool"] = "pushmower"
      print(f"You bought and equipped {game_data['tool']} you currently have {game_data['money']} money")
    else:
      print("Not enough money")

  if (game_data["tool"] == "pushmower"):
    player_choice = int(input("""
                          You can...
                          [1] Make 50 money cutting the lawn with your pushmower?
                          [2] Quit Landscaper?
                          [3] Buy a fancy battery-powered lawnmower for 250 money?
                          """))
    if (player_choice == 1):
      game_data["money"] += 50
      print(f"You now have a total of {game_data['money']} money")
    
    elif (player_choice == 2):
      game_data["quit"] = True

    elif (player_choice == 3 and game_data["money"] >= 250):
      game_data["money"] -= 250
      game_data["tool"] = "battery-powered lawnmower"
      print(f"You bought and equipped {game_data['tool']} you currently have {game_data['money']} money")
    else:
      print("Not enough money")

  if (game_data["tool"] == "battery-powered lawnmower"):
    player_choice = int(input("""
                          You can...
                          [1] Make 100 money cutting the lawn with your pushmower?
                          [2] Quit Landscaper?
                          [3] Hire a team of starving students for 500 money?
                          """))
    if (player_choice == 1):
      game_data["money"] += 100
      print(f"You now have a total of {game_data['money']} money")
    
    elif (player_choice == 2):
      game_data["quit"] = True

    elif (player_choice == 3 and game_data["money"] >= 500):
      game_data["money"] -= 500
      game_data["tool"] = "starving students"
      print(f"You bought and equipped {game_data['tool']} you currently have {game_data['money']} money")
    else:
      print("Not enough money")

  if (game_data["tool"] == "starving students"):
    player_choice = int(input("""
                          You can...
                          [1] Make 250 money cutting the lawn with your team of starving students?
                          [2] Quit Landscaper?
                          """))

    if (player_choice) == 1:
      game_data["money"] += 250
      print(f"You now have a total of {game_data['money']} money")

    elif (player_choice == 2):
      game_data["quit"] = True







  #if (player_choice == 3):
  #  game_data["money"] -= 5
  #  print("You bought the rusty scissors")
    
  #if (player_choice == 4):
  #  game_data["money"] += 5
  #  print(f"You now have a total of {game_data['money']} money")
  #  player_choice = int(input("""
  #                        You can...
  #                        [4] Make 5 money cutting the lawn with your rusty scissors?
  #                        [2] Quit Landscaper?
  #                        """))

