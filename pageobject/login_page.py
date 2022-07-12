from base.basepage import BasePage	# 导入基类中封装的方法
import allure	# 导入allure

class LoginPage(BasePage):
    # 元素定位，元素位置信息
    agreement = "com.sankuai.meituan:id/permission_agree_btn"
    #agreement ="com.miui.home:id/icon_icon", description = "美团"
    get_loc_info = "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
    get_pho_perm = "com.android.permissioncontroller:id/permission_deny_button"
    notice = "暂不"
    login_in_now = "com.sankuai.meituan:id/button"
    pwd_login = "com.sankuai.meituan:id/user_password_login"
    username = "com.sankuai.meituan:id/passport_mobile_phone"
    password = "com.sankuai.meituan:id/edit_password"
    tick = "com.sankuai.meituan:id/passport_account_checkbox"
    click_login = "com.sankuai.meituan:id/login_button"
    mine = "我的"
    growth = "com.sankuai.meituan:id/grouth_tv"

    # 行为，页面操作
    def login(self,user,pwd):			# 登录流程，以首次运行APP为例
        self.click(self.agreement)		# 同意使用APP协议
        self.click(self.get_loc_info)	# 获取位置信息，选择【使用时允许】
        self.click(self.get_pho_perm)	# 获取电话权限，选择【拒绝】
        self.click_text(self.notice)	# 是否开启消息通知，选择【暂不】
        self.click(self.login_in_now)	# 点击首页的【马上登录】
        self.click(self.pwd_login)		# 登录方式选择【密码登录】
        self.input(self.username,user)	# 输入用户名
        self.input(self.password,pwd)	# 输入密码
        self.click(self.tick)			# 勾选同意用户协议
        self.click(self.click_login)	# 点击【登录】
        self.click(self.mine)			# 点击【我的】
        self.assert_exited(self.growth) # 断言，因登录成功才显示成长值，故以此元素是否出现判断是否登录成功
        self.click(self.homepage)		# 切到首页
