#!/usr/bin/env python
# -*- coding: utf-8 -*-

from timeit import default_timer as timer
from matplotlib import pyplot as plt
from tqdm import tqdm
from statistics import mean
import random
from search import linear_search, binary_search


def generate_sorted_data(sz):
    """
    Возвращает массив чисел без повторов, отсортированный в порядке
    возрастания
    """
    a = [1]
    for i in range(sz - 1):
        a.append(a[i] + random.randint(1, 10))
    return a


def measure_search_time(search_alg, sz, repeats):
    """
    Возвращает результат замеров скорости выполнения поиска в массиве длины sz.
    """
    data = generate_sorted_data(sz)
    results = []
    for i in range(repeats):
        v = random.choice(data)
        start = timer()
        search_alg(data, v)
        end = timer()
        results.append(end - start)
    return mean(results)


def main():
    algorithms = {
        'linear_search': linear_search,
        'binary_search': binary_search
    }

    sizes = []
    avg_time = {alg: [] for alg in algorithms}
    for sz in tqdm(range(10, 50000, 1000)):
        sizes.append(sz)
        for alg_name, f in algorithms.items():
            avg_time[alg_name].append(measure_search_time(f, sz, 500))
    
    for alg_name in algorithms:
        plt.plot(sizes, avg_time[alg_name], label=alg_name)
    #plt.plot(sizes, avg_time)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
