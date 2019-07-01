### 启动项目
```

conda activate py36
python manage.py runserver

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