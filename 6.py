#6. Write a python program to Generate Fibonacci Sequence.

n_0_0030 = 0
n_1_0030 = 1
print(n_0_0030,"\n",n_1_0030)

count_0030 = 10

while (count_0030-2)>0:
    n_val_0030 = n_0_0030 + n_1_0030
    n_0_0030 = n_1_0030
    n_1_0030 = n_val_0030
    count_0030 = count_0030-1
    print(n_val_0030," ")