from datetime import datetime
end_time = datetime(datetime.now().year,datetime.now().month,datetime.now().day,0,10)
sites_to_block = ['www.facebook.com','www.instagram.com','www.Facebook.com']
path = r'C:\Windows\System32\drivers\etc\hosts'

redirect="127.0.0.1"
print("Hioo")

while True:
   
    if datetime.now()<end_time:
        print("blocking sites!")
        
        with open(path,'r+') as file:
            content = file.read()
            for site in sites_to_block:
                if site not in content:
                    file.write(redirect+" "+site+"\n")
        print("\nSites blocked")
    else:
        with open(path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in sites_to_block):
                    file.write(line)
            
            file.truncate()
        break
