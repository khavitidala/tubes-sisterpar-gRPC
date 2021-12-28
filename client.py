import grpc
from serverapp_proto import penduduk_pb2, penduduk_pb2_grpc

with grpc.insecure_channel('localhost:50051') as channel:
    stub = penduduk_pb2_grpc.PendudukControllerStub(channel)
    nmnik = input("Masukkan NIK: ")
    pelapor = input("Masukkan nama pelapor: ")
    terduga = input("Masukkan nama terduga: ")
    alamat = input("Masukkan alamat: ")
    gejala = input("Masukkan gelaja yang dialami: ")
    
    try:
        res = stub.Create(penduduk_pb2.Penduduk(nik_pelapor=nmnik, nama_pelapor=pelapor, nama_terduga=terduga, alamat_terduga=alamat, gejala=gejala))
        print("========PENJEMPUTAN========")
        print("Nama terduga covid\t:", terduga)
        print("Nama Penanggung Jawab Petugas\t:", res.nama_petugas)
        print("Jumlah petugas\t:", res.jumlah)
        print("Waktu penjemputan\t:", res.tgl_jemput)
        print("===========================")
    except:
        print("NIK yang dimasukkan tidak valid!")
