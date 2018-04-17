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
        self.headset.poor_signal_handlers.append(self.poor_signal_handler)
        #self.headset.disconnected_handlers.append(self.disconected_handler)
    def attention_handler(self, headset, attention):
        #print("Attention handler called %i" % (attention))
        self.attention_sum += attention
        self.attention_readings += 1
    def poor_signal_handler(self,headset, poor_signal):
        print("poor signal: ", str(poor_signal))
    def disconected_handler(self, headset):
        print("Headset disconected OOPS!")
    def report_average(self):
        if self.attention_readings == 0:
            return 50
        return self.attention_sum / self.attention_readings
    def reset_attention_reading(self):
        self.attention_sum = 0
        self.attention_readings = 0

