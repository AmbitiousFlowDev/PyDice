import random


class DiceController:
    chosen_dice = range(1,7)

    def roll_dice_once(self):
        return random.choice(DiceController.chosen_dice)
    
    def roll_dice_twice(self):
        return (random.choice(DiceController.chosen_dice) , random.choice(DiceController.chosen_dice))