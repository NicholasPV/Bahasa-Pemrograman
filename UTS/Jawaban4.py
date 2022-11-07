print("====================\nNESTED LOOPING\n====================")
pulau = ["Kalimantan", "Sumatra", "Sulawesi"]
bagian = [" West", " North", " South"]
for a in range(3):
    for b in range(3):
        print(pulau[a] + bagian[b])
