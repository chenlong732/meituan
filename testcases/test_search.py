import uiautomator2 as u2
import pytest
from pageobject.search_page import SearchPage	# 导入上一步操作流程中的类


class TestSearch:
    keyword = ["奶茶","桌球","景点"]
    @pytest.mark.parametrize("value",keyword)	# 使用pytest参数化，搜索三个关键字
    @allure.title("搜索")
    def test_search(self,value):
        driver = u2.connect("48fd6742")
        driver.app_start("com.sankuai.meituan")
        search_page = SearchPage(driver=driver)
        search_page.search(value)
