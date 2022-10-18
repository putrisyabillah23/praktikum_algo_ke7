# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 18:10:20 2022

@author: putri
"""

umur = "0"
total = 0
while (umur != ""):
    umur = input ("masukan umur :")
    if umur != "" :
        umur_angka = int(umur)
        if umur_angka <= 2 :
            print ("gratis")
            price = 0
        elif umur_angka >= 3 and umur_angka <= 12 :
            print ("harga Rp.14.000")
            price = 14
        elif umur_angka >= 65 :
            print ("harga Rp.18.000")
            price = 18
        else :
            print ("harga Rp.23.000")
            price = 23
        total = total + price
        print ("total : %0.2f" % total)

jumlah = int(input("masukan jumlah uang :"))
hasil = jumlah - total 
print ("kembalian : %0.2f" % hasil )