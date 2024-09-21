import time

def busy_wait(delay):
    """Busy-wait for a specified delay in seconds."""
    end_time = time.time() + delay
    while time.time() < end_time:
        pass  # Do nothing, just wait

def main():
    iterations = 100000  # Total number of iterations
    sleep_delay = 0.09  # Initial sleep delay in seconds
    previous_time = 0  # To store the time of the previous iteration

    for i in range(iterations):
        start_time = time.time()  # Record the start time
        
        # Simulate the delay using busy-waiting
        busy_wait(sleep_delay)
        
        end_time = time.time()  # Record the end time
        iteration_time = end_time - start_time  # Calculate iteration time
        
        # Calculate the difference in execution time from the previous iteration
        if i > 0:
            time_difference = iteration_time - previous_time
        else:
            time_difference = 0
        
        # Report the execution time and the difference
        print(f"Iteration {i + 1}:")
        # print(f"  Execution Time: {iteration_time:.30f} seconds")
        print(f"  Difference from Previous Iteration: {time_difference:.2f} seconds\n")

        # Update the previous_time for the next iteration
        previous_time = iteration_time

        # Gradually decrease the sleep delay for the next iteration
        sleep_delay *= 1.5  # Example: increase delay by 10%

if __name__ == "__main__":
    main()










