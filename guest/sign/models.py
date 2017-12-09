from django.db import models


# Create your models here.
# 发布会表

class Event(models.Model):
    name = models.CharField(max_length=100)  # 发布会标题
    limit = models.IntegerField()  # 参加人数
    status = models.BooleanField()  # 状态
    address = models.CharField(max_length=200)  # 地址
    start_time = models.DateField('events time')  # 发布会时间
    create_time = models.DateField(auto_now=True)  # 创建时间，自动获取

    def __str__(self):
        return self.name


"""
ForeignKey 的第二个位置参数on_delete
on_delete指的是通过ForeignKey连接起来的对象被删除后，当前字段怎么变化。
常见的选项有：
　　models.CASCADE,对就对象删除后，包含ForeignKey的字段也会被删除
　　models.PROTECT,删除时会引起ProtectedError
　　models.SET_NULL,注意只有当当前字段设置null设置为True才有效，此情况会将ForeignKey字段设置为null
　　models.SET_DEFAULT ,同样，当前字段设置了default才有效，此情况会将ForeignKey 字段设置为default 值
　　moels.SET,此时需要指定set的值
　　models.DO_NOTHING ,什么也不做
"""


# 嘉宾表
class Guest(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # 关联发布会id
    realname = models.CharField(max_length=64)  # 真实姓名
    phone = models.CharField(max_length=16)  # 电话
    email = models.EmailField()  # 邮箱
    sign = models.BooleanField()  # 签到状态
    create_time = models.DateTimeField(auto_now=True)  # 创建时间，自动获取

    class Meta:
        unique_together = ("event", "phone")

    def __str__(self):
        return self.realname
