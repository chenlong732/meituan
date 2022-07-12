from base.basepage import BasePage	# 导入基类，直接调用公共方法
import allure

class SearchPage(BasePage):
    # 元素定位信息
    inputfield = "com.sankuai.meituan:id/search_edit_flipper_container"
    clicksearch = "com.sankuai.meituan:id/search"
    inputvalue = "com.sankuai.meituan:id/search_edit"
    back = "com.sankuai.meituan:id/back"

    def search(self,value):					# 搜索操作流程
        self.click(self.inputfield)			# 点击搜索框
        self.clear(self.inputvalue)			# 每次搜索前线清空搜索框
        self.input(self.inputvalue,value)	# 定位输入框并输入关键字
        self.click(self.clicksearch)		# 点击【搜索】按钮
        self.click(self.back)				# 返回到上一级
        self.click(self.back)				# 返回到首页
