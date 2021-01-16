from mainPrograme import mainPrograme

main = mainPrograme()
main.printIntroduction()
chosen_choice = main.getChoice()
main.runChoice(chosen_choice)