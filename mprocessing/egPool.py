import multiprocessing
import time
#https://stackoverflow.com/questions/20887555/dead-simple-example-of-using-multiprocessing-queue-pool-and-locking

data = (
    ['a', '2'], ['b', '4'], ['c', '6'], ['d', '8'],
    ['e', '1'], ['f', '3'], ['g', '5'], ['h', '7']
)

the_time=5
def mp_worker(inputs):
    print (" Processs %s\tWaiting %s seconds" % (inputs, the_time))
    time.sleep(int(the_time))
    print (" Process %s\tDONE" % inputs)

def mp_handler():
    p = multiprocessing.Pool(2)
    p.map(mp_worker, data)
    
    
#If you want "a lock for each pool limit" so that your processes run in tandem pairs, ala:
#A waiting B waiting | A done , B done | C waiting , D waiting | C done, D done | ...    

def mp_handler_pair():
    subdata = zip(data[0::2], data[1::2])
    for task1, task2 in subdata:
        p = multiprocessing.Pool(2)
        p.map(mp_worker, (task1, task2))

if __name__ == '__main__':
    #mp_handler_pair()
    mp_handler()