import time

# measuring execution time
start_time = time.time()

time.sleep(10) 

# measuring execution time
end_time = time.time()

# calculating the total execution time
execution_time = end_time - start_time


print("Time "+"{:,.2f}".format(execution_time)+" seconds")