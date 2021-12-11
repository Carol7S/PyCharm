import queue
import requests
import threading

def zid(wenjian):
    words = queue.Queue()
    with open(wenjian) as txt:
        for i in txt:
            i = i.strip()
            words.put(i)

    return words

def confirm(zidian):
    while True:
        if zidian.empty():
            return
        else:
            i = zidian.get()
            i = i.strip()
            url = i+"/admin/index.php"
            requests.packages.urllib3.disable_warnings()
            response = requests.get(url, verify=False)
            if(response.status_code == 200):
                print(url)

def main():
    zd = zid("ip.txt")
    threads = []
    for i in range(10):
        t = threading.Thread(target=confirm, args=(zd,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print("扫描结束......")



if __name__ == "__main__":
    main()