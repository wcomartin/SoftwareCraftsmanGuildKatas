def last_element(input):
    new_input = input[1:]
    if len(new_input) == 0:
        return input[0]
    return last_element(new_input)

last_element("Silly")

def nth(lst, cnt):
    if cnt == 0:
        return(lst[0])
    else:
        return nth(lst[1:], cnt - 1)

nth([0,1,2,3,5], 3)

def count_iter(input, *args):
    if len(input) == 0:
        return args[0]
    return count_iter(input[1:], (args[0] + 1 if args else 1))

def count_iter2(input, index = 1)
    if len(input) == 0:
        return index
    return count_iter2(input[1:], index + 1)

count_iter([0,1,2,3,4,5])

def find_max(input, max=0):
    if len(input) == 0:
        return max
    return find_max(input[1:], (input[0] if input[0] > max else max))

find_max([1,2,3,45,3,1,54,567,52])

