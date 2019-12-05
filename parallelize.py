
from itertools import islice
import os
import multiprocessing
__version__ = '1.0.0.0_qb'
def get_per_cpu(seq,cpu_number= "half"):
    if isinstance(cpu_number, int):
        cpu_number_in = cpu_number
    elif isinstance(cpu_number,float):
        cpu_number_in = int(cpu_number)
    elif isinstance(cpu_number,str):
        if cpu_number == "all":
            cpu_number_in = multiprocessing.cpu_count()
        elif cpu_number == "half":
            cpu_number_in = int( multiprocessing.cpu_count() / 2 )
        elif cpu_number == "quarter":
            cpu_number_in = int( multiprocessing.cpu_count() / 4 )
        else:
            try:
                cpu_number_in =int(cpu_number)
            except:
                print("error,cannot recognize cpu number")
    if cpu_number_in > multiprocessing.cpu_count():
        print("cpu number is too large. Turn into max cpu count.")
        cpu_number_in1 = min(cpu_number_in,multiprocessing.cpu_count())
        cpu_number_in = cpu_number_in1
    #print("cpu number:",cpu_number_in)
    def per_cpu(seq,cpu_number_in):
        return (islice(seq, cpu, None, cpu_number_in) for cpu in range(cpu_number_in))
    return per_cpu(seq,cpu_number_in)

def parallelize(seq,cpu_number):
    pids = []
    fork = get_per_cpu(seq,cpu_number=cpu_number)
    for slice in fork:
        pid = os.fork()
        if pid == 0:
            for item in slice:
                yield item
            os._exit(0)
        else:
            pids.append(pid)
    
    for pid in pids:
        os.waitpid(pid,0)

if __name__ == '__main__':
    for i in parallelize(range(10),cpu_number = "half"):
        print(i)
        import time
        time.sleep(2)