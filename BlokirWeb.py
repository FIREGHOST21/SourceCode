#import libraries
from datetime import datetime as dt
#Windows host file path
hostsPath=r"C:\windows\system32\drivers\etc\hosts"
redirect="127.0.0.1"
#Add the websites you want to block in this list
websites=["www.icons8.com","icons8.com"]
while True:
       #Duration During which, website blocker will work
       if dt(dt.now().year,dt.now().month,dt.now().day,9)<dt.now()<
       dt(dt.now().year,dt.now().month,dt.now().day,18):
             print ("Sorry Not Allowed"):
             with open(hostsPath,'r+') as file:
                 for site in websites:
                     if sites in content:
                        pass  
                        else:
                            file.write(redirect + " "+site+\n")
else:
    with open(hostsPath,'r+') as file:
        content=file.readlines()
        file.seek(0)
        for line in content:
            if not any(site in line for site in websites):
                file.write(line)
            file.truncate()
        print ("Allowed Access!")
        time.sleep(5)