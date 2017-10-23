import time
from kaeruprofiler import profile_with_key, init


class Target:
    def __init__(self, key_data):
        self.key_data = key_data

    @profile_with_key('key_data')
    def run(self):
        time.sleep(1)


init()
Target('3').run()
Target('4').run()
Target('3').run()
Target('3').run()
Target('5').run()
Target('6').run()
Target('4').run()
