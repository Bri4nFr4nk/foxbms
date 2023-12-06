# Programm für die Konvertierung der CAN-Daten des ID0x180
# nach Angabe des Dateninhaltes der Nachricht 
# durch Aufteilung in 3 Blöcke zu je 4 Hex-Zeichen und 2 Blöcke 
# zu je 2 Hex-Zeichen, anschließend Umwandlung in Dezimalzahlen und Division durch 100
# und Subtraktion des Offsets 128.0 und Ausgabe aller Werte

can_message = 0xA438A43808390001

# Aufteilung in 3 Blöcke zu je 4 Hex-Zeichen und 2 Blöcke zu je 2 Hex-Zeichen durch bitweises Schieben
can_part_1 = can_message >> (12*4)
can_part_2 = can_message >> (8*4) & 0xFFFF
can_part_3 = can_message >> (4*4) & 0xFFFF
can_part_4 = can_message >> (2*4) & 0xFF
can_part_5 = can_message & 0xFF

# Vertauschung der Bytepaare der einzelnen Blöcke wegen Big-Endian
can_part_1 = ((can_part_1 & 0xFF) << 8) | ((can_part_1 >> 8) & 0xFF)
can_part_2 = ((can_part_2 & 0xFF) << 8) | ((can_part_2 >> 8) & 0xFF)
can_part_3 = ((can_part_3 & 0xFF) << 8) | ((can_part_3 >> 8) & 0xFF)

# Division der einzelnen Werte durch 100 und Subtraktion des Offsets 128.0
can_part_1 = (can_part_1 / 100) - 128.0
can_part_2 = (can_part_2 / 100) - 128.0
can_part_3 = (can_part_3 / 100) - 128.0
can_part_4 = (can_part_4 / 1) - 0
can_part_5 = (can_part_5 / 1) - 0

# Ausgabe der einzelnen Werte
print("Celltemp_mean: ", can_part_1)
print("Celltemp_min: ", can_part_2)
print("Celltemp_max: ", can_part_3)
print("ModNumber_temp_min: ", can_part_4)
print("ModNumber_temp_max: ", can_part_5)


