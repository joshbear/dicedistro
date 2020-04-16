import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


class Dice:
    """Store values and functions for a die object.
       kind: either 'numbers' or 'text'
    """
    sides = []
    kind = 'text'
    name = None

    def __init__(self, sides: list, name: str=None):
        self.sides = sides
        if all(isinstance(x, (int, float)) for x in sides):
            self.kind = 'numbers'
        if name is not None: self.name = name
        else: self.name = f'd{len(self.sides)} ({self.kind})'

    def __str__(self):
        return(f'{self.name}: {str(self.sides)}')

    def __repr__(self):
        return(f'{self.name}: {str(self.sides)}')

    def roll(self):
        return self.sides[random.randint(0, len(self.sides) - 1)]


def roll_dice(dice: list, num_rolls: int=100000, verbose=False, plot=False,
              title=None):
    result = {}
    for roll in range(num_rolls):
        values = []
        for die in dice:
            values.append(die.roll())
        if all(x.kind == 'numbers' for x in dice):
            roll_name = str(np.sum(values))
        else:
            values_as_strings = [str(x) for x in values]
            roll_name = ' / '.join(sorted(values_as_strings))
        if roll_name in result.keys():
            result[roll_name] = result[roll_name] + 1
        else:
            result[roll_name] = 1
            # some code just for checking values
    if verbose is True:
        print('\nResult of your dice roll:')
        for name, sum in result.items():
            pct = sum / num_rolls * 100
            print(f'  {name.rjust(20)}: {str(sum).ljust(7, " ")} ({pct:.1f}%)')
    if plot is True:
        x = list(result.keys())
        if all(x.kind == 'numbers' for x in dice):
            x.sort(key=int)
        y = []
        for key in x:
            y.append(result[key] / num_rolls * 100)
        fig, ax = plt.subplots(figsize=(5, 4), dpi=144)
        ax.grid(b=True, which='major', color='k', linewidth=0.2)
        sns.set_style('whitegrid')
        bars = sns.barplot(x, y, ax=ax, order=x)
        for bar in bars.patches:
            bars.annotate(f'{bar.get_height():.1f}%',
                          (bar.get_x() + bar.get_width() / 2., bar.get_height()),
                          ha='center', va='center', xytext=(0, 10),
                          textcoords='offset points', fontsize=8)
        ax.set_ylim([0, 100])
        ax.set_ylabel('Percentage')
        plt.xticks(rotation=90)
        if title is not None:
            ax.set_title(title)
        else:
            ax.set_title(f'Dice: {", ".join([x.name for x in dice])}')
        dice_key = '\n'.join([str(x) for x in set(dice)])
        plt.text(0.99, 0.99, dice_key, verticalalignment='top',
                 horizontalalignment='right',
                 fontweight='regular', fontsize=9, transform=ax.transAxes)
        plt.show()



"""
results = {}

for i in range(1000000):
    rolls = r.roll([d, d])
    roll_val = '_'.join(rolls)
    if roll_val in results.keys():
        results[roll_val] = results[roll_val] + 1
    else:
        results[roll_val] = 1


plt.bar(results.keys(), results.values())
plt.show()

dn1 = dd.Dice([0, 0, 0, 1, -1, 0], name='DN1')
dn2 = dd.Dice([0, 0, 1, 1, -1, -1], name='DN2')

dr2 = dd.Dice([0, 0, 0, 1, 1, 0], name='DR2')
dl2 = dd.Dice([0, 0, 0, -1, -1, 0], name='DL2')

dr1 = dd.Dice([0, 0, 0, 0, 1, 0], name='DR1')
dl1 = dd.Dice([0, 0, 0, 0, -1, 0], name='DL1')

d2 = dd.Dice([0, 0, 0, 0, -1, -1])

d = dd.Dice(['miss', 'miss', 'hit', 'hit', 'hit', 'excellent'])
d2 = dd.Dice(['miss', 'miss', 'hit', 'hit', 'hit', 'hit'], kind='text')
d3 = dd.Dice(['miss', 'hit', 'hit', 'hit', 'hit', 'hit'])
d4 = dd.Dice(['miss', 'excellent', 'hit', 'hit', 'hit', 'hit'])

r = dd.Roller()

"""
