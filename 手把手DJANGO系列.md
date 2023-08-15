## python django 指南

part2 - 181  
part3 - 223  
part4 - 272  


---  

要做的事：
-建立/安裝 一個 virtual environment
-建立一個空白的django 項目
-建立git .
---

### 建立一個virtual environment  

```
mkvirtualenv brte //這個是env的名稱
```

### 建立一個空白的django 項目

1. 用pip 安裝 django 3.2.14版本
```
pip install django==3.2.14
```
2. 用pip freeze 來查看 是否安裝了django 
```
pip freeze 
```
3. 建立django project  
```
django-admin startproject btre
```
### 建立.git

1. 用git init 來建立.git
```
git init
```
2. 建立.gitgnore 
```
# Django #
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
media

# Backup files # 
*.bak 

# If you are using PyCharm # 
# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf

# AWS User-specific
.idea/**/aws.xml

# Generated files
.idea/**/contentModel.xml

# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml

# Gradle
.idea/**/gradle.xml
.idea/**/libraries

# File-based project format
*.iws

# IntelliJ
out/

# JIRA plugin
atlassian-ide-plugin.xml

# Python # 
*.py[cod] 
*$py.class 

# Distribution / packaging 
.Python build/ 
develop-eggs/ 
dist/ 
downloads/ 
eggs/ 
.eggs/ 
lib/ 
lib64/ 
parts/ 
sdist/ 
var/ 
wheels/ 
*.egg-info/ 
.installed.cfg 
*.egg 
*.manifest 
*.spec 

# Installer logs 
pip-log.txt 
pip-delete-this-directory.txt 

# Unit test / coverage reports 
htmlcov/ 
.tox/ 
.coverage 
.coverage.* 
.cache 
.pytest_cache/ 
nosetests.xml 
coverage.xml 
*.cover 
.hypothesis/ 

# Jupyter Notebook 
.ipynb_checkpoints 

# pyenv 
.python-version 

# celery 
celerybeat-schedule.* 

# SageMath parsed files 
*.sage.py 

# Environments 
.env 
.venv 
env/ 
venv/ 
ENV/ 
env.bak/ 
venv.bak/ 

# mkdocs documentation 
/site 

# mypy 
.mypy_cache/ 

# Sublime Text # 
*.tmlanguage.cache 
*.tmPreferences.cache 
*.stTheme.cache 
*.sublime-workspace 
*.sublime-project 

# sftp configuration file 
sftp-config.json 

# Package control specific files Package 
Control.last-run 
Control.ca-list 
Control.ca-bundle 
Control.system-ca-bundle 
GitHub.sublime-settings 

# Visual Studio Code # 
.vscode/* 
!.vscode/settings.json 
!.vscode/tasks.json 
!.vscode/launch.json 
!.vscode/extensions.json 
.history
```

---

###  part2 - 181

耍做的事：
- 建立一個名叫pages app  
- 連結pages app

---

#### 建立一個名叫pages app  

1. 在終端機
 ```
 python manage.py startapp pages
 ```

#### 連結pages app

1. btre/settings.py  
在INSTALLED_APPS裹加入pages  
```
...

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages' // 加入pages app
]


...
```

---

## part3 - 223  

要做的事:  
- 在pages urls.py增加url  
- 在pages views.py增加function  
- 在btre urls.py增加url

---

#### 在pages views.py增加function  
1. 在pages views.py 裹  
```
from django.shortcuts import render
from django.http import HttpResponse //增加了這個

def index(request): //增加了function
    return HttpResponse("<h1>hi</h1>")

```

#### 在pages urls.py增加url  

1. 在pages 裹新增 urls.py
```
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index")
]

```

#### 在btre urls.py增加url

1. 在btre/urls.py
```
from django.contrib import admin
from django.urls import path , include //增加include

urlpatterns = [
    path('', include('pages.urls')), // 增加了這個
    path('admin/', admin.site.urls),
    
]

```  
---
## part4 - 273  
要做的事:
- 建立template為了顥示pages app的內容  

---
#### 建立template為了顥示pages app的內容  

1. 在btre/settings.py  
```
...

import os // 增加這個
from pathlib import Path

...

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')], // 增加os.path.join(BASE_DIR,'templates')
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

...

```  

2.  在主目錄裹加建templates文件夾,在templates裹加建pages文件夾和base.html，
在pages裹創建about.html 和 index.html

```
.
├── btre
├── manage.py
├── pages
└── templates
    ├── base.html
    └── pages
        ├── about.html
        └── index.html

```  
3. pages/urls.py 
```
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('about',views.about, name="about") //增加了這個
]
```
4. pages/views.py  
```
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"pages/index.html") //改了return render(request,"pages/index.html")

def about(request): //增加了
    return render(request,"pages/about.html") //增加了
```
5. templates/base.html  
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BT Real Estate</title>
</head>
<body>
    {% block content %}

    {% endblock %}
</body>
</html>
```  
6. templates/pages/about.html  
```
{% extends 'base.html' %}{% block content %}
<h1>about</h1>
{% endblock %}
```  
7. templates/pages/index.html  
```
{% extends 'base.html' %} {% block content %}
<h1>home</h1>
{% endblock %}
```  
----