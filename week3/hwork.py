# Python代码，需要在Python环境下运行
# 声明编码格式为UTF-8
# 有两个文件A和B，每个文件里存储了一行字母，要求将这两个文件合并到一起（按字母顺序排序），并输出到一个新文件C中
if __name__ == '__main__':
    # 打开文件file1.txt，并读取所有内容到变量a中
    fp = open(r'file1.txt')  # r表示不转义
    a = fp.read()  # read()方法用于从文件读取指定的字节数，如果未给定或为负则读取所有。
    fp.close()  # 关闭文件
    # 打开文件file2.txt，并读取所有内容到变量b中
    fp = open(r'file2.txt')  # r表示不转义
    b = fp.read()  # read()方法用于从文件读取指定的字节数，如果未给定或为负则读取所有。
    fp.close()
    # 打开文件file3.txt并准备写入合并后的内容
    fp = open(r'file3.txt', 'w')
    # 将a和b连接成一个列表，并按字母顺序排序
    l = list(a + b)  # list() 方法用于将元组转换为列表。
    l.sort()  # sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
    # 将排序后的列表转换成一个字符串
    s = ''
    s = s.join(l)
    # 将排序后的字符串写入到file3.txt中
    fp.write(s)
    fp.close()
 # 定义一个读取文件的函数


def read(filename):  # filename是形参
    # 打开文件并读取所有行
    f = open(filename, "r+")  # r+表示可读可写
    a = f.readlines()  # readlines() 方法用于读取所有行(直到结束符 EOF)并返回列表，该列表可以由 Python 的 for... in ... 结构进行处理。如果碰到结束符 EOF 则返回空字符串。
    # 返回读取到的所有行
    return a

 # 将file1.txt和file2.txt中的内容读取到一个列表中并连接，然后按字母顺序排序
# r表示不转义    #list() 方法用于将元组转换为列表。  #join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
s = list("".join(read(r'file1.txt')+read(r'file2.txt')))
s.sort()
# 将排序后的字符串写入到test.txt中
s1 = "".join(s)  # join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
t = open("test.txt", "w+")  # w+表示可读可写
# writelines() 方法用于向文件中写入一序列的字符串。这一序列字符串可以是由迭代对象产生的，如一个字符串列表。每个字符串后会加上换行符。
t.writelines(s1)
t.close()  # 关闭文件
