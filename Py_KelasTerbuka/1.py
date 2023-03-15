import time
start_time = time.time()

nama = "fj"

print ("hello world")
print ("hello fj")
print (f"okeh {nama}")

for i in range (1,1000):
    a = 10

print(time.time() - start_time, "detik")
# compile file akan lebih cepet daripada interpret
# cara compile = python -m py_compile nama file