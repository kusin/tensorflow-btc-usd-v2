import time

def konversi_detik(detik):
  """
  Fungsi untuk mengkonversi nilai detik ke format jam, menit, dan detik.

  Args:
    detik: Nilai detik yang ingin dikonversi (int).

  Returns:
    Tuple yang berisi nilai jam, menit, dan detik (tuple).
  """
  waktu = time.gmtime(detik)  # Mengubah detik ke waktu struct
  jam = waktu.tm_hour
  menit = waktu.tm_min
  detik = waktu.tm_sec

  return jam, menit, detik

start = time.time()

# Contoh penggunaan
detik_input = int(input("Masukkan nilai detik: "))
jam, menit, detik = konversi_detik(detik_input)
print("{:0>2}:{:0>2}:{:0>2}".format(int(jam),int(menit),int(detik)))


# Set akhir waktu komputasi 
# Set waktu komputasi

end = time.time()
waktu = start - end
print(start)
print(end)


