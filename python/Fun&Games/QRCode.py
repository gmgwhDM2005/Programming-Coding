import webbrowser as wb, time as t

url=input('URL: ')
if not 'http' in url:
    url='https://' + url
print(f'Generating QR for {url}')
t.sleep(1)
wb.open(f'https://api.qrserver.com/v1/create-qr-code/?size=200x200&data={url}')
