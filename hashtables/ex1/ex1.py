#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    # initialize a hash table
    ht = HashTable(16)
    # add the first weight to the hash table
    hash_table_insert(ht, weights[0], 0)
    # initialize a current index
    cur_index = 1
    # loop incrementally adding weights and checking against limit
    while cur_index < length:
        cur_weight = weights[cur_index]
        # insert the new weight to the hash table
        hash_table_insert(ht, cur_weight, cur_index)
        # calculate needed pair
        needed_pair = limit - cur_weight
        # check too see whether the needed pair exists in the hash table
        target = hash_table_retrieve(ht, needed_pair)
        if target:
            # handle case where pair is found at (0,1)
            if cur_index == 1:
                return (cur_index, 0)
            # order the pair with largest index first
            elif target > cur_index:
                return (target, cur_index)
            else:
                return (cur_index, target)
        # increment the cur_index
        cur_index += 1
    # return None if limit is not met by end of loop
    return None

def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
