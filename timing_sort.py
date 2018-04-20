import sort, random, csv, timeit

def timing_sort(start, stop, step):
    global a
    results = []
    population = list(range(0, stop))
    for n in range(start, stop, step):
        size = start + n
        a = random.sample(population, size)
        tn = timeit.timeit("sort.sort5(a)", number=500, globals=globals())
        print("\tn={}\tSize = {}\tTiempo={}".format(n,size,tn))
        results.append((size, tn))
    return results

def sort_time_save(filename="datos/sort5.csv", start=10, stop=1000, step=100):
    results = timing_sort(start, stop, step)
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['i', 'n', 'time'])
        for i, (n, tn) in enumerate(results):
            writer.writerow([i, n, tn])