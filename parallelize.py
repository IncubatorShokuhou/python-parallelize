
from itertools import islice
import os
import multiprocessing
__version__ = '1.0.0.0_qb'
def get_per_cpu(seq,n_jobs= "half"):
    if isinstance(n_jobs, int):
        n_jobs_in = n_jobs
    elif isinstance(n_jobs,float):
        n_jobs_in = int(n_jobs)
    elif isinstance(n_jobs,str):
        if n_jobs == "all":
            n_jobs_in = multiprocessing.cpu_count()
        elif n_jobs == "half":
            n_jobs_in = int( multiprocessing.cpu_count() / 2 )
        elif n_jobs == "quarter":
            n_jobs_in = int( multiprocessing.cpu_count() / 4 )
        else:
            try:
                n_jobs_in =int(n_jobs)
            except:
                print("Error,cannot recognize n_jobs.Please use an integer or 'all','half','quarter' ")
                raise
    if n_jobs_in > multiprocessing.cpu_count():
        print("n_jobs is too large. Turn into max cpu count.")
        n_jobs_in1 = min(n_jobs_in,multiprocessing.cpu_count())
        n_jobs_in = cpu_number_in1
    #print("cpu number:",cpu_number_in)
    def per_cpu(seq,n_jobs_in):
        return (islice(seq, cpu, None, n_jobs_in) for cpu in range(n_jobs_in))
    return per_cpu(seq,n_jobs_in)

def parallelize(seq,n_jobs= "half"):
    """
    input:
    seq: for loop
    n_jobs: number of cpu to be used. Default value is "half".
    """
    pids = []
    fork = get_per_cpu(seq,n_jobs=n_jobs)
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
    for i in parallelize(range(10),n_jobs = "half"):
        print(i)
        import time
        time.sleep(2)
