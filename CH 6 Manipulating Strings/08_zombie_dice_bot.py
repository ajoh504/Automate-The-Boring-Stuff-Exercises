"""
Create game bots that use different roll strategies to play the zombie dice game. The game rules are contained in the my_zombie class.
    
    My classes are as follows. Other example classes were provided in the text:
    
    my_zombie(name="My Zombie Bot"),
    random_roll_bot(name="Random Roll Bot"),
    two_shotguns_bot(name="Stop at 2 shotguns"),
    one_to_four_bot(name="One to four rolls"),
    guns_beat_brains_bot(name="Guns beat brains"
    
    The only code sections that I wrote are the "roll strategy" sections. All other code was provided in the text. 
"""
import zombiedice, random


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

        # my_zombie roll strategy:
        brains = 0
        while dice_roll_results is not None:
            brains += dice_roll_results["brains"]
            if brains < 2:
                dice_roll_results = zombiedice.roll()  # roll again
            else:
                break


class random_roll_bot:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, game_state):
        # game_state is a dict with info about the current state of the game

        dice_roll_results = zombiedice.roll()

        # random_roll_bot roll strategy:
        roll_again = 0
        while dice_roll_results is not None:
            roll_again = random.randint(1, 100)
            if roll_again % 2 == 0:  # if divisible by 2, roll again
                dice_roll_results = zombiedice.roll()
            else:
                break


class two_shotguns_bot:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, game_state):
        # game_state is a dict with info about the current state of the game

        dice_roll_results = zombiedice.roll()

        # two_shotguns_bot roll strategy:
        shotguns = 0
        while dice_roll_results is not None:
            shotguns += dice_roll_results["shotgun"]
            if shotguns < 2:
                dice_roll_results = zombiedice.roll()  # roll again
            else:
                break


class one_to_four_bot:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, game_state):
        # game_state is a dict with info about the current state of the game

        dice_roll_results = zombiedice.roll()

        # one_to_four_bot roll strategy:
        shotguns = 0
        rolls = 1
        while dice_roll_results is not None:
            shotguns += dice_roll_results["shotgun"]
            if (
                shotguns < 2 and rolls < 5
            ):  # stops rolling either at 2 shotguns or 4 rolls
                dice_roll_results = zombiedice.roll()
                rolls += 1
            else:
                break


class guns_beat_brains_bot:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, game_state):
        # game_state is a dict with info about the current state of the game

        dice_roll_results = zombiedice.roll()

        # guns_beat_brains_bot roll strategy:
        shotguns = 0
        brains = 0
        while dice_roll_results is not None:
            shotguns += dice_roll_results["shotgun"]
            brains += dice_roll_results["brains"]
            if shotguns <= brains:
                dice_roll_results = zombiedice.roll()
            else:
                break  # stops rolling if more shotguns than brains


zombies = (
    zombiedice.examples.RollsUntilInTheLeadZombie(name="Until Leading"),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(
        name="Stop at 1 Shotgun", minShotguns=1
    ),
    my_zombie(name="My Zombie Bot"),
    random_roll_bot(name="Random Roll Bot"),
    two_shotguns_bot(name="Stop at 2 shotguns"),
    one_to_four_bot(name="One to four rolls"),
    guns_beat_brains_bot(name="Guns beat brains"),
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
# zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
