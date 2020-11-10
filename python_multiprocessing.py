# 理解Python的多进程并行处理
# 通过python的multiprocessing库，Pool类

import multiprocessing
from multiprocessing import Pool
import time

# num是数据列表中的一个元素，run是map中对数据列表中每个元素做的操作
def run(num):
    time.sleep(1)
    return num * num

if __name__ == '__main__':
    print("== 通过python的multiprocessing库，Pool类,理解Python的多进程并行处理 ==")
    print("="*20, "并行处理", "="*20)
    data = [1, 2, 3, 4, 5, 6]
    start = time.time()         # 记录起始时间
    cores = multiprocessing.cpu_count()  # 获取机器的cpu核数, 12
    pool = Pool(cores)          # Pool类可以提供指定数量的进程供用户调用，当有新的请求提交到Pool中时，如果池还没有满，就会创建一个新的进程来执行请求
    # print(cores)
    result = pool.map(run, data)        # run函数处理data数据列表
    pool.close()                #关闭进程池，不再接受新的进程
    pool.join()                 #主进程阻塞等待子进程的退出
    # print(result)
    end = time.time()           # 记录结束时间
    print("处理时间：", end - start)
    print("处理结果：", result)

    print("=" * 20, "顺序处理", "=" * 20)
    start_ = time.time()
    result_ = [run(d) for d in data]
    end_ = time.time()
    print("处理时间：", end_ - start_)
    print("处理结果：", result_)
