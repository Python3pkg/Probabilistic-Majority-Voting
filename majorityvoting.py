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
        # TODO: go with popular votes

        # middle part
        for w in range((windows - 1) // 2, len(self.probabilities) - (windows - 1) // 2):           # window for which to calculate the voting results
            cut = self.probabilities[w - (windows - 1) // 2 : w + (windows - 1) // 2 + 1]           # all voters
            results.append(self.get_majority(cut, windows))
            print(results)
            # TODO: delete
            break

        # last couple windows
        # TODO: go with popular votes

        return results

    def get_majority(self, cut, windows):
        single_window = [[] for i in range(windows)]
        cats = len(cut[0])                                          # categories

        for voter in cut:
            max = -sys.maxsize - 1
            for i in range(cats):
                if voter[i] > max:
                    max = voter[i]
            single_window[voter.index(max)].append(voter)           # append to respective windows
        
        len_list = [[] for i in range(windows)]                     # number of voters for each category
        for i in range(windows):
            len_list[i] = len(single_window[i])
        len_list = sorted(len_list, reverse=True)                   # descending order

        if len_list[0] == len_list[1]:                              # more than one majority
            # when electoral collage fails, we count on popular votes
            popvotes = [0] * cats
            for voter in cut:
                for i in range(cats):
                    popvotes[i] += voter[i]
            maxvotes = 0
            maxindex = 0
            for i in range(cats):
                if popvotes[i] > maxvotes:
                    maxvotes = popvotes[i]
                    maxindex = i
            return maxindex
        else:                                                        # clear winner
            maxlen = 0
            maxindex = 0
            for i in range(len(single_window)):
                if len(single_window[i]) > maxlen:
                    maxlen = len(single_window[i])
                    maxindex = i
            return maxindex

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