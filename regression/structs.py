#a APB
#t apb_request
apb_request = {
    "paddr":32,
    "penable":1,
    "psel":1,
    "pwrite":1,
    "pwdata":32,
}

#t apb_response
apb_response = {
    "prdata":32,
    "pready":1,
    "perr":1,
}

#t apb_processor_response
apb_processor_response = {
    "acknowledge":1,
    "rom_busy":1,
}

#t apb_processor_request
apb_processor_request = {
    "valid":1,
    "address":16,
}

#t apb_rom_request
apb_rom_request = {
    "enable":1,
    "address":16,
}

#a CSR
csr_request  = {"valid":1, "read_not_write":1, "select":16, "address":16, "data":32}
csr_response = {"acknowledge":1, "read_data_valid":1, "read_data_error":1, "read_data":32}

#a SRAM
sram_access_req  = {"valid":1, "id":8, "read_not_write":1, "byte_enable":8, "address":32, "write_data":64}
sram_access_resp = {"valid":1, "id":8, "ack":1, "data":64}

#a Timer
#t timer_control
timer_control = {"reset_counter":1,
                 "enable_counter":1,
                 "advance":1,
                 "retard":1,
                 "lock_to_master":1,
                 "lock_window_lsb":2,
                 "synchronize":2,
                 "synchronize_value":64,
                 "block_writes":1,
                 "bonus_subfraction_add":8,
                 "bonus_subfraction_sub":8,
                 "fractional_adder":4,
                 "integer_adder":8,
}

#t timer_value
timer_value = {"irq":1,
               "locked":1,
               "value":64,
}

#t timer_sec_nsec
timer_sec_nsec = {"valid":1,
               "sec":35,
               "nsec":30,
}

#a I/O
#t uart_rx
uart_rx = {"rxd":1, "rts":1}

#t uart_tx
uart_tx = {"txd":1, "cts":1}

#t mdio
mdio = {"mdc":1, "mdio":1, "mdio_enable":1}

#t i2c
i2c = {"scl":1, "sda":1}

#t i2c_master_request
i2c_master_request = {"valid":1,
                      "cont":1,
                      "data":32,
                      "num_in":3,
                      "num_out":3,
}

#t i2c_master_response
i2c_master_response = {"ack":1,
                       "in_progress":1,
                       "response_valid":1,
                       "response_type":3,
                       "data":32,
}

#t i2c_conf
i2c_conf = {"divider":8, "period":8}

#a clocking - bit_delay and phase_measure
#t t_bit_delay_config 
bit_delay_config = { "op":2, "select":1, "value":9}

#t t_bit_delay_response
bit_delay_response = { "op_ack":1, "delay_value":9, "sync_value":1}

#t phase_measure_request
phase_measure_request = {"valid":1}

#t phase_measure_response
phase_measure_response = {"ack":1, "abort":1, "valid":1, "delay":9, "initial_delay":9, "initial_value":1}

#t eye_track_request
eye_track_request = {"enable":1, "seek_enable":1, "track_enable":1, "measure":1, "phase_width":9, "min_eye_width":9}

#t eye_track_response
eye_track_response = {"measure_ack":1, "locked":1, "eye_data_valid":1, "data_delay":9, "eye_width":9, "eye_center":9}

#a dprintf
#t dprintf_byte
dprintf_byte = {"address":16,
                "data":8,
                "last":1,
                "valid":1,
}

#t dprintf_req_4
dprintf_req_4 = {
    "valid":1,
    "address":16,
    "data_0":64,
    "data_1":64,
    "data_2":64,
    "data_3":64,
    }

#t dprintf_req_2
dprintf_req_2 = {
    "valid":1,
    "address":16,
    "data_0":64,
    "data_1":64,
    }

#t vcu108_inputs
vcu108_inputs = {
    "i2c":i2c,
    "eth_int_n":1,
    "mdio":1,
    "uart_rx":uart_rx,
    "switches":4,
    "buttons":5}

#t vcu108_outputs
vcu108_outputs = {
    "i2c":i2c,
    "i2c_reset_mux_n":1,
    "eth_reset_n":1,
    "mdio":mdio,
    "uart_tx":uart_tx,
    "leds":8,
}

#t adv7511
adv7511 = {"spdif":1,
           "hsync":1,
           "vsync":1,
           "de":1,
           "data":16,
}
#t mem_flash_in
#t mem_flash_out

#a Network
packet_stat_type = {"okay":0, "short":1, "long":2, "data_error":3, "carrier":4}
packet_stat = {"valid":1, "stat_type":3, "byte_count":16, "is_broadcast":1, "is_multicast":1}

#a Ethernet
#t tbi_valid
tbi_valid = {"valid":1, "data":10}

#t gmii_tx
gmii_tx = {"tx_en":1, "tx_er":1, "txd":8}

#t gmii_rx
gmii_rx = {"rx_dv":1, "rx_er":1, "rxd":8, "rx_crs":1}

#t sgmii_gasket_control
sgmii_gasket_control = {"write_config":1, "write_address":4, "write_data":32}

#t sgmii_gasket_status
sgmii_gasket_status = {"rx_sync":1, "rx_sync_toggle":1, "rx_symbols_since_sync":32, "an_config":16}
#t dec_8b10b_data - t_8b10b_dec_data
dec_8b10b_data = {
    "valid":1,
    "data":8,
    "is_control":1,
    "is_data":1,
    "disparity_positive":1,
}

#t symbol_8b10b - t_8b10b_symbol
symbol_8b10b = {
    "disparity_positive":1,
    "symbol":10,
}

#t enc_8b10b_data -  t_8b10b_enc_data
enc_8b10b_data = {
    "data":8,
    "is_control":1,
    "disparity":1,
}

