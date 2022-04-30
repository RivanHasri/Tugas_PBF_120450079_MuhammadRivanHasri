# Nomor 1a
addku = lambda x: x+10
powku = lambda x: x**2
kurku = lambda x: x - 2*x

f_komp = lambda f,g: lambda x: f(g(x))
my_f_kom = f_komp(kurku,f_komp(powku,addku))

my_f_kom(10)

# Nomor 1b
inv_addku = lambda x: x - 10
inv_powku = lambda x: x**0.5
inv_kurku = lambda x: -1*x

my_f_kom_inv = f_komp(inv_addku,f_komp(inv_powku,inv_kurku))
my_f_kom_inv(-400)

# Nomor 2
from spetools import *

mhs = [3,
   [120000,75000,50000],
   5.5 * 10**6,
   False]

data = [mhs, [val1, val2, val3, val4]]
comp_final = mycompose(gabung_val,bobot,total_ukt)
comp_final(data) / 10**6

# Nomor 3
dat = '-3x^5 + 2x^2 -4x +5'
fss = (split, chdepan, eqkan, toarr2d, sortdesc, calctur, tostr, prettykan, prettysign)
my_turunan = mycompose(*fss)
my_turunan(dat)

# Nomor 4
keranjang = [
    {'Jumlah_Barang': 5, 'Harga:': 10 },
    {'Jumlah_Barang': 7, 'Harga:': 20 },
    {'Jumlah_Barang': 20, 'Harga:': 4.5 }
]

@calc_time_decorator
@pajak_decorator
def hitung_pembayaran_1(keranjang):
    return r( lambda a,b: a + (b['Jumlah_Barang'] * b['Harga:']), keranjang, 0) * 1000

hitung_pembayaran_1(keranjang)