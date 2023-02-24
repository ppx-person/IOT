import time
print("begin")
start = time.ticks_ms()
time.sleep(1)
delta = time.ticks_diff(time.ticks_ms(), start)
print(delta)
print("end")