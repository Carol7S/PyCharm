with open("ip.txt") as txt:
    for i in txt:
        i = i.strip()
        if "80" in i:
            print("http://" + i)
        #else:
        #    print("https://"+i)