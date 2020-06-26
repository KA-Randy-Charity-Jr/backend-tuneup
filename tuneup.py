#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

__author__ = "Randy Charity Jr worked with Leanne Benson"
import timeit
import cProfile
import pstats
import functools
import collections


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    def profiler(*args, **kwargs):
        with cProfile.Profile() as p:
            result = func(*args, **kwargs)
        stat = pstats.Stats(p).sort_stats('cumulative')
        stat.print_stats(5)
    return profiler


def read_movies(src):
    """Returns a list of movie titles."""
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        return f.read().splitlines()


def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    return [movie for movie, count in collections.Counter(movies).items() if count > 1]


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer(stmt='find_duplicate_movies("movies.txt")',
                     setup='from __main__ import find_duplicate_movies')
    time = t.repeat(repeat=7, number=3)
    print("Minimum of Average Performances: {}".format(min(time) / 3))


@profile
def main():
    """Computes a list of duplicate movie entries."""
    result = find_duplicate_movies('movies.txt')
    timeit_helper()
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))


if __name__ == '__main__':
    main()
