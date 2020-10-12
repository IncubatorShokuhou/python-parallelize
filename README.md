python-parallelize
==================
人肉闭包好！
==================
Simple fork/join parallelism with Python's `for` loop



Quick Start
-----------

Installation

```shell
pip install git+https://github.com/IncubatorShokuhou/python-parallelize.git
```

Parallel iteration with a process/CPU:

```python
import os
from parallelize import parallelize
    
for i in parallelize(range(100),n_jobs = "half"):   
#n_jobs can be "all","half","quarter" or any integer not more than the number of cpus( which can be caculated by multiprocessing.cpu_count())
    print(os.getpid(), i)
```
