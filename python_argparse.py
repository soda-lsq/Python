# 理解python中的argparse模块, argparse 模块可以让人轻松编写用户友好的命令行接口。
# 程序定义它需要的参数，然后 argparse 将弄清如何从 sys.argv 解析出那些参数。
# argparse 模块还会自动生成帮助和使用手册，并在用户给程序传入无效参数时报出错误信息。

import argparse
from pprint import pprint

'''
使用argparse主要有三个步骤：
1. 创建 ArgumentParser() 对象
2. 调用 add_argument() 方法添加参数
3. 使用 parse_args() 解析添加的参数
'''

print("----- 理解python中的argparse模块, argparse 模块可以让人轻松编写用户友好的命令行接口。-----")

print("1. 创建解析器对象")
parser = argparse.ArgumentParser()

print("2. 添加参数 - 可单独放在args.py文件中，再在主文件中调用args.py中的model_args()方法完成参数添加")
print("   下面以深度学习常用参数为例，格式为'--'前缀 + 可选参数名 + 定义type + default默认值 + 参数描述help")
parser.add_argument('--batch-size', type=int, default=64, metavar='N',
                        help='input batch size for training (default: 64)')
parser.add_argument('--momentum', type=float, default=0.5, metavar='M',
                        help='SGD momentum (default: 0.5)')
parser.add_argument('--no-cuda', action='store_true', default=False,
                        help='disables CUDA training')
parser.add_argument('--save-model', action='store_true', default=False,
                        help='For Saving the current Model')

print("3. 解析参数")
# ArgumentParser 通过 parse_args() 方法解析参数。它将检查命令行，把每个参数转换为适当的类型然后调用相应的操作。
args = parser.parse_args()

print("4. 打印参数，使用vars(), pprint()")
pprint(vars(args))
'''
· vars() 函数返回对象object的属性和属性值的字典对象。

· pprint()模块打印出来的数据结构更加完整，每行为一个数据结构，更加方便阅读打印输出结果。
特别是对于特别长的数据打印，print()输出结果都在一行，不方便查看，而pprint()采用分行打印输出.
所以对于数据结构比较复杂、数据长度较长的数据，适合采用pprint()打印方式。当然，一般情况多数采用print()。
'''


