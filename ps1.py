###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    #pass
    dup_cows=cows.copy()
    remaining=limit
    All_trips=[]
    one_trip=[]
    while dup_cows!={}:
        a=findmaxcowwithinremaining(dup_cows,remaining)
        if a!='':
            remaining-=dup_cows[a]
            one_trip.append(a)
            del dup_cows[a]
        else:
            All_trips.append(one_trip)
            one_trip=[]
            remaining=limit
    All_trips.append(one_trip)
    return All_trips

def findmaxcowwithinremaining(dup_cows,remaining):
    maxi=0
    maxcow=''
    for i in dup_cows:
        if maxi<dup_cows[i] and dup_cows[i]<=remaining:
            maxcow=i
            maxi=dup_cows[i]
    return maxcow            
                        
    
# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    #pass
    #print(cows)
    cs=list(cows.keys())
    csp=get_partitions(cs)
    prevcsplen=float('inf')
    finali=[]
    for i in csp:
        found=True
        for k in i:
            tripsummer=0
            for j in k:
                tripsummer+=cows[j]
            if tripsummer>limit: #or (tripsummer==limit and len(i)>1):
                found=False
                break
        if found==True:
            if prevcsplen>len(i):
                finali=i
                prevcsplen=len(i)                
            #return i
    return finali     

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    #pass
    cows = load_cows("ps1_cow_data.txt")
    limit=10
    start=time.time()
    a=greedy_cow_transport(cows, limit)
    end=time.time()
    print(len(a))
    print(end-start)
    start=time.time()
    b=brute_force_cow_transport(cows, limit)
    print(len(b))
    end=time.time()
    print(end-start)

"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

#cows = load_cows("ps1_cow_data.txt")
limit=100
cows={'Miss Bella': 25, 'MooMoo': 50, 'Horns': 25, 'Lotus': 40, 'Boo': 20, 'Milkshake': 40}
#print(cows)

#print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))
#compare_cow_transport_algorithms()

