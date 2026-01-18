# list untuk nyimpan tugas-tugas2
tugas_list = []
id_counter = 1

def lihat_tugas():
    print("\n=== DAFTAR TUGAS ===")
    
    if len(tugas_list) == 0:
        print("Belum ada tugas nih")
    else:
        print("ID | Tugas | Deadline | Status")
        print("-" * 50)
        for t in tugas_list:
            print(f"{t['id']} | {t['nama']} | {t['deadline']} | {t['status']}")
    
    input("\nEnter...")

def tambah():
    global id_counter
    
    print("\n=== TAMBAH TUGAS ===")
    nama = input("Tugas: ")
    dl = input("Deadline (contoh: 20/01/2026): ")
    
    if nama == "" or dl == "":
        print("Harus diisi semua!")
        input("\nEnter...")
        return
    
    tugas_baru = {
        "id": id_counter,
        "nama": nama,
        "deadline": dl,
        "status": "belum"
    }
    
    tugas_list.append(tugas_baru)
    id_counter += 1
    
    print("Berhasil ditambahkan!")
    input("\nEnter...")

def selesaikan():
    print("\n=== TANDAI SELESAI ===")
    
    if len(tugas_list) == 0:
        print("Ga ada tugas")
        input("\nEnter...")
        return
    
    try:
        id_cari = int(input("ID tugas: "))
    except:
        print("ID harus angka!")
        input("\nEnter...")
        return
    
    ketemu = False
    for t in tugas_list:
        if t["id"] == id_cari:
            ketemu = True
            if t["status"] == "selesai":
                print("Udah selesai kok")
            else:
                t["status"] = "selesai"
                print(f"Tugas '{t['nama']}' selesai!")
            break
    
    if not ketemu:
        print("ID ga ketemu")
    
    input("\nEnter...")

def hapus():
    print("\n=== HAPUS TUGAS ===")
    
    if len(tugas_list) == 0:
        print("Ga ada tugas")
        input("\nEnter...")
        return
    
    try:
        id_cari = int(input("ID tugas yang mau dihapus: "))
    except:
        print("ID harus angka!")
        input("\nEnter...")
        return
    
    for i in range(len(tugas_list)):
        if tugas_list[i]["id"] == id_cari:
            konfirm = input(f"Yakin hapus '{tugas_list[i]['nama']}'? (y/n): ")
            if konfirm == "y":
                tugas_list.pop(i)
                print("Udah dihapus")
            else:
                print("Batal")
            input("\nEnter...")
            return
    
    print("ID ga ketemu")
    input("\nEnter...")

def filter_status():
    print("\n=== FILTER ===")
    print("1. Yang belum selesai")
    print("2. Yang udah selesai")
    
    pilih = input("\nPilih: ")
    
    if pilih == "1":
        cari = "belum"
    elif pilih == "2":
        cari = "selesai"
    else:
        print("Salah pilih!")
        input("\nEnter...")
        return
    
    hasil = []
    for t in tugas_list:
        if t["status"] == cari:
            hasil.append(t)
    
    print(f"\nTugas yang {cari}:")
    
    if len(hasil) == 0:
        print(f"Ga ada yang {cari}")
    else:
        print("ID | Tugas | Deadline | Status")
        print("-" * 50)
        for t in hasil:
            print(f"{t['id']} | {t['nama']} | {t['deadline']} | {t['status']}")
    
    input("\nEnter...")

def info():
    print("\n=== INFO ===")
    
    total = len(tugas_list)
    selesai = 0
    belum = 0
    
    for t in tugas_list:
        if t["status"] == "selesai":
            selesai += 1
        else:
            belum += 1
    
    print(f"Total: {total} tugas")
    print(f"Selesai: {selesai}")
    print(f"Belum: {belum}")
    
    if total > 0:
        persen = (selesai / total) * 100
        print(f"Progress: {persen:.0f}%")
    
    input("\nEnter...")

# program utama
def main():
    print("\n=============================")
    print("   TO-DO LIST APP")
    print("=============================")
    print("Halo! Atur tugas kamu disini")
    input("\nEnter buat mulai...")
    
    while True:
        print("\n=============================")
        print("       MENU")
        print("=============================")
        print("1. Lihat Semua Tugas")
        print("2. Tambah Tugas")
        print("3. Tandai Selesai")
        print("4. Hapus Tugas")
        print("5. Filter Tugas")
        print("6. Info")
        print("7. Keluar")
        
        menu = input("\nPilih (1-7): ")
        
        if menu == "1":
            lihat_tugas()
        elif menu == "2":
            tambah()
        elif menu == "3":
            selesaikan()
        elif menu == "4":
            hapus()
        elif menu == "5":
            filter_status()
        elif menu == "6":
            info()
        elif menu == "7":
            print("\nOke bye! Semangat ngerjain tugasnya!\n")
            break
        else:
            print("\nSalah input!")
            input("\nEnter...")

if __name__ == "__main__":
    main()