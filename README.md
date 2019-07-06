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


## dev recond
```
# -*- coding: utf-8 -*-

```
model 中的class 也是从上往下执行的  下面的class 使用其他class 放下面会检测不到

pip 安装目录在 `/anaconda3/envs/py36/lib/python3.6/site-packages`

## 后台管理
xadmin
[github 上 django2分支](https://github.com/sshwsfc/xadmin/tree/django2)
需要把项目下的[xadmin](https://github.com/sshwsfc/xadmin/tree/django2/xadmin 
)放项目中



项目开发参考：https://blog.starmeow.cn/feature/1/?page=2
