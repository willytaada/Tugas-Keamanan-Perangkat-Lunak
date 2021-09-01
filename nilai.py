print("      **** PROGRAM MENGHITUNG NILAI AKHIR ****")
print("     ------------------------------------------")
print("")
nama  =str(input("MASUKKAN NAMA         :"))
nim   =float(input    ("MASUKAN NIM         :"))
print("")
partisipasi   =float(input    ("MASUKAN NILAI PARTISIPASI   :"))
uts   =float(input    ("MASUKAN NILAI UTS   :"))
uas   =float(input    ("MASUKAN NILAI UAS   :"))
tugas=float(input     ("MASUKAN NILAI TUGAS :"))

partisipasi=partisipasi*2;
uts=uts*2;
uas=uas*3;
tugas=tugas*3;
nilai_akhir=(partisipasi+uts+uas+tugas)/10;

print("")
print("         *** HASIL NILAI AKHIR ***")
print("        ---------------------------")
print("")

print("NAMA         :%s"%nama)
print("NIM          :%s"%nim)
print("NILAI UTS    :%d"%partisipasi)
print("NILAI UTS    :%d"%uas)
print("NILAI UAS    :%d"%uts)
print("NALAI TUGAS  :%d"%tugas)
print("")
print("HASIL NILAI AKHIR: %d", float(nilai_akhir))
print("")
if nilai_akhir >=80:
    print ("NILAI HURUF  : A")
elif nilai_akhir >=70:
    print ("NILAI HURUF  : B")
elif nilai_akhir >=55:
    print ("NILAI HURUF : C")
elif nilai_akhir >=40:
    print ("NILAI HURUF  : D")
elif nilai_akhir >=39:
    print ("NILAI HURUF : F")

if nilai_akhir >=60:
    print ("KETERANGAN : LULUS")
else :
    print ("KETERANGAN : TIDAK LULUS")