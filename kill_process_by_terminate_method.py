import random
import multiprocessing
from time import sleep
import pandas as pd


def do_work(i):
    '''
    Note: in practice, usually it is a complicated function with many input arguments.
    '''
    print('Started at process = {}'.format(i))
    x = round(random.random(), 2)
    sleep(0.2)  # A dummy of a expensive calculation
    print("at proccess = {}: generated value = {} ".format(i, x))
    return x


def run_and_terminate_process(num_runs=2, num_procs=3, target_value=0.9):
    '''
    :param num_runs: Numnber of times to run by making Pool. In practice,
                     it may be run with a different set of arguments
    :param num_procs: Number of processes.

    NOTE: If one process met a certain condition, it will terminate all
    processes. Otherwise, it will run and stop as normal
    :return:
    '''
    all_outputs = []
    for num_run in range(num_runs):
        print('\n\nAt num_runs = ', num_run)
        p = multiprocessing.Pool(num_procs)

        list_x = []  # To store output of this num_run

        # A callback function
        def check_x_value(x):
            list_x.append(x)
            # Note: p is visible (in the scope of run_and_terminate_process())
            if x > target_value:
                p.terminate()  # To kill all pool workers
                print("Terminating at x = {}".format(x))
			else:
				pass  # it will wait for another process to be finished to check the condition
				      # and if all the processes did not meet the condition, it will finish as normal.
        # End of callback function

        # Run for every process
        for i in range(num_procs):
            p.apply_async(do_work, args=(i,), callback=check_x_value)
        # End of for i ...
        p.close()
        p.join()
        all_outputs.append(list_x)
    return all_outputs


if __name__ == '__main__':
    all_outputs = run_and_terminate_process(num_runs=2,
                                            num_procs=3,
                                            target_value=0.9)
    print('all_outputs = ', all_outputs)

'''
C:\ProgramData\Anaconda3\python.exe D:\Code\kill_process_using_terminate_method.py
---------------------------------------
TEST 1: 
NO process can generate a value > 0.9 so it run all process and finish the
program normally.

At num_runs =  0
Started at process = 0
at proccess = 0: generated value = 0.04
Started at process = 1
at proccess = 1: generated value = 0.55
Started at process = 2
at proccess = 2: generated value = 0.28

At num_runs =  1
Started at process = 0
at proccess = 0: generated value = 0.06
Started at process = 1
at proccess = 1: generated value = 0.46
Started at process = 2
at proccess = 2: generated value = 0.12


all_outputs =  [[0.04, 0.55, 0.28], [0.06, 0.46, 0.12]]

---------------------------------------
TEST 2:
At num_runs =  0
Started at process = 0
Started at process = 1
Started at process = 2
at proccess = 0: generated value = 0.95 
at proccess = 1: generated value = 0.08 

Terminating at x = 0.95  # So in fact process 2 still not generated value 
but it has been terminate


At num_runs =  1
Started at process = 0
Started at process = 1
Started at process = 2
at proccess = 0: generated value = 0.45 
at proccess = 1: generated value = 0.93 
at proccess = 2: generated value = 0.86 
Terminating at x = 0.93  # Terminating at x = 0.93 but other processes have
been already generated

all_outputs =  [[0.95], [0.45, 0.93]]  # Note some output may not be 
collected if the proccess is terminated immediately after meeting the condition
'''
