const CSR_MPRJ_WB_IENA_OUT: *mut u32 = 0xf0003800u32 as _;

pub fn wishbone_enable(enable: bool) {
    unsafe {
        core::ptr::write_volatile(CSR_MPRJ_WB_IENA_OUT, enable as u32);
    }
}
