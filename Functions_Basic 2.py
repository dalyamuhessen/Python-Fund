# def countdown(num):
#   result=[]
#   while num>0:
#     result.append(num)
#     num-=1
#   return result
# print(countdown(5))

# def print_and_return(lst):
#         print(lst[0])
#         return lst[1]
# result=print_and_return([1,2])
# print("Returned value:", result)

# def first_plus_length(lst):
#     return lst[0] + len(lst)
# print(first_plus_length([1,2,3,4,5]))


# def values_greater_than_second(lst):
#     if len(lst)<2:
#         return False
#     second=lst[1]
#     new_list=[]
#     for num in lst:
#         if num>second:
#             new_list.append(num)
#     print(len(new_list))
#     return new_list
# print(values_greater_than_second([5,2,3,2,1,4]))
# print(values_greater_than_second([3]))

def length_and_value(size,value):
    result=[]
    for i in range(size):
        result.append(value)
    return result
