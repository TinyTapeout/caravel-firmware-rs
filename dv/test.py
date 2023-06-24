import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, with_timeout, ClockCycles

@cocotb.test()
async def test_blinky(dut):
    clock = Clock(dut.clk, 25, units="ns") # 40 MHz
    cocotb.start_soon(clock.start())

    # Start caravel
    dut.RSTB.value = 0
    dut.power1.value = 0
    dut.power2.value = 0
    dut.power3.value = 0
    dut.power4.value = 0

    await ClockCycles(dut.clk, 8)
    dut.power1.value = 1
    await ClockCycles(dut.clk, 8)
    dut.power2.value = 1
    await ClockCycles(dut.clk, 8)
    dut.power3.value = 1
    await ClockCycles(dut.clk, 8)
    dut.power4.value = 1

    await ClockCycles(dut.clk, 80)
    dut.RSTB.value = 1

    # Test for blink pattern
    await with_timeout(FallingEdge(dut.gpio), 1000, 'us')
    await with_timeout(RisingEdge(dut.gpio), 100, 'us')
    await with_timeout(FallingEdge(dut.gpio), 100, 'us')
    await with_timeout(RisingEdge(dut.gpio), 100, 'us')
    await with_timeout(FallingEdge(dut.gpio), 100, 'us')
    await with_timeout(RisingEdge(dut.gpio), 100, 'us')
    await with_timeout(FallingEdge(dut.gpio), 100, 'us')
    await with_timeout(RisingEdge(dut.gpio), 100, 'us')
    await with_timeout(FallingEdge(dut.gpio), 100, 'us')
    await with_timeout(RisingEdge(dut.gpio), 100, 'us')
