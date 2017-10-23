from kaeruprofiler import profile_with_key


class Target:
    def __init__(self, key_data):
        self.key_data = key_data

    @profile_with_key('key_data')
    def run(self):
        print(self.key_data * 3)


Target('3').run()
Target('4').run()
Target('3').run()
