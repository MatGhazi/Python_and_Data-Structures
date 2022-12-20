import time 

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time() - start
        print(f"It takes  {end} seconds")
    return wrapper

@timer
def new_task():
    time.sleep(2)
    
new_task()
