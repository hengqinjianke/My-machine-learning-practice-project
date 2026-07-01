import re


class Customer:
    """客户类"""

    def __init__(self, c_id, name, age="None", phone="None", email="None"):
        """初始化客户信息"""
        self.id = c_id
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email

    @staticmethod
    def check_id(c_id):
        """检查 id 是否为纯数字"""
        return c_id.isdigit()

    @staticmethod
    def check_name(name):
        """检查姓名是否为字符"""
        return name.isalpha()

    @staticmethod
    def check_age(age):
        """检查年龄是否为数字"""
        return age.isdigit()

    @staticmethod
    def check_phone(phone):
        """检查手机号格式"""
        return True if re.match(r"^1[345789]\d{9}$", phone) else False

    @staticmethod
    def check_email(email):
        """检查邮箱格式"""
        pattern = r"[\w!#$%&'*+\-/=?^`{|}~.]+@[\w!#$%&'*+\-/=?^`{|}~.]+\.[a-zA-Z]{2,}$"
        return True if re.match(pattern, email) else False

    def __str__(self):
        """打印客户信息"""
        return (
            f"Id: {self.id:<5}, "
            f"Name: {self.name:<10}, "
            f"Age: {self.age:<5}, "
            f"Phone: {self.phone:<15}, "
            f"Email: {self.email:<25}"
        )
c1 = Customer("1", "张三", "18", "13999999999", "123@qq.com")
print(c1)
print(Customer.check_id("123"))