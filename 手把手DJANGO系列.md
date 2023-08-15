## python django 指南

part2 - 181  
part3 - 223  
part4 - 272  
part5 - 377  



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
## part5 - 377  
要做的事:
- 加入static
---
#### 加入static  
1. 在project btre 裹開static文件夾,而static裹加入css , img js webfonts 等文件夾 （來源在dist 內assets）

```
.
├── btre
│   ├── __pycache__
│   ├── settings.py
│   ├── static
│   │   ├── css
│   │   ├── img
│   │   ├── js
│   │   └── webfonts
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── pages
└── templates
    ├── base.html
    └── pages
        ├── about.html
        └── index.html

```
2. 在btre/settings.py
```

...
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR,'static') //增加這個
STATIC_URL = '/static/'
STATICFILES_DIRS = [   //增加
    os.path.join(BASE_DIR,'btre/static') //增加
]  //增加

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

```

3. 在終端機  
```
python manage.py collectstatic
```

在全局位置多了1個名叫static的文件夾,而內有admin ,css ,img , js ,webfonts 才是成功  
```
.
├── btre
├── db.sqlite3
├── manage.py
├── pages
├── static
│   ├── admin
│   │   ├── css
│   │   ├── fonts
│   │   ├── img
│   │   └── js
│   ├── css
│   ├── img
│   ├── js
│   └── webfonts
└── templates
    ├── base.html
    └── pages
        ├── about.html
        └── index.html

```
4. templates/base.html  
```
{% load static %}  //加了 {% load static %} 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BT Real Estate</title>
    <meta name="description" content="" /> //加了
<meta name="viewport" content="width=device-width, initial-scale=1" /> //加了
<!-- Font Awesome -->
<link rel="stylesheet" href="{% static 'css/all.css' %}" /> //加了
<!-- Bootstrap -->
<link rel="stylesheet" href="{% static 'css/bootstrap.css' %}" /> //加了
<!-- Custom -->
<link rel="stylesheet" href="{% static 'css/style.css' %}" />//加了
<!-- Lightbox -->
<link rel="stylesheet" href="{% static 'css/lightbox.min.css' %}" />//加了
</head>
<body>

      <!-- Top Bar -->   //加了 整個TOP BAR
  <section id="top-bar" class="p-3">
    <div class="container">
      <div class="row">
        <div class="col-md-4">
          <i class="fas fa-phone"></i> +852 2982 0546
        </div>
        <div class="col-md-4">
          <i class="fas fa-envelope-open"></i> contact@btrealestate.co
        </div>
        <div class="col-md-4">
          <div class="social text-right">
            <a href="#">
              <i class="fab fa-twitter"></i>
            </a>
            <a href="#">
              <i class="fab fa-facebook"></i>
            </a>
            <a href="#">
              <i class="fab fa-linkedin"></i>
            </a>
            <a href="#">
              <i class="fab fa-instagram"></i>
            </a>
            <a href="#">
              <i class="fab fa-pinterest"></i>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

   <!-- Navbar -->  //加了整個Navbar
   <nav class="navbar navbar-expand-lg navbar-dark bg-primary sticky-top">
    <div class="container">
      <a class="navbar-brand" href="index.html">
        <img src="assets/img/logo.png" class="logo" alt="">
      </a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <ul class="navbar-nav">
          <li class="nav-item active mr-3">
            <a class="nav-link" href="index.html">Home</a>
          </li>
          <li class="nav-item mr-3">
            <a class="nav-link" href="about.html">About</a>
          </li>
          <li class="nav-item mr-3">
            <a class="nav-link" href="listings.html">Featured Listings</a>
          </li>
        </ul>

        <ul class="navbar-nav ml-auto">
          <li class="nav-item mr-3">
            <a class="nav-link" href="register.html">
              <i class="fas fa-user-plus"></i> Register</a>
          </li>
          <li class="nav-item mr-3">
            <a class="nav-link" href="login.html">
              <i class="fas fa-sign-in-alt"></i>

              Login</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

    {% block content %}

    {% endblock %}

      <!-- Footer -->  //加了加了整個Footer
  <footer id="main-footer" class="py-4 bg-primary text-white text-center">
    Copyright &copy;
    <span class="year"></span> BT Real Estate
  </footer>

  <script src="{% static 'js/jquery-3.3.1.min.js' %} "></script>  //加了
  <script src="{% static 'js/bootstrap.bundle.min.js' %} "></script> //加了
  <script src="{% static 'js/lightbox.min.js' %} "></script> //加了
  <script src="{% static 'js/main.js' %} "></script> //加了
</body>
</html>
```