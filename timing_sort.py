import sort_list, random, csv, timeit
a = None

def timing_sort(start, stop, step):
    global a
    results = []
    population = list(range(0, stop))
    for n in range(start, stop, step):
        size = start + n
        a = random.sample(population, size)
        print("Size={}".format(size))
        tn = timeit.timeit("sort_list.sortList(a)", number=500, globals=globals())
        results.append((size, tn))
    return results

def sort_time_save(filename="data/sort_list.csv", start=10, stop=1000, step=100):
    results = timing_sort(start, stop, step)
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['i', 'n', 'time'])
        for i, (n, tn) in enumerate(results):
            writer.writerow([i, n, tn])