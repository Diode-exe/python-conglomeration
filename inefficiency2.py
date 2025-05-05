import time
import math
from multiprocessing import Process, Queue

def slow_pi():
    # Bailey–Borwein–Plouffe formula for pi
    pi = sum(1/16**k * (
        4/(8*k+1) - 2/(8*k+4) - 1/(8*k+5) - 1/(8*k+6)
    ) for k in range(1000))
    return pi

def calculate_char(target_ascii, q):
    # Just to waste CPU for no reason
    _ = slow_pi()
    time.sleep(0.5)  # Simulate I/O delay
    q.put(chr(target_ascii))

def print_hello_world():
    chars = [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]
    processes = []
    q = Queue()

    for ascii_val in chars:
        p = Process(target=calculate_char, args=(ascii_val, q))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    output = ''
    while not q.empty():
        output += q.get()

    print("Output:", output)

print("Launching incredibly inefficient print operation...")
start = time.time()
print_hello_world()
end = time.time()
print(f"Done! Took {end - start:.2f} seconds. Completely unnecessary.")
