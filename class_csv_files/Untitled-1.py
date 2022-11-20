

for value in range(30,80):
    t1 = time.perf_counter()
    iter_fibonacci(value)
    t_iter = time.perf_counter() - t1

    t1 = time.perf_counter()
    rec_fibonacci(value)
    t_rec = time.perf_counter()-t1
    print(f'{value},iter:{t_iter: .3f}, recursive{t_rec: .3f}')





import time

def selection_sort(lst):
    for value in range(len(lst) - 1):
        tmp = lst[value]
        pos = value
        for counter in range(value+1, len(lst)):
            if lst[counter] < tmp:
                tmp = lst[counter]
                pos = counter

        old = lst[value]
        lst[value] = tmp
        lst[pos] = old
        
    return lst

def insertion_sort(lst):
    for i in range(1, len(lst)):
        for j in range(0, i):
            if (lst[i] < lst[j]):
                item = lst.pop(i)
                lst.insert(j, item)
                
    return lst

def bubble_sort(lst):
    for j in range(0, len(lst) - 1):
        counter = 0
        for i in range(0, len(lst) - 1):
            if (lst[i] > lst[i+1]):
                counter += 1
                tmp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = tmp
        
        if counter == 0:
            break
                
    return lst

def merge(my_left, my_right):
    result = []
    pos_left = 0
    pos_right = 0
    
    while pos_left < len(my_left) and pos_right < len(my_right):
        if my_left[pos_left] < my_right[pos_right]:
            result.append(my_left[pos_left])
            pos_left += 1
        else:
            result.append(my_right[pos_right])
            pos_right += 1
            
    while pos_left < len(my_left):
        result.append(my_left[pos_left])
        pos_left += 1
    
    while pos_right < len(my_right):
        result.append(my_right[pos_right])
        pos_right += 1
        
    return result

def merge_sort(lst):
    if len(lst) == 1:
        return lst
    
    left = lst[0:len(lst)//2]
    right = lst[len(lst)//2:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)











t1 = time.perf_counter
