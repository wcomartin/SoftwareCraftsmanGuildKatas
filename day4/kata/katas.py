def reverse_a_list(lst, *args):
    new_list = args[0] if args else []
    if not lst:
        return args[0]
    new_list.append(lst.pop())
    return reverse_a_list(lst, new_list)

def compress_a_sequence(lst):
    def runner(lst, idx=0):
        new_idx = idx + 1
        val = None
        try:
            val = lst[new_idx]
        except IndexError:
            return lst

        if lst[idx] == val:
            try:
                lst.pop(new_idx)
            except AttributeError:
                lst = lst[:idx + 1] + lst[new_idx + 1:]
            finally:
                new_idx = idx

        return runner(lst, idx)
    return runner(lst)