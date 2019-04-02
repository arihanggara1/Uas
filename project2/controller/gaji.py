def gaji() :
    from texttable import Texttable
    table1 = Texttable ()
    no1 = 0
    nama1 = []
    jabatan = []
    gaji = []
    jawab1 = "y"
    while (jawab1 == "y"):
        
        jab = input("Jabatan : ")
        if    jab == 'Operator':
              nama1.append(input("Masukan nama : "))
              jabatan.append ('Operator')
              gaji.append('Rp.4.950.000')
              jawab1 = input ("Tambah data (y/t)? ")
              no1 += 1
        elif  jab == 'Programmer':
              nama1.append(input("Masukan nama : "))
              jabatan.append ('Programmer')
              gaji.append('Rp.15.000.000')
              jawab1 = input ("Tambah data (y/t)? ")
              no1 += 1  
        else :
              print ("Jabatan Tidak Ada!")
              pilih = input("Tambah (y/t)? ")
              if pilih == 'y':
                 jawab1 = 'y'
              else:
                  jawab1 = 't'
    for ic in range(no1):
        table1.add_rows([['NO','NAMA','JABATAN','GAJI'],[ic+1,nama1[ic],jabatan[ic],gaji[ic]]])
    print (table1.draw())
