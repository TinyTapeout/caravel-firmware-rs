export COCOTB_REDUCED_LOG_FMT=1

export LIBPYTHON_LOC=$(shell cocotb-config --libpython)

all: coco_test

coco_test: ../firmware.vmem
	rm -rf sim_build/
	mkdir sim_build/

	iverilog -Ttyp -DFUNCTIONAL -DSIM -DUSE_POWER_PINS -DUNIT_DELAY=#1 \
	-f$(VERILOG_PATH)/includes/includes.rtl.caravel \
	-o sim_build/sim.vvp firmware_tb.v user_project_wrapper.v

	MODULE=test vvp -M $$(cocotb-config --prefix)/cocotb/libs -m libcocotbvpi_icarus sim_build/sim.vvp
	! grep failure results.xml

../firmware.bin: ../src/*.rs
	cargo objcopy --release -- -O binary ../firmware.bin

../firmware.vmem: ../firmware.bin
	bincopy convert -i binary -o verilog_vmem $< $@

.PHONY: gtkwave
gtkwave: firmware_tb.vcd
	gtkwave firmware_tb.vcd firmware_tb.gtkw

