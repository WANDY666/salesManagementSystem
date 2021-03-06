# 销售管理系统设计文档

经过讨论，并受到新开业的超市所启发，我们小组认为超市是一个贴近生活，而且也很适合设计数据库管理系统的一个情景。于是我们决定作出一个销售管理系统。本人负责后端，使用Django实现。

### 实现效果

![image-20210926231225901](https://s3.bmp.ovh/imgs/2021/09/acdf5f214fccbae7.png)

更多图请查看**数据库.pptx**

### 数据元素表	

![image-20210926230459070](https://s3.bmp.ovh/imgs/2021/09/652f7f172e8ee5d5.png)

### E-R图

![image-20210926230027372](https://s3.bmp.ovh/imgs/2021/09/6525beef657d575a.png)

### 范式等级

3NF：即每一个非主属性既不传递依赖于码，也不部分依赖于码。

十二个元素里逐一分析，由于每种主码都只有一个属性，不存在部分依赖。

**超市**

+ 非主属性仅有一个成立时间，不存在传递

**员工**

+ 非主属性有姓名、性别、联系方式、年龄、密码

+ 因为即使姓名、联系方式、年龄、性别和密码都一样，也不能百分之百保证是同一个人，所

以3NF

**工资记录**

+ 非主属性有金额、日期、备注。

+ 因为金额和日期和备注都一样也不能确定是同一条工资记录，所以3NF

**仓库表**

+ 非主属性仅有仓库类别，不存在传递

**仓库**

+ 非主属性仅有每种商品数量，不存在传递

**商品**

+ 非主属性有商品名称、销售价格、生产厂家

+ 商品名称和生产厂家确定的话，随着时间原因，销售价格也不能确定。

+ 任意两个确定，推不出第三个

**销售表**

+ 非主属性有销售数量，单价

+ 显然满足要求

**销售记录**

+ 非主属性仅有销售表的总价这一个，不存在传递

**采购表**

+ 非主属性有采购数量和单价

+ 显然满足要求

**采购记录**

+ 非主属性有采购表的总价和所在仓库

+ 显然满足要求

**会员信息**

+ 姓名，性别，联系方式，年龄，密码，剩余金额，vip等级

+ 分析同员工，也满足要求

**会员购买记录表**

+ 非主属性仅有销售表的总价，不存在传递

**综上所述，所有的关系均可到3NF级**。



