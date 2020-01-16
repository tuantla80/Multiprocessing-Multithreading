import random
import multiprocessing
from time import sleep


list_x = []
def do_work(i, terminate, met_condition, target_value):

	while not terminate.is_set():  # It will do until a process meets a certain condition
		x = round(random.random(), 2)
		print("at proccess = {}: generated value = {} ".format(i, x))
		list_x.append(x)
		if x > target_value:  # the certain condition
			print("Terminating at x = {}".format(x))
			met_condition.set()
			break
	# End of while
	print ("process {} is done".format(i))
	# sleep(0.1)  # meaning that it is quite a expensive calculation
	#return None


def run_and_terminate_by_event(num_runs=2, num_procs=3, target_value=0.9):

	all_outputs = []
	for num_run in range(num_runs):
		print('\n\nAt num_run = ', num_run)
		terminate = multiprocessing.Event()
		met_condition = multiprocessing.Event()
 
		for i in range(num_procs):
			p = multiprocessing.Process(target=do_work, 
			                            args=(i, terminate, met_condition, target_value))
			p.start()
		# End of for i
		met_condition.wait()
		terminate.set()

		
if __name__ == '__main__':
	all_outputs = run_and_terminate_by_event(num_runs=2, 
                                        	num_procs=2, 
                                        	target_value=0.8)
	
	print('all_outputs = ', all_outputs)