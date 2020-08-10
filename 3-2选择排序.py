num = [80,18,72,95,29,45,12,29]
#升序 
def SelectionSort(num):

    current_index= 0

    while current_index<len(num):
        min_index = current_index
        for i in range(current_index,len(num)):
            if num[i] < num[min_index]:
                min_index = i
        t = num[current_index]
        num[current_index] = num[min_index]
        num[min_index] = t
        current_index += 1
SelectionSort(num)
print(num)