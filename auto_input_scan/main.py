import os
import threading
import queue

def zid(wenjian):
    words = queue.Queue()
    with open(wenjian) as txt:
        for i in txt:
            i = i.strip()
            words.put(i)

    return words


def zhix(zidian):
    while True:
        if zidian.empty():
            return
        else:
            i = zidian.get()
            i = i.strip()
            ml = "/Users/zhangzhechao/ctf/x_ray/rad_darwin_amd64 -t "+i+" --http-proxy 127.0.0.1:8080"
            os.system(ml)

def main():
    zd = zid("ip.txt")
    threads = []
    for i in range(10):
        t = threading.Thread(target=zhix, args=(zd,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("扫描结束......")

if __name__ == "__main__":
    main()