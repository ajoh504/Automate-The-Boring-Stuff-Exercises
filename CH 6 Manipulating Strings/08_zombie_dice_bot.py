import zombiedice

class my_zombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, game_state):
        # game_state is a dict with info about the current state of the game

        dice_roll_results = zombiedice.roll()
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}
