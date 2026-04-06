# Cocotb-GHDL CI/CD Template

## Overview

This document describes the automated verification pipeline for VHDL-based designs in a simple fashion (easy-to-scale). The pipeline utilizes GHDL for simulation and Cocotb for Python-based verification. It is executed via GitHub Actions to ensure continuous testing of hardware logic.

### Dependencies

- **Simulation/Verification:**
  - `Python`
  - `Cocotb`
  - `GHDL`
- **GitHub Actions:**
  - `actions/checkout@v4`
  - `ghdl/setup-ghdl@v1`
  - `mikepenz/action-junit-report@v4`

## File System Structure

The repository must maintain the following structure for the automated scripts to resolve paths correctly:

- `src/`: Directory containing all VHDL source files (.vhd).
- `tests/`: Directory containing Python test modules (.py) and the Makefile.
- `.github/workflows/`: Directory containing the YAML pipeline configuration.

## Cocotb Runner

```py
import os
from pathlib import Path

from cocotb_tools.runner import get_runner

def run_tests():
    sim = os.getenv("SIM", "ghdl")

    proj_path = Path(__file__).resolve().parent

    sources = [proj_path / "../src/example.vhd"] # !!! Add more sources here !!!

    runner = get_runner(sim)
    runner.build(
        sources=sources,
        hdl_toplevel="example",
    )

    runner.test(hdl_toplevel="example", test_module="basic_test")
    runner.test(hdl_toplevel="example", test_module="random_test")

    # !!! Add more test here !!! #

if __name__ == "__main__":
    run_tests()
```

---

#### Maintenance Notes

- Artifact Retention: The JUnit XML results are retained by GitHub for a period defined by the repository's retention policy, allowing for historical audit of design stability.