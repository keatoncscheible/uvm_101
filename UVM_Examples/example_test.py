# Example Python Test

import uvm

class ExampleTest(uvm.UvmTest):
    def build_phase(self, phase):
        # Testbench setup code
        pass

    def run_phase(self, phase):
        # Testbench run code
        pass

uvm.run_test(ExampleTest)
