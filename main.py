#! /usr/bin/env python3
# coding: utf-8

import argparse

import numpy as np
import matplotlib.pyplot as plt

from monty_hall.game.game import Choice, games


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode", help="""PLAY or STAT""", default="STAT")
    parser.add_argument("-i", "--iteration", help="""Iteration count. STAT mode only""",
                        default="10000")
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()

    if args.mode == "STAT":
        plot = plt.bar(
            [1, 2],
            [sum(games(Choice.CHANGE, np.random.randint(3, size=int(args.iteration)))),
             sum(games(Choice.KEEP, np.random.randint(3, size=int(args.iteration))))],
            tick_label=["Change", "Keep"])
        plt.show()
    else:
        pass