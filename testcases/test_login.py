import uiautomator2 as u2
import pytest
from pageobject.login_page import LoginPage	# 导入上一步操作流程中的类


@allure.story('测试美团APP')
@allure.title("APP登录")
# 连接手机并启动APP进行登录
class TestLogin:	# 类以Test开头
    def test_login(self):   # 方法以test_或_test开头
        driver = u2.connect("48fd6742")
        driver.app_start("com.sankuai.meituan", stop=True)
        login_page = LoginPage(driver=driver)
        login_page.login("15012844489","a1354267")
