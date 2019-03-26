#!/usr/bin/env python
# -*- coding: utf-8 -*-


def linear_search(data, value):
    for i, v in enumerate(data):
        if v > value:
            return None
        if v == value:
            return i
    return None


def binary_search(data, value):
    # Реализуйте алгоритм здесь
    pass

