import sys


def fibonacci(n):  # 定义一个生成器函数，生成n个斐波那契数列的数
    a, b, counter = 0, 1, 0  # 初始化变量a、b和counter
    while True:  # 进入无限循环
        if (counter > n):  # 判断counter是否大于n
            return  # 如果是，退出函数
        yield a  # 产出当前的数
        a, b = b, a + b  # 更新斐波那契数列的值
        counter += 1  # counter加1


f = fibonacci(10)  # 创建一个生成器对象f，生成10个斐波那契数列的数
while True:  # 进入无限循环
    try:
        print(next(f), end=" ")  # 打印生成器中的下一个数
    except StopIteration:  # 捕捉异常
        sys.exit()  # 退出程序
a