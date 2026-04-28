# Try and write as many different methods to remove duplicates from a list.
# Below are some example function names that may help hint at some possible options (do try and submit at least 2 different ways in order to challenge yourself).
# Try and include a sort function as well which will sort the list after duplicates have been removed and then print the list to the terminal.

# Reminder: below are just some example function names. These are just examples of 5 different ways to remove duplicates, and how to print sorted (there are more ways). Have fun, try your own approaches!
# sample_list = [1, 5, 3, 6, 3, 5, 6, 1, 2,7,7,9,0,0,11,-5,-3]

# print_list(remove_naive(sample_list))
# print_list(remove_conds(sample_list))
# print_list(remove_set(sample_list))
# print_list(remove_enum(sample_list))
# print_list(remove_coll(sample_list)) #uses OrderedDict

# #output expected

# [-5, -3, 0, 1, 2, 3, 5, 6, 7, 9, 11]
# [-5, -3, 0, 1, 2, 3, 5, 6, 7, 9, 11]
# [-5, -3, 0, 1, 2, 3, 5, 6, 7, 9, 11]
# [-5, -3, 0, 1, 2, 3, 5, 6, 7, 9, 11]
# [-5, -3, 0, 1, 2, 3, 5, 6, 7, 9, 11]

def sort(ls): 
    for i in range(len(ls)): 
        for j in range(0, len(ls) - i - 1):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
    
    return ls 

def remove_set(ls): 
    return sort(list(set(ls)))

def remove_loop(ls): 
    final = []

    for i in ls:
        if i not in final: 
            final.append(i)
            
    return sort(final) 


from collections import OrderedDict

def remove_dict(ls): 
    return sort(list(OrderedDict.fromkeys(ls)))


def main():
    sample_list = [1, 5, 3, 6, 3, 5, 6, 1, 2, 7, 7, 9, 0, 0, 11, -5, -3]

    print(remove_set(sample_list))
    print(remove_loop(sample_list))
    print(remove_dict(sample_list))

if __name__ == "__main__":
    main()
