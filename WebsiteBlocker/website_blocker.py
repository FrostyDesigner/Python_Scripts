import time
from datetime import datetime as dt
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
hosts_temp=r"C:\GitHub\Python_Scripts\WebsiteBlocker\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com"]

#military time
#next line checking for the date and 0800 (8:00 am)
date1 = dt(dt.now().year, dt.now().month, dt.now().day, 8)
date2 = dt.now()
#next line checking for the date and if after 1600 (4:00 pm)
date3 = dt(dt.now().year, dt.now().month, dt.now().day, 16)


while True:
    #orig
    #if dt(dt.now().year, dt.now().month, dt.now().day, 16) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
    #test
    if date1 < date2 < date3:
        print("Working Hours...")
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(hosts_temp, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
        print("Fun Hours...")
    time.sleep(5)

