'''
Samiksha Dharmadhikari                            Nithya Balasundar
1001740496                                        1001763661

'''
import time
class selection:
    #function fof selection sort
    def selectionSort(object, array, size):
        for i in range (size):

            # find the minimum element
            min_ele = i

            for j in range (i + 1, len (array)):
                if array[min_ele] > array[j]:
                    min_ele = j

            # Swap using the temp varaiable
            temp = array[i]
            array[i] = array[min_ele]
            array[min_ele] = temp
#return the sorted array
        return array

arr = []
i = 0
size = int (input ("Enter the array size : "))
for i in range (size):
    value = int (input ("Enter the  Element %d of List : " % i))
    arr.append (value)
sstart_time = time.perf_counter ()
r=selection.selectionSort(object,arr,size)
selection_time = time.perf_counter () - sstart_time
print ("Selection sort results:", r)
print ("Selection sort Runtime=", selection_time)


