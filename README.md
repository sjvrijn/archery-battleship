# :bow_and_arrow: Archery Battleship :dart:

[![Python Version](https://img.shields.io/badge/Python-3.10-blue)](https://python.org)

Simulation playtesting of 'battleship' as an archery game

<img src="https://www.tricorder.se/wp-content/uploads/Siege-of-Damietta-1218-1489x1536.jpeg" width="256" title="Archery Battleship! Or Battleship Archery, whichever makes more sense" alt="medieval image of archers on a ship"/>

[(imgage source)](https://www.tricorder.se/?p=3310)


## Introduction

Instead of always shooting at the same concentric circles :dart:, it's always
fun to shake things up by having something else to target. One such idea: Let's
play a game of 'battleship' through archery!

The goal of this project is to run playtesting simulations of the rules to make
sure the game is both feasible to play, and doesn't take too long.


## Gameplay/Rules

The currently envisioned rules for 'Archery Battleship' are as follows:

 - The game is played on a board of N x N\* squares
 - A fleet consists of M\* ships, of length s1\*, s2\*, ..., sM\*
 - Each player secretly assigns their fleet as per usual [rules]
 - Per turn, each player shoots a standard salvo of 3 arrows at the target
 - A player shoots the other player's board where their arrows hit the board
 - Shooter's advantage: If a line between squares is hit, the player may choose

\* suitable values for N, M, s1, ..., sM are to be determined using this software,
see the ['Simulations'](#simulations) section.


## Instructions

To work with this code:

```bash
# clone repository
git clone git@github.com:sjvrijn/archery-battleship.git

# enter folder
cd archery-battleship

# [Recommended] prepare and activate a Python 3.10+ virtual environment

# perform a local (editable) install
pip install -e .

# currently, 'game.py' is the file to run
python src/battleship/game.py
```

This will run the currently defined simulations.


## Simulations

To come up with reasonable values for N, M, s1, ..., sM, this code can
soon<sup>TM</sup> run simulations with all kinds of different parameters.
Configurable parameters include:
 - Board size (in \#squares)
 - Fleet composition
 - Strategy
 - Archers' average accuracy (soon<sup>TM</sup>)
 - Board size (in cm) (soon<sup>TM</sup>)


[rules]: https://en.wikipedia.org/wiki/Battleship_(game)
