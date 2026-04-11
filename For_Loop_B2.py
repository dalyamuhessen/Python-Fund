def biggie_size(lst):
    for i in range(len(lst)):
        if lst[i]>0:
            lst[i]="big"
    return lst

print(biggie_size([-1, 3, 5, -5]))



def count_positives(lst):
    sum=0
    for i in range(len(lst)):
        if lst[i]>0 :
            sum+=1
    lst[-1]=sum
    return lst
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))


def sum_total(lst):
    sum=0
    for i in range(len(lst)):
        sum+=lst[i]
    return sum
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

def average(lst):
    sum=0
    for i in range(len(lst)):
        sum+=lst[i]
    return sum/len(lst)
print(average([1,2,3,4]))


def length(lst):
    sum=0
    for i in lst:
        sum+=1
    return sum
print(length([37,2,1,-9]))
print(length([]))


def minimum(lst):
    if len(lst) == 0:
        return False
    minim = lst[0]
    for i in lst:
        if i < minim:
            minim = i

    return minim

print(minimum([37, 2, 1, -9]))
print(minimum([]))



def minimum(lst):
    if len(lst) == 0:
        return False
    minim = lst[0]
    for i in lst:
        if i > minim:
            minim = i

    return minim

print(minimum([37, 2, 1, -9]))
print(minimum([]))


def ultimate_analysis(lst):
    if len(lst) == 0:
        return False
    total = 0
    min= lst[0]
    max= lst[0]

    for i in lst:
        total += i
        if i < min:
            min = i
        if i > max:
            max = i
    length = len(lst)
    average = total / length
    return {
        'sumTotal': total,
        'average': average,
        'minimum': min,
        'maximum': max,
        'length': length
    }

print(ultimate_analysis([37, 2, 1, -9]))

def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst
print(reverse_list([37, 2, 1, -9]))