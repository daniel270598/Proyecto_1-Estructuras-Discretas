
arre = {6,8,2,4,2,8,0,2134,66,777}

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
