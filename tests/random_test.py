import cocotb
import random
from cocotb.triggers import Timer

def generate_rd_input():
    """Generate random input values."""
    a = random.randint(0, 1)
    b = random.randint(0, 1)
    return a, b

@cocotb.test()
async def and_or_operations(dut):
    """Test the AND and OR operations."""    
    for _ in range(10): # Run 10 iterations with random inputs
        a, b = generate_rd_input()  # Generate random inputs
        dut.a.value = a
        dut.b.value = b
        await Timer(1, unit="ns")  # wait a bit for input to propagate
        cocotb.log.info("Testing with inputs: a=%s, b=%s, iteration: %d", a, b, _)
        cocotb.log.debug("and_res:   %s, expected: %s", dut.and_res.value, a & b)
        cocotb.log.debug("or_res:    %s, expected: %s", dut.or_res.value, a | b)
        assert dut.and_res.value == a & b, f"AND result is incorrect: {dut.and_res.value} != {a & b}"
        assert dut.or_res.value == a | b, f"OR result is incorrect: {dut.or_res.value} != {a | b}"
    