# config

创建mysql数据库 testdb,打开settings.py 配置

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': '数据库名字',
            'HOST': 'localhost',
            'PORT': 3306,
            'USER': 'MySQL账号',
            'PASSWORD': 'MySQL密码',
        }
    }

在本地数据库中创建 all_data 表

    字段: 
    id(主键自增), 
    encode(longtext), 
    insert_date(datetime)

Terminal ——> 数据表反向生成

    py manage.py inspectdb # 查看数据表模型
    py manage.py inspectdb > models.py # 生成新的models.py 文件, 替换掉APP项目里的models.py




