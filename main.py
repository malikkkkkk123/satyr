import time

meme_dict = {
            "CRINGE" : "Sesuatu yang sangat aneh atau memalukan",
            "LOL" : "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL" : "anggapan terhadap lelucon", 
            'CREEPY' : 'menakutkan, tidak menyenangkan',
            'SHEESH' : 'sedikit ketidaksetujuan',
            'AGGRO' : 'untuk menjadi agresif/marah'
            }
print('halo!')
time.sleep(1)
nama = input('namamu siapa?')
time.sleep(1)
print('Halo', nama)
time.sleep(1)
for i in range(5):
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua! dan ketik 5 kali!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print('error')
