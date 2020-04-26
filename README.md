python-parallelize
==================

Simple fork/join parallelism with Python's `for` loop

人肉闭包好！

Quick Start
-----------

Installation

pip install git+https://github.com/IncubatorShokuhou/python-parallelize.git

Parallel iteration with a process/CPU:

```python
import os
from parallelize import parallelize
    
for i in parallelize(range(100),cpu_number = "half"):   #cpu_number can be "all","half","quarter" or any integer
    print(os.getpid(), i)
```
