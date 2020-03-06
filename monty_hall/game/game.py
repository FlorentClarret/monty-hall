#! /usr/bin/env python3
# coding: utf-8

from enum import Enum
from random import randint


class Choice(Enum):
    CHANGE = 1
    KEEP = 2


def game(choice, first_pick):
    doors = [0, 1, 2]
    treasure = randint(0, 2)

    doors.remove(first_pick)

    if first_pick == treasure:
        doors.remove(doors[randint(0, 1)])
    else:
        doors = [treasure]

    return treasure == (first_pick if choice == Choice.KEEP else doors[0])


def games(choice, first_picks):
    result = []
    for first_pick in first_picks:
        result.append(game(choice, first_pick))

    return result
