from django.db import models

# Create your models here.

class NIK(models.Model):
    nik = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.nik

class Penduduk(models.Model):
    nik_pelapor = models.CharField(max_length=30, null=False, blank=False)
    nama_pelapor = models.CharField(max_length=50)
    nama_terduga = models.CharField(max_length=50)
    alamat_terduga = models.CharField(max_length=512)
    gejala = models.CharField(max_length=512)
    nama_petugas = models.CharField(max_length=50, null=True, blank=True)
    tgl_jemput = models.CharField(max_length=50, null=True, blank=True)
    jumlah = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nama_terduga

