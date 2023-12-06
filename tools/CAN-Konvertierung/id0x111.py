# Angabe des Dateninhaltes der Nachricht
#can_message = 0x0000000000010000
can_message = 0x0000000100000000

# Aufteilung in 1 Block mit 8 Bit, 1 Block mit 3 Bit, 1 Block mit 5 Bit und 6 Blöcke wieder mit 8 Bit durch bitweises Schieben
can_part_1 = can_message >> (14*4)
can_part_2 = can_message >> (13*4+1) & 0b111
can_part_3 = can_message >> (12*4) & 0b11111
can_part_4 = can_message >> (10*4) & 0xFF
can_part_5 = can_message >> (8*4) & 0xFF
can_part_6 = can_message >> (6*4) & 0xFF
can_part_7 = can_message >> (4*4) & 0xFF
can_part_8 = can_message >> (2*4) & 0xFF
can_part_9 = can_message & 0xFF

# Vertauschung der Bytepaare der einzelnen Blöcke wegen Big-Endian
# can_part_1 = ((can_part_1 & 0xFF) << 8) | ((can_part_1 >> 8) & 0xFF)
# can_part_2 = ((can_part_2 & 0xFF) << 8) | ((can_part_2 >> 8) & 0xFF)
# can_part_3 = ((can_part_3 & 0xFF) << 8) | ((can_part_3 >> 8) & 0xFF)


# Ausgabe der einzelnen Werte
print("error_overvoltage: ", can_part_1)
print("error_undervoltage: ", can_part_2)
print("error_deep_discharge: ", can_part_3)
print("error_temperature_MCU0: ", can_part_4)
print("error_contactor: ", can_part_5)
print("error_selftest: ", can_part_6)
print("error_cantiming: ", can_part_7)
print("error_current_sensor: ", can_part_8)
print("error_balancing_active: ", can_part_9)

