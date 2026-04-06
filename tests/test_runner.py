# test_runner.py

import os
from pathlib import Path

from cocotb_tools.runner import get_runner


def run_tests():
    sim = os.getenv("SIM", "ghdl")

    proj_path = Path(__file__).resolve().parent

    sources = [proj_path / "../src/example.vhd"]

    runner = get_runner(sim)
    runner.build(
        sources=sources,
        hdl_toplevel="example",
    )

    runner.test(hdl_toplevel="example", test_module="basic_test")
    runner.test(hdl_toplevel="example", test_module="random_test")


if __name__ == "__main__":
    run_tests()