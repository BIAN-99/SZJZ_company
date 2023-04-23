import json

from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

# 获取浏览器设置对象
option = webdriver.EdgeOptions()

# 设置浏览器不自动退出
option.add_experimental_option('detach', True)

# 获取浏览器,并把以上设置传入

driver = webdriver.Edge(options=option)

# 获取浏览地址并打开
url = 'https://www.bilibili.com'
driver.get(url)
sleep(1)

# 浏览器界面最大化
driver.maximize_window()
sleep(3)
# 首先清除由于浏览器打开已有的cookies
driver.delete_all_cookies()
with open('cookies.txt', 'r') as f:
    # 使用json读取cookies 注意读取的是文件 所以用load而不是loads
    cookies_list = json.load(f)
    for cookie in cookies_list:
        driver.add_cookie(cookie)
# 刷新浏览器界面,刷新后即显示登录后的界面
driver.refresh()
sleep(3)
# 获取输入框元素并点击开始输入
get_input = driver.find_element(By.CLASS_NAME, 'nav-search-input')
get_input.click()
# 通过键盘操作在输入框内输入搜索内容
get_input.send_keys('棋手战英')
sleep(3)
# 退格删除操作
get_input.send_keys(Keys.BACKSPACE)
sleep(2)
# 再次输入
get_input.send_keys('鹰')
sleep(2)
# 获取搜索按钮元素并点击搜索,也可不用获取此元素,直接使用键盘回车操作get_input.send_keys(Keys.ENTER)
get_search = driver.find_element(By.XPATH, '//*[@class="nav-search-btn"]')
get_search.click()
sleep(3)
# 获取所有窗口
handle = driver.window_handles
# 跳转到最后一个窗口
driver.switch_to.window(handle[-1])
# 获取视频标题元素并点击进入
get_title = driver.find_element(By.CSS_SELECTOR, "[title='弈周棋讯|灵动的洁宝回来了']")
get_title.click()
sleep(8)
# 获取所有窗口
handle = driver.window_handles
# 跳转到最后一个窗口
driver.switch_to.window(handle[-1])
# 滚动条操作,通过控制执行JS语句实现
driver.execute_script('window.scrollBy(0,550)')
sleep(5)
# 创建动作链对象,可以进行鼠标操作
chains = ActionChains(driver)
# 获取正在播放的视频元素
get_video = driver.find_element(By.XPATH, "//*[@class='player-wrap']")
# 用鼠标操作将鼠标移动到上面获取的元素上
chains.move_to_element(get_video)
# 鼠标操作执行点击动作,即使正在播放的视频暂停
chains.click()
# 动作执行语句,没这句话以上动作无法执行
chains.perform()
# 获取评论区文本框
get_pinglun = driver.find_element(By.TAG_NAME, "textarea")
# 鼠标移动到评论区文本框并点击
chains.move_to_element(get_pinglun)
chains.click()
chains.perform()
# 输入评论内容
get_pinglun.send_keys('鹰鹰鹰~')
# 获取发布按钮
get_push = driver.find_element(By.CLASS_NAME, 'send-text')
# 点击发布按钮,发布评论内容
get_push.click()
