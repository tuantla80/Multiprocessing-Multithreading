'''
In general, it is not recommended to mix multiprocessing and multithreading
together in the same program. In some special cases, however, we many combine
them as an below example.
Author: TLA. Tuan
Last update: 2019-12-31
'''

import multiprocessing
import threading
import time


def do_something(values, name):
    '''
    INPUT:
    values: a list of values
    name: a string (name) corresponding with values (list)
    OUTPUT:
    results: as a list

    EXAMPLE:
    > results = do_something(values=[1, 2, 3], name='test')
    > results = [{'test': 2}, {'test': 4}, {'test': 6}]
    '''
    results = []
    for v in values:
        time.sleep(v)  # Assuming this part will take time in real application
        results.append({name: v * v})  # Just an example to return something
        print('results = ', results)
    return results


def make_multi_threads(values, name):
    '''
    Purpose: to spawn multi threads for each process
    Without lack of generalization, we assume number of threads equals to
    length of values.

    INPUT:
    values: a list of values.
    name: a string
    OUTPUT
    Thread will be spawned an run the do_something() function
    '''
    num_threads = len(values)

    print('\nvalues = {}, name = {} with num_threads = {}'
          .format(values, name, num_threads))

    threads = []
    for i in range(num_threads):
        _values_at_this_thread = [values[i]]  #even one value, need a list type
        thread = threading.Thread(target=do_something,
                                  args=(_values_at_this_thread, name))
        print('Run at process= {} with thread = {}'.format(
            multiprocessing.current_process().name, thread.name))

        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    return None


def run_multiprocessesing_with_multithreading(num_processes, values, name):
    '''
    Purpose: To run run multiprocessesing mixing with multithreading
    INPUT:
    num_processes: number of processes
    values: a list of values (rf. do_something() function)
    name: a string (name) corresponding with values (list)
    OUTPUT:
    - run do_something() function on multithreading
    '''
    num_threads = len(values) // num_processes + 1

    # Running multi processes with multithreading
    processes = []
    for i in range(num_processes):
        _values_at_this_process = values[i*num_threads: (i+1)*num_threads]
        # print('_values_at_this_process = ', _values_at_this_process)
        process = multiprocessing.Process(target=make_multi_threads,
                                          args=(_values_at_this_process, name))

        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    return None


if __name__ == "__main__":
    time_start = time.time()
    # INPUT PARAMETERS
    values =  [1, 2, 3, 4, 5]  #  [2, 2, 2, 2, 2]
    name = 'test'
    num_processes = 2  # Decide to run 2 CPUs

    # Run
    run_multiprocessesing_with_multithreading(num_processes, values, name)
    print('total time = {} seconds'.format(time.time() - time_start))
    print('The end!')

# The OUPUT
# C:\ProgramData\Anaconda3\python.exe D:/Parallel/multiprocessing_multithreading.py

# TEST 1: values = [1, 2, 3, 4, 5]
# values = [1, 2, 3], name = test with num_threads = 3
# Run at process= Process-1 with thread = Thread-1
# Run at process= Process-1 with thread = Thread-2
# Run at process= Process-1 with thread = Thread-3
#
# values = [4, 5], name = test with num_threads = 2
# Run at process= Process-2 with thread = Thread-1
# Run at process= Process-2 with thread = Thread-2

# results =  [{'test': 1}]
# results =  [{'test': 4}]
# results =  [{'test': 9}]
# results =  [{'test': 16}]
# results =  [{'test': 25}]
# total time = 5.174933195114136 seconds
# The end!

# It is quite good since if run sequential, we need sum([1, 2, 3, 4,
# 5]) = 15s since we make sleep for each element in values list.
# And note that in real application, we need to think how to divide values
# in a smart ways (refer to TEST 2)

# TEST 2: values = [2, 2, 2, 2, 2]
# values = [2, 2, 2], name = test with num_threads = 3
# Run at process= Process-1 with thread = Thread-1
# Run at process= Process-1 with thread = Thread-2
# Run at process= Process-1 with thread = Thread-3
#
# values = [2, 2], name = test with num_threads = 2
# Run at process= Process-2 with thread = Thread-1
# Run at process= Process-2 with thread = Thread-2

# results =  [{'test': 4}]
# results =  [{'test': 4}]
# results =  [{'test': 4}]
# results =  [{'test': 4}]
# results =  [{'test': 4}]
# total time = 2.1811118125915527 seconds
# The end!

