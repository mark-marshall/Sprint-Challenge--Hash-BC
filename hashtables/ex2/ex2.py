#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # initializethe hash table
    hashtable = HashTable(length)
    #initialize an array for the route
    route = [None] * length
    # loop overthe tickets array and add them to the hash table
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    # add the starting destination to the route
    first_leg = hash_table_retrieve(hashtable, "NONE")
    route[0] = first_leg
    #loop over rest of route array to calculate each additional destination
    for i in (num + 1 for num in range(len(route) - 1)):
        route[i] = hash_table_retrieve(hashtable, route[i-1])
    #return the route
    return route
