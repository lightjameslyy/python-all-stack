# ############### 定义 ###############
class Foo:
    def func(self):
        pass

    # 定义property属性
    @property
    def prop(self):
        pass


# ############### 调用 ###############
foo_obj = Foo()
foo_obj.func()  # 调用实例方法
foo_obj.prop  # 调用property属性


# ############### 定义 ###############
class Goods:

    @property
    def size(self):
        return 100


# ############### 调用 ###############
goods_obj = Goods()
ret = goods_obj.size
print(ret)