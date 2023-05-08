import requests

session = requests.session()
params_login = {
    "username": "anton",
    "password": "123"
}
response = session.post("http://192.168.31.162:8888/doLogin", params=params_login)
print("登录", response)
formData = {
    "age": "18",
    "degree": "中专",
    "employeeGWId": 4,
    "major": "456",
    "name": "幻灯片",
    "originId": 4,
    "school": "asd",
    "sex": "男",
    "telephone": "10356789456"
}

response = session.post("http://192.168.31.162:8888/cus/advanced/addCustomer", json=formData)
print("添加", response.json())

# with open("登录-post传参.html", "wb") as f:
#     f.write(response.text.encode('utf-8'))
