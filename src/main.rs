#![no_std]
#![no_main]

extern crate riscv_rt;

use riscv_rt::entry;

mod delay;
mod gpio;
mod mprj;
mod uart;

mod uart_printer;
use uart_printer::Printer;

#[panic_handler]
fn panic(_info: &::core::panic::PanicInfo) -> ! {
    loop {}
}

#[entry]
fn main() -> ! {
    gpio::init();
    uart::init();
    mprj::commit();

    uart::write_str("Hello, Caravel!\n");

    let mut count = 0;
    loop {
        gpio::write(0);
        delay::wait(2000000);
        gpio::write(1);
        delay::wait(2000000);
        println!("Counter: {}!", count);
        count += 1;
    }
}
