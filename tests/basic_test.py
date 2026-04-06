import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def and_or_operations(dut):
    """Test the AND and OR operations."""
    a, b = 0, 0  # Generate random inputs
    dut.a.value = a
    dut.b.value = b
    await Timer(1, unit="ns")  # wait a bit for input to propagate
    cocotb.log.info("Testing with inputs: a=%s, b=%s", a, b)
    cocotb.log.debug("and_res:   %s, expected: %s", dut.and_res.value, a & b)
    cocotb.log.debug("or_res:    %s, expected: %s", dut.or_res.value, a | b)
    assert dut.and_res.value == a & b, f"AND result is incorrect: {dut.and_res.value} != {a & b}"
    assert dut.or_res.value == a | b, f"OR result is incorrect: {dut.or_res.value} != {a | b}"

    a, b = 0, 1  # Generate random inputs
    dut.a.value = a
    dut.b.value = b
    await Timer(1, unit="ns")  # wait a bit for input to propagate
    cocotb.log.info("Testing with inputs: a=%s, b=%s", a, b)
    cocotb.log.debug("and_res:   %s, expected: %s", dut.and_res.value, a & b)
    cocotb.log.debug("or_res:    %s, expected: %s", dut.or_res.value, a | b)
    assert dut.and_res.value == a & b, f"AND result is incorrect: {dut.and_res.value} != {a & b}"
    assert dut.or_res.value == a | b, f"OR result is incorrect: {dut.or_res.value} != {a | b}"

    a, b = 1, 0  # Generate random inputs
    dut.a.value = a
    dut.b.value = b
    await Timer(1, unit="ns")  # wait a bit for input to propagate
    cocotb.log.info("Testing with inputs: a=%s, b=%s", a, b)
    cocotb.log.debug("and_res:   %s, expected: %s", dut.and_res.value, a & b)
    cocotb.log.debug("or_res:    %s, expected: %s", dut.or_res.value, a | b)
    assert dut.and_res.value == a & b, f"AND result is incorrect: {dut.and_res.value} != {a & b}"
    assert dut.or_res.value == a | b, f"OR result is incorrect: {dut.or_res.value} != {a | b}"

    a, b = 1, 1  # Generate random inputs
    dut.a.value = a
    dut.b.value = b
    await Timer(1, unit="ns")  # wait a bit for input to propagate
    cocotb.log.info("Testing with inputs: a=%s, b=%s", a, b)
    cocotb.log.debug("and_res:   %s, expected: %s", dut.and_res.value, a & b)
    cocotb.log.debug("or_res:    %s, expected: %s", dut.or_res.value, a | b)
    assert dut.and_res.value == a & b, f"AND result is incorrect: {dut.and_res.value} != {a & b}"
    assert dut.or_res.value == a | b, f"OR result is incorrect: {dut.or_res.value} != {a | b}"

    