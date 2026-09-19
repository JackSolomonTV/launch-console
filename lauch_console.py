def menu():
  print("1: About Me")
  print("2: My Goals")
  print("3: Past Projects")
  print("4: Exit")
def choice():
  choice = input("Choose: ")
  if choice == "1":
    about_me()
  elif choice == "2":
    goals()
  elif choice == "3":
    past_projects()
  elif choice == "4":
    print("Goodbye!")
    return False
  else:
    print("Invalid choice!")
  return True

def about_me():
  print("Hi, my name is Jack Culbertson, aka JackSolomonTV, and i am a Youtuber, programmer, and also i like video games a lot :D")
def goals(): 
  print("I will be working on QuestForge this year for my Code2College Elite 101 Course, outside of that i want to be a programmer full time when i grow up.")
def past_projects(): 
  print("So far, I have made a Minecraft mod on CurseForge, a 3d LiDAR game that won best 3d game, and a Discord bot with an embedded LLM that you can talk to, which is based on a boss from my Minecraft mod.")
print("Welcome to the Launch Console!")
name = input("What is your name? ")
print(f"Welcome, {name}")
open = True
while open:
  menu()
  open = choice()

