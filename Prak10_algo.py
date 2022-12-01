# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 22:11:39 2022

@author: 62817
"""

def data_list(a=0, data=[], i=1):
    if (a == 0):
        return 0
    else :
        isi = int(input("masukkan angka ke-" + str(i) + " : "))
        data.append(isi)
        if(a == 1):
            return data
        else:
            i += 1
            return data_list(a-1, data, i)
def b_sort(angka):
    for i in range(len(angka)):
        for a in range (0, len(angka) - i - 1):
            if angka[a] > angka[a + 1]:
                x = angka[a]
                angka[a] = angka[a+1]
                angka[a+1] = x
                
jumlah = int(input("berapa banyak angka yang ingin disortir : "))
angka = data_list(a = jumlah)
print("\nangka sebelum disortir :")
print(angka)
b_sort(angka)
print("\nangka setelah disortir :")
print(angka)
