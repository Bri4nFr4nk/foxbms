# Angabe des Dateninhaltes der Nachricht
can_message = 0x00F0000000000000

# Aufteilung in 8 Blöcke zu je 2 Hex-Zeichen durch bitweises Schieben
can_part_1 = can_message >> (14*4)
can_part_2 = can_message >> (12*4) & 0xFF
can_part_3 = can_message >> (10*4) & 0xFF
can_part_4 = can_message >> (8*4) & 0xFF
can_part_5 = can_message >> (6*4) & 0xFF
can_part_6 = can_message >> (4*4) & 0xFF
can_part_7 = can_message >> (2*4) & 0xFF
can_part_8 = can_message & 0xFF


# Ausgabe der einzelnen Werte
print("general_error: ", can_part_1)
print("current_state: ", hex(can_part_2))
print("error_overtemp_charge: ", can_part_3)
print("error_undertemp_charge: ", can_part_4)
print("error_overtemp_discharge: ", can_part_5)
print("error_undertemp_discharge: ", can_part_6)
print("error_overcurrent_charge: ", can_part_7)
print("error_overcurrent_discharge: ", can_part_8)


