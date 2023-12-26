from keterpencilan.adding_csv_data import *  # mengimport adding_csv_data dari modul keterpencilan
from keterpencilan.dijkstra import *  # mengimport dijkstra dari modul keterpencilan


# fungsi untuk menampilkan ke layar data jarak
def text_display_data_jarak(daftar_jalan):
    print("")  # mengeprint satu baris kosong
    print("Data Jarak")  # mengeprint teks
    print("\tAsal\t\tTujuan\t\tJarak")  # mengeprint teks diatur dengan \t agar berada di tengah
    for i in range(len(daftar_jalan)):  # melakukan looping sebanyak panjangnya data yang ada di daftar_jalan
        print(str(i + 1) + "\t" + daftar_jalan[i][0].strip('"'),
              "\t" +  # mengeprint setiap data yang merupakan data jarak
              daftar_jalan[i][1].strip('"'), "\t" +  # lalu, juga diatur dengan \t agar berada di tengah
              str(float(daftar_jalan[i][2])))

    print("")  # mengeprint teks
    print("  Pilih tampilkan:")  # mengeprint teks
    print("  1. Kota dengan nilai keterpencilan normal")  # mengeprint teks
    print("  2. Perhitungan nilai keterpencilan berdasarkan kota asal")  # mengeprint teks
    print("  3. Keluar")  # mengeprint teks


# fungsi untuk menampilkan ke layar data keterpencilan optimal
def text_display_keterpencilan_optimal(list_shortest_path_by_cities):
    print("")  # mengeprint teks
    print("1. Keterpencilan optimal")  # mengeprint teks
    print("\tKota\t\tNilai Keterpencilan")  # mengeprint teks diatur dengan \t agar berada di tengah
    for i in range(len(
            list_shortest_path_by_cities)):  # melakukan looping sebanyak panjangnya data yang ada di list_shortest_path_by_cities
        print(str(i + 1) + "\t" + list_shortest_path_by_cities[i][0].strip('"'),
              "\t" +  # mengeprint setiap data yang merupakan data keterpencilan optimal
              str(float(list_shortest_path_by_cities[i][1])))

    print("")  # mengeprint teks

    print("Kota terbaik untuk lokasi gudang logistik adalah",
          list_shortest_path_by_cities[0][0].strip('"') + ",")  # mengeprint teks
    print("yaitu dengan nilai keterpencilan sebesar", str(list_shortest_path_by_cities[0][1]),
          "hari\n")  # mengeprint teks

    print("  Pilih tampilkan:")  # mengeprint teks
    print("  0. Data Jarak")  # mengeprint teks
    print("  1. Kota dengan nilai keterpencilan normal")  # mengeprint teks
    print("  2. Perhitungan nilai keterpencilan berdasarkan kota asal")  # mengeprint teks
    print("  3. Keluar")  # mengeprint teks


# fungsi untuk menampilkan ke layar data keterpencilan dari kota yang dipilih terhadap setiap kota lainnya
def text_display_keterpencilan_a_town(FROM_name, FROM, list_shortest_path_by_a_city):
    print("")  # mengeprint teks
    print("2. Keterpencilan", FROM_name)  # mengeprint teks serta nama kota yang dipilih
    print("\tAsal\t\tTujuan\t\tJarak")  # mengeprint teks
    for i in range(len(
            list_shortest_path_by_a_city)):  # melakukan looping sebanyak panjangnya data yang ada di list_shortest_path_by_cities
        print(str(i + 1) + "\t" + list_shortest_path_by_a_city[i][0].strip('"'),
              "\t" +  # mengeprint setiap data yang merupakan data keterpencilan dari kota yang dipilih terhadap setiap kota lainnya
              list_shortest_path_by_a_city[i][1].strip('"'), "\t" +
              str(float(list_shortest_path_by_a_city[i][2])))

    print("")  # mengeprint teks

    print("Skor keterpencilan kota", FROM_name, "adalah",
          str(list_shortest_path_by_a_city[-1][-1]) + ", di mana")  # mengeprint teks
    print("jarak terjauh dari", FROM_name, "adalah saat mengirim ke", list_shortest_path_by_a_city[-1][1].strip('"'),
          # mengeprint teks
          "\n")

    print("  Pilih tampilkan:")  # mengeprint teks
    print("  0. Data Jarak")  # mengeprint teks
    print("  1. Kota dengan nilai keterpencilan normal")  # mengeprint teks
    print("  2. Perhitungan nilai keterpencilan berdasarkan kota asal")  # mengeprint teks
    print("  3. Keluar")  # mengeprint teks


# fungsi untuk memulai menampilkan hasil ke layar
def start_display(daftar_jalan, daftar_kota):
    choice = 0  # mendefinisikan 0 ke variabel choice
    while choice is not None:  # melakukan looping selama choice bukan None
        if choice == 0:  # kondisi ketika choice berisikan nilai 0
            data0 = destination_list(
                daftar_jalan)  # memanggil fungsi destination_list dan menaruh hasilnya di variabel data0
            text_display_data_jarak(
                data0)  # memanggil fungsi text_display_data_jarak, untuk menampilkan data jarak ke layar
            choice = int(input("Input your choice: "))  # meminta kepada pengguna program nilai dari choice
            while choice == 0:  # kondisi ketika choicenya adalah 0
                print("Please input the available choices")  # mengeprint teks
                choice = int(input("Input your choice: "))  # meminta kembali kepada pengguna program nilai dari choice

        elif choice == 1:  # kondisi ketika choice berisikan nilai 1
            data1 = shortest_path_of_nodes_to_list(daftar_kota,
                                                   Graph())  # memanggil fungsi shortest_path_of_nodes_to_list dan menaruh hasilnya di variabel data1
            text_display_keterpencilan_optimal(data1)   # memanggil fungsi text_display_keterpencilan_optimal, untuk menampilkan data keterpencilan optimal ke layar
            choice = int(input("Input your choice: "))  # meminta kepada pengguna program nilai dari choice

        elif choice == 2:   # kondisi ketika choice berisikan nilai 2
            FROM = None # mendefinisikan nilai None ke variabel FROM
            FROM_name = str(input("Masukkan kota awal: "))  # meminta kepada pengguna program kota yang mau dipilih, lalu menaruh hasilnya di variabel FROM_name
            cities = city_list(daftar_kota)    # memanggil fungsi city_list untuk mendapatkan data list daftar kota, lalu menyimpannya di variabel cities
            stats = False   # mendefinisikan nilai False ke variabel stats

            for i in range(len(cities)): # melakukan looping sebanyak panjangnya data yang ada di cities
                if cities[i].strip('"') == FROM_name:   # kondisi ketika nama kota yang dipilih berada dalam daftar kota
                    FROM = i   # mendefinisikan nilai i ke variabel FROM
                    stats = True    # mengganti isi variabel dari stats menjadi True

            if stats == False:  # kondisi ketika stats berisikan False
                print("You inputed the unavailable city")   # mengeprint teks

            else:   # kondisi ketika stats berisikan True
                data2 = shortest_path_of_a_node_to_list(shortest_path(FROM, Graph()), FROM, daftar_kota)   # memanggil fungsi shortest_path_of_a_node_to_list dan menaruh hasilnya di variabel data2
                text_display_keterpencilan_a_town(FROM_name, FROM, data2)   # memanggil fungsi text_display_keterpencilan_a_town, untuk menampilkan data keterpencilan dari kota yang dipilih ke layar
                choice = int(input("Input your choice: ")) # meminta kepada pengguna program nilai dari choice

        elif choice == 3:   # kondisi ketika choice berisikan nilai 3
            print("")   # mengeprint teks
            print("Have a good day!! Bye!!")    # mengeprint teks
            break   # menghentikan looping while, dan juga menghentikan meminta nilai dari choice kepada pengguna program

        else:   # kondisi ketika choice berisikan nilai bukan 0,1,2,3
            print("")   # mengeprint teks
            print("Please input the available choices") # mengeprint teks
            choice = int(input("Input your choice: "))  # meminta kembali kepada pengguna program nilai dari choice
