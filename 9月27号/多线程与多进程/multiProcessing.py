# 多进程 multiProcessing
from multiprocessing import Process, Pool
import os, time, random


# print('process %s staring' % os.getgid())
# pid = os.fork()
# if pid == 0:
#     print('I am child_process %s, my parent_process is %s' % (os.getpid(), (os.getppid())))
# else:
#     print('I %s just created a child_process %s' % (os.getpid(), pid))


# 子进程要执行的代码
def run_process(name):
    print('run child process %s--%s' % (name, os.getpid()))


# if __name__ == '__main__':
#     print('parent process %s' % os.getgid())
#     child_p = Process(target=run_process, args=('test',))
#     print("child process will start")
#     child_p.start()
#     child_p.join()
#     print("child process ended")


# 进程池

def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start_time = time.time()
    time.sleep(random.random() * 3)
    end_time = time.time()
    print('Task %s runing %.2f second' % (os.getpid(), (end_time - start_time)))


if __name__ == '__main__':
    print("parent process is %s " % os.getpid())
    mzp_pool = Pool(4)
    for i in range(5):
        mzp_pool.apply_async(long_time_task, args=(i,))
    print('waiting for all process done')
    mzp_pool.close()
    mzp_pool.join()
    print("all child process done")