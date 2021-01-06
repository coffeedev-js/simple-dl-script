port urllib.request

DL_PATH = "/path/to/download/files/to/"

print("downloading")

for i in range(100):
  url = f"https://subdomain.domain.tld/directory/00000/00000/{"00" if i < 10 else "0"}{i}.jpg"
  urllib.request.urlretrieve(url, DL_PATH + str(i) + ".jpg")
  print(f"Downloaded {i}")

print("...Done")
