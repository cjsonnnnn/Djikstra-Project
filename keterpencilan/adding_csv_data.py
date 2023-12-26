#GraphParsing
# Fungsi untuk mengubah bentuk data daftar kota ke dalam bentuk list
def city_list(daftar_kota):
    town_list = open(daftar_kota, "r").read()  # membuka file csv daftar kota, lalu menyimpannya di variabel town_list
    town_list = town_list.split(",")  # memisahakan data sehingga tidak ada lebih dari satu data yang terbaca satu

    return town_list  # menyimpan dan mengembalikan town_list


# Fungsi untuk mengubah bentuk data daftar jalan ke dalam bentuk list
def destination_list(daftar_jalan):
    my_file = open(daftar_jalan)  # membuka file csv daftar jalan, lalu menyimpannya di variabel my_file
    my_line = my_file.readline()  # membaca satu baris data dari my_file, lalu menyimpannya di variabel my_line
    way_list = []  # membuat suatu list dengan nama way_list

    while my_line:  # melakukan looping selama my_line "True"
        my_line = my_line.split(",")  # memisahakan data sehingga tidak ada lebih dari satu data yang terbaca satu
        way_list.append(my_line)  # menyimpan dan menambahkan data my_line ke dalam variabel way_list
        my_line = my_file.readline()  # membaca satu baris data dari my_file, lalu menyimpannya di variabel my_line

    # memperbaiki format text, terutama ketika ada kelebihan spasi. Contohnya => ' "Yokyakarta"', seharusnya '"Yokyakarta"'
    new_waylist = []  # membuat suatu list dengan nama new_waylist
    for i in way_list:  # melakukan looping pengambilan data dari way_list (suatu list ukuran nxn) secara satu per satu
        inside = []  # membuat suatu list dengan nama inside
        for j in i:  # melakukan looping pengambilan data dari i (suatu list ukuran n) secara satu per satu
            inside.append(j.replace(" ",
                                    ""))  # mengubah format text yang memiliki kelebihan spasi menjadi tidak ada, lalu menambahkannya ke dalam list inside
        new_waylist.append(inside)  # menyimpan dan menambahkan data inside ke dalam variabel new_waylist

    return new_waylist  # menyimpan dan mengembalikan new_waylist


# Fungsi untuk menggunakan angka sebagai representasi kota awal, kota tujuan, dan jarak
# yang kemudian disajikan dalam bentuk library
def daftar_jalan_numlist(daftar_jalan, daftar_kota):
    list_town = city_list(
        daftar_kota)  # memanggil fungsi city_list untuk mendapatkan data list daftar kota, lalu menyimpannya di variabel list_town
    lib_town = {}  # membuat suatu library kosong yang berada di variabel lib_town
    for i in range(len(list_town)):  # melakukan looping sebanyak panjangnya data yang ada di list_town
        lib_town[list_town[i]] = i  # membuat key berupa nama kota dan value berupa indexnya

    # Merepresentasikan kota dalam daftar jalan menjadi angka, lalu memiliki nilai jarak
    way_list = destination_list(
        daftar_jalan)  # memanggil fungsi destination_list untuk mendapatkan data daftar jalan berupa list, lalu menyimpannya di variabel way_list
    numway_list = []  # membuat suatu list kosong di variabel numway_list

    for i in way_list:  # melakukan looping pengambilan data dari way_list (suatu list ukuran nxn) secara satu per satu
        inside_numway = []  # membuat suatu list kosong di variabel inside_numway
        for j in i:  # melakukan looping pengambilan data dari i (suatu list ukuran n) secara satu per satu
            if j in list_town:  # kondisi ketika nilai j berada di list_town (list berukuran n)
                inside_numway.append(lib_town[j])  # menambakan value dari key j di lib_town ke dalam list inside_numway
        numway_list.append(inside_numway)  # menambahkan list inside_numway ke dalam list _numway_list

    # Membuat list berisikan jarak
    distance = []  # membuat suatu list kosong di variabel distance
    for i in way_list:  # melakukan looping pengambilan data dari way_list (suatu list ukuran nxn) secara satu per satu
        distance.append(
            float(i[-1]))  # menambahkan data paling terakhir dari setiap list, yaitu data jarak ke dalam list distance

    # Membuat library dengan key adalah numway_list dan valuenya adalah jarak
    lib_way = {}  # membuat suatu library kosong yang berada di variabel lib_way
    for i in range(len(way_list)):  # melakukan looping sebanyak panjangnya data yang ada di way_list
        lib_way[tuple(numway_list[i])] = distance[
            i]  # membuat key berupa data dari numway list di index i, lalu mengubahnya ke dalam bentuk tuple dan value berupa data jarak

    return lib_way  # menyimpan dan mengembalikan new_waylist

# Fungsi untuk membuat sebuah graph tidak berarah (dua arah) dalam bentuk list nxn
def create_graph_tidak_berarah(daftar_jalan, daftar_kota):
    thecitylist = city_list(
        daftar_kota)  # memanggil fungsi city_list untuk mendapatkan data list daftar kota, lalu menyimpannya di variabel thecitylist
    graph = [[None] * len(thecitylist)] * len(
        thecitylist)  # membuat suatu list berisikan nilai None dengan ukuran nxn (n= panjang dari data di thecitylist)
    new_graph = []  # membuat suatu list kosong di variabel new_graph
    numway_lib = daftar_jalan_numlist(daftar_jalan,
                                      daftar_kota)  # memanggil fungsi daftar_jalan_numlist untuk mendapatkan data list daftar jalan, lalu menyimpannya di variabel numway_lib

    for i in range(len(graph)):  # melakukan looping sebanyak panjangnya data yang ada di graph
        inside_newgraph = []  # membuat suatu list kosong di variabel inside_newgraph
        for j in range(len(graph)):  # melakukan looping sebanyak panjangnya data yang ada di graph
            if (i, j) in numway_lib:  # kondisi ketika tuple (i, j) berada di numway_lib
                inside_newgraph.append(
                    numway_lib[(i, j)])  # manambahkan value dari key (i,j) di numway_lib ke inside_newgraph

            elif (j, i) in numway_lib:  # kondisi ketika tuple (j, i) berada di numway_lib
                inside_newgraph.append(
                    numway_lib[(j, i)])  # manambahkan value dari key (j,i) di numway_lib ke inside_newgraph

            else:  # kondisi ketika tuple (i, j) dan (j, i) tidak berada di numway_lib
                inside_newgraph.append(None)  # manambahkan nilai None ke inside_newgraph
        new_graph.append(inside_newgraph)  # manambahkan data di inside_newgraph ke new_graph

    return new_graph  # menyimpan dan mengembalikan new_graph
#GraphParsing

#Complexity
# Kompleksitas Algoritma diatas : O(n^2)
# N = titik = 5
# V = sisi = 6
#Complexity