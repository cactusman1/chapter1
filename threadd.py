import threading
import time  # Import time module to measure execution time

def calc_fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return calc_fibonacci(n-1) + calc_fibonacci(n-2)

if __name__ == "__main__":  # Corrected "__main__" here
    threads = []
    
    # Start the timer before creating threads
    start_time = time.time()
    
    # Create and start 4 threads
    for i in range(4):
        t = threading.Thread(target=calc_fibonacci, args=(30,))
        threads.append(t)
        print(f"Starting thread {i+1}")
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()
    
    # Calculate the execution time after all threads are done
    end_time = time.time()
    
    print("All threads finished")
    print(f"Execution time: {end_time - start_time} seconds")

