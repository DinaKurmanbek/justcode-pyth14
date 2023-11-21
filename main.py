import requests

url = "https://httpbin.org/image/jpeg"

a = requests.get(url)
# print(type(a))
# print(a)
# print(a.status_code)
binary_img = a.content

print ("Print for test changes")

with open("test_img.jpg" , "wb") as file:
    file.write(binary_img)

