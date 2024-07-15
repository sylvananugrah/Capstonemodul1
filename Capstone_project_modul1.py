from datetime import datetime;

# Data Pasien Penyakit Dalam RS. Pedjoeang Sehat
list_pasien = [
{'id':101,'nama': 'Husen Akbar', 'usia': 60, 'jenis_kelamin': 'Pria', 'alamat': 'Jl. Kalasan No. 5, Tangerang Selatan','tanggal_registrasi': '2023-06-12', 'kamar': 'Teratai', 'nama_penyakit': 'Stroke', 'dokter': 'dr. khaira,Sp.PD' },
{'id':102,'nama': 'Siti Nurlela', 'usia': 63, 'jenis_kelamin': 'Wanita', 'alamat': 'Jl. Yos Sudarso No. 10, Tangerang','tanggal_registrasi': '2022-10-09', 'kamar': 'Melati', 'nama_penyakit': 'Gagal Jantung', 'dokter': 'dr. Hastari Soekardi,Sp.S'},
{'id':103,'nama': 'Melinda Cantika', 'usia': 55, 'jenis_kelamin': 'Wanita', 'alamat': 'Jl. Benda Barat No. 5, Depok','tanggal_registrasi': '2021-07-17', 'kamar': 'Mawar', 'nama_penyakit': 'Diabetes Melitus', 'dokter': 'dr. Tito Ardi,Sp.PD'},
{'id':104,'nama': 'Sukirman Hadi', 'usia': 75, 'jenis_kelamin': 'Pria', 'alamat': 'Jl. Prambanan No. 15, Jakarta Pusat','tanggal_registrasi': '2020-03-21', 'kamar': 'Sakura', 'nama_penyakit': 'Gagal Ginjal', 'dokter': 'dr. Serina Citra,Sp.PD'},
{'id':105,'nama': 'Nuri Permata', 'usia': 45, 'jenis_kelamin': 'Wanita', 'alamat': 'Jl. Imam Bonjol No. 9, Jakarta Selatan','tanggal_registrasi': '2024-04-04', 'kamar': 'Kamboja', 'nama_penyakit': 'Tuberkulosis', 'dokter': 'dr. Meva Dowinta,Sp.PD'},
{'id':106,'nama': 'Budi Sudarsono', 'usia': 80, 'jenis_kelamin': 'Pria', 'alamat': 'Jl. Sukolilo No. 11, Jakarta Timur','tanggal_registrasi': '2022-06-10', 'kamar': 'Melati', 'nama_penyakit': 'Gagal Jantung', 'dokter': 'dr. Hastari Soekardi,Sp.S'},
{'id':107,'nama': 'Catrine Ningsih', 'usia': 55, 'jenis_kelamin': 'Wanita', 'alamat': 'Jl. Patimura No. 21, Bogor','tanggal_registrasi': '2019-08-10', 'kamar': 'Mawar', 'nama_penyakit': 'Diabetes Melitus', 'dokter': 'dr. Tito Ardi,Sp.PD'},
{'id':108,'nama': 'Yusuf Hidayah', 'usia': 67, 'jenis_kelamin': 'Pria', 'alamat': 'Jl. Sukabakti No. 14, Bogor','tanggal_registrasi': '2017-08-10', 'kamar': 'Teratai', 'nama_penyakit': 'Stroke', 'dokter': 'dr. khaira,Sp.PD'},
{'id':109,'nama': 'Ali Sanjaya', 'usia': 71, 'jenis_kelamin': 'Pria', 'alamat': 'Jl. Gotong Royong No. 8, Bekasi','tanggal_registrasi': '2020-03-23', 'kamar': 'Teratai', 'nama_penyakit': 'Stroke', 'dokter': 'dr. khaira,Sp.PD'},
{'id':110,'nama': 'Nurlela Laili', 'usia': 51, 'jenis_kelamin': 'Wanita', 'alamat': 'Jl. Arya Putra No. 9, Jakarta Timur','tanggal_registrasi': '2022-04-12', 'kamar': 'Mawar', 'nama_penyakit': 'Diabetes Melitus', 'dokter': 'dr. Tito Ardi,Sp.PD'}
]

# Data Riwayat Kematian Pasien
riwayat_kematian = [
{'id':75,'nama': 'Anggi Prastiwi', 'usia': 60, 'jenis_kelamin': 'Wanita', 'nama_penyakit': 'Gagal Jantung'},
{'id':80,'nama': 'Julio Satrio', 'usia': 63, 'jenis_kelamin': 'Pria','nama_penyakit': 'Stoke'},
{'id':91,'nama': 'Randi Setiawan', 'usia': 80, 'jenis_kelamin': 'Pria','nama_penyakit': 'Gagal Jantung'},
{'id':98,'nama': 'Satya Bagus', 'usia': 75, 'jenis_kelamin': 'Pria', 'nama_penyakit': 'Stroke'},
{'id':45,'nama': 'Cantika listi', 'usia': 45, 'jenis_kelamin': 'Wanita','nama_penyakit': 'Diabetes Melitus'},
{'id':55,'nama': 'Yulianti', 'usia': 80, 'jenis_kelamin': 'Wanita','nama_penyakit': 'Diabetes Melitus'},
{'id':87,'nama': 'Dodo Anggoro', 'usia': 55, 'jenis_kelamin': 'Pria','nama_penyakit': 'Stroke'},
{'id':77,'nama': 'Didit Mulyadi', 'usia': 67, 'jenis_kelamin': 'Pria','nama_penyakit': 'Stroke'},
{'id':34,'nama': 'Siti Maemunah', 'usia': 71, 'jenis_kelamin': 'Wanita','nama_penyakit': 'Diabetes Melitus'},
{'id':65,'nama': 'Sekar Indah', 'usia': 51, 'jenis_kelamin': 'Wanita','nama_penyakit': 'Diabetes Melitus'},
{'id':25,'nama': 'Ningrum Fitri', 'usia': 51, 'jenis_kelamin': 'Wanita','nama_penyakit': 'Leukimia'}
]


# Data Dokter Spesialis Penyakit Dalam RS. Pedjoeang Sehat
list_dokter = [
{'id_dokter': 1,'nama': 'dr. khaira,Sp.PD','jenis_kelamin': 'Wanita', 'bidang_keahlian': 'Stroke'},
{'id_dokter': 2,'nama': 'dr. Hastari Soekardi,Sp.S','jenis_kelamin': 'Wanita', 'bidang_keahlian': 'Gagal Jantung'},
{'id_dokter': 3,'nama': 'dr. Tito Ardi,Sp.PD','jenis_kelamin': 'Pria', 'bidang_keahlian': 'Diabetes Melitus'},
{'id_dokter': 4,'nama': 'dr. Serina Citra,Sp.PD','jenis_kelamin': 'Wanita', 'bidang_keahlian': 'Gagal Ginjal'},
{'id_dokter': 5,'nama': 'dr. Meva Dowinta,Sp.PD','jenis_kelamin': 'Wanita', 'bidang_keahlian': 'Tuberkulosis'}
]

# Kamar Rumah Sakit Pedjoeang Sehat
list_kamar = ['Teratai', 'Melati', 'Mawar', 'Sakura', 'Kamboja']


# Main Menu
def main_menu():
    menu = input('''
### Selamat Datang di Rumah Sakit Pedjoeang Sehat ###
    “the greatest wealth is health and vice versa”
                     
List Menu:
1. Menampilkan Data Pasien Rawat Inap Penyakit Dalam
2. Menambahkan Pasien Baru
3. Menghapus Data Pasien
4. Pengkinian Data Pasien
5. Menu Dokter                 
6. Daftar Riwayat Kematian Pasien
7. Keluar Program
Masukkan angka Menu yang ingin dijalankan :''')

    if menu == '1':
        menu_1()
    elif menu == '2':
        menu_2()
    elif menu == '3':
        menu_3()
    elif menu == '4':
        menu_4()
    elif menu == '5':
        menu_5()
    elif menu == '6':
        menu_6()
    elif menu == '7':
        print("Terimakasih Telah Berkunjung")
        exit() 
    else:
        print("Input Tidak Valid")
        main_menu()


# Menjalankan Program 1 Menampilkan Data Pasien
def menu_1():
    menu = input('''
Menampilkan Data Pasien Rawat Inap Penyakit Dalam
1. Menampilkan Seluruh Data Pasien Rawat Inap Penyakit Dalam
2. Mencari Informasi Perawatan Pasien Rawat Inap Penyakit Dalam
3. Kembali ke Menu Awal
Masukkan angka Menu yang ingin dijalankan :''')

    if menu == '1':
        print('Data Pasien Rawat Inap Penyakit Dalam')
        print(f"{'Nomor':<5}|{'Nama':<17}|{'Usia':<4}|{'J. Kelamin':<10}|{'Alamat':<38}|{'Tanggal Daftar':<14}|{'Kamar':<7}|{'Nama Penyakit':<17}|{'Dokter':<15}")
        for pasien in range(len(list_pasien)):
            print(f"{list_pasien[pasien]['id']:<5}|{list_pasien[pasien]['nama']:<17}|{list_pasien[pasien]['usia']:<4}|{list_pasien[pasien]['jenis_kelamin']:<10}|{list_pasien[pasien]['alamat']:<38}|{list_pasien[pasien]['tanggal_registrasi']:<14}|{list_pasien[pasien]['kamar']:<7}|{list_pasien[pasien]['nama_penyakit']:<17}|{list_pasien[pasien]['dokter']:<15}")
    
    elif menu == '2':
        try:
            while True:
                nama = input('Masukkan nama lengkap pasien: ')
                data = list(filter(lambda pasien: pasien if pasien['nama'] == nama.title() else '', list_pasien))
                print(f'Nama pasien {data[0]['nama']} mengalami sakit {data[0]['nama_penyakit']} sedang dirawat di kamar {data[0]['kamar']} dan berada dalam penanganan {data[0]['dokter']}')
                break
        except IndexError:
            print('Nama pasien tidak terdaftar, Silahkan input ulang nama lengkap dengan benar')
    elif menu == '3':
        main_menu()
    else:
        print('Menu tidak tersedia')
    menu_1()

# Menjalankan Progam 2 Menambahkan Data Pasien Baru
def menu_2():
    menu = input('''
Menambah Data Pasien
1. Menambah Data Pasien
2. Kembali ke Menu Awal
Masukkan angka Menu yang ingin dijalankan :''')

    if menu == '1':
        # pengisian_nama_pasien
        try:
            while True:
                input_nama = input("Masukkan nama pasien: ")
                if len(input_nama) > 0:
                    kata = input_nama.split()
                    satukan = ''.join(kata)
                    if satukan.isalpha():
                        break
                    else:
                        print("Isi nama pasien dengan huruf alfabet.")
            # pengisian_usia
            input_usia = int(input('Masukkan usia pasien: '))
            # pengisian_kelamin 
            while True:
                input_kelamin = input('Masukkan jenis Kelamin (Pria/Wanita): ')
                if input_kelamin.lower() == 'pria' or input_kelamin.lower() == 'wanita':
                    break
                else:
                    print('Silahkan isi jenis kelamin yang sesuai')
            # pengisian_alamat
            input_alamat = input('Masukkan alamat pasien (nama jl & kab/kota): ')
            # pengisian_kamar
            while True :
                input_kamar = input('Masukkan kamar pasien: ')
                if input_kamar.capitalize() in list_kamar:
                    break
                else:
                    print('Kamar yang di input tidak tersedia')
            # pengisian_nama_penyakit
            input_penyakit = input('Masukkan nama penyakit pasien: ')
            # pengisian_dokter
            input_dokter = input('Masukkan nama dokter: ')
            # proses penambahan data
            list_pasien.append({
                    'id':list_pasien[len(list_pasien)-1]['id'] + 1 , 
                    'nama':input_nama,
                    'usia':input_usia,
                    'jenis_kelamin':input_kelamin.capitalize(),
                    'alamat':input_alamat,
                    'tanggal_registrasi' : datetime.now().strftime("%Y-%m-%d"),
                    'kamar':input_kamar.capitalize(),
                    'nama_penyakit':input_penyakit.capitalize(),
                    'dokter':input_dokter
                    })
            # Proses penambahan pada tampilan
            print(f"{'Nomor':<5}|{'Nama':<17}|{'Usia':<4}|{'J. Kelamin':<10}|{'Alamat':<38}|{'Tanggal Daftar':<14}|{'Kamar':<7}|{'Nama Penyakit':<17}|{'Dokter':<15}")
            for pasien in range(len(list_pasien)):
                print(f"{list_pasien[pasien]['id']:<5}|{list_pasien[pasien]['nama']:<17}|{list_pasien[pasien]['usia']:<4}|{list_pasien[pasien]['jenis_kelamin']:<10}|{list_pasien[pasien]['alamat']:<38}|{list_pasien[pasien]['tanggal_registrasi']:<14}|{list_pasien[pasien]['kamar']:<7}|{list_pasien[pasien]['nama_penyakit']:<17}|{list_pasien[pasien]['dokter']:<15}")
                print("Data Pasien Berhasil ditambahkan !!!")
        except ValueError:
            print('Isi usia pasien dengan angka')        
    elif menu == '2':
        main_menu()
    else:
        print('Menu tidak tersedia')  
    menu_2()


# Menjalankan Progam 3 Menghapus Data Pasien
def menu_3():
    menu = input('''
Menghapus Data Pasien
1. Menghapus Data Pasien
2. Kembali ke Menu Awal
Masukkan angka Menu yang ingin dijalankan :''')

    if menu == '1':
        try:
            print(f"{'Nomor':<5}|{'Nama':<17}|{'Usia':<4}|{'J. Kelamin':<10}|{'Alamat':<38}|{'Tanggal Daftar':<14}|{'Kamar':<7}|{'Nama Penyakit':<17}|{'Dokter':<15}")
            for pasien in range(len(list_pasien)):
                print(f"{list_pasien[pasien]['id']:<5}|{list_pasien[pasien]['nama']:<17}|{list_pasien[pasien]['usia']:<4}|{list_pasien[pasien]['jenis_kelamin']:<10}|{list_pasien[pasien]['alamat']:<38}|{list_pasien[pasien]['tanggal_registrasi']:<14}|{list_pasien[pasien]['kamar']:<7}|{list_pasien[pasien]['nama_penyakit']:<17}|{list_pasien[pasien]['dokter']:<15}")
            delete_id = int(input('Masukkan id pasien yang ingin dihapus : '))
            data_delete = list(filter(lambda pasien: pasien if pasien['id'] == delete_id else '', list_pasien))
            print()
            print('List Hapus:')
            print(f"{'Nomor':<5}|{'Nama':<17}|{'Usia':<4}|{'J. Kelamin':<10}|{'Alamat':<38}|{'Tanggal Daftar':<14}|{'Kamar':<7}|{'Nama Penyakit':<17}|{'Dokter':<15}")
            print(f"{data_delete[0]['id']:<5}|{data_delete[0]['nama']:<17}|{data_delete[0]['usia']:<4}|{data_delete[0]['jenis_kelamin']:<10}|{data_delete[0]['alamat']:<38}|{data_delete[0]['tanggal_registrasi']:<14}|{data_delete[0]['kamar']:<7}|{data_delete[0]['nama_penyakit']:<17}|{data_delete[0]['dokter']:<15}")
            konfirmasi_hapus = input(f"Apakah yakin ingin menghapus data pasien dengan id nomor {data_delete[0]['id']}? (Ya/Tidak) : ")
            if konfirmasi_hapus.lower() == 'tidak':
                print('Penghapusan data pasien dibatalkan')
            elif konfirmasi_hapus.lower() == 'ya':
                list_pasien.remove(data_delete[0])
                print(f"{'Nomor':<5}|{'Nama':<17}|{'Usia':<4}|{'J. Kelamin':<10}|{'Alamat':<38}|{'Tanggal Daftar':<14}|{'Kamar':<7}|{'Nama Penyakit':<17}|{'Dokter':<15}")
                for pasien in range(len(list_pasien)):
                    print(f"{list_pasien[pasien]['id']:<5}|{list_pasien[pasien]['nama']:<17}|{list_pasien[pasien]['usia']:<4}|{list_pasien[pasien]['jenis_kelamin']:<10}|{list_pasien[pasien]['alamat']:<38}|{list_pasien[pasien]['tanggal_registrasi']:<14}|{list_pasien[pasien]['kamar']:<7}|{list_pasien[pasien]['nama_penyakit']:<17}|{list_pasien[pasien]['dokter']:<15}")
                    print('Data pasien berhasil dihapus !!!')
            else:
                print('Data yang di input tidak sesuai')
        except ValueError:
                print()
                print('Nomor id pasien tidak terdaftar, Silahkan input ulang')
        except IndexError:
                print()
                print('Nomor id pasien tidak terdaftar, Silahkan input ulang')
    elif menu == '2':
        main_menu()
    else:
        print('Menu tidak tersedia')
    menu_3()


# Menjalankan Progam 4 Pengkinian Data
def menu_4():
    menu = input('''
Pengkinian Data Pasien
1. Perbarui Data Pasien
2. Kembali ke Menu Awal
Masukkan angka Menu yang ingin dijalankan :''')

    if menu == '1':
        try:
            print(f"{'Nomor':<5}|{'Nama':<17}|{'Usia':<4}|{'J. Kelamin':<10}|{'Alamat':<38}|{'Tanggal Daftar':<14}|{'Kamar':<7}|{'Nama Penyakit':<17}|{'Dokter':<15}")
            for pasien in range(len(list_pasien)):
                print(f"{list_pasien[pasien]['id']:<5}|{list_pasien[pasien]['nama']:<17}|{list_pasien[pasien]['usia']:<4}|{list_pasien[pasien]['jenis_kelamin']:<10}|{list_pasien[pasien]['alamat']:<38}|{list_pasien[pasien]['tanggal_registrasi']:<14}|{list_pasien[pasien]['kamar']:<7}|{list_pasien[pasien]['nama_penyakit']:<17}|{list_pasien[pasien]['dokter']:<15}")
            edit_id = int(input('Masukkan Nomor id Pasien yang ingin perbarui : '))
            edit_data = list(filter(lambda pasien: pasien if pasien['id'] == edit_id else '', list_pasien))
            print()
            print('List Edit:')
            print(f"{'Nomor':<5}|{'Nama':<17}|{'Usia':<4}|{'J. Kelamin':<10}|{'Alamat':<38}|{'Tanggal Daftar':<14}|{'Kamar':<7}|{'Nama Penyakit':<17}|{'Dokter':<15}")
            print(f"{edit_data[0]['id']:<5}|{edit_data[0]['nama']:<17}|{edit_data[0]['usia']:<4}|{edit_data[0]['jenis_kelamin']:<10}|{edit_data[0]['alamat']:<38}|{edit_data[0]['tanggal_registrasi']:<14}|{edit_data[0]['kamar']:<7}|{edit_data[0]['nama_penyakit']:<17}|{edit_data[0]['dokter']:<15}")
            konfirmasi_input = True
            while konfirmasi_input :
                edit = input(f"Apakah ingin mengupdate data dengan nomor pasien {edit_data[0]['id']} (Ya/Tidak) : ")
                if edit.lower() == 'ya':
                    konfirmasi_input = False
                    menu_edit = True
                    while menu_edit:
                        list_edit = input('''
Pilih kolom yang ingin diupdate
1. Nama
2. Usia
3. Alamat
4. Dokter
5. Kembali ke Menu Edit
Masukkan angka kolom yang ingin diupdate :''')
                        # Edit Kolom Nama
                        if list_edit == '1':
                            edit_nama = True
                            while edit_nama :
                                nama_baru = input("Masukkan Nama Pasien : ")
                                if len(nama_baru) > 0:
                                    kata = nama_baru.split()
                                    satukan = ''.join(kata)
                                    if satukan.isalpha() == True:
                                        edit_nama = False
                                    else:
                                        print("Isi nama pasien dengan huruf alfabet")
                            print(f"Data nama akan berubah dari {edit_data[0]['nama']} menjadi {nama_baru}")
                            konfirmasi_nama = True
                            while konfirmasi_nama:
                                confirm_nama = input("Apakah Anda tetap ingin memperbarui nama pasien? (Ya/Tidak) : ")
                                if confirm_nama.lower() == 'ya':
                                    konfirmasi_nama = False
                                    edit_data[0]['nama'] = nama_baru.title()
                                    print(f"{'Nomor':<5}|{'Nama':<17}|{'Usia':<4}|{'J. Kelamin':<10}|{'Alamat':<38}|{'Tanggal Daftar':<14}|{'Kamar':<7}|{'Nama Penyakit':<17}|{'Dokter':<15}")
                                    print(f"{edit_data[0]['id']:<5}|{edit_data[0]['nama']:<17}|{edit_data[0]['usia']:<4}|{edit_data[0]['jenis_kelamin']:<10}|{edit_data[0]['alamat']:<38}|{edit_data[0]['tanggal_registrasi']:<14}|{edit_data[0]['kamar']:<7}|{edit_data[0]['nama_penyakit']:<17}|{edit_data[0]['dokter']:<15}")
                                    print("Data Berhasil Di Update !!!")
                                    konfirmasi_isiLagi = True
                                    while konfirmasi_isiLagi :
                                        edit_lagi = input('Apakah Anda ingin memperbarui keterangan yang lain ? (Ya/Tidak): ')
                                        if edit_lagi.lower() == 'ya':
                                            konfirmasi_isiLagi = False
                                            menu_edit = True
                                        elif edit_lagi.lower() == 'tidak':
                                            konfirmasi_isiLagi = False
                                            menu_edit = False
                                        else:
                                            print('Data yang di input tidak sesuai')
                                elif confirm_nama.lower() == 'tidak':
                                    konfirmasi_nama = False
                                    print('Pembaruan nama pasien dibatalkan')
                                else:
                                    print('Data yang di input tidak sesuai')
                        # Edit Kolom Usia                
                        elif list_edit == '2':
                            try:
                                usia_baru = int(input('Masukkan usia pasien: '))
                                print(f"Data usia akan berubah dari {edit_data[0]['usia']} menjadi {usia_baru}")   
                                konfirmasi_usia = True
                                while konfirmasi_usia:
                                    confirm_usia = input("Apakah Anda tetap ingin memperbarui usia pasien? (Ya/Tidak) : ")
                                    if confirm_usia.lower() == 'ya':
                                        konfirmasi_usia = False
                                        edit_data[0]['usia'] = usia_baru
                                        print(f"{'Nomor':<5}|{'Nama':<17}|{'Usia':<4}|{'J. Kelamin':<10}|{'Alamat':<38}|{'Tanggal Daftar':<14}|{'Kamar':<7}|{'Nama Penyakit':<17}|{'Dokter':<15}")
                                        print(f"{edit_data[0]['id']:<5}|{edit_data[0]['nama']:<17}|{edit_data[0]['usia']:<4}|{edit_data[0]['jenis_kelamin']:<10}|{edit_data[0]['alamat']:<38}|{edit_data[0]['tanggal_registrasi']:<14}|{edit_data[0]['kamar']:<7}|{edit_data[0]['nama_penyakit']:<17}|{edit_data[0]['dokter']:<15}")
                                        print("Data Berhasil Di Update !!!")
                                        konfirmasi_isiLagi = True
                                        while konfirmasi_isiLagi :
                                            edit_lagi = input('Apakah Anda ingin memperbarui keterangan yang lain ? (Ya/Tidak): ')
                                            if edit_lagi.lower() == 'ya':
                                                konfirmasi_isiLagi = False
                                                menu_edit = True
                                            elif edit_lagi.lower() == 'tidak':
                                                konfirmasi_isiLagi = False
                                                menu_edit = False
                                            else:
                                                print('Data yang di input tidak sesuai')
                                    elif confirm_usia.lower() == 'tidak':
                                        konfirmasi_usia = False
                                        print('Pembaruan usia pasien dibatalkan')
                                    else :
                                        print("Data yang di input tidak Sesuai")
                            except ValueError:
                                print('Masukkan Usia dengan nilai angka')
                        # Edit Kolom Alamat
                        elif list_edit == '3':
                            alamat_baru = input('Masukkan alamat pasien: ')
                            print(f'Data alamat akan berubah dari{edit_data[0]['alamat']} menjadi {alamat_baru}')
                            konfirmasi_alamat = True
                            while konfirmasi_alamat:
                                confirm_alamat = input('Apakah Anda tetap ingin memperbarui alamat pasien ? (ya/tidak)')
                                if confirm_alamat.lower() == 'ya':
                                    konfirmasi_alamat = False
                                    edit_data[0]['alamat'] = alamat_baru
                                    print(f"{'Nomor':<5}|{'Nama':<17}|{'Usia':<4}|{'J. Kelamin':<10}|{'Alamat':<38}|{'Tanggal Daftar':<14}|{'Kamar':<7}|{'Nama Penyakit':<17}|{'Dokter':<15}")
                                    print(f"{edit_data[0]['id']:<5}|{edit_data[0]['nama']:<17}|{edit_data[0]['usia']:<4}|{edit_data[0]['jenis_kelamin']:<10}|{edit_data[0]['alamat']:<38}|{edit_data[0]['tanggal_registrasi']:<14}|{edit_data[0]['kamar']:<7}|{edit_data[0]['nama_penyakit']:<17}|{edit_data[0]['dokter']:<15}")
                                    print("Data Berhasil Di Update !!!")
                                    konfirmasi_isiLagi = True
                                    while konfirmasi_isiLagi:
                                        edit_lagi = input('Apakah Anda ingin memperbarui keterangan yang lain ? (Ya/Tidak): ')
                                        if edit_lagi.lower() == 'ya':
                                            konfirmasi_isiLagi = False
                                            menu_edit = True
                                        elif edit_lagi.lower() == 'tidak':
                                            konfirmasi_isiLagi = False
                                            menu_edit = False
                                        else:
                                            print('Data yang di input tidak sesuai')
                                elif confirm_alamat.lower() == 'tidak':
                                    konfirmasi_alamat = False
                                    print('Pembaruan alamat pasien dibatalkan')
                                else :
                                    print("Data yang di input tidak sesuai")
                        # Edit Kolom Dokter
                        elif list_edit == '4':
                            dokter_baru = input('Masukkan nama dokter yang menangani pasien: ')
                            print(f'Data nama dokter akan berubah dari{edit_data[0]['dokter']} menjadi {dokter_baru}')
                            konfirmasi_dokter = True
                            while konfirmasi_dokter:
                                confirm_dokter = input('Apakah Anda tetap ingin memperbarui nama dokter ? (ya/tidak)')
                                if confirm_dokter.lower() == 'ya':
                                    konfirmasi_dokter = False
                                    edit_data[0]['dokter'] = dokter_baru
                                    print(f"{'Nomor':<5}|{'Nama':<17}|{'Usia':<4}|{'J. Kelamin':<10}|{'Alamat':<38}|{'Tanggal Daftar':<14}|{'Kamar':<7}|{'Nama Penyakit':<17}|{'Dokter':<15}")
                                    print(f"{edit_data[0]['id']:<5}|{edit_data[0]['nama']:<17}|{edit_data[0]['usia']:<4}|{edit_data[0]['jenis_kelamin']:<10}|{edit_data[0]['alamat']:<38}|{edit_data[0]['tanggal_registrasi']:<14}|{edit_data[0]['kamar']:<7}|{edit_data[0]['nama_penyakit']:<17}|{edit_data[0]['dokter']:<15}")
                                    print("Data Berhasil Di Update !!!")
                                    konfirmasi_isiLagi = True
                                    while konfirmasi_isiLagi:
                                        edit_lagi = input('Apakah Anda ingin memperbarui keterangan yang lain ? (Ya/Tidak): ')
                                        if edit_lagi.lower() == 'ya':
                                            konfirmasi_isiLagi = False
                                            menu_edit = True
                                        elif edit_lagi.lower() == 'tidak':
                                            konfirmasi_isiLagi = False
                                            menu_edit = False
                                        else:
                                            print('Data yang di input tidak sesuai')
                                elif confirm_dokter.lower() == 'tidak':
                                    konfirmasi_dokter = False
                                    print('Pembaruan penanganan dokter dibatalkan')
                        elif list_edit == '5':
                            menu_4()
                        else:
                            print('Data yang di input tidak sesuai')
                elif edit.lower() == 'tidak' :
                    konfirmasi_input = False
                    print('Pengkinian data pasien dibatalkan')
                else :
                    print("Input tidak valid")
        except IndexError:
                print()
                print('Nomor id pasien tidak terdaftar, Silahkan input ulang')
        except ValueError:
                print()
                print('Nomor id pasien tidak terdaftar, Silahkan input ulang')     
    elif menu == '2':
        main_menu()
    else:
        print('Menu Tidak Tersedia')
    menu_4()    

# Menjalankan Progam 5 Menu Dokter
def menu_5():
    menu = input('''
Menu Dokter
1. Menampilkan Data Dokter
2. Menambah Data Dokter
3. Menghapus Data Dokter
4. Kembali ke Menu Awal
Masukkan angka Menu yang ingin dijalankan :''')
    # Menampilkan Data Dokter
    if menu == '1':
        print()
        print('Data Dokter yang bertugas')
        print(f"{'Id Dokter':<10}|{'Nama':<25}|{'Jenis Kelamin':<15}|{'Bidang Keahlian':<17}|")
        for dokter in range(len(list_dokter)):
            print(f"{list_dokter[dokter]['id_dokter']:<10}|{list_dokter[dokter]['nama']:<25}|{list_dokter[dokter]['jenis_kelamin']:<15}|{list_dokter[dokter]['bidang_keahlian']:<17}|")
    
    # Menambahkan Data Dokter
    elif menu == '2':
        # pengisian_nama_dokter
        while True:
            input_dokter = input("Masukkan nama dokter beserta gelarnya: ")
            if input_dokter.isascii:
                break
            else:
                print("Isi nama dokter dengan benar.")
        # pengisian_jenis_kelamin
        while True:
                input_kelamin = input('Masukkan jenis Kelamin (Pria/Wanita): ')
                if input_kelamin.lower() == 'pria' or input_kelamin.lower() == 'wanita':
                    break
                else:
                    print('Silahkan isi jenis kelamin yang sesuai')
        # pengisian_bidang_keahlian
        while True:
            input_keahlian = input('Masukkan keahlian pada bidang penyakit dalam: ')
            if len(input_keahlian) > 0:
                kata = input_keahlian.split()
                satukan = ''.join(kata)
                if satukan.isalpha():
                    break
                else:
                    print("Isi bidang keahlian dengan huruf alfabet.")
        # proses penambahan data
        list_dokter.append({
                'id_dokter':list_dokter[len(list_dokter)-1]['id_dokter'] + 1 , 
                'nama':input_dokter,
                'jenis_kelamin':input_kelamin.capitalize(),
                'bidang_keahlian':input_keahlian
                })
        # Proses penambahan pada tampilan
        print(f"{'Id Dokter':<10}|{'Nama':<25}|{'Jenis Kelamin':<15}|{'Bidang Keahlian':<17}|")
        for dokter in range(len(list_dokter)):
            print(f"{list_dokter[dokter]['id_dokter']:<10}|{list_dokter[dokter]['nama']:<25}|{list_dokter[dokter]['jenis_kelamin']:<15}|{list_dokter[dokter]['bidang_keahlian']:<17}|")
    # Menhapus Data Dokter
    elif menu == '3':
        try:
            print('Data Dokter yang bertugas')
            print(f"{'Id Dokter':<10}|{'Nama':<25}|{'Jenis Kelamin':<15}|{'Bidang Keahlian':<17}|")
            for dokter in range(len(list_dokter)):
                print(f"{list_dokter[dokter]['id_dokter']:<10}|{list_dokter[dokter]['nama']:<25}|{list_dokter[dokter]['jenis_kelamin']:<15}|{list_dokter[dokter]['bidang_keahlian']:<17}|")
            delete_dokter = int(input('Masukkan Id dokter yang ingin di hapus: '))
            data_delete = list(filter(lambda dokter: dokter if dokter['id_dokter'] == delete_dokter else '', list_dokter))
            print()
            print('List Hapus:')
            print(f"{'Id Dokter':<10}|{'Nama':<25}|{'Jenis Kelamin':<15}|{'Bidang Keahlian':<17}|")
            print(f"{data_delete[0]['id_dokter']:<10}|{data_delete[0]['nama']:<25}|{data_delete[0]['jenis_kelamin']:<15}|{data_delete[0]['bidang_keahlian']:<17}")
            konfirmasi_hapus = input(f"Apakah yakin ingin menghapus data dokter dengan id nomor {data_delete[0]['id_dokter']}? (Ya/Tidak) : ")
            if konfirmasi_hapus.lower() == 'tidak':
                print('Penghapusan data dokter dibatalkan')
            elif konfirmasi_hapus.lower() == 'ya':
                list_dokter.remove(data_delete[0])
                print(f"{'Id Dokter':<10}|{'Nama':<25}|{'Jenis Kelamin':<15}|{'Bidang Keahlian':<17}|")
                for dokter in range(len(list_dokter)):
                    print(f"{list_dokter[dokter]['id_dokter']:<10}|{list_dokter[dokter]['nama']:<25}|{list_dokter[dokter]['jenis_kelamin']:<15}|{list_dokter[dokter]['bidang_keahlian']:<17}|")
                    print('Data dokter berhasil dihapus !!!')
        except ValueError:
                print()
                print('Nomor id dokter tidak terdaftar, Silahkan input ulang')
        except IndexError:
                print()
                print('Nomor id dokter tidak terdaftar, Silahkan input ulang')
    elif menu == '4':
        main_menu()
    else:
        print('Menu tidak tersedia')
    menu_5()


# Menjalankan Progam 6 Daftar Riwayat Kematian
def menu_6():
    menu = input('''
Menu Dokter
1. Menampilkan Daftar Kematian
2. Menghitung Jumlah Kematian terbesar berdasarkan penyakit
3. Kembali ke Menu Awal
Masukkan angka Menu yang ingin dijalankan :''')
    
    if menu == '1':
        print(f"{'Id':<3}|{'Nama':<25}|{'Usia':<5}|{'Jenis Kelamin':<15}|{'Nama Penyakit':<15}")
        for dafmat in range(len(riwayat_kematian)):
            print(f"{riwayat_kematian[dafmat]['id']:<3}|{riwayat_kematian[dafmat]['nama']:<25}|{riwayat_kematian[dafmat]['usia']:<5}|{riwayat_kematian[dafmat]['jenis_kelamin']:<15}|{riwayat_kematian[dafmat]['nama_penyakit']:<15}")
            
    elif menu == '2':
        jumlah_penyakit = {}
        for pasien in riwayat_kematian:
            penyakit = pasien['nama_penyakit']
            if penyakit not in jumlah_penyakit:
                jumlah_penyakit[penyakit] = 0
            jumlah_penyakit[penyakit] += 1
        
        # Menampilkan hasil
        for penyakit, jumlah in jumlah_penyakit.items():
            print(f"Penyakit: {penyakit}, Jumlah: {jumlah}")

    elif menu == '3':
        main_menu()



main_menu()





