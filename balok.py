print("      **** PROGRAM MENGHITUNG LUAS DAN VOLUME BALOK ****")
print("     ------------------------------------------")
print("")
panjang   =float(input    ("MASUKAN NILAI PANJANG   :"))
lebar   =float(input    ("MASUKAN NILAI LEBAR   :"))
tinggi=float(input     ("MASUKAN NILAI TINGGI :"))

volume=panjang*lebar*tinggi;
luas=2*((panjang*lebar)+(panjang*tinggi)+(lebar*tinggi));

print("")
print("         *** HASIL LUAS DAN VOLUME BALOK ***")
print("        ---------------------------")
print("")
print("NILAI PANJANG    :%d"%panjang)
print("NILAI LEBAR    :%d"%lebar)
print("NALAI TINGGI  :%d"%tinggi)
print("")
print("HASIL LUAS: %d", float(luas))
print("HASIL VOLUME: %d", float(volume))