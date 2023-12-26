from keterpencilan.adding_csv_data import *  # mengimport adding_csv_data dari modul keterpencilan

#GraphStructure
class Graph:  # membuat class yang berisikan graph
    def __init__(self):
        self.internal_array = create_graph_tidak_berarah("keterpencilan/DaftarJalan.csv",
                                                         "keterpencilan/DaftarKota.csv") 
                                                          # mengisi atribut class dengan graph tidak berarah
#GraphStructure

#GraphMemory
# Memori yang digunakan untuk menyimpan titik dan sisi adalah graf berbentuk 5 * 5
# Ukuran graf O(N^2)
# N = titik = 5
# V = sisi = 6
#GraphMemory


# fungsi untuk mencari neighbor dari node
def find_neighbor(FROM, graph):
    neighbors = []  # membuat suatu list dengan nama neighbors
    internal_array = graph.internal_array  # membuat objek dengan nama internal_array yang berisikan graph tidak berarah
    for i in range(
            len(internal_array[FROM])):  # melakukan looping sebanyak panjangnya data yang ada di internal_array[FROM]
        if internal_array[FROM][i] is not None:  # kondisi ketika graph tidak berarah pada index FROM, i tidak kosong
            neighbors.append(i)  # menambahkan dan menyimpan data i ke list neighbors
    return neighbors  # menyimpan dan mengembalikan neighbors


# fungsi untuk mencari besarnya nilai weight dari graph
def get_weight(FROM, TO, graph):
    internal_array = graph.internal_array  # membuat objek dengan nama internal_array yang berisikan graph tidak berarah
    weight = internal_array[FROM][TO]  # mendefinisikan weight sebagai nilai dari graph di index FROM, TO

    return weight  # menyimpan dan mengembalikan neighbors


# fungsi untuk melakukan eksplorasi jarak terpendek dari suatu kota menuju kota lain
# fungsi ini dibuat khusus untuk menghindari adanya variabel yang bersifat global
def digging_to_TO2(FROM, queue, graph_tidak_berarah, all_nodes_weight, pass_nodes):
    for i in queue:  # melakukan looping sebanyak panjangnya data yang ada di queue
        weight_FROM = all_nodes_weight[FROM]  # mendefinisikan weight_FROM sebagai nilai dari list di index FROM
        all_nodes_weight[i] = min(get_weight(FROM, i, graph_tidak_berarah) + weight_FROM,
                                  all_nodes_weight[i])  # mencari serta mengambil nilai weight terendah

    for j in queue:  # melakukan looping sebanyak panjangnya data yang ada di queue
        pass_nodes.append(FROM)  # menambahkan dan menyimpan data FROM ke list pass_nodes
        queue_neighbor = []  # membuat suatu list dengan nama queue_neighbor
        for k in find_neighbor(j,
                               graph_tidak_berarah):  # melakukan looping pengambilan data dari find_neighbor secara satu per satu
            if k not in pass_nodes:  # kondisi ketika k tidak ada tidak list pass_nodes
                queue_neighbor.append(k)  # menambahkan dan menyimpan data k ke list queue_neighbor
        all_nodes_weight = digging_to_TO2(j, queue_neighbor, graph_tidak_berarah, all_nodes_weight,
                                          pass_nodes)  # malakukan rekursi (memanggil fungsi diri sendiri) lalu menyimpan nilainya di variable all_nodes_weight

    return all_nodes_weight  # menyimpan dan mengembalikan all_nodes_weight


# fungsi untuk melakukan eksplorasi jarak terpendek dari suatu kota menuju kota lain
def digging_to_TO1(FROM, queue, graph_tidak_berarah, all_nodes_weight, pass_nodes):
    for i in queue:  # melakukan looping sebanyak panjangnya data yang ada di queue
        weight_FROM = all_nodes_weight[FROM]  # mendefinisikan weight_FROM sebagai nilai dari list di index FROM
        all_nodes_weight[i] = min(get_weight(FROM, i, graph_tidak_berarah) + weight_FROM,
                                  all_nodes_weight[i])  # mencari serta mengambil nilai weight terendah

    for j in queue:  # melakukan looping sebanyak panjangnya data yang ada di queue
        pass_nodes = [FROM]  # mendefinisikan data FROM berupa list ke dalam variabel pass_nodes
        queue_neighbor = []  # membuat suatu list dengan nama queue_neighbor

        for k in find_neighbor(j,
                               graph_tidak_berarah):  # melakukan looping pengambilan data dari find_neighbor secara satu per satu
            if k not in pass_nodes:  # kondisi ketika k tidak ada tidak list pass_nodes
                queue_neighbor.append(k)  # menambahkan dan menyimpan data k ke list queue_neighbor
        all_nodes_weight = digging_to_TO2(j, queue_neighbor, graph_tidak_berarah, all_nodes_weight,
                                          pass_nodes)  # memanggil fungsi digging_to_TO2, lalu menyimpan nilainya di variable all_nodes_weight

    return all_nodes_weight  # menyimpan dan mengembalikan all_nodes_weight


# fungsi untuk mencari jarak terpendek
# fungsi lobby dari mencari jarak terpendek
def shortest_path(FROM, graph_tidak_berarah):
    internal_array = graph_tidak_berarah.internal_array  # membuat objek dengan nama internal_array yang berisikan graph tidak berarah
    if len(internal_array) > 1:  # kondisi ketika panjang dari graph lebih dari satu
        weight = 0  # mendefinisikan weight kota awal sebagai 0

        all_nodes_weight = {FROM: weight}  # membuat library berisikan FROM sebagai key dan weight (0) sebagai weightnya

        for i in range(len(internal_array)):  # melakukan looping sebanyak panjangnya data yang ada di internal_array
            if i is not FROM:  # kondisi ketika i tidak sama dengan nilai dari FROM
                all_nodes_weight[i] = float("inf")  # mendefinisikan nilai node sebagai infinity

        queue = find_neighbor(FROM, graph_tidak_berarah)  # menaruh setiap node tetangga di variabel queue
        pass_nodes = []  # membuat suatu list dengan nama pass_nodes

        all_nodes_weight = digging_to_TO1(FROM, queue, graph_tidak_berarah, all_nodes_weight,
                                          pass_nodes)  # memanggil fungsi digging_to_TO1, lalu menyimpan nilainya di variable all_nodes_weight

        return all_nodes_weight  # menyimpan dan mengembalikan all_nodes_weight

    elif len(internal_array) <= 1:  # kondisi ketika panjang dari graph kurang atau sama dengan 1
        return  # menyimpan dan mengembalikan None

#RadEcc 
# BUAT PILIHAN MENU 2
# fungsi untuk menyajikan hasil shortest path berdasarkan kota asal dalam bentuk list berukuran nxn
def shortest_path_of_a_node_to_list(shortest_path, FROM, daftar_kota):
    cities = city_list(
        daftar_kota)  # memanggil fungsi city_list untuk mendapatkan data list daftar kota, lalu menyimpannya di variabel cities
    FROM_name = cities[FROM]  # menyimpan nama kota awal dalam variabel FROM_name

    # membuat list version dari shortest path. Contoh [["Yakarta", "Yenpasar", 1]]
    shortest_path_list = []  # membuat suatu list kosong di variabel shortest_path_list
    for i in range(len(shortest_path)):  # melakukan looping sebanyak panjangnya data yang ada di shortest_path
        shortest_path_list.append([FROM_name, cities[i], shortest_path[
            i]])  # menambahkan suatu list berisikan kota awal dan tujuan beserta jarak keterpencilannya ke dalam shortest_path_list
    sorting_short = sorted(sorted(shortest_path_list, key=lambda x: x[1]), key=lambda x: x[-1])

    # melakukan sort berdasarkan value nilai keterpencilan dan jikalau ada yang sama akan diurutkan berdasarkan alfabet

    return sorting_short  # menyimpan dan mengembalikan sorted_shortest_path_list
#RadEcc 


# BUAT PILIHAN MENU 1
# fungsi untuk menyajikan hasil shortest path dari keseluruhan kota dalam bentuk list berukuran nxn
def shortest_path_of_nodes_to_list(daftar_kota, graph_tidak_berarah):
    cities = city_list(
        daftar_kota)  # memanggil fungsi city_list untuk mendapatkan data list daftar kota, lalu menyimpannya di variabel cities

    all_nodes_distances = []  # membuat suatu list kosong di variabel all_nodes_distances
    for i in range(len(cities)):  # melakukan looping sebanyak panjangnya data yang ada di cities
        all_nodes_distances.append(
            shortest_path_of_a_node_to_list(shortest_path(i, graph_tidak_berarah), i,
                                            daftar_kota))  # menambahakan data dari keseluruhan shortest path

    all_max_nodes_distances = []  # membuat suatu list kosong di variabel all_max_nodes_distances
    for i in all_nodes_distances:  # melakukan looping pengambilan data dari all_nodes_distances secara satu per satu
        all_max_nodes_distances.append(i[-1])  # mengambil dan lalu menambahkan keterpencilan dari setiap kota

    distances = []  # membuat suatu list kosong di variabel distances
    for i in all_max_nodes_distances:  # melakukan looping pengambilan data dari all_max_nodes_distances secara satu per satu
        distances.append([i[0], i[-1]])  # mengambil dan lalu menambahkan awal dan jarak dari setiap nilai keterpencilan
    sorting_short = sorted(sorted(distances, key=lambda x: x[0]), key=lambda x: x[-1])
    # melakukan sort berdasarkan value nilai keterpencilan dan jikalau ada yang sama akan diurutkan berdasarkan alfabet

    return sorting_short  # menyimpan dan mengembalikan distances
