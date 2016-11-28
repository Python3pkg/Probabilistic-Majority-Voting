#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

class MajorityVoting(object):
    'Probablistic Majority Voting class'

    def __init__(self, probabilities, categories):
        self.probabilities = probabilities
        self.categories = categories
        try:
            self.check_arguments()
        except Exception:
            raise               # in which case the object creation (__new__()) will fail

    def vote(self, windows=5):
        if windows <= 1 or windows % 2 == 0:
            raise ValueError('Number of windows has to be a positive odd number larger than 1')

        results = []

        # first couple windows
        # TODO:

        # middle part
        for w in range(2, len(self.probabilities) - 2):         # window for which to calculate the voting results
            cut = self.probabilities[w - (windows - 1) // 2 : w + (windows - 1) // 2 + 1]       # all voters
            results.append(self.get_majority(cut, windows))
            return

        # last couple windows
        # TODO:

        return results

    def get_majority(self, cut, windows):
        single_window = [[]] * windows

        for voter in cut:
            max = -sys.maxsize - 1
            for i in range(len(voter)):
                if voter[i] > max:
                    max = voter[i]
                single_window[voter.index(max)].append(voter)           # append to respective windows
            
        # TODO:
        # print(single_window)

    def check_arguments(self):
        if type(self.probabilities) is not list or type(self.categories) is not list:
            raise TypeError('Input argument type incorrect')
        elif len(self.probabilities) <= 0:
            raise Exception('No windows with predicted probabilities found in the table')
        elif len(self.probabilities[0]) != len(self.categories):
            raise IndexError('Number of categories does not match the columns in the table')

def main():
    print("Only meant to be called from other program through imports")

if __name__ == "__main__":
    main()