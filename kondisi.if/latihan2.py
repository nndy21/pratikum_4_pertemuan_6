print("=== Program mengurutan data ===")
jumlah_data = int(input("Masukkan jumlah data (minimal 3): "))
if jumlah_data < 3:
    print("Jumlah data harus minimal 3!")
else:
    data = []
    for i in range(jumlah_data):
        nilai = int(input(f"Masukkan data ke-{i+1}: "))
        data.append(nilai)
    data.sort()
    print("\nurutan bilangan:")
    for d in data:
        print(d)
