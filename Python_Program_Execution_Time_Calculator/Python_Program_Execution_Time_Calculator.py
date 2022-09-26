from time import time
start = time()

for i in range(1000):
    for j in range(1000):
        i=i+1

end = time()
execution_time = end - start
print("Execution Time : ", execution_time)