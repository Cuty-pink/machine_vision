import numpy as np

x = np.arange(32)
x.shape = (8, 4)
# x = np.arange(32).reshape(8, 4)
print(x)
print(x.shape)  # 返回维度元组
print(x[[4, 2, 1, 7]])
print(x[[-4, -2, -1, -7]])
# 迭代器对象
# 迭代顺序默认行序优先
z = np.arange(6).reshape(3, 2)
for i in np.nditer(z):
    print(i, end=",")
print("\n")

# "F"表示列序优先， "C"表示行序优先
for i in np.nditer(z.T.copy(order="C")):
    print(i, end=",")
print("\n")
for i in np.nditer(z.T.copy("F")):
    print(i, end=",")
print("\n")
# nditer对象有一个可选参数：op_flags ——> (read_write, write_only), 默认为只读read_only
for i in np.nditer(z, op_flags=["readwrite"]):
    i[...] = 2 * i
print(z)
# external_loop 表示给出的值是具有多个值的一维数组，而不是零维数组
for i in np.nditer(z, flags=["external_loop"], order="F"):
    print(i, end=",")
