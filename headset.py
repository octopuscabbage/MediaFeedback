import mindwave, time

class Headset:
    def __init__(self):
        self.headset = mindwave.Headset('/dev/ttyUSB0')
        time.sleep(2)

        self.headset.autoconnect()
        print("Connecting...")

        while self.headset.status != 'connected':
            time.sleep(0.5)
            if self.headset.status == 'standby':
                self.headset.connect()
                print("Retrying connect...")
        print("Connected.")

        self.attention_sum = 0;
        self.attention_readings = 0;
        self.headset.attention_handlers.append(self.attention_handler)
    def attention_handler(self, headset, attention):
        print("Attention handler called %i" % (attention))
        self.attention_sum += attention
        self.attention_readings += 1
    def report_average(self):
        return self.attention_sum / self.attention_readings
    def reset_attention_reading(self):
        self.attention_sum = 0
        self.attention_readings = 0

