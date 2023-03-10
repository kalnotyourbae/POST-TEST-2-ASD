di baris pertama, data listnya di flatten menjadi satu dimensi, caranya dengan menggunakan list comperehension ( pemahaman). Lalu, menghitung panjang list serta mengatur akar kuadrat dari panjang list tersebut. 

Variabel prev berfungsi untuk menyimpan indeks langkah akhir yang berhasil, lalu kemudian diimplementasikan kedalam loop ( perulangan ) berikutnya

di loop pertama, indeks step ( langkah) maju dengan menjumlahlan akar kuadrat dari panjang list ke prev. Apabila prev lebih besar/sama dengan panjang list, maka berarti nilai target tidak ditemukan dalam list, dan akan melakukan return ( kembali) 

pada loop kedua, indeks maju satu per satu dari prev, dan apabila indeks ini sama dengan langkah berikutnya atau melebih dari panjang list, maka berarti nilai target yg dicari tidak ditemukan dalam list, dan akan melakukan return lagi

jika nilai target yg dicari itu ditemukan pada flat_arr[prev], maka fungsi map_index akan digunakan untuk memetakan indeks kembali ke nested list ( list bersarant) yg asli. Function ini menghitung indeks dengan mengulang melalui setiap sub list dalam list asli lalu mengurangi indeks target dari panjang setiap sublist didalam list. Apabila indeks target mencapai 0, maka indeks asli telah ditemukan dan akan dikembalikan sebagai pasangan indeks sub list dan indeks dalam sub list. Jika sublist yg terakhir sudah dilalui, maka artinya indeks asli adalah indeks dalam list utama dan akan langsung di return

selanjutnya program akan menguji fungsi dari jump_search dengan mencari beberapa nilai dalam list "listnya" dan menampilkan hasil dari pencarian yg diminta
