import mindwave, time
import numpy as np
import matplotlib.pyplot as plt


headset = mindwave.Headset('/dev/ttyUSB0')
time.sleep(2)

headset.connect()
print("Connecting...")

while headset.status != 'connected':
    time.sleep(0.5)
    if headset.status == 'standby':
        headset.connect()
        print("Retrying connect...")
print("Connected.")

i = 0;
while True:
    print("Attention: %s, Meditation: %s" % (headset.attention, headset.meditation))
    print("Strength: %s" % (headset.poor_signal))
    i += 1
    print(headset.status)
    plt.scatter(i, headset.attention,[255,0,0]);
    plt.scatter(i, headset.meditation);


    plt.pause(0.05)

plt.show()
