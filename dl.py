#download script written by xTakoyakii
#Does it make any sense to you? Probably not, it's very specific logic for a very specific project that i've whipped up to make my life easier.
import urllib.request

print("Downloading...")
nr = 0 #always starts with 0

#Two while loops are needed since the file names usually consist out of decimal numbers that cannot be simply incremented, thus the URL has to be broken in parts
while nr is not 9: #9 is the last digit before the number becomes a double digit number
    nr +=1
    url="https://subdomain.domain.tld/directory/00000/00000/00"+str(nr)+".jpg"
    urllib.request.urlretrieve(url, "/path_to_download_files_to"+str(nr)+".jpg")
    print("Downloaded: "+ str(nr))
    
#Counts up from 10. 99 is the maximal number, a higher number would require another break in the URL
while nr is not 99:
    nr +=1
    url="https://subdomain.domain.tld/directory/00000/00000/0"+str(nr)+".jpg"
    urllib.request.urlretrieve(url, "/path_to_download_files_to"+str(nr)+".jpg")
    print("Downloaded: "+ str(nr))
print("...Done!")
print("nr value= "+ str(nr)) #Just a test that nr has the desired value at the end