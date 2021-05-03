# Christina Andrea Putri - Universitas Kristen Duta Wacana

# Agria membuat program sederhana untuk menuliskan judul-judul drama korea yang ia sukai. Ada 2 command yaitu tambah (menambah data) dan selesai (output).
# Bagaimana hasilnya jika ia ingin memasukkan 5 judul drama korea favoritnya?

# Input : jumlah data, judul 
# Proses : memasukkan data ke dalam list, mengubah list menjadi bentuk tuples
# Output : data-data dalam tuples dan list

try:
    while True:
        inp=int(input("Jumlah data:"))
        emp = [] 
        for i in range(inp):
            inp_data = input("Judul drama %d:"%(i+1))
            emp.append(inp_data)

            empt = tuple(emp)
        
        comm=input("Command : ")
        while comm=="tambah":
            inp=int(input("Jumlah data:"))
         
            for i in range(inp):
                inp_data = input("Judul drama %d:"%(i+1))
                emp.append(inp_data)

            empt = tuple(emp)
            comm=input("Command : ")
        else : 
            print("Input data telah selesai.")

            print("Dalam tuples: ", empt)
            print("Dalam list : ", emp)
            for i in empt:
                print("##", i)
            break

except:
    print("Code error")
