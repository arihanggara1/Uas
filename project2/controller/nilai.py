def nilai() :
    from texttable import Texttable
    table2 = Texttable ()
    print ("\nMenu Nilai")
    no2 = 0      
    nama2 = []
    nim = []
    nilai_tugas = []
    nilai_uts = []
    nilai_uas = []
    jawab2 = "y"
    while(jawab2 == "y"):
         nama2.append(input("Masukan Nama : "))
         nim.append(input("Masukan NIM  : "))
         nilai_tugas.append(input("Nilai Tugas  : "))
         nilai_uts.append(input("Nilai UTS    : "))
         nilai_uas.append(input("Nilai UAS    : "))
         jawab2 = input("\nTambah data (y/t)? ")
         print ("")
         no2 += 1
    for ia in range(no2):
        tugas = int(nilai_tugas[ia])
        uts = int(nilai_uts[ia])
        uas = int(nilai_uas[ia])
        akhir = (tugas*30/100) + (uts*35/100) + (uas*35/100)
        table2.set_cols_dtype(['a','i','i','i','i','i','i'])
        table2.add_rows([['NO','NAMA','NIM','TUGAS','UTS','UAS','AKHIR'],[ia+1,nama2[ia],nim[ia],nilai_tugas[ia],nilai_uts[ia],nilai_uas[ia],akhir]])
    print (table2.draw())
           
