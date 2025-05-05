options = input("Way to print hello world? ")
if options == "1":
    import time
    import math

    # Unnecessarily deep nested functions for each letter
    def get_H():
        def level1():
            def level2():
                return chr(int(math.sqrt(7225)))  # sqrt(7225) == 85 == 'U', then offset
            return chr(ord(level2()) - 13)
        return level1()

    def get_e():
        return chr(sum([ord('a') - 1 for _ in range(5)]))  # 'e' == 101

    def get_l():
        return chr(int("66", 8) + 21)  # Octal conversion

    def get_o():
        i = 0
        while i < 5000000:  # Just to waste time
            i += 1
        return chr(111)

    def get_comma():
        return chr(ord('.') - 2)

    def get_space():
        return " " * int(math.sqrt(1))

    def get_w():
        return chr(ord('v') + 1)

    def get_r():
        r = 50
        for _ in range(1000000):  # Waste more time
            r += 0
        return chr(r + 64)

    def get_d():
        return chr(int("144") - 43)

    def get_excl():
        return chr(0b100001)

    # Useless recursive Fibonacci to stall
    def slow_fib(n):
        if n <= 1:
            return n
        return slow_fib(n-1) + slow_fib(n-2)

    # Spin the CPU before printing
    print("Calculating inefficiency...")
    slow_fib(30)

    # Print the letters, one by one, with artificial delay
    output = (
        get_H() + get_e() + get_l() + get_l() + get_o() +
        get_comma() + get_space() + get_w() +
        get_o() + get_r() + get_l() + get_d() + get_excl()
    )

    for c in output:
        print(c, end="", flush=True)
        time.sleep(0.2)

    print("\nDone! That only took way too long.")
elif options == "2":
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
elif options == "3":
    import time
    from multiprocessing import Process, Queue

    def slow_pi():
        # Just a CPU-hogging calculation
        pi = sum(1/16**k * (
            4/(8*k+1) - 2/(8*k+4) - 1/(8*k+5) - 1/(8*k+6)
        ) for k in range(1000))
        return pi

    def calculate_char(index, target_ascii, q):
        _ = slow_pi()
        time.sleep(0.5)  # Fake I/O delay
        q.put((index, chr(target_ascii)))

    def print_hello_world():
        text = "Hello, world!"
        processes = []
        q = Queue()

        for i, char in enumerate(text):
            p = Process(target=calculate_char, args=(i, ord(char), q))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

        results = []
        while not q.empty():
            results.append(q.get())

        results.sort(key=lambda x: x[0])  # Sort by index
        output = ''.join(char for _, char in results)
        print("Output:", output)

    print("Launching painfully inefficient 'Hello, world!'...")
    start = time.time()
    print_hello_world()
    end = time.time()
    print(f"Done in {end - start:.2f} seconds. This is a crime against efficiency.")
elif options == "4":
    import base64
    import tempfile
    import subprocess
    import time
    import os
    
    text = "Hello, world!"
    temp_files = []
    
    def encode_char(c):
        encoded = base64.b64encode(c.encode()).decode()
        return encoded
    
    def launch_subprocess(index, c):
        encoded = encode_char(c)
        tmp = tempfile.NamedTemporaryFile(delete=False, mode='w+t')
        tmp.write(f"{index}:{encoded}")
        tmp.close()
        temp_files.append(tmp.name)
    
        python_code = (
            f"import time, base64; "
            f"time.sleep(2); "
            f"f=open('{tmp.name}', 'r'); "
            f"line=f.read(); "
            f"idx,b64=line.strip().split(':'); "
            f"char=base64.b64decode(b64).decode(); "
            f"f.close(); "
            f"f=open('{tmp.name}', 'w'); "
            f"f.write(f'{{idx}}:{{char}}'); "
            f"f.close()"
        )
    
        subprocess.call(["python3", "-c", python_code])
    
    print("Initiating ultra inefficient Hello, world!")
    for idx, char in enumerate(text):
        launch_subprocess(idx, char)
    
    time.sleep(3)  # Add insult to injury
    
    letters = []
    for fname in temp_files:
        with open(fname, 'r') as f:
            line = f.read()
            idx, char = line.strip().split(':')
            letters.append((int(idx), char))
        os.remove(fname)
    
    letters.sort()
    output = ''.join(char for _, char in letters)
    
    # Dramatic rendering
    for char in output:
        time.sleep(0.3)
        print(char, end='', flush=True)
    
    print("\nDone. The inefficiency is strong with this one.")
    