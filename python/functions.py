import time

def wave(sleep_time):
    print("Hello")
    time.sleep(sleep_time)
    print(" Hello")
    time.sleep(sleep_time)
    print("  Hello")
    time.sleep(sleep_time)
    print("   Hello")
    time.sleep(sleep_time)
    print("  Hello")
    time.sleep(sleep_time)
    print(" Hello")
    time.sleep(sleep_time)
    print("Hello")
    time.sleep(sleep_time)

for i in range(0,10):
    wave(.3) #we call the wave function and make sleep_time = .1