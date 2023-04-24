from time import sleep

from PIL import Image
from selenium import webdriver

# 创建设置对象
from selenium.webdriver.common.by import By

from 识别验证码.class0424.fateadm_api import FateadmApi # 注意FateadmApi放的位置

option = webdriver.ChromeOptions()
# 设置浏览器不自动关闭
option.add_experimental_option('detach', True)
# 创建驱动对象
driver = webdriver.Chrome(options=option)
# 打开页面
driver.get('http://192.168.31.162:8080')
# 窗口最大化
driver.maximize_window()
sleep(2)
# 获取验证码元素
element_captcha_img = driver.find_element(By.ID, 'captcha_img')
codeInput = driver.find_element(By.CSS_SELECTOR, '[name="verifyCodeActual"]')
btn = driver.find_element(By.CSS_SELECTOR, '[value="提交"]')
# 获得图片尺寸
print(element_captcha_img.location)
print(element_captcha_img.size)
# 缩放问题 所以*1.5
left = element_captcha_img.location['x'] * 1.5
top = element_captcha_img.location['y'] * 1.5
right = left + element_captcha_img.size['width'] * 1.5
bottom = top + element_captcha_img.size['height'] * 1.5
print(left, top, right, bottom)
sleep(2)
# 截图
driver.save_screenshot('window_image.png')
# 从大图中截取小图
windowImage = Image.open('window_image.png')
# 截取
codeImg = windowImage.crop((left, top, right, bottom))
# 保存
codeImg.save('codeImg.png')
sleep(2)
pd_id = "137810"
pd_key = "bNoLyv6RRhs50JiRv8TG2vZ826zioq5i"
app_id = "337810"
app_key = "V/EpIFT6lV+zv65h5BHIoMxllb/28DDP"
# 具体类型可以查看官方网站的价格页选择具体的类型，不清楚类型的，可以咨询客服
pred_type = "30400"
# 初始化api接口
api = FateadmApi(app_id, app_key, pd_id, pd_key)
# 查询余额接口
# balance = api.QueryBalcExtend()  # 直接返余额
# api.QueryBalc()

# 通过文件识别验证码
# 通过文件进行验证码识别,请使用自己的图片文件替换
# 如果是通过url直接获取内存图片，这直接调用 Predict接口就好
file_name = 'codeImg.png'
res = api.PredictFromFileExtend(pred_type, file_name)  # 直接返回识别结果
print(res)
# 将识别出来的验证码输入文本框中
codeInput.send_keys(res)
# 点击提交按钮
btn.click()
sleep(2)
driver.quit()
