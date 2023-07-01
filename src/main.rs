#![no_std]
#![no_main]

extern crate riscv_rt;

use riscv_rt::entry;

mod gpio;
mod delay;

#[panic_handler]
fn panic(_info: &::core::panic::PanicInfo) -> ! {
    loop {}
}

#[entry]
fn main() -> ! {
    gpio::gpio_init();

    loop {
        gpio::gpio_write(0);
        delay::wait(2000000);
        gpio::gpio_write(1);
        delay::wait(2000000);
    }
}
