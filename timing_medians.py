import random, csv, timeit
import Medians
a = None
b = 0

def timing_medians(med,start, stop, step):
    global a
    results = []
    population = list(range(0, stop))
    for n in range(start, stop, step):
        size = start + n
        a = random.sample(population, size)
        print("Size={}".format(size))
        tn = timeit.timeit("median_of_medians(a,b)", number=500, globals=globals())
        results.append((size, tn))
    return results

def medians_time_save(med,filename="Cuadernos/medians.csv", start=5, stop=100, step=5):
    results = timing_medians(med,start, stop, step)
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['i', 'n', 'time'])
        for i, (n, tn) in enumerate(results):
            writer.writerow([i, n, tn])