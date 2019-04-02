from texttable import Texttable
import datetime
def pay():
    x = datetime.datetime.now()
    table= Texttable ()
    no=0
    nama=[]
    nim=[]
    kelas=[]
    pay_uts_uas=[]
    pay_bulan=[]
    pay_seminar=[]
    pay_kas=[]
    admin=[]
    jawab3 = "y"
    while(jawab3 == "y"):
        print (("\n"),("_"*3),("PEMBAYARAN"),("_"*3))  
        nama=(input("Masukan Nama  : "))
        nim=(input("Masukan NIM   : "))
        kelas=(input("Masukan Kelas : "))
        pilih = (input("Bayar UTS/UAS (y/t) ? "))
        if pilih =='y':
            print ("Pilih jenis pembayaran")
            print ("1.UAS")
            print ("2.UTS")
            jawab = 'y'
            while(jawab == 'y'):
                pilih1 = (input("Pilih JENIS PEMBAYARAN (1/2) ? "))
                if   pilih1 == '1':
                     uts_uas = 'UTS'
                     pay_uts_uas=50000
                     jawab = 't'
                elif pilih1 == '2':
                     uts_uas = 'UAS'
                     pay_uts_uas=100000
                     jawab = 't'
                    
                else  :
                     print ("\n!!! DATA YANG ANDA MASUKAN SALAH, INPUT KEMBALI !!!")
                     jawab = 'y'
        else:
             uts_uas = 0
             pay_uts_uas =0
        pilih = (input("Bayar BULANAN (y/t) ? "))
        if pilih == 'y':
            bulanan =int(input("\n-- BULANAN -- \nDi bayar untuk berapa bulan ? "))
            d_bulanan = 'BULANAN'
            pay_bulan=5000000*bulanan
        else :
            bulanan_ = ''
            pay_bulan=0
        pilih = (input("Bayar SEMINAR (y/t) ? "))
        if  pilih == 'y':
            seminar  = 'SEMINAR'
            pay_seminar=100000
        else :
            seminar = ''
            pay_seminar=0
        pilih = (input("Bayar KAS (y/t) ? "))
        if  pilih == 'y':
            d_kas = 'KAS'
            kas = int(input("\n-- KAS -- \nDi bayar untuk berapa bulan ? "))
            pay_kas=20000*kas
            
        else :
            kas = ''
            pay_kas=0
        print ("Biaya Admin 5000");input('')
        admin=5000
        no=+1
        for ia in range(no):
            total_bayar = pay_uts_uas+pay_bulan+pay_seminar+pay_kas
            grand_total = total_bayar+admin
        table.add_rows([['NO','UTS','UAS','BULAN','SEMINAR','KAS','TOTAL','ADMIN','GRAND TOTAL','TANGGAL TRANSAKSI'],
                        [ia+1,pay_uts_uas,pay_uts_uas,pay_bulan,pay_seminar,pay_kas,total_bayar,admin,grand_total,x]])
        print("_"*30)
        print("Rincian Pembayaran")
        print("_"*30)
        print ("Nama "," "*2,nama)
        print ("Nim "," "*3,nim)
        print ("Kelas "," "*1,kelas)
        print (table.draw())
        jawab3 = input("\n  Tambahkan Data PEMBAYARAN (y/t)? ") ; print("")
