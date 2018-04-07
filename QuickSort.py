

def quickSort(arre, pri, pultimo):
    ult = pultimo
    pi = pri

    while(pri < ult):
        if arre[pi] > arre[pri]:
            pri + 1
        else:
            arre[pi], arre[pri] = arre[pri], arre[pi]
    quickSort(arre,pri ,pi)
    quickSort(arre,pi,len(arre) )
    
