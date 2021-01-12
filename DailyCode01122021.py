# ------------------------------------------------------
#	Daily Code	01/12/2021
#   "Modules and Packages" Lesson from learnpython.org
#   Coded by: Banehowl
# ------------------------------------------------------

# A Module is a piece of software that has a specific functionality. For example, when building a ping pong
# game, one module would be responsible for the game logic, and another module would be responsible for
# drawing the game on the screen. Each module is a different file, which can be edited separately.

# Writing modules
# Modules in Python is simply python files with the .py extension. The name of the module will be the
# name of the file. A Python module can have a set of functions, classes, or variables defined and
# implemented

# In the ping pong example above, the files would be organized below:
# mygame/
# mygame/game.py
# mygame/draw.py

# Modules are imported from other modules using the 'import' command. In this example, the game.py
# script may look something like this:

# # game.py
# # import the draw module
# import draw
#
# def play_game()
#     ...
#
# def main()
#     result = play_game()
#     draw.draw_game(result)
#
# # this means that if this script is executed, then main() will be executed
# if _name_ == '_main_';:
#    main()

# The draw module may look something like this:

# # draw.py
#
# def draw_game()
#     ...
#
# def clear_screen(screen)
#     ...

