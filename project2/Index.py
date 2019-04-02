from controller.gaji import gaji
from controller.nilai import nilai
from controller.kalkulator import kalkulator
from controller.pay import pay
import getpass
import datetime

def login():
      print("_"*15)
      print("Selamat Datang Di Pelita Bangsa ")
      print("Silahkan Login Terlebih Dahulu")
      print("_"*15)
      username = input("Username : ")
      password = getpass.getpass("Password : ")
      if username == "ari" and password =="123":
       menu()
      else:
          print("ID tidak ada")
def menu ():       
            print ("Menu")
            print ("1.Penggajian")
            print ("2.Penilaian")
            print ("3.Kalkulator")
            print ("4.Pembayaran")
            Ychoice = int(input("Masukan Pilihan : "))
            if Ychoice == 1:
               gaji ()
            elif Ychoice == 2:
               nilai ()
            elif Ychoice == 3:
               kalkulator()
            elif Ychoice == 4:
               pay()
            else:
                print("pilian tidak ada.")
            choice()
def end():
    print("Terimakasih")
    logout()
def choice():
            choice = input("Kembali Ke Menu (y/t)? ")
            if choice == 'y':
                menu()
            else:
                end()
def logout():
            auth = input("Kembali Ke Login (y/t)? ")
            if auth == 'y':
                login()
            else:
                print("Sampai Jumpa")
                
login()
