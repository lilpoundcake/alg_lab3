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
    a = 0
    b = len(data) - 1
    c = round(b/2)
    if data[c] == value:
        return c
    for i in range(1, len(data)):
        if data[c] == value:
            return c
        elif value > data[c]:
            a = c
            c = round((a+b)/2)
        elif value < data[c]:
            b = c
            c = round((a+b)/2)


