### 项目简介
> 这是一个django在线教育平台项目  django入坑中 

[项目开发参考：](https://blog.starmeow.cn/feature/1/?page=2)

[github:](https://github.com/xyliurui/OnlineLearningPlatform)
### 启动项目
```

conda activate py36
python manage.py runserver  或者 python manage.py runserver 0.0.0.0:8000

```

迁移数据库

```
python manage.py makemigrations

python manage.py migrate

```



## 后台管理
xadmin
[github 上 django2分支](https://github.com/sshwsfc/xadmin/tree/django2)
需要把项目下的[xadmin](https://github.com/sshwsfc/xadmin/tree/django2/xadmin 
)放项目中



## 开发规范

1. 一般class 之间空两行
2. 不加分号 ；
3. py文件开头加上
```py
# -*- coding: utf-8 -*-
```


## dev recond

model 中的class 也是从上往下执行的  下面的class 使用其他class 放下面会检测不到

pip 安装目录在 `/anaconda3/envs/py36/lib/python3.6/site-packages`