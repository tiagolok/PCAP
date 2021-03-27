try:
    stream = open("C:/Users/Peter Lok/Desktop/Python/PCAP/file.txt", "rt")
    # processing goes here
    stream.close()
except Exception as exc:
    print("Cannot open the file:", exc)
