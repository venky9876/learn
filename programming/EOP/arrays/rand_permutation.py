# Design an algorithm that creates uniformly random permutations of {0,1,2,...,n-1}. You are given a random number generator that returns integers in the set {0,1,2,..,n-1} with equal probability. Use as few calls to it as possible.

import random_sampling from uniform_subsample

def compute_random_permutation(n):
    permutation = list(range(n))
    random_sampling(n,permutation)
    return permutation

