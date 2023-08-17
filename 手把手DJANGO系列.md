## python django 指南

part2 - 181  
part3 - 223  
part4 - 272  
part5 - 377  
part6 - 568    
part7 - 729  
part8 - 1355  
part9 - 1483  
part10 - 1881  
part11 - 1923  
part12 - 2126  




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
---

## part6 - 568  
要做的事：
- 加入partials  

---

1. 在templates裹開一個partials交件夾，裹面有_footer.html , _navbar.html , _topbar  

```
.
├── btre
├── db.sqlite3
├── manage.py
├── pages
├── static
└── templates
    ├── base.html
    ├── pages
    │   ├── about.html
    │   └── index.html
    └── partials
        ├── _footer.html
        ├── _navbar.html
        └── _topbar.html


```

2. templates/base.html  
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BT Real Estate</title>
    <meta name="description" content="" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<!-- Font Awesome -->
<link rel="stylesheet" href="{% static 'css/all.css' %}" />
<!-- Bootstrap -->
<link rel="stylesheet" href="{% static 'css/bootstrap.css' %}" />
<!-- Custom -->
<link rel="stylesheet" href="{% static 'css/style.css' %}" />
<!-- Lightbox -->
<link rel="stylesheet" href="{% static 'css/lightbox.min.css' %}" />
</head>
<body>

      <!-- Top Bar -->
  {% include 'partials/_topbar.html' %} //整個變了{% include 'partials/_topbar.html' %}
  

   <!-- Navbar -->
  {% include 'partials/_navbar.html' %} //整個變了 {% include 'partials/_navbar.html' %}

    {% block content %}

    {% endblock %}

      <!-- Footer -->
      {% include 'partials/_footer.html' %} //整個變了{% include 'partials/_footer.html' %}

  <script src="{% static 'js/jquery-3.3.1.min.js' %} "></script>
  <script src="{% static 'js/bootstrap.bundle.min.js' %} "></script>
  <script src="{% static 'js/lightbox.min.js' %} "></script>
  <script src="{% static 'js/main.js' %} "></script>
</body>
</html>
```

3. templates/partials/_footer.html  
```
<footer id="main-footer" class="py-4 bg-primary text-white text-center">
    Copyright &copy;
    <span class="year"></span> BT Real Estate
  </footer>
```  
4. templates/partials/_navbar.html  
```
{% load static %}
<!-- Navbar -->
<nav class="navbar navbar-expand-lg navbar-dark bg-primary sticky-top">
<div class="container">
<a class="navbar-brand" href="index.html">
<!-- logo also need to update the assets folder -->
<img src="{% static 'img/logo.png' %}" class="logo" alt="" />
</a>
<button
class="navbar-toggler"
type="button"
data-toggle="collapse"
data-target="#navbarNavAltMarkup"
>
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
<i class="fas fa-user-plus"></i> Register</a
>
</li>
<li class="nav-item mr-3">
<a class="nav-link" href="login.html">
<i class="fas fa-sign-in-alt"></i>
Login</a
>
</li>
</ul>
</div>
</div>
</nav>
```  
5. templates/partials/_topbar.html
```
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
```  
## part7 - 729  

要做的事:
- 改變about內容  
- 改變index內容  
- 在about頁面加入static
- url轉跳  

---
#### 改變about內容

1. templates/pages/about.html  
```
{% extends 'base.html' %} {% block content %}
  <section id="showcase-inner" class="py-5 text-white">
    <div class="container">
      <div class="row text-center">
        <div class="col-md-12">
          <h1 class="display-4">About BT Real Estate</h1>
          <p class="lead">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Sunt, pariatur!</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Breadcrumb -->
  <section id="bc" class="mt-3">
    <div class="container">
      <nav aria-label="breadcrumb">
        <ol class="breadcrumb">
          <li class="breadcrumb-item">
            <a href="index.html">
              <i class="fas fa-home"></i> Home</a>
          </li>
          <li class="breadcrumb-item active"> About</li>
        </ol>
      </nav>
    </div>
  </section>

  <section id="about" class="py-4">
    <div class="container">
      <div class="row">
        <div class="col-md-8">
          <h2>We Search For The Perfect Home</h2>
          <p class="lead">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Sunt, pariatur!</p>
          <img src="assets/img/about.jpg" alt="">
          <p class="mt-4">Lorem ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis esse officia repudiandae ad saepe ex, amet
            neque quod accusamus rem quia magnam magni dolorum facilis ullam minima perferendis? Exercitationem at quaerat
            commodi id libero eveniet harum perferendis laborum molestias quia.</p>
        </div>
        <div class="col-md-4">
          <div class="card">
            <img class="card-img-top" src="assets/img/realtors/kyle_.jpg" alt="Seller of the month">
            <div class="card-body">
              <h5 class="card-title">Seller Of The Month</h5>
              <h6 class="text-secondary">Kyle Brown</h6>
              <p class="card-text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Omnis nesciunt amet, illo itaque similique repellat.
                content.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Work -->
  <section id="work" class="bg-dark text-white text-center">
    <h2 class="display-4">We Work For You</h2>
    <h4>Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem velit aperiam, unde aliquid at similique!</h4>
    <hr>
    <a href="listings.html" class="btn btn-secondary text-white btn-lg">View Our Featured Listings</a>
  </section>

  <!-- Team -->
  <section id="team" class="py-5">
    <div class="container">
      <h2 class="text-center">Our Team</h2>
      <div class="row text-center">
        <div class="col-md-4">
          <img src="assets/img/realtors/kyle_.jpg" alt="" class="rounded-circle mb-3">
          <h4>Kyle Brown</h4>
          <p class="text-success">
            <i class="fas fa-award text-success mb-3"></i> Realtor</p>
          <hr>
          <p>
            <i class="fas fa-phone"></i> (+852)9555-5555</p>
          <p>
            <i class="fas fa-envelope-open"></i> kyle@btrealestate.co</p>
        </div>

        <div class="col-md-4">
          <img src="assets/img/realtors/mark_.jpg" alt="" class="rounded-circle mb-3">
          <h4>Mark Hudson</h4>
          <p class="text-success">Realtor</p>
          <hr>
          <p>
            <i class="fas fa-phone"></i> (+852)9444-4444</p>
          <p>
            <i class="fas fa-envelope-open"></i> mark@btrealestate.co</p>
        </div>

        <div class="col-md-4">
          <img src="assets/img/realtors/jenny_.jpg" alt="" class="rounded-circle mb-3">
          <h4>Jenny Johnson</h4>
          <p class="text-success">Realtor</p>
          <hr>
          <p>
            <i class="fas fa-phone"></i> (+852)9333-3333</p>
          <p>
            <i class="fas fa-envelope-open"></i> jenny@btrealestate.co</p>
        </div>
      </div>
    </div>
  </section>

{% endblock %}
```



#### 改變index內容  

1. templates/pages/index.html  
```
{% extends 'base.html' %} {% block content %}
  <!-- Showcase -->
  <section id="showcase">
    <div class="container text-center">
      <div class="home-search p-5">
        <div class="overlay p-5">
          <h1 class="display-4 mb-4">
            Property Searching Just Got So Easy
          </h1>
          <p class="lead">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Recusandae quas, asperiores eveniet vel nostrum magnam
            voluptatum tempore! Consectetur, id commodi!</p>
          <div class="search">
            <form action="search.html">
              <!-- Form Row 1 -->
              <div class="form-row">
                <div class="col-md-4 mb-3">
                  <label class="sr-only">Keywords</label>
                  <input type="text" name="keywords" class="form-control" placeholder="Keyword (Pool, Garage, etc)">
                </div>

                <div class="col-md-4 mb-3">
                  <label class="sr-only">City</label>
                  <input type="text" name="city" class="form-control" placeholder="City">
                </div>

                <div class="col-md-4 mb-3">
                  <label class="sr-only">State</label>
                  <select name="state" class="form-control">
                    <option selected="true" disabled="disabled">State (All)</option>
                    <option value="A">Central and West</option>
                    <option value="C">Eastern</option>
                    <option value="D">Southern</option>
                    <option value="B">Wan Chai</option>
                    <option value="G">Kowloon City</option>
                    <option value="J">Kwun Tong</option>
                    <option value="F">Sham Shui Po</option>
                    <option value="H">Wong Tai Sin</option>
                    <option value="E">Yau Tsim Mong</option>
                    <option value="T">Island</option>
                    <option value="S">Kwai Tsing</option>
                    <option value="N">North</option>
                    <option value="Q">Sai Kung</option>
                    <option value="R">Sha Tin</option>
                    <option value="P">Tai Po</option>
                    <option value="K">Tsuen Wan</option>
                    <option value="L">Tuen Mun</option>
                    <option value="M">Yuen Long</option>
                  </select>
                </div>
              </div>
              <!-- Form Row 2 -->
              <div class="form-row">
                <div class="col-md-6 mb-3">
                  <label class="sr-only">Bedrooms</label>
                  <select name="bedrooms" class="form-control">
                    <option selected="true" disabled="disabled">Bedrooms (All)</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                    <option value="6">6</option>
                    <option value="7">7</option>
                    <option value="8">8</option>
                    <option value="9">9</option>
                    <option value="10">10</option>
                  </select>
                </div>
                <div class="col-md-6 mb-3">
                  <select name="price" class="form-control" id="type">
                    <option selected="true" disabled="disabled">Max Price (Any)</option>
                    <option value="1000000">$1,000,000</option>
                    <option value="2000000">$2,000,000</option>
                    <option value="3000000">$3,000,000</option>
                    <option value="4000000">$4,000,000</option>
                    <option value="5000000">$5,000,000</option>
                    <option value="6000000">$6,000,000</option>
                    <option value="7000000">$7,000,000</option>
                    <option value="8000000">$8,000,000</option>
                    <option value="9000000">$9,000,000</option>
                    <option value="10000000">$100M+</option>
                  </select>
                </div>
              </div>
              <button class="btn btn-secondary btn-block mt-4" type="submit">Submit form</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Listings -->
  <section id="listings" class="py-5">
    <div class="container">
      <h3 class="text-center mb-3">Latest Listings</h3>
      <div class="row">
        <!-- Listing 1 -->
        <div class="col-md-6 col-lg-4 mb-4">
          <div class="card listing-preview">
            <img class="card-img-top" src="assets/img/homes/home-1_.jpg" alt="">
            <div class="card-img-overlay">
              <h2>
                <span class="badge badge-secondary text-white">$5,380,000</span>
              </h2>
            </div>
            <div class="card-body">
              <div class="listing-heading text-center">
                <h4 class="text-primary">Tai Sang Building, 1A Shanshi Street, Kennedy Town, Hong Kong</h4>
                <p>
                  <i class="fas fa-map-marker text-secondary"></i> Central and West </p>
              </div>
              <hr>
              <div class="row py-2 text-secondary">
                <div class="col-6">
                  <i class="fas fa-th-large"></i> Sqft: 3708</div>
                <div class="col-6">
                  <i class="fas fa-car"></i> Parking space: 0</div>
              </div>
              <div class="row py-2 text-secondary">
                <div class="col-6">
                  <i class="fas fa-bed"></i> Bedrooms: 2</div>
                <div class="col-6">
                  <i class="fas fa-bath"></i> Bathrooms: 1</div>
              </div>
              <hr>
              <div class="row py-2 text-secondary">
                <div class="col-6">
                  <i class="fas fa-user"></i> Kyle Brown</div>
              </div>
              <div class="row text-secondary pb-2">
                <div class="col-6">
                  <i class="fas fa-clock"></i> 5 days ago</div>
              </div>
              <hr>
              <a href="listing.html" class="btn btn-primary btn-block">More Info</a>
            </div>
          </div>
        </div>

        <!-- Listing 2 -->
        <div class="col-md-6 col-lg-4 mb-4">
          <div class="card listing-preview">
            <img class="card-img-top" src="assets/img/homes/home-2_.jpg" alt="">
            <div class="card-img-overlay">
              <h2>
                <span class="badge badge-secondary text-white">$5,550,000</span>
              </h2>
            </div>
            <div class="card-body">
              <div class="listing-heading text-center">
                <h4 class="text-primary">Block A, Shun Lee Building</h4>
                <p>
                  <i class="fas fa-map-marker text-secondary"></i> 240 Ferry Street, Yau Ma Tei, Kowloon</p>
              </div>
              <hr>
              <div class="row py-2 text-secondary">
                <div class="col-6">
                  <i class="fas fa-th-large"></i> Sqft: 4812</div>
                <div class="col-6">
                  <i class="fas fa-car"></i> Parking space: 1</div>
              </div>
              <div class="row py-2 text-secondary">
                <div class="col-6">
                  <i class="fas fa-bed"></i> Bedrooms: 2</div>
                <div class="col-6">
                  <i class="fas fa-bath"></i> Bathrooms: 1</div>
              </div>
              <hr>
              <div class="row py-2 text-secondary">
                <div class="col-6">
                  <i class="fas fa-user"></i> Mark Hudson</div>
              </div>
              <div class="row text-secondary pb-2">
                <div class="col-6">
                  <i class="fas fa-clock"></i> 5 days ago</div>
              </div>
              <hr>
              <a href="listing.html" class="btn btn-primary btn-block">More Info</a>
            </div>
          </div>
        </div>

        <!-- Listing 3 -->
        <div class="col-md-6 col-lg-4 mb-4">
          <div class="card listing-preview">
            <img class="card-img-top" src="assets/img/homes/home-3_.jpg" alt="">
            <div class="card-img-overlay">
              <h2>
                <span class="badge badge-secondary text-white">$300,580,000</span>
              </h2>
            </div>
            <div class="card-body">
              <div class="listing-heading text-center">
                <h4 class="text-primary">Talent Bay Phase 1 Tower 2</h4>
                <p>
                  <i class="fas fa-map-marker text-secondary"></i>Tai Po</p>
              </div>
              <hr>
              <div class="row py-2 text-secondary">
                <div class="col-6">
                  <i class="fas fa-th-large"></i> Sqft: 24444</div>
                <div class="col-6">
                  <i class="fas fa-car"></i> Parking space: 0</div>
              </div>
              <div class="row py-2 text-secondary">
                <div class="col-6">
                  <i class="fas fa-bed"></i> Bedrooms: 5</div>
                <div class="col-6">
                  <i class="fas fa-bath"></i> Bathrooms: 3</div>
              </div>
              <hr>
              <div class="row py-2 text-secondary">
                <div class="col-6">
                  <i class="fas fa-user"></i> Mark Hudson</div>
              </div>
              <div class="row text-secondary pb-2">
                <div class="col-6">
                  <i class="fas fa-clock"></i> 5 days ago</div>
              </div>
              <hr>
              <a href="listing.html" class="btn btn-primary btn-block">More Info</a>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <section id="services" class="py-5 bg-secondary text-white">
    <div class="container">
      <div class="row text-center">
        <div class="col-md-4">
          <i class="fas fa-comment fa-4x mr-4"></i>
          <hr>
          <h3>Consulting Services</h3>
          <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Incidunt, debitis nam! Repudiandae, provident iste consequatur
            hic dignissimos ratione ea quae.</p>
        </div>
        <div class="col-md-4">
          <i class="fas fa-home fa-4x mr-4"></i>
          <hr>
          <h3>Propery Management</h3>
          <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Incidunt, debitis nam! Repudiandae, provident iste consequatur
            hic dignissimos ratione ea quae.</p>
        </div>
        <div class="col-md-4">
          <i class="fas fa-suitcase fa-4x mr-4"></i>
          <hr>
          <h3>Renting & Selling</h3>
          <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Incidunt, debitis nam! Repudiandae, provident iste consequatur
            hic dignissimos ratione ea quae.</p>
        </div>
      </div>
    </div>
  </section>
{% endblock %}
```
---

####  在about頁面加入static

1. templates/pages/about.html
之後把about.html改成這樣
```
{% extends 'base.html' %}
{% load static %}   //增加
{% block title %}| About{% endblock title %}  //增加
{% block content %}
<!-- Breadcrumb -->
<section id="bc" class="mt-3">
    <div class="container">
        <nav aria-label="breadcrumb">
            <ol class="breadcrumb">
                <li class="breadcrumb-item">
                    <a href="{% url 'index' %}"> //改了
                        <i class="fas fa-home"></i> Home</a>
                </li>
                <li class="breadcrumb-item active"> About</li>
            </ol>
        </nav>
    </div>
</section>

<section id="about" class="py-4">
    <div class="container">
        <div class="row">
            <div class="col-md-8">
                <h2>We Search For The Perfect Home</h2>
                <p class="lead">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Sunt, pariatur!</p>
                <img src="{% static 'img/about.jpg' %}" alt=""> //改了
                <p class="mt-4">Lorem ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis esse officia
                    repudiandae ad saepe ex, amet
                    neque quod accusamus rem quia magnam magni dolorum facilis ullam minima perferendis? Exercitationem
                    at quaerat
                    commodi id libero eveniet harum perferendis laborum molestias quia.</p>
            </div>
            <div class="col-md-4">
                {% if mvp_realtor %} //改了
                <div class="card">
                    <img class="card-img-top" src="{{ mvp_realtor.photo.url }}" alt="Seller of the month"> //改了
                    <div class="card-body">
                        <h5 class="card-title">Seller Of The Month</h5>
                        <h6 class="text-secondary">{{ mvp_realtor.name }}</h6> //改了
                        <p class="card-text">{{ mvp_realtor.description }}</p> //改了
                    </div>
                </div>
                {% endif %}  //改了
            </div>
        </div>
    </div>
</section>

<!-- Work -->
<section id="work" class="bg-dark text-white text-center">
    <h2 class="display-4">We Work For You</h2>
    <h4>Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem velit aperiam, unde aliquid at similique!</h4>
    <hr>
    <a href="listings.html" class="btn btn-secondary text-white btn-lg">View Our Featured Listings</a> 
</section>

<!-- Team -->
<section id="team" class="py-5">
    <div class="container">
        <h2 class="text-center">Our Team</h2>
        <div class="row text-center">
            {% if realtors %} //增加
            {% for realtor in realtors %} //增加
            <div class="col-md-4">
                <img src="{{ realtor.photo.url }}" alt="" class="rounded-circle mb-3"> //增加
                <h4>{{ realtor.name }}</h4> //增加
                <p class="text-success">
                    <i class="fas fa-award text-success mb-3"></i> Realtor</p>
                <hr>
                <p>
                    <i class="fas fa-phone"></i> {{ realtor.phone }}</p> //增加
                <p>
                    <i class="fas fa-envelope-open"></i> {{ realtor.email }}</p> //增加
            </div>

            {% endfor %} //增加

            {% else %} //增加
            <div class="col-md-12"> //增加
                <p>No Realtors available</p> //增加
            </div>  //增加
            {% endif %} //增加
        </div>
    </div>
</section>

{% endblock content %}
```
2. btre/pages/views.py
```
from django.shortcuts import render
from django.http import HttpResponse
from realtors.models import Realtor //增加

# Create your views here.
def index(request):
    return render(request,"pages/index.html")

def about(request):
    realtors = Realtor.objects.order_by('-hire_date') //增加
    mvp_realtor = Realtor.objects.filter(is_mvp=True).first() //增加
    context = { //增加
        'realtors': realtors, //增加
        'mvp_realtor': mvp_realtor, //增加
    } //增加

    return render(request,"pages/about.html")
```  
3. 新開名叫realtors的app  
在終端機  
```
python manage.py startapp realtors
```
4. realtors/models.py  
```
from django.db import models
from django.utils import timezone

# Create your models here.

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
```

5. realtors/admin.py  
```
from django.contrib import admin
from .models import Realtor

# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(Realtor, RealtorAdmin)
```
6. btre/settings.py  
```
...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages',
    'realtors' //增加
]
...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'btre_prod', //增加
        'USER': 'postgres', //增加
        'PASSWORD': '1234', //增加
        'HOST': '5432' //增加
    }
}
...

```
7. 在終端機  
```
python manage.py makemigrations
python manage.py migrate
```  
8. 建立superuser
```
python manage.py createsuperuser
```
#### url轉跳
1. templates/partials/_navbar.html
```
{% load static %}
<!-- Navbar -->
<nav class="navbar navbar-expand-lg navbar-dark bg-primary sticky-top">
<div class="container">
<a class="navbar-brand" href="{% url 'index' %}"> //改了
<!-- logo also need to update the assets folder -->
<img src="{% static 'img/logo.png' %}" class="logo" alt="" />
</a>
<button
class="navbar-toggler"
type="button"
data-toggle="collapse"
data-target="#navbarNavAltMarkup"
>
<span class="navbar-toggler-icon"></span>
</button>
<div class="collapse navbar-collapse" id="navbarNavAltMarkup">
<ul class="navbar-nav">
<li class="nav-item active mr-3">
<a class="nav-link" href="{% url 'index' %}">Home</a> //改了
</li>
<li class="nav-item mr-3">
<a class="nav-link" href="{% url 'about' %}">About</a> //改了
</li>
<li class="nav-item mr-3">
<a class="nav-link" href="listings.html">Featured Listings</a>
</li>
</ul>
<ul class="navbar-nav ml-auto">
<li class="nav-item mr-3">
<a class="nav-link" href="register.html">
<i class="fas fa-user-plus"></i> Register</a
>
</li>
<li class="nav-item mr-3">
<a class="nav-link" href="login.html">
<i class="fas fa-sign-in-alt"></i>
Login</a
>
</li>
</ul>
</div>
</div>
</nav>
```
---

## part8 - 1355  
要做的事:
- 建立listings app  
- listings url  
- listings html  
- listings views  

---
#### 建立listings app 
1. 在終端機  
```
python manage.py startapp listings
```  

#### listings url 
1. 在listings裹新增urls.py  
```
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='listings'),
    path('<int:listing_id>',views.listing,name='listing'),
    path('search',views.search,name='search')
]

```
2. btre/urls.py
```
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('', include('pages.urls')),
    path('listings/',include('listings.urls')),//增加
    path('admin/', admin.site.urls)
    
]


```
3. btre/settings.py
```
...

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages',
    'realtors',
    'listings'
]
...
```
4. templates/partials/_navbar.html  
```
...

<div class="collapse navbar-collapse" id="navbarNavAltMarkup">
<ul class="navbar-nav">
<li class="nav-item active mr-3">
<a class="nav-link" href="{% url 'index' %}">Home</a>
</li>
<li class="nav-item mr-3">
<a class="nav-link" href="{% url 'about' %}">About</a>
</li>
<li class="nav-item mr-3">
<a class="nav-link" href="{% url 'listings' %}">Featured Listings</a> //增加
</li>
</ul>
...
```
templates/pages/about.html  
```
...

<!-- Work -->
<section id="work" class="bg-dark text-white text-center">
    <h2 class="display-4">We Work For You</h2>
    <h4>Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem velit aperiam, unde aliquid at similique!</h4>
    <hr>
    <a href="{% url 'listings' %}" class="btn btn-secondary text-white btn-lg">View Our Featured Listings</a>
</section>
...
```  
---
#### listings views  

1. listings/views.py  
```
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'listings/listings.html')

def listing(request):
    return render(request,'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html') 
```
---

#### listings html 
在templates裹新開listings的文件夾，裹面分別開listing.html , listings.html , search.html
1. templates/listings/listing.html
```
<h1>listing</h1>
```
2. templates/listings/listings.html
```
<h1>listings</h1>
```
3. templates/listings/search.html
```
<h1>searching</h1>
```

---

## part9 - 1483  
要做的事:
- listings html內容改變  
- listings admin  
- listings models

----

#### listings html內容改變  

1. templates/listings/listings.html  

```
{% extends 'base.html' %}
{% block title %}| Browse Property Listings{% endblock title %}
{% block content %}
<section id="showcase-inner" class="py-5 text-white">
  <div class="container">
    <div class="row text-center">
      <div class="col-md-12">
        <h1 class="display-4">Browse Our Properties</h1>
        <p class="lead">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Sunt, pariatur!</p>
      </div>
    </div>
  </div>
</section>

<!-- Breadcrumb -->
<section id="bc" class="mt-3">
  <div class="container">
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item">
          <a href="index.html">
            <i class="fas fa-home"></i> Home</a>
        </li>
        <li class="breadcrumb-item active"> Browse Listings</li>
      </ol>
    </nav>
  </div>
</section>

<!-- Listings -->
<section id="listings" class="py-4">
  <div class="container">
    <div class="row">

      <!-- Listing 1 -->
      <div class="col-md-6 col-lg-4 mb-4">
        <div class="card listing-preview">
          <img class="card-img-top" src="assets/img/homes/home-1_.jpg" alt="">
          <div class="card-img-overlay">
            <h2>
              <span class="badge badge-secondary text-white">$5,380,000</span>
            </h2>
          </div>
          <div class="card-body">
            <div class="listing-heading text-center">
              <h4 class="text-primary">Tai Sang Building, 1A Shanshi Street, Kennedy Town, Hong Kong</h4>
              <p>
                <i class="fas fa-map-marker text-secondary"></i> Central and West</p>
            </div>
            <hr>
            <div class="row py-2 text-secondary">
              <div class="col-6">
                <i class="fas fa-th-large"></i> Sqft: 3708</div>
              <div class="col-6">
                <i class="fas fa-car"></i> Parking space: 0</div>
            </div>
            <div class="row py-2 text-secondary">
              <div class="col-6">
                <i class="fas fa-bed"></i> Bedrooms: 2</div>
              <div class="col-6">
                <i class="fas fa-bath"></i> Bathrooms: 1</div>
            </div>
            <hr>
            <div class="row py-2 text-secondary">
              <div class="col-12">
                <i class="fas fa-user"></i> Kyle Brown</div>
            </div>
            <div class="row text-secondary pb-2">
              <div class="col-6">
                <i class="fas fa-clock"></i> 2 days ago</div>
            </div>
            <hr>
            <a href="listing.html" class="btn btn-primary btn-block">More Info</a>
          </div>
        </div>
      </div>

      <!-- Listing 2 -->
      <div class="col-md-6 col-lg-4 mb-4">
        <div class="card listing-preview">
          <img class="card-img-top" src="assets/img/homes/home-2_.jpg" alt="">
          <div class="card-img-overlay">
            <h2>
              <span class="badge badge-secondary text-white">$5,550,000</span>
            </h2>
          </div>
          <div class="card-body">
            <div class="listing-heading text-center">
              <h4 class="text-primary">Block A, Shun Lee Building</h4>
              <p>
                <i class="fas fa-map-marker text-secondary"></i> 240 Ferry Street, Yau Ma Tei, Kowloon</p>
            </div>
            <hr>
            <div class="row py-2 text-secondary">
              <div class="col-6">
                <i class="fas fa-th-large"></i> Sqft: 4812</div>
              <div class="col-6">
                <i class="fas fa-car"></i> Parking space: 1</div>
            </div>
            <div class="row py-2 text-secondary">
              <div class="col-6">
                <i class="fas fa-bed"></i> Bedrooms: 2</div>
              <div class="col-6">
                <i class="fas fa-bath"></i> Bathrooms: 1</div>
            </div>
            <hr>
            <div class="row py-2 text-secondary">
              <div class="col-6">
                <i class="fas fa-user"></i> Mark Hudson</div>
            </div>
            <div class="row text-secondary pb-2">
              <div class="col-6">
                <i class="fas fa-clock"></i> 5 days ago</div>
            </div>
            <hr>
            <a href="listing.html" class="btn btn-primary btn-block">More Info</a>
          </div>
        </div>
      </div>

      <!-- Listing 3 -->
      <div class="col-md-6 col-lg-4 mb-4">
        <div class="card listing-preview">
          <img class="card-img-top" src="assets/img/homes/home-3_.jpg" alt="">
          <div class="card-img-overlay">
            <h2>
              <span class="badge badge-secondary text-white">$300,580,000</span>
            </h2>
          </div>
          <div class="card-body">
            <div class="listing-heading text-center">
              <h4 class="text-primary">Talent Bay Phase 1 Tower 2</h4>
              <p>
                <i class="fas fa-map-marker text-secondary"></i>Tai Po</p>
            </div>
            <hr>
            <div class="row py-2 text-secondary">
              <div class="col-6">
                <i class="fas fa-th-large"></i> Sqft: 24444</div>
              <div class="col-6">
                <i class="fas fa-car"></i> Parking space: 0</div>
            </div>
            <div class="row py-2 text-secondary">
              <div class="col-6">
                <i class="fas fa-bed"></i> Bedrooms: 5</div>
              <div class="col-6">
                <i class="fas fa-bath"></i> Bathrooms: 3</div>
            </div>
            <hr>
            <div class="row py-2 text-secondary">
              <div class="col-6">
                <i class="fas fa-user"></i> Mark Hudson</div>
            </div>
            <div class="row text-secondary pb-2">
              <div class="col-6">
                <i class="fas fa-clock"></i> 5 days ago</div>
            </div>
            <hr>
            <a href="listing.html" class="btn btn-primary btn-block">More Info</a>
          </div>
        </div>
      </div>

      <!-- Listing 4 -->
      <div class="col-md-6 col-lg-4 mb-4">
        <div class="card listing-preview">
          <img class="card-img-top" src="assets/img/homes/home-4_.jpg" alt="">
          <div class="card-img-overlay">
            <h2>
              <span class="badge badge-secondary text-white">$3,380,000</span>
            </h2>
          </div>
          <div class="card-body">
            <div class="listing-heading text-center">
              <h4 class="text-primary">Tianyuhai Block 5B Middle Floor Room D No. 18 Baotai Street</h4>
              <p>
                <i class="fas fa-map-marker text-secondary"></i>Sai Kung Ma On Shan</p>
            </div>
            <hr>
            <div class="row py-2 text-secondary">
              <div class="col-6">
                <i class="fas fa-th-large"></i> Sqft: 2927</div>
              <div class="col-6">
                <i class="fas fa-car"></i> Garage: 2</div>
            </div>
            <div class="row py-2 text-secondary">
              <div class="col-6">
                <i class="fas fa-bed"></i> Bedrooms: 4</div>
              <div class="col-6">
                <i class="fas fa-bath"></i> Bathrooms: 1</div>
            </div>
            <hr>
            <div class="row py-2 text-secondary">
              <div class="col-6">
                <i class="fas fa-user"></i> Jenny Johnson</div>
            </div>
            <div class="row text-secondary pb-2">
              <div class="col-6">
                <i class="fas fa-clock"></i> 5 days ago</div>
            </div>
            <hr>
            <a href="listing.html" class="btn btn-primary btn-block">More Info</a>
          </div>
        </div>
      </div>

      <!-- Listing 5 -->
      <div class="col-md-6 col-lg-4 mb-4">
        <div class="card listing-preview">
          <img class="card-img-top" src="assets/img/homes/home-5_.jpg" alt="">
          <div class="card-img-overlay">
            <h2>
              <span class="badge badge-secondary text-white">$7,230,000</span>
            </h2>
          </div>
          <div class="card-body">
            <div class="listing-heading text-center">
              <h4 class="text-primary">Complete. Tower 1, High Floor, Room C, No. 98, Dahe Road</h4>
              <p>
                <i class="fas fa-map-marker text-secondary"></i>Tsuen Wan </p>
            </div>
            <hr>
            <div class="row py-2 text-secondary">
              <div class="col-6">
                <i class="fas fa-th-large"></i> Sqft: 2207</div>
              <div class="col-6">
                <i class="fas fa-car"></i> Garage: 1</div>
            </div>
            <div class="row py-2 text-secondary">
              <div class="col-6">
                <i class="fas fa-bed"></i> Bedrooms: 3</div>
              <div class="col-6">
                <i class="fas fa-bath"></i> Bathrooms: 1.5</div>
            </div>
            <hr>
            <div class="row py-2 text-secondary">
              <div class="col-6">
                <i class="fas fa-user"></i> Kyle Brown</div>
            </div>
            <div class="row text-secondary pb-2">
              <div class="col-6">
                <i class="fas fa-clock"></i> 5 days ago</div>
            </div>
            <hr>
            <a href="listing.html" class="btn btn-primary btn-block">More Info</a>
          </div>
        </div>
      </div>

      <!-- Listing 6 -->
      <div class="col-md-6 col-lg-4 mb-4">
        <div class="card listing-preview">
          <img class="card-img-top" src="assets/img/homes/home-6_.jpg" alt="">
          <div class="card-img-overlay">
            <h2>
              <span class="badge badge-secondary text-white">$1,200,780,000</span>
            </h2>
          </div>
          <div class="card-body">
            <div class="listing-heading text-center">
              <h4 class="text-primary">Cambridge Road bungalow </h4>
              <p>
                <i class="fas fa-map-marker text-secondary"></i>Kowloon City</p>
            </div>
            <hr>
            <div class="row py-2 text-secondary">
              <div class="col-6">
                <i class="fas fa-th-large"></i> Sqft: 7285</div>
              <div class="col-6">
                <i class="fas fa-car"></i> Garage: 1</div>
            </div>
            <div class="row py-2 text-secondary">
              <div class="col-6">
                <i class="fas fa-bed"></i> Bedrooms: 25</div>
              <div class="col-6">
                <i class="fas fa-bath"></i> Bathrooms: 10</div>
            </div>
            <hr>
            <div class="row py-2 text-secondary">
              <div class="col-6">
                <i class="fas fa-user"></i> Kyle Brown</div>
            </div>
            <div class="row text-secondary pb-2">
              <div class="col-6">
                <i class="fas fa-clock"></i> 5 days ago</div>
            </div>
            <hr>
            <a href="listing.html" class="btn btn-primary btn-block">More Info</a>
          </div>
        </div>
      </div>

    </div>

    <div class="row">
      <div class="col-md-12">
        <ul class="pagination">
          <li class="page-item disabled">
            <a class="page-link" href="#">&laquo;</a>
          </li>
          <li class="page-item active">
            <a class="page-link" href="#">1</a>
          </li>
          <li class="page-item">
            <a class="page-link" href="#">2</a>
          </li>
          <li class="page-item">
            <a class="page-link" href="#">3</a>
          </li>
          <li class="page-item">
            <a class="page-link" href="#">&raquo;</a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</section>
{% endblock content %}
```
#### listings admin  
1. listings/admin.py
```
from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'city',
                     'state', 'zipcode', 'price')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
```
---

#### listings models
1. listings/models.py
```
from django.db import models
from django.utils import timezone
from realtors.models import Realtor


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.title
```
2. 在終端機  

```
python manage.py makemigrations
python manage.py migrate
```
----

## part10 - 1881  
要做的事:
- 上傳圖片  

1. btre/settings.py  
```
...



STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'btre/static')
]


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  //增加
MEDIA_URL = '/media/'  //增加




....
```

2. btre/urls.py  
```
from django.contrib import admin
from django.urls import path , include
from django.conf import settings //增加
from django.conf.urls.static import static//增加

urlpatterns = [
    path('', include('pages.urls')),
    path('listings/',include('listings.urls')),
    path('admin/', admin.site.urls)
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) //增加
```
---
## part11 - 1923  
要做的事:
- 增加 base html  
- listings data 容入 listings html  

---  
#### 增加 base html  
1. 在templates裹開一個admin的文件夾，裹面開base_site.html  

templates/admin/base_site.html  
```
{% extends 'admin/base.html' %}
{% load static %}


{% block branding %}
<h1 id="head">
    <img src="{% static 'img/logo.png' %}" alt="BT Real Estate" height="50px" width="80px" class="brand_img">
    Admin Area
</h1>
{% endblock branding %}


{% block extrastyle %}
<link rel="stylesheet" href="{% static 'css/admin.css' %}">
{% endblock extrastyle %}
```
---
#### listings data 容入 listings html  
1. listings/views.py  
```
from django.shortcuts import render

from .models import Listing  //增加
# Create your views here.


def index(request):
    listings = Listing.objects.all()  //增加
    context = {  //增加
        'listings': listings  //增加
    }  //增加

    return render(request, 'listings/listings.html', context)  //增加context

def listing(request):
    return render(request,'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html') 
```

2. templates/listings/listings.html
```
{% extends 'base.html' %}
{% load humanize %} //增加

{% block content %}
<section id="showcase-inner" class="py-5 text-white">
  <div class="container">
    <div class="row text-center">
      <div class="col-md-12">
        <h1 class="display-4">Browse Our Properties</h1>
        <p class="lead">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Sunt, pariatur!</p>
      </div>
    </div>
  </div>
</section>

<!-- Breadcrumb -->
<section id="bc" class="mt-3">
  <div class="container">
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item">
          <a href="index.html">
            <i class="fas fa-home"></i> Home</a>
        </li>
        <li class="breadcrumb-item active"> Browse Listings</li>
      </ol>
    </nav>
  </div>
</section>

<!-- Listings -->

<section id="listings" class="py-4">
  <div class="container">
    <div class="row">

      <!-- Listing 1 -->
{% if listings %} //增加

{% for listing in listings %} //增加

      <div class="col-md-6 col-lg-4 mb-4">
        <div class="card listing-preview">
          <img class="card-img-top" src="{{listing.photo_main.url}}" alt=""> //改了
          <div class="card-img-overlay">
            <h2>
              <span class="badge badge-secondary text-white">${{listing.price | intcomma}}</span>//改了
            </h2>
          </div>
          <div class="card-body">
            <div class="listing-heading text-center">
              <h4 class="text-primary">{{listing.title}}</h4> //改了
              <p>
                <i class="fas fa-map-marker text-secondary"></i>{{listing.city}}{{listing.state}} {{listing.zipcode}}</p> //改了
            </div>
            <hr>
            <div class="row py-2 text-secondary">
              <div class="col-6">
                <i class="fas fa-th-large"></i> Sqft: {{listing.zipcode}}</div> //改了
              <div class="col-6">
                <i class="fas fa-car"></i> Garage: {{listing.garage}}</div> //改了
            </div>
            <div class="row py-2 text-secondary">
              <div class="col-6">
                <i class="fas fa-bed"></i> Bedrooms: {{listing.bedrooms}}</div> //改了
              <div class="col-6">
                <i class="fas fa-bath"></i> Bathrooms: {{listing.bathroom}}</div> //改了
            </div>
            <hr>
            <div class="row py-2 text-secondary">
              <div class="col-12">
                <i class="fas fa-user"></i> {{listing.realtor}}</div> //改了
            </div>
            <div class="row text-secondary pb-2">
              <div class="col-6">
                <i c2 days agolass="fas fa-clock"></i> {{ listing.list_date | timesince }}</div> //改了
            </div>
            <hr>
            <a href="{% url 'listing' listing.id %}" class="btn btn-primary btn-block">More Info</a> //改了 
          </div>
        </div>
      </div>
      {% endfor %} {% else %}   //增加
      <div class="col-md-12">
        <!--No data then display no data message -->
        <p>No Listings Available</p>
        </div>
        {% endif %}  //增加
        </div>
   

    <div class="row">
      <div class="col-md-12">
        {% if listings.has_other_pages %}  //增加
        <ul class="pagination">
          {% if listings.has_previous %}  //增加
          <li class="page-items">  //增加
            <a  //增加
            href="?page={{listings.previous_page_number}}"  //增加
            class="page-link"  //增加
            ></a>  //增加
            </li>
            {% else %}   //增加

          <li class="page-item disabled">
            <a class="page-link" href="#">&laquo;</a>
          </li>
          {% endif %}  //增加
          <li class="page-item active">
            <a class="page-link" href="#">1</a>
          </li>
          <li class="page-item">
            <a class="page-link" href="#">2</a>
          </li>
          <li class="page-item">
            <a class="page-link" href="#">3</a>
          </li>
          <li class="page-item">
            <a class="page-link" href="#">&raquo;</a>
          </li>
        </ul>
        {% endif %}  //增加
      </div>
    </div>
  </div>
</section>
{% endblock content %}
```

3. btre/settings.py  
```
...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize', //增加
    'pages',
    'realtors',
    'listings'
]
...

```

## part12 - 2126  

要做的事:
- 補回之前的css  
- listings.html 最後修改  - 12549  
---

####  補回之前的css  
1.  btre/static/css/all.css
```
/*!
 * Font Awesome Free 5.3.1 by @fontawesome - https://fontawesome.com
 * License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License)
 */
.fa,
.fas,
.far,
.fal,
.fab {
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  display: inline-block;
  font-style: normal;
  font-variant: normal;
  text-rendering: auto;
  line-height: 1; }

.fa-lg {
  font-size: 1.33333em;
  line-height: 0.75em;
  vertical-align: -.0667em; }

.fa-xs {
  font-size: .75em; }

.fa-sm {
  font-size: .875em; }

.fa-1x {
  font-size: 1em; }

.fa-2x {
  font-size: 2em; }

.fa-3x {
  font-size: 3em; }

.fa-4x {
  font-size: 4em; }

.fa-5x {
  font-size: 5em; }

.fa-6x {
  font-size: 6em; }

.fa-7x {
  font-size: 7em; }

.fa-8x {
  font-size: 8em; }

.fa-9x {
  font-size: 9em; }

.fa-10x {
  font-size: 10em; }

.fa-fw {
  text-align: center;
  width: 1.25em; }

.fa-ul {
  list-style-type: none;
  margin-left: 2.5em;
  padding-left: 0; }
  .fa-ul > li {
    position: relative; }

.fa-li {
  left: -2em;
  position: absolute;
  text-align: center;
  width: 2em;
  line-height: inherit; }

.fa-border {
  border: solid 0.08em #eee;
  border-radius: .1em;
  padding: .2em .25em .15em; }

.fa-pull-left {
  float: left; }

.fa-pull-right {
  float: right; }

.fa.fa-pull-left,
.fas.fa-pull-left,
.far.fa-pull-left,
.fal.fa-pull-left,
.fab.fa-pull-left {
  margin-right: .3em; }

.fa.fa-pull-right,
.fas.fa-pull-right,
.far.fa-pull-right,
.fal.fa-pull-right,
.fab.fa-pull-right {
  margin-left: .3em; }

.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
          animation: fa-spin 2s infinite linear; }

.fa-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
          animation: fa-spin 1s infinite steps(8); }

@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
            transform: rotate(0deg); }
  100% {
    -webkit-transform: rotate(360deg);
            transform: rotate(360deg); } }

@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
            transform: rotate(0deg); }
  100% {
    -webkit-transform: rotate(360deg);
            transform: rotate(360deg); } }

.fa-rotate-90 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";
  -webkit-transform: rotate(90deg);
          transform: rotate(90deg); }

.fa-rotate-180 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";
  -webkit-transform: rotate(180deg);
          transform: rotate(180deg); }

.fa-rotate-270 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";
  -webkit-transform: rotate(270deg);
          transform: rotate(270deg); }

.fa-flip-horizontal {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";
  -webkit-transform: scale(-1, 1);
          transform: scale(-1, 1); }

.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(1, -1);
          transform: scale(1, -1); }

.fa-flip-horizontal.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(-1, -1);
          transform: scale(-1, -1); }

:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  -webkit-filter: none;
          filter: none; }

.fa-stack {
  display: inline-block;
  height: 2em;
  line-height: 2em;
  position: relative;
  vertical-align: middle;
  width: 2em; }

.fa-stack-1x,
.fa-stack-2x {
  left: 0;
  position: absolute;
  text-align: center;
  width: 100%; }

.fa-stack-1x {
  line-height: inherit; }

.fa-stack-2x {
  font-size: 2em; }

.fa-inverse {
  color: #fff; }

/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
readers do not read off random characters that represent icons */
.fa-500px:before {
  content: "\f26e"; }

.fa-accessible-icon:before {
  content: "\f368"; }

.fa-accusoft:before {
  content: "\f369"; }

.fa-ad:before {
  content: "\f641"; }

.fa-address-book:before {
  content: "\f2b9"; }

.fa-address-card:before {
  content: "\f2bb"; }

.fa-adjust:before {
  content: "\f042"; }

.fa-adn:before {
  content: "\f170"; }

.fa-adversal:before {
  content: "\f36a"; }

.fa-affiliatetheme:before {
  content: "\f36b"; }

.fa-air-freshener:before {
  content: "\f5d0"; }

.fa-algolia:before {
  content: "\f36c"; }

.fa-align-center:before {
  content: "\f037"; }

.fa-align-justify:before {
  content: "\f039"; }

.fa-align-left:before {
  content: "\f036"; }

.fa-align-right:before {
  content: "\f038"; }

.fa-alipay:before {
  content: "\f642"; }

.fa-allergies:before {
  content: "\f461"; }

.fa-amazon:before {
  content: "\f270"; }

.fa-amazon-pay:before {
  content: "\f42c"; }

.fa-ambulance:before {
  content: "\f0f9"; }

.fa-american-sign-language-interpreting:before {
  content: "\f2a3"; }

.fa-amilia:before {
  content: "\f36d"; }

.fa-anchor:before {
  content: "\f13d"; }

.fa-android:before {
  content: "\f17b"; }

.fa-angellist:before {
  content: "\f209"; }

.fa-angle-double-down:before {
  content: "\f103"; }

.fa-angle-double-left:before {
  content: "\f100"; }

.fa-angle-double-right:before {
  content: "\f101"; }

.fa-angle-double-up:before {
  content: "\f102"; }

.fa-angle-down:before {
  content: "\f107"; }

.fa-angle-left:before {
  content: "\f104"; }

.fa-angle-right:before {
  content: "\f105"; }

.fa-angle-up:before {
  content: "\f106"; }

.fa-angry:before {
  content: "\f556"; }

.fa-angrycreative:before {
  content: "\f36e"; }

.fa-angular:before {
  content: "\f420"; }

.fa-ankh:before {
  content: "\f644"; }

.fa-app-store:before {
  content: "\f36f"; }

.fa-app-store-ios:before {
  content: "\f370"; }

.fa-apper:before {
  content: "\f371"; }

.fa-apple:before {
  content: "\f179"; }

.fa-apple-alt:before {
  content: "\f5d1"; }

.fa-apple-pay:before {
  content: "\f415"; }

.fa-archive:before {
  content: "\f187"; }

.fa-archway:before {
  content: "\f557"; }

.fa-arrow-alt-circle-down:before {
  content: "\f358"; }

.fa-arrow-alt-circle-left:before {
  content: "\f359"; }

.fa-arrow-alt-circle-right:before {
  content: "\f35a"; }

.fa-arrow-alt-circle-up:before {
  content: "\f35b"; }

.fa-arrow-circle-down:before {
  content: "\f0ab"; }

.fa-arrow-circle-left:before {
  content: "\f0a8"; }

.fa-arrow-circle-right:before {
  content: "\f0a9"; }

.fa-arrow-circle-up:before {
  content: "\f0aa"; }

.fa-arrow-down:before {
  content: "\f063"; }

.fa-arrow-left:before {
  content: "\f060"; }

.fa-arrow-right:before {
  content: "\f061"; }

.fa-arrow-up:before {
  content: "\f062"; }

.fa-arrows-alt:before {
  content: "\f0b2"; }

.fa-arrows-alt-h:before {
  content: "\f337"; }

.fa-arrows-alt-v:before {
  content: "\f338"; }

.fa-assistive-listening-systems:before {
  content: "\f2a2"; }

.fa-asterisk:before {
  content: "\f069"; }

.fa-asymmetrik:before {
  content: "\f372"; }

.fa-at:before {
  content: "\f1fa"; }

.fa-atlas:before {
  content: "\f558"; }

.fa-atom:before {
  content: "\f5d2"; }

.fa-audible:before {
  content: "\f373"; }

.fa-audio-description:before {
  content: "\f29e"; }

.fa-autoprefixer:before {
  content: "\f41c"; }

.fa-avianex:before {
  content: "\f374"; }

.fa-aviato:before {
  content: "\f421"; }

.fa-award:before {
  content: "\f559"; }

.fa-aws:before {
  content: "\f375"; }

.fa-backspace:before {
  content: "\f55a"; }

.fa-backward:before {
  content: "\f04a"; }

.fa-balance-scale:before {
  content: "\f24e"; }

.fa-ban:before {
  content: "\f05e"; }

.fa-band-aid:before {
  content: "\f462"; }

.fa-bandcamp:before {
  content: "\f2d5"; }

.fa-barcode:before {
  content: "\f02a"; }

.fa-bars:before {
  content: "\f0c9"; }

.fa-baseball-ball:before {
  content: "\f433"; }

.fa-basketball-ball:before {
  content: "\f434"; }

.fa-bath:before {
  content: "\f2cd"; }

.fa-battery-empty:before {
  content: "\f244"; }

.fa-battery-full:before {
  content: "\f240"; }

.fa-battery-half:before {
  content: "\f242"; }

.fa-battery-quarter:before {
  content: "\f243"; }

.fa-battery-three-quarters:before {
  content: "\f241"; }

.fa-bed:before {
  content: "\f236"; }

.fa-beer:before {
  content: "\f0fc"; }

.fa-behance:before {
  content: "\f1b4"; }

.fa-behance-square:before {
  content: "\f1b5"; }

.fa-bell:before {
  content: "\f0f3"; }

.fa-bell-slash:before {
  content: "\f1f6"; }

.fa-bezier-curve:before {
  content: "\f55b"; }

.fa-bible:before {
  content: "\f647"; }

.fa-bicycle:before {
  content: "\f206"; }

.fa-bimobject:before {
  content: "\f378"; }

.fa-binoculars:before {
  content: "\f1e5"; }

.fa-birthday-cake:before {
  content: "\f1fd"; }

.fa-bitbucket:before {
  content: "\f171"; }

.fa-bitcoin:before {
  content: "\f379"; }

.fa-bity:before {
  content: "\f37a"; }

.fa-black-tie:before {
  content: "\f27e"; }

.fa-blackberry:before {
  content: "\f37b"; }

.fa-blender:before {
  content: "\f517"; }

.fa-blind:before {
  content: "\f29d"; }

.fa-blogger:before {
  content: "\f37c"; }

.fa-blogger-b:before {
  content: "\f37d"; }

.fa-bluetooth:before {
  content: "\f293"; }

.fa-bluetooth-b:before {
  content: "\f294"; }

.fa-bold:before {
  content: "\f032"; }

.fa-bolt:before {
  content: "\f0e7"; }

.fa-bomb:before {
  content: "\f1e2"; }

.fa-bone:before {
  content: "\f5d7"; }

.fa-bong:before {
  content: "\f55c"; }

.fa-book:before {
  content: "\f02d"; }

.fa-book-open:before {
  content: "\f518"; }

.fa-book-reader:before {
  content: "\f5da"; }

.fa-bookmark:before {
  content: "\f02e"; }

.fa-bowling-ball:before {
  content: "\f436"; }

.fa-box:before {
  content: "\f466"; }

.fa-box-open:before {
  content: "\f49e"; }

.fa-boxes:before {
  content: "\f468"; }

.fa-braille:before {
  content: "\f2a1"; }

.fa-brain:before {
  content: "\f5dc"; }

.fa-briefcase:before {
  content: "\f0b1"; }

.fa-briefcase-medical:before {
  content: "\f469"; }

.fa-broadcast-tower:before {
  content: "\f519"; }

.fa-broom:before {
  content: "\f51a"; }

.fa-brush:before {
  content: "\f55d"; }

.fa-btc:before {
  content: "\f15a"; }

.fa-bug:before {
  content: "\f188"; }

.fa-building:before {
  content: "\f1ad"; }

.fa-bullhorn:before {
  content: "\f0a1"; }

.fa-bullseye:before {
  content: "\f140"; }

.fa-burn:before {
  content: "\f46a"; }

.fa-buromobelexperte:before {
  content: "\f37f"; }

.fa-bus:before {
  content: "\f207"; }

.fa-bus-alt:before {
  content: "\f55e"; }

.fa-business-time:before {
  content: "\f64a"; }

.fa-buysellads:before {
  content: "\f20d"; }

.fa-calculator:before {
  content: "\f1ec"; }

.fa-calendar:before {
  content: "\f133"; }

.fa-calendar-alt:before {
  content: "\f073"; }

.fa-calendar-check:before {
  content: "\f274"; }

.fa-calendar-minus:before {
  content: "\f272"; }

.fa-calendar-plus:before {
  content: "\f271"; }

.fa-calendar-times:before {
  content: "\f273"; }

.fa-camera:before {
  content: "\f030"; }

.fa-camera-retro:before {
  content: "\f083"; }

.fa-cannabis:before {
  content: "\f55f"; }

.fa-capsules:before {
  content: "\f46b"; }

.fa-car:before {
  content: "\f1b9"; }

.fa-car-alt:before {
  content: "\f5de"; }

.fa-car-battery:before {
  content: "\f5df"; }

.fa-car-crash:before {
  content: "\f5e1"; }

.fa-car-side:before {
  content: "\f5e4"; }

.fa-caret-down:before {
  content: "\f0d7"; }

.fa-caret-left:before {
  content: "\f0d9"; }

.fa-caret-right:before {
  content: "\f0da"; }

.fa-caret-square-down:before {
  content: "\f150"; }

.fa-caret-square-left:before {
  content: "\f191"; }

.fa-caret-square-right:before {
  content: "\f152"; }

.fa-caret-square-up:before {
  content: "\f151"; }

.fa-caret-up:before {
  content: "\f0d8"; }

.fa-cart-arrow-down:before {
  content: "\f218"; }

.fa-cart-plus:before {
  content: "\f217"; }

.fa-cc-amazon-pay:before {
  content: "\f42d"; }

.fa-cc-amex:before {
  content: "\f1f3"; }

.fa-cc-apple-pay:before {
  content: "\f416"; }

.fa-cc-diners-club:before {
  content: "\f24c"; }

.fa-cc-discover:before {
  content: "\f1f2"; }

.fa-cc-jcb:before {
  content: "\f24b"; }

.fa-cc-mastercard:before {
  content: "\f1f1"; }

.fa-cc-paypal:before {
  content: "\f1f4"; }

.fa-cc-stripe:before {
  content: "\f1f5"; }

.fa-cc-visa:before {
  content: "\f1f0"; }

.fa-centercode:before {
  content: "\f380"; }

.fa-certificate:before {
  content: "\f0a3"; }

.fa-chalkboard:before {
  content: "\f51b"; }

.fa-chalkboard-teacher:before {
  content: "\f51c"; }

.fa-charging-station:before {
  content: "\f5e7"; }

.fa-chart-area:before {
  content: "\f1fe"; }

.fa-chart-bar:before {
  content: "\f080"; }

.fa-chart-line:before {
  content: "\f201"; }

.fa-chart-pie:before {
  content: "\f200"; }

.fa-check:before {
  content: "\f00c"; }

.fa-check-circle:before {
  content: "\f058"; }

.fa-check-double:before {
  content: "\f560"; }

.fa-check-square:before {
  content: "\f14a"; }

.fa-chess:before {
  content: "\f439"; }

.fa-chess-bishop:before {
  content: "\f43a"; }

.fa-chess-board:before {
  content: "\f43c"; }

.fa-chess-king:before {
  content: "\f43f"; }

.fa-chess-knight:before {
  content: "\f441"; }

.fa-chess-pawn:before {
  content: "\f443"; }

.fa-chess-queen:before {
  content: "\f445"; }

.fa-chess-rook:before {
  content: "\f447"; }

.fa-chevron-circle-down:before {
  content: "\f13a"; }

.fa-chevron-circle-left:before {
  content: "\f137"; }

.fa-chevron-circle-right:before {
  content: "\f138"; }

.fa-chevron-circle-up:before {
  content: "\f139"; }

.fa-chevron-down:before {
  content: "\f078"; }

.fa-chevron-left:before {
  content: "\f053"; }

.fa-chevron-right:before {
  content: "\f054"; }

.fa-chevron-up:before {
  content: "\f077"; }

.fa-child:before {
  content: "\f1ae"; }

.fa-chrome:before {
  content: "\f268"; }

.fa-church:before {
  content: "\f51d"; }

.fa-circle:before {
  content: "\f111"; }

.fa-circle-notch:before {
  content: "\f1ce"; }

.fa-city:before {
  content: "\f64f"; }

.fa-clipboard:before {
  content: "\f328"; }

.fa-clipboard-check:before {
  content: "\f46c"; }

.fa-clipboard-list:before {
  content: "\f46d"; }

.fa-clock:before {
  content: "\f017"; }

.fa-clone:before {
  content: "\f24d"; }

.fa-closed-captioning:before {
  content: "\f20a"; }

.fa-cloud:before {
  content: "\f0c2"; }

.fa-cloud-download-alt:before {
  content: "\f381"; }

.fa-cloud-upload-alt:before {
  content: "\f382"; }

.fa-cloudscale:before {
  content: "\f383"; }

.fa-cloudsmith:before {
  content: "\f384"; }

.fa-cloudversify:before {
  content: "\f385"; }

.fa-cocktail:before {
  content: "\f561"; }

.fa-code:before {
  content: "\f121"; }

.fa-code-branch:before {
  content: "\f126"; }

.fa-codepen:before {
  content: "\f1cb"; }

.fa-codiepie:before {
  content: "\f284"; }

.fa-coffee:before {
  content: "\f0f4"; }

.fa-cog:before {
  content: "\f013"; }

.fa-cogs:before {
  content: "\f085"; }

.fa-coins:before {
  content: "\f51e"; }

.fa-columns:before {
  content: "\f0db"; }

.fa-comment:before {
  content: "\f075"; }

.fa-comment-alt:before {
  content: "\f27a"; }

.fa-comment-dollar:before {
  content: "\f651"; }

.fa-comment-dots:before {
  content: "\f4ad"; }

.fa-comment-slash:before {
  content: "\f4b3"; }

.fa-comments:before {
  content: "\f086"; }

.fa-comments-dollar:before {
  content: "\f653"; }

.fa-compact-disc:before {
  content: "\f51f"; }

.fa-compass:before {
  content: "\f14e"; }

.fa-compress:before {
  content: "\f066"; }

.fa-concierge-bell:before {
  content: "\f562"; }

.fa-connectdevelop:before {
  content: "\f20e"; }

.fa-contao:before {
  content: "\f26d"; }

.fa-cookie:before {
  content: "\f563"; }

.fa-cookie-bite:before {
  content: "\f564"; }

.fa-copy:before {
  content: "\f0c5"; }

.fa-copyright:before {
  content: "\f1f9"; }

.fa-couch:before {
  content: "\f4b8"; }

.fa-cpanel:before {
  content: "\f388"; }

.fa-creative-commons:before {
  content: "\f25e"; }

.fa-creative-commons-by:before {
  content: "\f4e7"; }

.fa-creative-commons-nc:before {
  content: "\f4e8"; }

.fa-creative-commons-nc-eu:before {
  content: "\f4e9"; }

.fa-creative-commons-nc-jp:before {
  content: "\f4ea"; }

.fa-creative-commons-nd:before {
  content: "\f4eb"; }

.fa-creative-commons-pd:before {
  content: "\f4ec"; }

.fa-creative-commons-pd-alt:before {
  content: "\f4ed"; }

.fa-creative-commons-remix:before {
  content: "\f4ee"; }

.fa-creative-commons-sa:before {
  content: "\f4ef"; }

.fa-creative-commons-sampling:before {
  content: "\f4f0"; }

.fa-creative-commons-sampling-plus:before {
  content: "\f4f1"; }

.fa-creative-commons-share:before {
  content: "\f4f2"; }

.fa-credit-card:before {
  content: "\f09d"; }

.fa-crop:before {
  content: "\f125"; }

.fa-crop-alt:before {
  content: "\f565"; }

.fa-cross:before {
  content: "\f654"; }

.fa-crosshairs:before {
  content: "\f05b"; }

.fa-crow:before {
  content: "\f520"; }

.fa-crown:before {
  content: "\f521"; }

.fa-css3:before {
  content: "\f13c"; }

.fa-css3-alt:before {
  content: "\f38b"; }

.fa-cube:before {
  content: "\f1b2"; }

.fa-cubes:before {
  content: "\f1b3"; }

.fa-cut:before {
  content: "\f0c4"; }

.fa-cuttlefish:before {
  content: "\f38c"; }

.fa-d-and-d:before {
  content: "\f38d"; }

.fa-dashcube:before {
  content: "\f210"; }

.fa-database:before {
  content: "\f1c0"; }

.fa-deaf:before {
  content: "\f2a4"; }

.fa-delicious:before {
  content: "\f1a5"; }

.fa-deploydog:before {
  content: "\f38e"; }

.fa-deskpro:before {
  content: "\f38f"; }

.fa-desktop:before {
  content: "\f108"; }

.fa-deviantart:before {
  content: "\f1bd"; }

.fa-dharmachakra:before {
  content: "\f655"; }

.fa-diagnoses:before {
  content: "\f470"; }

.fa-dice:before {
  content: "\f522"; }

.fa-dice-five:before {
  content: "\f523"; }

.fa-dice-four:before {
  content: "\f524"; }

.fa-dice-one:before {
  content: "\f525"; }

.fa-dice-six:before {
  content: "\f526"; }

.fa-dice-three:before {
  content: "\f527"; }

.fa-dice-two:before {
  content: "\f528"; }

.fa-digg:before {
  content: "\f1a6"; }

.fa-digital-ocean:before {
  content: "\f391"; }

.fa-digital-tachograph:before {
  content: "\f566"; }

.fa-directions:before {
  content: "\f5eb"; }

.fa-discord:before {
  content: "\f392"; }

.fa-discourse:before {
  content: "\f393"; }

.fa-divide:before {
  content: "\f529"; }

.fa-dizzy:before {
  content: "\f567"; }

.fa-dna:before {
  content: "\f471"; }

.fa-dochub:before {
  content: "\f394"; }

.fa-docker:before {
  content: "\f395"; }

.fa-dollar-sign:before {
  content: "\f155"; }

.fa-dolly:before {
  content: "\f472"; }

.fa-dolly-flatbed:before {
  content: "\f474"; }

.fa-donate:before {
  content: "\f4b9"; }

.fa-door-closed:before {
  content: "\f52a"; }

.fa-door-open:before {
  content: "\f52b"; }

.fa-dot-circle:before {
  content: "\f192"; }

.fa-dove:before {
  content: "\f4ba"; }

.fa-download:before {
  content: "\f019"; }

.fa-draft2digital:before {
  content: "\f396"; }

.fa-drafting-compass:before {
  content: "\f568"; }

.fa-draw-polygon:before {
  content: "\f5ee"; }

.fa-dribbble:before {
  content: "\f17d"; }

.fa-dribbble-square:before {
  content: "\f397"; }

.fa-dropbox:before {
  content: "\f16b"; }

.fa-drum:before {
  content: "\f569"; }

.fa-drum-steelpan:before {
  content: "\f56a"; }

.fa-drupal:before {
  content: "\f1a9"; }

.fa-dumbbell:before {
  content: "\f44b"; }

.fa-dyalog:before {
  content: "\f399"; }

.fa-earlybirds:before {
  content: "\f39a"; }

.fa-ebay:before {
  content: "\f4f4"; }

.fa-edge:before {
  content: "\f282"; }

.fa-edit:before {
  content: "\f044"; }

.fa-eject:before {
  content: "\f052"; }

.fa-elementor:before {
  content: "\f430"; }

.fa-ellipsis-h:before {
  content: "\f141"; }

.fa-ellipsis-v:before {
  content: "\f142"; }

.fa-ello:before {
  content: "\f5f1"; }

.fa-ember:before {
  content: "\f423"; }

.fa-empire:before {
  content: "\f1d1"; }

.fa-envelope:before {
  content: "\f0e0"; }

.fa-envelope-open:before {
  content: "\f2b6"; }

.fa-envelope-open-text:before {
  content: "\f658"; }

.fa-envelope-square:before {
  content: "\f199"; }

.fa-envira:before {
  content: "\f299"; }

.fa-equals:before {
  content: "\f52c"; }

.fa-eraser:before {
  content: "\f12d"; }

.fa-erlang:before {
  content: "\f39d"; }

.fa-ethereum:before {
  content: "\f42e"; }

.fa-etsy:before {
  content: "\f2d7"; }

.fa-euro-sign:before {
  content: "\f153"; }

.fa-exchange-alt:before {
  content: "\f362"; }

.fa-exclamation:before {
  content: "\f12a"; }

.fa-exclamation-circle:before {
  content: "\f06a"; }

.fa-exclamation-triangle:before {
  content: "\f071"; }

.fa-expand:before {
  content: "\f065"; }

.fa-expand-arrows-alt:before {
  content: "\f31e"; }

.fa-expeditedssl:before {
  content: "\f23e"; }

.fa-external-link-alt:before {
  content: "\f35d"; }

.fa-external-link-square-alt:before {
  content: "\f360"; }

.fa-eye:before {
  content: "\f06e"; }

.fa-eye-dropper:before {
  content: "\f1fb"; }

.fa-eye-slash:before {
  content: "\f070"; }

.fa-facebook:before {
  content: "\f09a"; }

.fa-facebook-f:before {
  content: "\f39e"; }

.fa-facebook-messenger:before {
  content: "\f39f"; }

.fa-facebook-square:before {
  content: "\f082"; }

.fa-fast-backward:before {
  content: "\f049"; }

.fa-fast-forward:before {
  content: "\f050"; }

.fa-fax:before {
  content: "\f1ac"; }

.fa-feather:before {
  content: "\f52d"; }

.fa-feather-alt:before {
  content: "\f56b"; }

.fa-female:before {
  content: "\f182"; }

.fa-fighter-jet:before {
  content: "\f0fb"; }

.fa-file:before {
  content: "\f15b"; }

.fa-file-alt:before {
  content: "\f15c"; }

.fa-file-archive:before {
  content: "\f1c6"; }

.fa-file-audio:before {
  content: "\f1c7"; }

.fa-file-code:before {
  content: "\f1c9"; }

.fa-file-contract:before {
  content: "\f56c"; }

.fa-file-download:before {
  content: "\f56d"; }

.fa-file-excel:before {
  content: "\f1c3"; }

.fa-file-export:before {
  content: "\f56e"; }

.fa-file-image:before {
  content: "\f1c5"; }

.fa-file-import:before {
  content: "\f56f"; }

.fa-file-invoice:before {
  content: "\f570"; }

.fa-file-invoice-dollar:before {
  content: "\f571"; }

.fa-file-medical:before {
  content: "\f477"; }

.fa-file-medical-alt:before {
  content: "\f478"; }

.fa-file-pdf:before {
  content: "\f1c1"; }

.fa-file-powerpoint:before {
  content: "\f1c4"; }

.fa-file-prescription:before {
  content: "\f572"; }

.fa-file-signature:before {
  content: "\f573"; }

.fa-file-upload:before {
  content: "\f574"; }

.fa-file-video:before {
  content: "\f1c8"; }

.fa-file-word:before {
  content: "\f1c2"; }

.fa-fill:before {
  content: "\f575"; }

.fa-fill-drip:before {
  content: "\f576"; }

.fa-film:before {
  content: "\f008"; }

.fa-filter:before {
  content: "\f0b0"; }

.fa-fingerprint:before {
  content: "\f577"; }

.fa-fire:before {
  content: "\f06d"; }

.fa-fire-extinguisher:before {
  content: "\f134"; }

.fa-firefox:before {
  content: "\f269"; }

.fa-first-aid:before {
  content: "\f479"; }

.fa-first-order:before {
  content: "\f2b0"; }

.fa-first-order-alt:before {
  content: "\f50a"; }

.fa-firstdraft:before {
  content: "\f3a1"; }

.fa-fish:before {
  content: "\f578"; }

.fa-flag:before {
  content: "\f024"; }

.fa-flag-checkered:before {
  content: "\f11e"; }

.fa-flask:before {
  content: "\f0c3"; }

.fa-flickr:before {
  content: "\f16e"; }

.fa-flipboard:before {
  content: "\f44d"; }

.fa-flushed:before {
  content: "\f579"; }

.fa-fly:before {
  content: "\f417"; }

.fa-folder:before {
  content: "\f07b"; }

.fa-folder-minus:before {
  content: "\f65d"; }

.fa-folder-open:before {
  content: "\f07c"; }

.fa-folder-plus:before {
  content: "\f65e"; }

.fa-font:before {
  content: "\f031"; }

.fa-font-awesome:before {
  content: "\f2b4"; }

.fa-font-awesome-alt:before {
  content: "\f35c"; }

.fa-font-awesome-flag:before {
  content: "\f425"; }

.fa-font-awesome-logo-full:before {
  content: "\f4e6"; }

.fa-fonticons:before {
  content: "\f280"; }

.fa-fonticons-fi:before {
  content: "\f3a2"; }

.fa-football-ball:before {
  content: "\f44e"; }

.fa-fort-awesome:before {
  content: "\f286"; }

.fa-fort-awesome-alt:before {
  content: "\f3a3"; }

.fa-forumbee:before {
  content: "\f211"; }

.fa-forward:before {
  content: "\f04e"; }

.fa-foursquare:before {
  content: "\f180"; }

.fa-free-code-camp:before {
  content: "\f2c5"; }

.fa-freebsd:before {
  content: "\f3a4"; }

.fa-frog:before {
  content: "\f52e"; }

.fa-frown:before {
  content: "\f119"; }

.fa-frown-open:before {
  content: "\f57a"; }

.fa-fulcrum:before {
  content: "\f50b"; }

.fa-funnel-dollar:before {
  content: "\f662"; }

.fa-futbol:before {
  content: "\f1e3"; }

.fa-galactic-republic:before {
  content: "\f50c"; }

.fa-galactic-senate:before {
  content: "\f50d"; }

.fa-gamepad:before {
  content: "\f11b"; }

.fa-gas-pump:before {
  content: "\f52f"; }

.fa-gavel:before {
  content: "\f0e3"; }

.fa-gem:before {
  content: "\f3a5"; }

.fa-genderless:before {
  content: "\f22d"; }

.fa-get-pocket:before {
  content: "\f265"; }

.fa-gg:before {
  content: "\f260"; }

.fa-gg-circle:before {
  content: "\f261"; }

.fa-gift:before {
  content: "\f06b"; }

.fa-git:before {
  content: "\f1d3"; }

.fa-git-square:before {
  content: "\f1d2"; }

.fa-github:before {
  content: "\f09b"; }

.fa-github-alt:before {
  content: "\f113"; }

.fa-github-square:before {
  content: "\f092"; }

.fa-gitkraken:before {
  content: "\f3a6"; }

.fa-gitlab:before {
  content: "\f296"; }

.fa-gitter:before {
  content: "\f426"; }

.fa-glass-martini:before {
  content: "\f000"; }

.fa-glass-martini-alt:before {
  content: "\f57b"; }

.fa-glasses:before {
  content: "\f530"; }

.fa-glide:before {
  content: "\f2a5"; }

.fa-glide-g:before {
  content: "\f2a6"; }

.fa-globe:before {
  content: "\f0ac"; }

.fa-globe-africa:before {
  content: "\f57c"; }

.fa-globe-americas:before {
  content: "\f57d"; }

.fa-globe-asia:before {
  content: "\f57e"; }

.fa-gofore:before {
  content: "\f3a7"; }

.fa-golf-ball:before {
  content: "\f450"; }

.fa-goodreads:before {
  content: "\f3a8"; }

.fa-goodreads-g:before {
  content: "\f3a9"; }

.fa-google:before {
  content: "\f1a0"; }

.fa-google-drive:before {
  content: "\f3aa"; }

.fa-google-play:before {
  content: "\f3ab"; }

.fa-google-plus:before {
  content: "\f2b3"; }

.fa-google-plus-g:before {
  content: "\f0d5"; }

.fa-google-plus-square:before {
  content: "\f0d4"; }

.fa-google-wallet:before {
  content: "\f1ee"; }

.fa-gopuram:before {
  content: "\f664"; }

.fa-graduation-cap:before {
  content: "\f19d"; }

.fa-gratipay:before {
  content: "\f184"; }

.fa-grav:before {
  content: "\f2d6"; }

.fa-greater-than:before {
  content: "\f531"; }

.fa-greater-than-equal:before {
  content: "\f532"; }

.fa-grimace:before {
  content: "\f57f"; }

.fa-grin:before {
  content: "\f580"; }

.fa-grin-alt:before {
  content: "\f581"; }

.fa-grin-beam:before {
  content: "\f582"; }

.fa-grin-beam-sweat:before {
  content: "\f583"; }

.fa-grin-hearts:before {
  content: "\f584"; }

.fa-grin-squint:before {
  content: "\f585"; }

.fa-grin-squint-tears:before {
  content: "\f586"; }

.fa-grin-stars:before {
  content: "\f587"; }

.fa-grin-tears:before {
  content: "\f588"; }

.fa-grin-tongue:before {
  content: "\f589"; }

.fa-grin-tongue-squint:before {
  content: "\f58a"; }

.fa-grin-tongue-wink:before {
  content: "\f58b"; }

.fa-grin-wink:before {
  content: "\f58c"; }

.fa-grip-horizontal:before {
  content: "\f58d"; }

.fa-grip-vertical:before {
  content: "\f58e"; }

.fa-gripfire:before {
  content: "\f3ac"; }

.fa-grunt:before {
  content: "\f3ad"; }

.fa-gulp:before {
  content: "\f3ae"; }

.fa-h-square:before {
  content: "\f0fd"; }

.fa-hacker-news:before {
  content: "\f1d4"; }

.fa-hacker-news-square:before {
  content: "\f3af"; }

.fa-hackerrank:before {
  content: "\f5f7"; }

.fa-hamsa:before {
  content: "\f665"; }

.fa-hand-holding:before {
  content: "\f4bd"; }

.fa-hand-holding-heart:before {
  content: "\f4be"; }

.fa-hand-holding-usd:before {
  content: "\f4c0"; }

.fa-hand-lizard:before {
  content: "\f258"; }

.fa-hand-paper:before {
  content: "\f256"; }

.fa-hand-peace:before {
  content: "\f25b"; }

.fa-hand-point-down:before {
  content: "\f0a7"; }

.fa-hand-point-left:before {
  content: "\f0a5"; }

.fa-hand-point-right:before {
  content: "\f0a4"; }

.fa-hand-point-up:before {
  content: "\f0a6"; }

.fa-hand-pointer:before {
  content: "\f25a"; }

.fa-hand-rock:before {
  content: "\f255"; }

.fa-hand-scissors:before {
  content: "\f257"; }

.fa-hand-spock:before {
  content: "\f259"; }

.fa-hands:before {
  content: "\f4c2"; }

.fa-hands-helping:before {
  content: "\f4c4"; }

.fa-handshake:before {
  content: "\f2b5"; }

.fa-hashtag:before {
  content: "\f292"; }

.fa-haykal:before {
  content: "\f666"; }

.fa-hdd:before {
  content: "\f0a0"; }

.fa-heading:before {
  content: "\f1dc"; }

.fa-headphones:before {
  content: "\f025"; }

.fa-headphones-alt:before {
  content: "\f58f"; }

.fa-headset:before {
  content: "\f590"; }

.fa-heart:before {
  content: "\f004"; }

.fa-heartbeat:before {
  content: "\f21e"; }

.fa-helicopter:before {
  content: "\f533"; }

.fa-highlighter:before {
  content: "\f591"; }

.fa-hips:before {
  content: "\f452"; }

.fa-hire-a-helper:before {
  content: "\f3b0"; }

.fa-history:before {
  content: "\f1da"; }

.fa-hockey-puck:before {
  content: "\f453"; }

.fa-home:before {
  content: "\f015"; }

.fa-hooli:before {
  content: "\f427"; }

.fa-hornbill:before {
  content: "\f592"; }

.fa-hospital:before {
  content: "\f0f8"; }

.fa-hospital-alt:before {
  content: "\f47d"; }

.fa-hospital-symbol:before {
  content: "\f47e"; }

.fa-hot-tub:before {
  content: "\f593"; }

.fa-hotel:before {
  content: "\f594"; }

.fa-hotjar:before {
  content: "\f3b1"; }

.fa-hourglass:before {
  content: "\f254"; }

.fa-hourglass-end:before {
  content: "\f253"; }

.fa-hourglass-half:before {
  content: "\f252"; }

.fa-hourglass-start:before {
  content: "\f251"; }

.fa-houzz:before {
  content: "\f27c"; }

.fa-html5:before {
  content: "\f13b"; }

.fa-hubspot:before {
  content: "\f3b2"; }

.fa-i-cursor:before {
  content: "\f246"; }

.fa-id-badge:before {
  content: "\f2c1"; }

.fa-id-card:before {
  content: "\f2c2"; }

.fa-id-card-alt:before {
  content: "\f47f"; }

.fa-image:before {
  content: "\f03e"; }

.fa-images:before {
  content: "\f302"; }

.fa-imdb:before {
  content: "\f2d8"; }

.fa-inbox:before {
  content: "\f01c"; }

.fa-indent:before {
  content: "\f03c"; }

.fa-industry:before {
  content: "\f275"; }

.fa-infinity:before {
  content: "\f534"; }

.fa-info:before {
  content: "\f129"; }

.fa-info-circle:before {
  content: "\f05a"; }

.fa-instagram:before {
  content: "\f16d"; }

.fa-internet-explorer:before {
  content: "\f26b"; }

.fa-ioxhost:before {
  content: "\f208"; }

.fa-italic:before {
  content: "\f033"; }

.fa-itunes:before {
  content: "\f3b4"; }

.fa-itunes-note:before {
  content: "\f3b5"; }

.fa-java:before {
  content: "\f4e4"; }

.fa-jedi:before {
  content: "\f669"; }

.fa-jedi-order:before {
  content: "\f50e"; }

.fa-jenkins:before {
  content: "\f3b6"; }

.fa-joget:before {
  content: "\f3b7"; }

.fa-joint:before {
  content: "\f595"; }

.fa-joomla:before {
  content: "\f1aa"; }

.fa-journal-whills:before {
  content: "\f66a"; }

.fa-js:before {
  content: "\f3b8"; }

.fa-js-square:before {
  content: "\f3b9"; }

.fa-jsfiddle:before {
  content: "\f1cc"; }

.fa-kaaba:before {
  content: "\f66b"; }

.fa-kaggle:before {
  content: "\f5fa"; }

.fa-key:before {
  content: "\f084"; }

.fa-keybase:before {
  content: "\f4f5"; }

.fa-keyboard:before {
  content: "\f11c"; }

.fa-keycdn:before {
  content: "\f3ba"; }

.fa-khanda:before {
  content: "\f66d"; }

.fa-kickstarter:before {
  content: "\f3bb"; }

.fa-kickstarter-k:before {
  content: "\f3bc"; }

.fa-kiss:before {
  content: "\f596"; }

.fa-kiss-beam:before {
  content: "\f597"; }

.fa-kiss-wink-heart:before {
  content: "\f598"; }

.fa-kiwi-bird:before {
  content: "\f535"; }

.fa-korvue:before {
  content: "\f42f"; }

.fa-landmark:before {
  content: "\f66f"; }

.fa-language:before {
  content: "\f1ab"; }

.fa-laptop:before {
  content: "\f109"; }

.fa-laptop-code:before {
  content: "\f5fc"; }

.fa-laravel:before {
  content: "\f3bd"; }

.fa-lastfm:before {
  content: "\f202"; }

.fa-lastfm-square:before {
  content: "\f203"; }

.fa-laugh:before {
  content: "\f599"; }

.fa-laugh-beam:before {
  content: "\f59a"; }

.fa-laugh-squint:before {
  content: "\f59b"; }

.fa-laugh-wink:before {
  content: "\f59c"; }

.fa-layer-group:before {
  content: "\f5fd"; }

.fa-leaf:before {
  content: "\f06c"; }

.fa-leanpub:before {
  content: "\f212"; }

.fa-lemon:before {
  content: "\f094"; }

.fa-less:before {
  content: "\f41d"; }

.fa-less-than:before {
  content: "\f536"; }

.fa-less-than-equal:before {
  content: "\f537"; }

.fa-level-down-alt:before {
  content: "\f3be"; }

.fa-level-up-alt:before {
  content: "\f3bf"; }

.fa-life-ring:before {
  content: "\f1cd"; }

.fa-lightbulb:before {
  content: "\f0eb"; }

.fa-line:before {
  content: "\f3c0"; }

.fa-link:before {
  content: "\f0c1"; }

.fa-linkedin:before {
  content: "\f08c"; }

.fa-linkedin-in:before {
  content: "\f0e1"; }

.fa-linode:before {
  content: "\f2b8"; }

.fa-linux:before {
  content: "\f17c"; }

.fa-lira-sign:before {
  content: "\f195"; }

.fa-list:before {
  content: "\f03a"; }

.fa-list-alt:before {
  content: "\f022"; }

.fa-list-ol:before {
  content: "\f0cb"; }

.fa-list-ul:before {
  content: "\f0ca"; }

.fa-location-arrow:before {
  content: "\f124"; }

.fa-lock:before {
  content: "\f023"; }

.fa-lock-open:before {
  content: "\f3c1"; }

.fa-long-arrow-alt-down:before {
  content: "\f309"; }

.fa-long-arrow-alt-left:before {
  content: "\f30a"; }

.fa-long-arrow-alt-right:before {
  content: "\f30b"; }

.fa-long-arrow-alt-up:before {
  content: "\f30c"; }

.fa-low-vision:before {
  content: "\f2a8"; }

.fa-luggage-cart:before {
  content: "\f59d"; }

.fa-lyft:before {
  content: "\f3c3"; }

.fa-magento:before {
  content: "\f3c4"; }

.fa-magic:before {
  content: "\f0d0"; }

.fa-magnet:before {
  content: "\f076"; }

.fa-mail-bulk:before {
  content: "\f674"; }

.fa-mailchimp:before {
  content: "\f59e"; }

.fa-male:before {
  content: "\f183"; }

.fa-mandalorian:before {
  content: "\f50f"; }

.fa-map:before {
  content: "\f279"; }

.fa-map-marked:before {
  content: "\f59f"; }

.fa-map-marked-alt:before {
  content: "\f5a0"; }

.fa-map-marker:before {
  content: "\f041"; }

.fa-map-marker-alt:before {
  content: "\f3c5"; }

.fa-map-pin:before {
  content: "\f276"; }

.fa-map-signs:before {
  content: "\f277"; }

.fa-markdown:before {
  content: "\f60f"; }

.fa-marker:before {
  content: "\f5a1"; }

.fa-mars:before {
  content: "\f222"; }

.fa-mars-double:before {
  content: "\f227"; }

.fa-mars-stroke:before {
  content: "\f229"; }

.fa-mars-stroke-h:before {
  content: "\f22b"; }

.fa-mars-stroke-v:before {
  content: "\f22a"; }

.fa-mastodon:before {
  content: "\f4f6"; }

.fa-maxcdn:before {
  content: "\f136"; }

.fa-medal:before {
  content: "\f5a2"; }

.fa-medapps:before {
  content: "\f3c6"; }

.fa-medium:before {
  content: "\f23a"; }

.fa-medium-m:before {
  content: "\f3c7"; }

.fa-medkit:before {
  content: "\f0fa"; }

.fa-medrt:before {
  content: "\f3c8"; }

.fa-meetup:before {
  content: "\f2e0"; }

.fa-megaport:before {
  content: "\f5a3"; }

.fa-meh:before {
  content: "\f11a"; }

.fa-meh-blank:before {
  content: "\f5a4"; }

.fa-meh-rolling-eyes:before {
  content: "\f5a5"; }

.fa-memory:before {
  content: "\f538"; }

.fa-menorah:before {
  content: "\f676"; }

.fa-mercury:before {
  content: "\f223"; }

.fa-microchip:before {
  content: "\f2db"; }

.fa-microphone:before {
  content: "\f130"; }

.fa-microphone-alt:before {
  content: "\f3c9"; }

.fa-microphone-alt-slash:before {
  content: "\f539"; }

.fa-microphone-slash:before {
  content: "\f131"; }

.fa-microscope:before {
  content: "\f610"; }

.fa-microsoft:before {
  content: "\f3ca"; }

.fa-minus:before {
  content: "\f068"; }

.fa-minus-circle:before {
  content: "\f056"; }

.fa-minus-square:before {
  content: "\f146"; }

.fa-mix:before {
  content: "\f3cb"; }

.fa-mixcloud:before {
  content: "\f289"; }

.fa-mizuni:before {
  content: "\f3cc"; }

.fa-mobile:before {
  content: "\f10b"; }

.fa-mobile-alt:before {
  content: "\f3cd"; }

.fa-modx:before {
  content: "\f285"; }

.fa-monero:before {
  content: "\f3d0"; }

.fa-money-bill:before {
  content: "\f0d6"; }

.fa-money-bill-alt:before {
  content: "\f3d1"; }

.fa-money-bill-wave:before {
  content: "\f53a"; }

.fa-money-bill-wave-alt:before {
  content: "\f53b"; }

.fa-money-check:before {
  content: "\f53c"; }

.fa-money-check-alt:before {
  content: "\f53d"; }

.fa-monument:before {
  content: "\f5a6"; }

.fa-moon:before {
  content: "\f186"; }

.fa-mortar-pestle:before {
  content: "\f5a7"; }

.fa-mosque:before {
  content: "\f678"; }

.fa-motorcycle:before {
  content: "\f21c"; }

.fa-mouse-pointer:before {
  content: "\f245"; }

.fa-music:before {
  content: "\f001"; }

.fa-napster:before {
  content: "\f3d2"; }

.fa-neos:before {
  content: "\f612"; }

.fa-neuter:before {
  content: "\f22c"; }

.fa-newspaper:before {
  content: "\f1ea"; }

.fa-nimblr:before {
  content: "\f5a8"; }

.fa-nintendo-switch:before {
  content: "\f418"; }

.fa-node:before {
  content: "\f419"; }

.fa-node-js:before {
  content: "\f3d3"; }

.fa-not-equal:before {
  content: "\f53e"; }

.fa-notes-medical:before {
  content: "\f481"; }

.fa-npm:before {
  content: "\f3d4"; }

.fa-ns8:before {
  content: "\f3d5"; }

.fa-nutritionix:before {
  content: "\f3d6"; }

.fa-object-group:before {
  content: "\f247"; }

.fa-object-ungroup:before {
  content: "\f248"; }

.fa-odnoklassniki:before {
  content: "\f263"; }

.fa-odnoklassniki-square:before {
  content: "\f264"; }

.fa-oil-can:before {
  content: "\f613"; }

.fa-old-republic:before {
  content: "\f510"; }

.fa-om:before {
  content: "\f679"; }

.fa-opencart:before {
  content: "\f23d"; }

.fa-openid:before {
  content: "\f19b"; }

.fa-opera:before {
  content: "\f26a"; }

.fa-optin-monster:before {
  content: "\f23c"; }

.fa-osi:before {
  content: "\f41a"; }

.fa-outdent:before {
  content: "\f03b"; }

.fa-page4:before {
  content: "\f3d7"; }

.fa-pagelines:before {
  content: "\f18c"; }

.fa-paint-brush:before {
  content: "\f1fc"; }

.fa-paint-roller:before {
  content: "\f5aa"; }

.fa-palette:before {
  content: "\f53f"; }

.fa-palfed:before {
  content: "\f3d8"; }

.fa-pallet:before {
  content: "\f482"; }

.fa-paper-plane:before {
  content: "\f1d8"; }

.fa-paperclip:before {
  content: "\f0c6"; }

.fa-parachute-box:before {
  content: "\f4cd"; }

.fa-paragraph:before {
  content: "\f1dd"; }

.fa-parking:before {
  content: "\f540"; }

.fa-passport:before {
  content: "\f5ab"; }

.fa-pastafarianism:before {
  content: "\f67b"; }

.fa-paste:before {
  content: "\f0ea"; }

.fa-patreon:before {
  content: "\f3d9"; }

.fa-pause:before {
  content: "\f04c"; }

.fa-pause-circle:before {
  content: "\f28b"; }

.fa-paw:before {
  content: "\f1b0"; }

.fa-paypal:before {
  content: "\f1ed"; }

.fa-peace:before {
  content: "\f67c"; }

.fa-pen:before {
  content: "\f304"; }

.fa-pen-alt:before {
  content: "\f305"; }

.fa-pen-fancy:before {
  content: "\f5ac"; }

.fa-pen-nib:before {
  content: "\f5ad"; }

.fa-pen-square:before {
  content: "\f14b"; }

.fa-pencil-alt:before {
  content: "\f303"; }

.fa-pencil-ruler:before {
  content: "\f5ae"; }

.fa-people-carry:before {
  content: "\f4ce"; }

.fa-percent:before {
  content: "\f295"; }

.fa-percentage:before {
  content: "\f541"; }

.fa-periscope:before {
  content: "\f3da"; }

.fa-phabricator:before {
  content: "\f3db"; }

.fa-phoenix-framework:before {
  content: "\f3dc"; }

.fa-phoenix-squadron:before {
  content: "\f511"; }

.fa-phone:before {
  content: "\f095"; }

.fa-phone-slash:before {
  content: "\f3dd"; }

.fa-phone-square:before {
  content: "\f098"; }

.fa-phone-volume:before {
  content: "\f2a0"; }

.fa-php:before {
  content: "\f457"; }

.fa-pied-piper:before {
  content: "\f2ae"; }

.fa-pied-piper-alt:before {
  content: "\f1a8"; }

.fa-pied-piper-hat:before {
  content: "\f4e5"; }

.fa-pied-piper-pp:before {
  content: "\f1a7"; }

.fa-piggy-bank:before {
  content: "\f4d3"; }

.fa-pills:before {
  content: "\f484"; }

.fa-pinterest:before {
  content: "\f0d2"; }

.fa-pinterest-p:before {
  content: "\f231"; }

.fa-pinterest-square:before {
  content: "\f0d3"; }

.fa-place-of-worship:before {
  content: "\f67f"; }

.fa-plane:before {
  content: "\f072"; }

.fa-plane-arrival:before {
  content: "\f5af"; }

.fa-plane-departure:before {
  content: "\f5b0"; }

.fa-play:before {
  content: "\f04b"; }

.fa-play-circle:before {
  content: "\f144"; }

.fa-playstation:before {
  content: "\f3df"; }

.fa-plug:before {
  content: "\f1e6"; }

.fa-plus:before {
  content: "\f067"; }

.fa-plus-circle:before {
  content: "\f055"; }

.fa-plus-square:before {
  content: "\f0fe"; }

.fa-podcast:before {
  content: "\f2ce"; }

.fa-poll:before {
  content: "\f681"; }

.fa-poll-h:before {
  content: "\f682"; }

.fa-poo:before {
  content: "\f2fe"; }

.fa-poop:before {
  content: "\f619"; }

.fa-portrait:before {
  content: "\f3e0"; }

.fa-pound-sign:before {
  content: "\f154"; }

.fa-power-off:before {
  content: "\f011"; }

.fa-pray:before {
  content: "\f683"; }

.fa-praying-hands:before {
  content: "\f684"; }

.fa-prescription:before {
  content: "\f5b1"; }

.fa-prescription-bottle:before {
  content: "\f485"; }

.fa-prescription-bottle-alt:before {
  content: "\f486"; }

.fa-print:before {
  content: "\f02f"; }

.fa-procedures:before {
  content: "\f487"; }

.fa-product-hunt:before {
  content: "\f288"; }

.fa-project-diagram:before {
  content: "\f542"; }

.fa-pushed:before {
  content: "\f3e1"; }

.fa-puzzle-piece:before {
  content: "\f12e"; }

.fa-python:before {
  content: "\f3e2"; }

.fa-qq:before {
  content: "\f1d6"; }

.fa-qrcode:before {
  content: "\f029"; }

.fa-question:before {
  content: "\f128"; }

.fa-question-circle:before {
  content: "\f059"; }

.fa-quidditch:before {
  content: "\f458"; }

.fa-quinscape:before {
  content: "\f459"; }

.fa-quora:before {
  content: "\f2c4"; }

.fa-quote-left:before {
  content: "\f10d"; }

.fa-quote-right:before {
  content: "\f10e"; }

.fa-quran:before {
  content: "\f687"; }

.fa-r-project:before {
  content: "\f4f7"; }

.fa-random:before {
  content: "\f074"; }

.fa-ravelry:before {
  content: "\f2d9"; }

.fa-react:before {
  content: "\f41b"; }

.fa-readme:before {
  content: "\f4d5"; }

.fa-rebel:before {
  content: "\f1d0"; }

.fa-receipt:before {
  content: "\f543"; }

.fa-recycle:before {
  content: "\f1b8"; }

.fa-red-river:before {
  content: "\f3e3"; }

.fa-reddit:before {
  content: "\f1a1"; }

.fa-reddit-alien:before {
  content: "\f281"; }

.fa-reddit-square:before {
  content: "\f1a2"; }

.fa-redo:before {
  content: "\f01e"; }

.fa-redo-alt:before {
  content: "\f2f9"; }

.fa-registered:before {
  content: "\f25d"; }

.fa-rendact:before {
  content: "\f3e4"; }

.fa-renren:before {
  content: "\f18b"; }

.fa-reply:before {
  content: "\f3e5"; }

.fa-reply-all:before {
  content: "\f122"; }

.fa-replyd:before {
  content: "\f3e6"; }

.fa-researchgate:before {
  content: "\f4f8"; }

.fa-resolving:before {
  content: "\f3e7"; }

.fa-retweet:before {
  content: "\f079"; }

.fa-rev:before {
  content: "\f5b2"; }

.fa-ribbon:before {
  content: "\f4d6"; }

.fa-road:before {
  content: "\f018"; }

.fa-robot:before {
  content: "\f544"; }

.fa-rocket:before {
  content: "\f135"; }

.fa-rocketchat:before {
  content: "\f3e8"; }

.fa-rockrms:before {
  content: "\f3e9"; }

.fa-route:before {
  content: "\f4d7"; }

.fa-rss:before {
  content: "\f09e"; }

.fa-rss-square:before {
  content: "\f143"; }

.fa-ruble-sign:before {
  content: "\f158"; }

.fa-ruler:before {
  content: "\f545"; }

.fa-ruler-combined:before {
  content: "\f546"; }

.fa-ruler-horizontal:before {
  content: "\f547"; }

.fa-ruler-vertical:before {
  content: "\f548"; }

.fa-rupee-sign:before {
  content: "\f156"; }

.fa-sad-cry:before {
  content: "\f5b3"; }

.fa-sad-tear:before {
  content: "\f5b4"; }

.fa-safari:before {
  content: "\f267"; }

.fa-sass:before {
  content: "\f41e"; }

.fa-save:before {
  content: "\f0c7"; }

.fa-schlix:before {
  content: "\f3ea"; }

.fa-school:before {
  content: "\f549"; }

.fa-screwdriver:before {
  content: "\f54a"; }

.fa-scribd:before {
  content: "\f28a"; }

.fa-search:before {
  content: "\f002"; }

.fa-search-dollar:before {
  content: "\f688"; }

.fa-search-location:before {
  content: "\f689"; }

.fa-search-minus:before {
  content: "\f010"; }

.fa-search-plus:before {
  content: "\f00e"; }

.fa-searchengin:before {
  content: "\f3eb"; }

.fa-seedling:before {
  content: "\f4d8"; }

.fa-sellcast:before {
  content: "\f2da"; }

.fa-sellsy:before {
  content: "\f213"; }

.fa-server:before {
  content: "\f233"; }

.fa-servicestack:before {
  content: "\f3ec"; }

.fa-shapes:before {
  content: "\f61f"; }

.fa-share:before {
  content: "\f064"; }

.fa-share-alt:before {
  content: "\f1e0"; }

.fa-share-alt-square:before {
  content: "\f1e1"; }

.fa-share-square:before {
  content: "\f14d"; }

.fa-shekel-sign:before {
  content: "\f20b"; }

.fa-shield-alt:before {
  content: "\f3ed"; }

.fa-ship:before {
  content: "\f21a"; }

.fa-shipping-fast:before {
  content: "\f48b"; }

.fa-shirtsinbulk:before {
  content: "\f214"; }

.fa-shoe-prints:before {
  content: "\f54b"; }

.fa-shopping-bag:before {
  content: "\f290"; }

.fa-shopping-basket:before {
  content: "\f291"; }

.fa-shopping-cart:before {
  content: "\f07a"; }

.fa-shopware:before {
  content: "\f5b5"; }

.fa-shower:before {
  content: "\f2cc"; }

.fa-shuttle-van:before {
  content: "\f5b6"; }

.fa-sign:before {
  content: "\f4d9"; }

.fa-sign-in-alt:before {
  content: "\f2f6"; }

.fa-sign-language:before {
  content: "\f2a7"; }

.fa-sign-out-alt:before {
  content: "\f2f5"; }

.fa-signal:before {
  content: "\f012"; }

.fa-signature:before {
  content: "\f5b7"; }

.fa-simplybuilt:before {
  content: "\f215"; }

.fa-sistrix:before {
  content: "\f3ee"; }

.fa-sitemap:before {
  content: "\f0e8"; }

.fa-sith:before {
  content: "\f512"; }

.fa-skull:before {
  content: "\f54c"; }

.fa-skyatlas:before {
  content: "\f216"; }

.fa-skype:before {
  content: "\f17e"; }

.fa-slack:before {
  content: "\f198"; }

.fa-slack-hash:before {
  content: "\f3ef"; }

.fa-sliders-h:before {
  content: "\f1de"; }

.fa-slideshare:before {
  content: "\f1e7"; }

.fa-smile:before {
  content: "\f118"; }

.fa-smile-beam:before {
  content: "\f5b8"; }

.fa-smile-wink:before {
  content: "\f4da"; }

.fa-smoking:before {
  content: "\f48d"; }

.fa-smoking-ban:before {
  content: "\f54d"; }

.fa-snapchat:before {
  content: "\f2ab"; }

.fa-snapchat-ghost:before {
  content: "\f2ac"; }

.fa-snapchat-square:before {
  content: "\f2ad"; }

.fa-snowflake:before {
  content: "\f2dc"; }

.fa-socks:before {
  content: "\f696"; }

.fa-solar-panel:before {
  content: "\f5ba"; }

.fa-sort:before {
  content: "\f0dc"; }

.fa-sort-alpha-down:before {
  content: "\f15d"; }

.fa-sort-alpha-up:before {
  content: "\f15e"; }

.fa-sort-amount-down:before {
  content: "\f160"; }

.fa-sort-amount-up:before {
  content: "\f161"; }

.fa-sort-down:before {
  content: "\f0dd"; }

.fa-sort-numeric-down:before {
  content: "\f162"; }

.fa-sort-numeric-up:before {
  content: "\f163"; }

.fa-sort-up:before {
  content: "\f0de"; }

.fa-soundcloud:before {
  content: "\f1be"; }

.fa-spa:before {
  content: "\f5bb"; }

.fa-space-shuttle:before {
  content: "\f197"; }

.fa-speakap:before {
  content: "\f3f3"; }

.fa-spinner:before {
  content: "\f110"; }

.fa-splotch:before {
  content: "\f5bc"; }

.fa-spotify:before {
  content: "\f1bc"; }

.fa-spray-can:before {
  content: "\f5bd"; }

.fa-square:before {
  content: "\f0c8"; }

.fa-square-full:before {
  content: "\f45c"; }

.fa-square-root-alt:before {
  content: "\f698"; }

.fa-squarespace:before {
  content: "\f5be"; }

.fa-stack-exchange:before {
  content: "\f18d"; }

.fa-stack-overflow:before {
  content: "\f16c"; }

.fa-stamp:before {
  content: "\f5bf"; }

.fa-star:before {
  content: "\f005"; }

.fa-star-and-crescent:before {
  content: "\f699"; }

.fa-star-half:before {
  content: "\f089"; }

.fa-star-half-alt:before {
  content: "\f5c0"; }

.fa-star-of-david:before {
  content: "\f69a"; }

.fa-star-of-life:before {
  content: "\f621"; }

.fa-staylinked:before {
  content: "\f3f5"; }

.fa-steam:before {
  content: "\f1b6"; }

.fa-steam-square:before {
  content: "\f1b7"; }

.fa-steam-symbol:before {
  content: "\f3f6"; }

.fa-step-backward:before {
  content: "\f048"; }

.fa-step-forward:before {
  content: "\f051"; }

.fa-stethoscope:before {
  content: "\f0f1"; }

.fa-sticker-mule:before {
  content: "\f3f7"; }

.fa-sticky-note:before {
  content: "\f249"; }

.fa-stop:before {
  content: "\f04d"; }

.fa-stop-circle:before {
  content: "\f28d"; }

.fa-stopwatch:before {
  content: "\f2f2"; }

.fa-store:before {
  content: "\f54e"; }

.fa-store-alt:before {
  content: "\f54f"; }

.fa-strava:before {
  content: "\f428"; }

.fa-stream:before {
  content: "\f550"; }

.fa-street-view:before {
  content: "\f21d"; }

.fa-strikethrough:before {
  content: "\f0cc"; }

.fa-stripe:before {
  content: "\f429"; }

.fa-stripe-s:before {
  content: "\f42a"; }

.fa-stroopwafel:before {
  content: "\f551"; }

.fa-studiovinari:before {
  content: "\f3f8"; }

.fa-stumbleupon:before {
  content: "\f1a4"; }

.fa-stumbleupon-circle:before {
  content: "\f1a3"; }

.fa-subscript:before {
  content: "\f12c"; }

.fa-subway:before {
  content: "\f239"; }

.fa-suitcase:before {
  content: "\f0f2"; }

.fa-suitcase-rolling:before {
  content: "\f5c1"; }

.fa-sun:before {
  content: "\f185"; }

.fa-superpowers:before {
  content: "\f2dd"; }

.fa-superscript:before {
  content: "\f12b"; }

.fa-supple:before {
  content: "\f3f9"; }

.fa-surprise:before {
  content: "\f5c2"; }

.fa-swatchbook:before {
  content: "\f5c3"; }

.fa-swimmer:before {
  content: "\f5c4"; }

.fa-swimming-pool:before {
  content: "\f5c5"; }

.fa-synagogue:before {
  content: "\f69b"; }

.fa-sync:before {
  content: "\f021"; }

.fa-sync-alt:before {
  content: "\f2f1"; }

.fa-syringe:before {
  content: "\f48e"; }

.fa-table:before {
  content: "\f0ce"; }

.fa-table-tennis:before {
  content: "\f45d"; }

.fa-tablet:before {
  content: "\f10a"; }

.fa-tablet-alt:before {
  content: "\f3fa"; }

.fa-tablets:before {
  content: "\f490"; }

.fa-tachometer-alt:before {
  content: "\f3fd"; }

.fa-tag:before {
  content: "\f02b"; }

.fa-tags:before {
  content: "\f02c"; }

.fa-tape:before {
  content: "\f4db"; }

.fa-tasks:before {
  content: "\f0ae"; }

.fa-taxi:before {
  content: "\f1ba"; }

.fa-teamspeak:before {
  content: "\f4f9"; }

.fa-teeth:before {
  content: "\f62e"; }

.fa-teeth-open:before {
  content: "\f62f"; }

.fa-telegram:before {
  content: "\f2c6"; }

.fa-telegram-plane:before {
  content: "\f3fe"; }

.fa-tencent-weibo:before {
  content: "\f1d5"; }

.fa-terminal:before {
  content: "\f120"; }

.fa-text-height:before {
  content: "\f034"; }

.fa-text-width:before {
  content: "\f035"; }

.fa-th:before {
  content: "\f00a"; }

.fa-th-large:before {
  content: "\f009"; }

.fa-th-list:before {
  content: "\f00b"; }

.fa-the-red-yeti:before {
  content: "\f69d"; }

.fa-theater-masks:before {
  content: "\f630"; }

.fa-themeco:before {
  content: "\f5c6"; }

.fa-themeisle:before {
  content: "\f2b2"; }

.fa-thermometer:before {
  content: "\f491"; }

.fa-thermometer-empty:before {
  content: "\f2cb"; }

.fa-thermometer-full:before {
  content: "\f2c7"; }

.fa-thermometer-half:before {
  content: "\f2c9"; }

.fa-thermometer-quarter:before {
  content: "\f2ca"; }

.fa-thermometer-three-quarters:before {
  content: "\f2c8"; }

.fa-thumbs-down:before {
  content: "\f165"; }

.fa-thumbs-up:before {
  content: "\f164"; }

.fa-thumbtack:before {
  content: "\f08d"; }

.fa-ticket-alt:before {
  content: "\f3ff"; }

.fa-times:before {
  content: "\f00d"; }

.fa-times-circle:before {
  content: "\f057"; }

.fa-tint:before {
  content: "\f043"; }

.fa-tint-slash:before {
  content: "\f5c7"; }

.fa-tired:before {
  content: "\f5c8"; }

.fa-toggle-off:before {
  content: "\f204"; }

.fa-toggle-on:before {
  content: "\f205"; }

.fa-toolbox:before {
  content: "\f552"; }

.fa-tooth:before {
  content: "\f5c9"; }

.fa-torah:before {
  content: "\f6a0"; }

.fa-torii-gate:before {
  content: "\f6a1"; }

.fa-trade-federation:before {
  content: "\f513"; }

.fa-trademark:before {
  content: "\f25c"; }

.fa-traffic-light:before {
  content: "\f637"; }

.fa-train:before {
  content: "\f238"; }

.fa-transgender:before {
  content: "\f224"; }

.fa-transgender-alt:before {
  content: "\f225"; }

.fa-trash:before {
  content: "\f1f8"; }

.fa-trash-alt:before {
  content: "\f2ed"; }

.fa-tree:before {
  content: "\f1bb"; }

.fa-trello:before {
  content: "\f181"; }

.fa-tripadvisor:before {
  content: "\f262"; }

.fa-trophy:before {
  content: "\f091"; }

.fa-truck:before {
  content: "\f0d1"; }

.fa-truck-loading:before {
  content: "\f4de"; }

.fa-truck-monster:before {
  content: "\f63b"; }

.fa-truck-moving:before {
  content: "\f4df"; }

.fa-truck-pickup:before {
  content: "\f63c"; }

.fa-tshirt:before {
  content: "\f553"; }

.fa-tty:before {
  content: "\f1e4"; }

.fa-tumblr:before {
  content: "\f173"; }

.fa-tumblr-square:before {
  content: "\f174"; }

.fa-tv:before {
  content: "\f26c"; }

.fa-twitch:before {
  content: "\f1e8"; }

.fa-twitter:before {
  content: "\f099"; }

.fa-twitter-square:before {
  content: "\f081"; }

.fa-typo3:before {
  content: "\f42b"; }

.fa-uber:before {
  content: "\f402"; }

.fa-uikit:before {
  content: "\f403"; }

.fa-umbrella:before {
  content: "\f0e9"; }

.fa-umbrella-beach:before {
  content: "\f5ca"; }

.fa-underline:before {
  content: "\f0cd"; }

.fa-undo:before {
  content: "\f0e2"; }

.fa-undo-alt:before {
  content: "\f2ea"; }

.fa-uniregistry:before {
  content: "\f404"; }

.fa-universal-access:before {
  content: "\f29a"; }

.fa-university:before {
  content: "\f19c"; }

.fa-unlink:before {
  content: "\f127"; }

.fa-unlock:before {
  content: "\f09c"; }

.fa-unlock-alt:before {
  content: "\f13e"; }

.fa-untappd:before {
  content: "\f405"; }

.fa-upload:before {
  content: "\f093"; }

.fa-usb:before {
  content: "\f287"; }

.fa-user:before {
  content: "\f007"; }

.fa-user-alt:before {
  content: "\f406"; }

.fa-user-alt-slash:before {
  content: "\f4fa"; }

.fa-user-astronaut:before {
  content: "\f4fb"; }

.fa-user-check:before {
  content: "\f4fc"; }

.fa-user-circle:before {
  content: "\f2bd"; }

.fa-user-clock:before {
  content: "\f4fd"; }

.fa-user-cog:before {
  content: "\f4fe"; }

.fa-user-edit:before {
  content: "\f4ff"; }

.fa-user-friends:before {
  content: "\f500"; }

.fa-user-graduate:before {
  content: "\f501"; }

.fa-user-lock:before {
  content: "\f502"; }

.fa-user-md:before {
  content: "\f0f0"; }

.fa-user-minus:before {
  content: "\f503"; }

.fa-user-ninja:before {
  content: "\f504"; }

.fa-user-plus:before {
  content: "\f234"; }

.fa-user-secret:before {
  content: "\f21b"; }

.fa-user-shield:before {
  content: "\f505"; }

.fa-user-slash:before {
  content: "\f506"; }

.fa-user-tag:before {
  content: "\f507"; }

.fa-user-tie:before {
  content: "\f508"; }

.fa-user-times:before {
  content: "\f235"; }

.fa-users:before {
  content: "\f0c0"; }

.fa-users-cog:before {
  content: "\f509"; }

.fa-ussunnah:before {
  content: "\f407"; }

.fa-utensil-spoon:before {
  content: "\f2e5"; }

.fa-utensils:before {
  content: "\f2e7"; }

.fa-vaadin:before {
  content: "\f408"; }

.fa-vector-square:before {
  content: "\f5cb"; }

.fa-venus:before {
  content: "\f221"; }

.fa-venus-double:before {
  content: "\f226"; }

.fa-venus-mars:before {
  content: "\f228"; }

.fa-viacoin:before {
  content: "\f237"; }

.fa-viadeo:before {
  content: "\f2a9"; }

.fa-viadeo-square:before {
  content: "\f2aa"; }

.fa-vial:before {
  content: "\f492"; }

.fa-vials:before {
  content: "\f493"; }

.fa-viber:before {
  content: "\f409"; }

.fa-video:before {
  content: "\f03d"; }

.fa-video-slash:before {
  content: "\f4e2"; }

.fa-vihara:before {
  content: "\f6a7"; }

.fa-vimeo:before {
  content: "\f40a"; }

.fa-vimeo-square:before {
  content: "\f194"; }

.fa-vimeo-v:before {
  content: "\f27d"; }

.fa-vine:before {
  content: "\f1ca"; }

.fa-vk:before {
  content: "\f189"; }

.fa-vnv:before {
  content: "\f40b"; }

.fa-volleyball-ball:before {
  content: "\f45f"; }

.fa-volume-down:before {
  content: "\f027"; }

.fa-volume-off:before {
  content: "\f026"; }

.fa-volume-up:before {
  content: "\f028"; }

.fa-vuejs:before {
  content: "\f41f"; }

.fa-walking:before {
  content: "\f554"; }

.fa-wallet:before {
  content: "\f555"; }

.fa-warehouse:before {
  content: "\f494"; }

.fa-weebly:before {
  content: "\f5cc"; }

.fa-weibo:before {
  content: "\f18a"; }

.fa-weight:before {
  content: "\f496"; }

.fa-weight-hanging:before {
  content: "\f5cd"; }

.fa-weixin:before {
  content: "\f1d7"; }

.fa-whatsapp:before {
  content: "\f232"; }

.fa-whatsapp-square:before {
  content: "\f40c"; }

.fa-wheelchair:before {
  content: "\f193"; }

.fa-whmcs:before {
  content: "\f40d"; }

.fa-wifi:before {
  content: "\f1eb"; }

.fa-wikipedia-w:before {
  content: "\f266"; }

.fa-window-close:before {
  content: "\f410"; }

.fa-window-maximize:before {
  content: "\f2d0"; }

.fa-window-minimize:before {
  content: "\f2d1"; }

.fa-window-restore:before {
  content: "\f2d2"; }

.fa-windows:before {
  content: "\f17a"; }

.fa-wine-glass:before {
  content: "\f4e3"; }

.fa-wine-glass-alt:before {
  content: "\f5ce"; }

.fa-wix:before {
  content: "\f5cf"; }

.fa-wolf-pack-battalion:before {
  content: "\f514"; }

.fa-won-sign:before {
  content: "\f159"; }

.fa-wordpress:before {
  content: "\f19a"; }

.fa-wordpress-simple:before {
  content: "\f411"; }

.fa-wpbeginner:before {
  content: "\f297"; }

.fa-wpexplorer:before {
  content: "\f2de"; }

.fa-wpforms:before {
  content: "\f298"; }

.fa-wrench:before {
  content: "\f0ad"; }

.fa-x-ray:before {
  content: "\f497"; }

.fa-xbox:before {
  content: "\f412"; }

.fa-xing:before {
  content: "\f168"; }

.fa-xing-square:before {
  content: "\f169"; }

.fa-y-combinator:before {
  content: "\f23b"; }

.fa-yahoo:before {
  content: "\f19e"; }

.fa-yandex:before {
  content: "\f413"; }

.fa-yandex-international:before {
  content: "\f414"; }

.fa-yelp:before {
  content: "\f1e9"; }

.fa-yen-sign:before {
  content: "\f157"; }

.fa-yin-yang:before {
  content: "\f6ad"; }

.fa-yoast:before {
  content: "\f2b1"; }

.fa-youtube:before {
  content: "\f167"; }

.fa-youtube-square:before {
  content: "\f431"; }

.fa-zhihu:before {
  content: "\f63f"; }

.sr-only {
  border: 0;
  clip: rect(0, 0, 0, 0);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px; }

.sr-only-focusable:active, .sr-only-focusable:focus {
  clip: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  position: static;
  width: auto; }
@font-face {
  font-family: 'Font Awesome 5 Brands';
  font-style: normal;
  font-weight: normal;
  src: url("../webfonts/fa-brands-400.eot");
  src: url("../webfonts/fa-brands-400.eot?#iefix") format("embedded-opentype"), url("../webfonts/fa-brands-400.woff2") format("woff2"), url("../webfonts/fa-brands-400.woff") format("woff"), url("../webfonts/fa-brands-400.ttf") format("truetype"), url("../webfonts/fa-brands-400.svg#fontawesome") format("svg"); }

.fab {
  font-family: 'Font Awesome 5 Brands'; }
@font-face {
  font-family: 'Font Awesome 5 Free';
  font-style: normal;
  font-weight: 400;
  src: url("../webfonts/fa-regular-400.eot");
  src: url("../webfonts/fa-regular-400.eot?#iefix") format("embedded-opentype"), url("../webfonts/fa-regular-400.woff2") format("woff2"), url("../webfonts/fa-regular-400.woff") format("woff"), url("../webfonts/fa-regular-400.ttf") format("truetype"), url("../webfonts/fa-regular-400.svg#fontawesome") format("svg"); }

.far {
  font-family: 'Font Awesome 5 Free';
  font-weight: 400; }
@font-face {
  font-family: 'Font Awesome 5 Free';
  font-style: normal;
  font-weight: 900;
  src: url("../webfonts/fa-solid-900.eot");
  src: url("../webfonts/fa-solid-900.eot?#iefix") format("embedded-opentype"), url("../webfonts/fa-solid-900.woff2") format("woff2"), url("../webfonts/fa-solid-900.woff") format("woff"), url("../webfonts/fa-solid-900.ttf") format("truetype"), url("../webfonts/fa-solid-900.svg#fontawesome") format("svg"); }

.fa,
.fas {
  font-family: 'Font Awesome 5 Free';
  font-weight: 900; }

```
2. btre/static/css/bootstrap.css  
```
/*!
 * Bootstrap v4.1.3 (https://getbootstrap.com/)
 * Copyright 2011-2018 The Bootstrap Authors
 * Copyright 2011-2018 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
:root {
  --blue: #10284e;
  --indigo: #6610f2;
  --purple: #6f42c1;
  --pink: #e83e8c;
  --red: #e94646;
  --orange: #fd7e14;
  --yellow: #ffc107;
  --green: #30caa0;
  --teal: #20c997;
  --cyan: #17a2b8;
  --white: #fff;
  --gray: #6c757d;
  --gray-dark: #343a40;
  --primary: #10284e;
  --secondary: #30caa0;
  --success: #20c997;
  --info: #17a2b8;
  --warning: #ffc107;
  --danger: #e94646;
  --light: #f8f9fa;
  --dark: #343a40;
  --breakpoint-xs: 0;
  --breakpoint-sm: 576px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 992px;
  --breakpoint-xl: 1200px;
  --font-family-sans-serif: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  --font-family-monospace: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; }

*,
*::before,
*::after {
  box-sizing: border-box; }

html {
  font-family: sans-serif;
  line-height: 1.15;
  -webkit-text-size-adjust: 100%;
  -ms-text-size-adjust: 100%;
  -ms-overflow-style: scrollbar;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0); }

@-ms-viewport {
  width: device-width; }

article, aside, figcaption, figure, footer, header, hgroup, main, nav, section {
  display: block; }

body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #212529;
  text-align: left;
  background-color: #fff; }

[tabindex="-1"]:focus {
  outline: 0 !important; }

hr {
  box-sizing: content-box;
  height: 0;
  overflow: visible; }

h1, h2, h3, h4, h5, h6 {
  margin-top: 0;
  margin-bottom: 0.5rem; }

p {
  margin-top: 0;
  margin-bottom: 1rem; }

abbr[title],
abbr[data-original-title] {
  text-decoration: underline;
  text-decoration: underline dotted;
  cursor: help;
  border-bottom: 0; }

address {
  margin-bottom: 1rem;
  font-style: normal;
  line-height: inherit; }

ol,
ul,
dl {
  margin-top: 0;
  margin-bottom: 1rem; }

ol ol,
ul ul,
ol ul,
ul ol {
  margin-bottom: 0; }

dt {
  font-weight: 700; }

dd {
  margin-bottom: .5rem;
  margin-left: 0; }

blockquote {
  margin: 0 0 1rem; }

dfn {
  font-style: italic; }

b,
strong {
  font-weight: bolder; }

small {
  font-size: 80%; }

sub,
sup {
  position: relative;
  font-size: 75%;
  line-height: 0;
  vertical-align: baseline; }

sub {
  bottom: -.25em; }

sup {
  top: -.5em; }

a {
  color: #10284e;
  text-decoration: none;
  background-color: transparent;
  -webkit-text-decoration-skip: objects; }
  a:hover {
    color: #03070f;
    text-decoration: underline; }

a:not([href]):not([tabindex]) {
  color: inherit;
  text-decoration: none; }
  a:not([href]):not([tabindex]):hover, a:not([href]):not([tabindex]):focus {
    color: inherit;
    text-decoration: none; }
  a:not([href]):not([tabindex]):focus {
    outline: 0; }

pre,
code,
kbd,
samp {
  font-family: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  font-size: 1em; }

pre {
  margin-top: 0;
  margin-bottom: 1rem;
  overflow: auto;
  -ms-overflow-style: scrollbar; }

figure {
  margin: 0 0 1rem; }

img {
  vertical-align: middle;
  border-style: none; }

svg {
  overflow: hidden;
  vertical-align: middle; }

table {
  border-collapse: collapse; }

caption {
  padding-top: 0.75rem;
  padding-bottom: 0.75rem;
  color: #6c757d;
  text-align: left;
  caption-side: bottom; }

th {
  text-align: inherit; }

label {
  display: inline-block;
  margin-bottom: 0.5rem; }

button {
  border-radius: 0; }

button:focus {
  outline: 1px dotted;
  outline: 5px auto -webkit-focus-ring-color; }

input,
button,
select,
optgroup,
textarea {
  margin: 0;
  font-family: inherit;
  font-size: inherit;
  line-height: inherit; }

button,
input {
  overflow: visible; }

button,
select {
  text-transform: none; }

button,
html [type="button"],
[type="reset"],
[type="submit"] {
  -webkit-appearance: button; }

button::-moz-focus-inner,
[type="button"]::-moz-focus-inner,
[type="reset"]::-moz-focus-inner,
[type="submit"]::-moz-focus-inner {
  padding: 0;
  border-style: none; }

input[type="radio"],
input[type="checkbox"] {
  box-sizing: border-box;
  padding: 0; }

input[type="date"],
input[type="time"],
input[type="datetime-local"],
input[type="month"] {
  -webkit-appearance: listbox; }

textarea {
  overflow: auto;
  resize: vertical; }

fieldset {
  min-width: 0;
  padding: 0;
  margin: 0;
  border: 0; }

legend {
  display: block;
  width: 100%;
  max-width: 100%;
  padding: 0;
  margin-bottom: .5rem;
  font-size: 1.5rem;
  line-height: inherit;
  color: inherit;
  white-space: normal; }

progress {
  vertical-align: baseline; }

[type="number"]::-webkit-inner-spin-button,
[type="number"]::-webkit-outer-spin-button {
  height: auto; }

[type="search"] {
  outline-offset: -2px;
  -webkit-appearance: none; }

[type="search"]::-webkit-search-cancel-button,
[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none; }

::-webkit-file-upload-button {
  font: inherit;
  -webkit-appearance: button; }

output {
  display: inline-block; }

summary {
  display: list-item;
  cursor: pointer; }

template {
  display: none; }

[hidden] {
  display: none !important; }

h1, h2, h3, h4, h5, h6,
.h1, .h2, .h3, .h4, .h5, .h6 {
  margin-bottom: 0.5rem;
  font-family: inherit;
  font-weight: 500;
  line-height: 1.2;
  color: inherit; }

h1, .h1 {
  font-size: 2.5rem; }

h2, .h2 {
  font-size: 2rem; }

h3, .h3 {
  font-size: 1.75rem; }

h4, .h4 {
  font-size: 1.5rem; }

h5, .h5 {
  font-size: 1.25rem; }

h6, .h6 {
  font-size: 1rem; }

.lead {
  font-size: 1.25rem;
  font-weight: 300; }

.display-1 {
  font-size: 6rem;
  font-weight: 300;
  line-height: 1.2; }

.display-2 {
  font-size: 5.5rem;
  font-weight: 300;
  line-height: 1.2; }

.display-3 {
  font-size: 4.5rem;
  font-weight: 300;
  line-height: 1.2; }

.display-4 {
  font-size: 3.5rem;
  font-weight: 300;
  line-height: 1.2; }

hr {
  margin-top: 1rem;
  margin-bottom: 1rem;
  border: 0;
  border-top: 1px solid rgba(0, 0, 0, 0.1); }

small,
.small {
  font-size: 80%;
  font-weight: 400; }

mark,
.mark {
  padding: 0.2em;
  background-color: #fcf8e3; }

.list-unstyled {
  padding-left: 0;
  list-style: none; }

.list-inline {
  padding-left: 0;
  list-style: none; }

.list-inline-item {
  display: inline-block; }
  .list-inline-item:not(:last-child) {
    margin-right: 0.5rem; }

.initialism {
  font-size: 90%;
  text-transform: uppercase; }

.blockquote {
  margin-bottom: 1rem;
  font-size: 1.25rem; }

.blockquote-footer {
  display: block;
  font-size: 80%;
  color: #6c757d; }
  .blockquote-footer::before {
    content: "\2014 \00A0"; }

.img-fluid {
  max-width: 100%;
  height: auto; }

.img-thumbnail {
  padding: 0.25rem;
  background-color: #fff;
  border: 1px solid #dee2e6;
  border-radius: 0.25rem;
  max-width: 100%;
  height: auto; }

.figure {
  display: inline-block; }

.figure-img {
  margin-bottom: 0.5rem;
  line-height: 1; }

.figure-caption {
  font-size: 90%;
  color: #6c757d; }

code {
  font-size: 87.5%;
  color: #e83e8c;
  word-break: break-word; }
  a > code {
    color: inherit; }

kbd {
  padding: 0.2rem 0.4rem;
  font-size: 87.5%;
  color: #fff;
  background-color: #212529;
  border-radius: 0.2rem; }
  kbd kbd {
    padding: 0;
    font-size: 100%;
    font-weight: 700; }

pre {
  display: block;
  font-size: 87.5%;
  color: #212529; }
  pre code {
    font-size: inherit;
    color: inherit;
    word-break: normal; }

.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll; }

.container {
  width: 100%;
  padding-right: 15px;
  padding-left: 15px;
  margin-right: auto;
  margin-left: auto; }
  @media (min-width: 576px) {
    .container {
      max-width: 540px; } }
  @media (min-width: 768px) {
    .container {
      max-width: 720px; } }
  @media (min-width: 992px) {
    .container {
      max-width: 960px; } }
  @media (min-width: 1200px) {
    .container {
      max-width: 1140px; } }

.container-fluid {
  width: 100%;
  padding-right: 15px;
  padding-left: 15px;
  margin-right: auto;
  margin-left: auto; }

.row {
  display: flex;
  flex-wrap: wrap;
  margin-right: -15px;
  margin-left: -15px; }

.no-gutters {
  margin-right: 0;
  margin-left: 0; }
  .no-gutters > .col,
  .no-gutters > [class*="col-"] {
    padding-right: 0;
    padding-left: 0; }

.col-1, .col-2, .col-3, .col-4, .col-5, .col-6, .col-7, .col-8, .col-9, .col-10, .col-11, .col-12, .col,
.col-auto, .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12, .col-sm,
.col-sm-auto, .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12, .col-md,
.col-md-auto, .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12, .col-lg,
.col-lg-auto, .col-xl-1, .col-xl-2, .col-xl-3, .col-xl-4, .col-xl-5, .col-xl-6, .col-xl-7, .col-xl-8, .col-xl-9, .col-xl-10, .col-xl-11, .col-xl-12, .col-xl,
.col-xl-auto {
  position: relative;
  width: 100%;
  min-height: 1px;
  padding-right: 15px;
  padding-left: 15px; }

.col {
  flex-basis: 0;
  flex-grow: 1;
  max-width: 100%; }

.col-auto {
  flex: 0 0 auto;
  width: auto;
  max-width: none; }

.col-1 {
  flex: 0 0 8.33333%;
  max-width: 8.33333%; }

.col-2 {
  flex: 0 0 16.66667%;
  max-width: 16.66667%; }

.col-3 {
  flex: 0 0 25%;
  max-width: 25%; }

.col-4 {
  flex: 0 0 33.33333%;
  max-width: 33.33333%; }

.col-5 {
  flex: 0 0 41.66667%;
  max-width: 41.66667%; }

.col-6 {
  flex: 0 0 50%;
  max-width: 50%; }

.col-7 {
  flex: 0 0 58.33333%;
  max-width: 58.33333%; }

.col-8 {
  flex: 0 0 66.66667%;
  max-width: 66.66667%; }

.col-9 {
  flex: 0 0 75%;
  max-width: 75%; }

.col-10 {
  flex: 0 0 83.33333%;
  max-width: 83.33333%; }

.col-11 {
  flex: 0 0 91.66667%;
  max-width: 91.66667%; }

.col-12 {
  flex: 0 0 100%;
  max-width: 100%; }

.order-first {
  order: -1; }

.order-last {
  order: 13; }

.order-0 {
  order: 0; }

.order-1 {
  order: 1; }

.order-2 {
  order: 2; }

.order-3 {
  order: 3; }

.order-4 {
  order: 4; }

.order-5 {
  order: 5; }

.order-6 {
  order: 6; }

.order-7 {
  order: 7; }

.order-8 {
  order: 8; }

.order-9 {
  order: 9; }

.order-10 {
  order: 10; }

.order-11 {
  order: 11; }

.order-12 {
  order: 12; }

.offset-1 {
  margin-left: 8.33333%; }

.offset-2 {
  margin-left: 16.66667%; }

.offset-3 {
  margin-left: 25%; }

.offset-4 {
  margin-left: 33.33333%; }

.offset-5 {
  margin-left: 41.66667%; }

.offset-6 {
  margin-left: 50%; }

.offset-7 {
  margin-left: 58.33333%; }

.offset-8 {
  margin-left: 66.66667%; }

.offset-9 {
  margin-left: 75%; }

.offset-10 {
  margin-left: 83.33333%; }

.offset-11 {
  margin-left: 91.66667%; }

@media (min-width: 576px) {
  .col-sm {
    flex-basis: 0;
    flex-grow: 1;
    max-width: 100%; }
  .col-sm-auto {
    flex: 0 0 auto;
    width: auto;
    max-width: none; }
  .col-sm-1 {
    flex: 0 0 8.33333%;
    max-width: 8.33333%; }
  .col-sm-2 {
    flex: 0 0 16.66667%;
    max-width: 16.66667%; }
  .col-sm-3 {
    flex: 0 0 25%;
    max-width: 25%; }
  .col-sm-4 {
    flex: 0 0 33.33333%;
    max-width: 33.33333%; }
  .col-sm-5 {
    flex: 0 0 41.66667%;
    max-width: 41.66667%; }
  .col-sm-6 {
    flex: 0 0 50%;
    max-width: 50%; }
  .col-sm-7 {
    flex: 0 0 58.33333%;
    max-width: 58.33333%; }
  .col-sm-8 {
    flex: 0 0 66.66667%;
    max-width: 66.66667%; }
  .col-sm-9 {
    flex: 0 0 75%;
    max-width: 75%; }
  .col-sm-10 {
    flex: 0 0 83.33333%;
    max-width: 83.33333%; }
  .col-sm-11 {
    flex: 0 0 91.66667%;
    max-width: 91.66667%; }
  .col-sm-12 {
    flex: 0 0 100%;
    max-width: 100%; }
  .order-sm-first {
    order: -1; }
  .order-sm-last {
    order: 13; }
  .order-sm-0 {
    order: 0; }
  .order-sm-1 {
    order: 1; }
  .order-sm-2 {
    order: 2; }
  .order-sm-3 {
    order: 3; }
  .order-sm-4 {
    order: 4; }
  .order-sm-5 {
    order: 5; }
  .order-sm-6 {
    order: 6; }
  .order-sm-7 {
    order: 7; }
  .order-sm-8 {
    order: 8; }
  .order-sm-9 {
    order: 9; }
  .order-sm-10 {
    order: 10; }
  .order-sm-11 {
    order: 11; }
  .order-sm-12 {
    order: 12; }
  .offset-sm-0 {
    margin-left: 0; }
  .offset-sm-1 {
    margin-left: 8.33333%; }
  .offset-sm-2 {
    margin-left: 16.66667%; }
  .offset-sm-3 {
    margin-left: 25%; }
  .offset-sm-4 {
    margin-left: 33.33333%; }
  .offset-sm-5 {
    margin-left: 41.66667%; }
  .offset-sm-6 {
    margin-left: 50%; }
  .offset-sm-7 {
    margin-left: 58.33333%; }
  .offset-sm-8 {
    margin-left: 66.66667%; }
  .offset-sm-9 {
    margin-left: 75%; }
  .offset-sm-10 {
    margin-left: 83.33333%; }
  .offset-sm-11 {
    margin-left: 91.66667%; } }

@media (min-width: 768px) {
  .col-md {
    flex-basis: 0;
    flex-grow: 1;
    max-width: 100%; }
  .col-md-auto {
    flex: 0 0 auto;
    width: auto;
    max-width: none; }
  .col-md-1 {
    flex: 0 0 8.33333%;
    max-width: 8.33333%; }
  .col-md-2 {
    flex: 0 0 16.66667%;
    max-width: 16.66667%; }
  .col-md-3 {
    flex: 0 0 25%;
    max-width: 25%; }
  .col-md-4 {
    flex: 0 0 33.33333%;
    max-width: 33.33333%; }
  .col-md-5 {
    flex: 0 0 41.66667%;
    max-width: 41.66667%; }
  .col-md-6 {
    flex: 0 0 50%;
    max-width: 50%; }
  .col-md-7 {
    flex: 0 0 58.33333%;
    max-width: 58.33333%; }
  .col-md-8 {
    flex: 0 0 66.66667%;
    max-width: 66.66667%; }
  .col-md-9 {
    flex: 0 0 75%;
    max-width: 75%; }
  .col-md-10 {
    flex: 0 0 83.33333%;
    max-width: 83.33333%; }
  .col-md-11 {
    flex: 0 0 91.66667%;
    max-width: 91.66667%; }
  .col-md-12 {
    flex: 0 0 100%;
    max-width: 100%; }
  .order-md-first {
    order: -1; }
  .order-md-last {
    order: 13; }
  .order-md-0 {
    order: 0; }
  .order-md-1 {
    order: 1; }
  .order-md-2 {
    order: 2; }
  .order-md-3 {
    order: 3; }
  .order-md-4 {
    order: 4; }
  .order-md-5 {
    order: 5; }
  .order-md-6 {
    order: 6; }
  .order-md-7 {
    order: 7; }
  .order-md-8 {
    order: 8; }
  .order-md-9 {
    order: 9; }
  .order-md-10 {
    order: 10; }
  .order-md-11 {
    order: 11; }
  .order-md-12 {
    order: 12; }
  .offset-md-0 {
    margin-left: 0; }
  .offset-md-1 {
    margin-left: 8.33333%; }
  .offset-md-2 {
    margin-left: 16.66667%; }
  .offset-md-3 {
    margin-left: 25%; }
  .offset-md-4 {
    margin-left: 33.33333%; }
  .offset-md-5 {
    margin-left: 41.66667%; }
  .offset-md-6 {
    margin-left: 50%; }
  .offset-md-7 {
    margin-left: 58.33333%; }
  .offset-md-8 {
    margin-left: 66.66667%; }
  .offset-md-9 {
    margin-left: 75%; }
  .offset-md-10 {
    margin-left: 83.33333%; }
  .offset-md-11 {
    margin-left: 91.66667%; } }

@media (min-width: 992px) {
  .col-lg {
    flex-basis: 0;
    flex-grow: 1;
    max-width: 100%; }
  .col-lg-auto {
    flex: 0 0 auto;
    width: auto;
    max-width: none; }
  .col-lg-1 {
    flex: 0 0 8.33333%;
    max-width: 8.33333%; }
  .col-lg-2 {
    flex: 0 0 16.66667%;
    max-width: 16.66667%; }
  .col-lg-3 {
    flex: 0 0 25%;
    max-width: 25%; }
  .col-lg-4 {
    flex: 0 0 33.33333%;
    max-width: 33.33333%; }
  .col-lg-5 {
    flex: 0 0 41.66667%;
    max-width: 41.66667%; }
  .col-lg-6 {
    flex: 0 0 50%;
    max-width: 50%; }
  .col-lg-7 {
    flex: 0 0 58.33333%;
    max-width: 58.33333%; }
  .col-lg-8 {
    flex: 0 0 66.66667%;
    max-width: 66.66667%; }
  .col-lg-9 {
    flex: 0 0 75%;
    max-width: 75%; }
  .col-lg-10 {
    flex: 0 0 83.33333%;
    max-width: 83.33333%; }
  .col-lg-11 {
    flex: 0 0 91.66667%;
    max-width: 91.66667%; }
  .col-lg-12 {
    flex: 0 0 100%;
    max-width: 100%; }
  .order-lg-first {
    order: -1; }
  .order-lg-last {
    order: 13; }
  .order-lg-0 {
    order: 0; }
  .order-lg-1 {
    order: 1; }
  .order-lg-2 {
    order: 2; }
  .order-lg-3 {
    order: 3; }
  .order-lg-4 {
    order: 4; }
  .order-lg-5 {
    order: 5; }
  .order-lg-6 {
    order: 6; }
  .order-lg-7 {
    order: 7; }
  .order-lg-8 {
    order: 8; }
  .order-lg-9 {
    order: 9; }
  .order-lg-10 {
    order: 10; }
  .order-lg-11 {
    order: 11; }
  .order-lg-12 {
    order: 12; }
  .offset-lg-0 {
    margin-left: 0; }
  .offset-lg-1 {
    margin-left: 8.33333%; }
  .offset-lg-2 {
    margin-left: 16.66667%; }
  .offset-lg-3 {
    margin-left: 25%; }
  .offset-lg-4 {
    margin-left: 33.33333%; }
  .offset-lg-5 {
    margin-left: 41.66667%; }
  .offset-lg-6 {
    margin-left: 50%; }
  .offset-lg-7 {
    margin-left: 58.33333%; }
  .offset-lg-8 {
    margin-left: 66.66667%; }
  .offset-lg-9 {
    margin-left: 75%; }
  .offset-lg-10 {
    margin-left: 83.33333%; }
  .offset-lg-11 {
    margin-left: 91.66667%; } }

@media (min-width: 1200px) {
  .col-xl {
    flex-basis: 0;
    flex-grow: 1;
    max-width: 100%; }
  .col-xl-auto {
    flex: 0 0 auto;
    width: auto;
    max-width: none; }
  .col-xl-1 {
    flex: 0 0 8.33333%;
    max-width: 8.33333%; }
  .col-xl-2 {
    flex: 0 0 16.66667%;
    max-width: 16.66667%; }
  .col-xl-3 {
    flex: 0 0 25%;
    max-width: 25%; }
  .col-xl-4 {
    flex: 0 0 33.33333%;
    max-width: 33.33333%; }
  .col-xl-5 {
    flex: 0 0 41.66667%;
    max-width: 41.66667%; }
  .col-xl-6 {
    flex: 0 0 50%;
    max-width: 50%; }
  .col-xl-7 {
    flex: 0 0 58.33333%;
    max-width: 58.33333%; }
  .col-xl-8 {
    flex: 0 0 66.66667%;
    max-width: 66.66667%; }
  .col-xl-9 {
    flex: 0 0 75%;
    max-width: 75%; }
  .col-xl-10 {
    flex: 0 0 83.33333%;
    max-width: 83.33333%; }
  .col-xl-11 {
    flex: 0 0 91.66667%;
    max-width: 91.66667%; }
  .col-xl-12 {
    flex: 0 0 100%;
    max-width: 100%; }
  .order-xl-first {
    order: -1; }
  .order-xl-last {
    order: 13; }
  .order-xl-0 {
    order: 0; }
  .order-xl-1 {
    order: 1; }
  .order-xl-2 {
    order: 2; }
  .order-xl-3 {
    order: 3; }
  .order-xl-4 {
    order: 4; }
  .order-xl-5 {
    order: 5; }
  .order-xl-6 {
    order: 6; }
  .order-xl-7 {
    order: 7; }
  .order-xl-8 {
    order: 8; }
  .order-xl-9 {
    order: 9; }
  .order-xl-10 {
    order: 10; }
  .order-xl-11 {
    order: 11; }
  .order-xl-12 {
    order: 12; }
  .offset-xl-0 {
    margin-left: 0; }
  .offset-xl-1 {
    margin-left: 8.33333%; }
  .offset-xl-2 {
    margin-left: 16.66667%; }
  .offset-xl-3 {
    margin-left: 25%; }
  .offset-xl-4 {
    margin-left: 33.33333%; }
  .offset-xl-5 {
    margin-left: 41.66667%; }
  .offset-xl-6 {
    margin-left: 50%; }
  .offset-xl-7 {
    margin-left: 58.33333%; }
  .offset-xl-8 {
    margin-left: 66.66667%; }
  .offset-xl-9 {
    margin-left: 75%; }
  .offset-xl-10 {
    margin-left: 83.33333%; }
  .offset-xl-11 {
    margin-left: 91.66667%; } }

.table {
  width: 100%;
  margin-bottom: 1rem;
  background-color: transparent; }
  .table th,
  .table td {
    padding: 0.75rem;
    vertical-align: top;
    border-top: 1px solid #dee2e6; }
  .table thead th {
    vertical-align: bottom;
    border-bottom: 2px solid #dee2e6; }
  .table tbody + tbody {
    border-top: 2px solid #dee2e6; }
  .table .table {
    background-color: #fff; }

.table-sm th,
.table-sm td {
  padding: 0.3rem; }

.table-bordered {
  border: 1px solid #dee2e6; }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #dee2e6; }
  .table-bordered thead th,
  .table-bordered thead td {
    border-bottom-width: 2px; }

.table-borderless th,
.table-borderless td,
.table-borderless thead th,
.table-borderless tbody + tbody {
  border: 0; }

.table-striped tbody tr:nth-of-type(odd) {
  background-color: rgba(0, 0, 0, 0.05); }

.table-hover tbody tr:hover {
  background-color: rgba(0, 0, 0, 0.075); }

.table-primary,
.table-primary > th,
.table-primary > td {
  background-color: #bcc3cd; }

.table-hover .table-primary:hover {
  background-color: #adb6c2; }
  .table-hover .table-primary:hover > td,
  .table-hover .table-primary:hover > th {
    background-color: #adb6c2; }

.table-secondary,
.table-secondary > th,
.table-secondary > td {
  background-color: #c5f0e4; }

.table-hover .table-secondary:hover {
  background-color: #b1ebdb; }
  .table-hover .table-secondary:hover > td,
  .table-hover .table-secondary:hover > th {
    background-color: #b1ebdb; }

.table-success,
.table-success > th,
.table-success > td {
  background-color: #c1f0e2; }

.table-hover .table-success:hover {
  background-color: #acebd8; }
  .table-hover .table-success:hover > td,
  .table-hover .table-success:hover > th {
    background-color: #acebd8; }

.table-info,
.table-info > th,
.table-info > td {
  background-color: #bee5eb; }

.table-hover .table-info:hover {
  background-color: #abdde5; }
  .table-hover .table-info:hover > td,
  .table-hover .table-info:hover > th {
    background-color: #abdde5; }

.table-warning,
.table-warning > th,
.table-warning > td {
  background-color: #ffeeba; }

.table-hover .table-warning:hover {
  background-color: #ffe8a1; }
  .table-hover .table-warning:hover > td,
  .table-hover .table-warning:hover > th {
    background-color: #ffe8a1; }

.table-danger,
.table-danger > th,
.table-danger > td {
  background-color: #f9cbcb; }

.table-hover .table-danger:hover {
  background-color: #f6b4b4; }
  .table-hover .table-danger:hover > td,
  .table-hover .table-danger:hover > th {
    background-color: #f6b4b4; }

.table-light,
.table-light > th,
.table-light > td {
  background-color: #fdfdfe; }

.table-hover .table-light:hover {
  background-color: #ececf6; }
  .table-hover .table-light:hover > td,
  .table-hover .table-light:hover > th {
    background-color: #ececf6; }

.table-dark,
.table-dark > th,
.table-dark > td {
  background-color: #c6c8ca; }

.table-hover .table-dark:hover {
  background-color: #b9bbbe; }
  .table-hover .table-dark:hover > td,
  .table-hover .table-dark:hover > th {
    background-color: #b9bbbe; }

.table-active,
.table-active > th,
.table-active > td {
  background-color: rgba(0, 0, 0, 0.075); }

.table-hover .table-active:hover {
  background-color: rgba(0, 0, 0, 0.075); }
  .table-hover .table-active:hover > td,
  .table-hover .table-active:hover > th {
    background-color: rgba(0, 0, 0, 0.075); }

.table .thead-dark th {
  color: #fff;
  background-color: #212529;
  border-color: #32383e; }

.table .thead-light th {
  color: #495057;
  background-color: #e9ecef;
  border-color: #dee2e6; }

.table-dark {
  color: #fff;
  background-color: #212529; }
  .table-dark th,
  .table-dark td,
  .table-dark thead th {
    border-color: #32383e; }
  .table-dark.table-bordered {
    border: 0; }
  .table-dark.table-striped tbody tr:nth-of-type(odd) {
    background-color: rgba(255, 255, 255, 0.05); }
  .table-dark.table-hover tbody tr:hover {
    background-color: rgba(255, 255, 255, 0.075); }

@media (max-width: 575.98px) {
  .table-responsive-sm {
    display: block;
    width: 100%;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    -ms-overflow-style: -ms-autohiding-scrollbar; }
    .table-responsive-sm > .table-bordered {
      border: 0; } }

@media (max-width: 767.98px) {
  .table-responsive-md {
    display: block;
    width: 100%;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    -ms-overflow-style: -ms-autohiding-scrollbar; }
    .table-responsive-md > .table-bordered {
      border: 0; } }

@media (max-width: 991.98px) {
  .table-responsive-lg {
    display: block;
    width: 100%;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    -ms-overflow-style: -ms-autohiding-scrollbar; }
    .table-responsive-lg > .table-bordered {
      border: 0; } }

@media (max-width: 1199.98px) {
  .table-responsive-xl {
    display: block;
    width: 100%;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    -ms-overflow-style: -ms-autohiding-scrollbar; }
    .table-responsive-xl > .table-bordered {
      border: 0; } }

.table-responsive {
  display: block;
  width: 100%;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  -ms-overflow-style: -ms-autohiding-scrollbar; }
  .table-responsive > .table-bordered {
    border: 0; }

.form-control {
  display: block;
  width: 100%;
  height: calc(2.25rem + 2px);
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  line-height: 1.5;
  color: #495057;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ced4da;
  border-radius: 0.25rem;
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out; }
  @media screen and (prefers-reduced-motion: reduce) {
    .form-control {
      transition: none; } }
  .form-control::-ms-expand {
    background-color: transparent;
    border: 0; }
  .form-control:focus {
    color: #495057;
    background-color: #fff;
    border-color: #265eb8;
    outline: 0;
    box-shadow: 0 0 0 0.2rem rgba(16, 40, 78, 0.25); }
  .form-control::placeholder {
    color: #6c757d;
    opacity: 1; }
  .form-control:disabled, .form-control[readonly] {
    background-color: #e9ecef;
    opacity: 1; }

select.form-control:focus::-ms-value {
  color: #495057;
  background-color: #fff; }

.form-control-file,
.form-control-range {
  display: block;
  width: 100%; }

.col-form-label {
  padding-top: calc(0.375rem + 1px);
  padding-bottom: calc(0.375rem + 1px);
  margin-bottom: 0;
  font-size: inherit;
  line-height: 1.5; }

.col-form-label-lg {
  padding-top: calc(0.5rem + 1px);
  padding-bottom: calc(0.5rem + 1px);
  font-size: 1.25rem;
  line-height: 1.5; }

.col-form-label-sm {
  padding-top: calc(0.25rem + 1px);
  padding-bottom: calc(0.25rem + 1px);
  font-size: 0.875rem;
  line-height: 1.5; }

.form-control-plaintext {
  display: block;
  width: 100%;
  padding-top: 0.375rem;
  padding-bottom: 0.375rem;
  margin-bottom: 0;
  line-height: 1.5;
  color: #212529;
  background-color: transparent;
  border: solid transparent;
  border-width: 1px 0; }
  .form-control-plaintext.form-control-sm, .form-control-plaintext.form-control-lg {
    padding-right: 0;
    padding-left: 0; }

.form-control-sm {
  height: calc( 1.8125rem + 2px);
  padding: 0.25rem 0.5rem;
  font-size: 0.875rem;
  line-height: 1.5;
  border-radius: 0.2rem; }

.form-control-lg {
  height: calc( 2.875rem + 2px);
  padding: 0.5rem 1rem;
  font-size: 1.25rem;
  line-height: 1.5;
  border-radius: 0.3rem; }

select.form-control[size], select.form-control[multiple] {
  height: auto; }

textarea.form-control {
  height: auto; }

.form-group {
  margin-bottom: 1rem; }

.form-text {
  display: block;
  margin-top: 0.25rem; }

.form-row {
  display: flex;
  flex-wrap: wrap;
  margin-right: -5px;
  margin-left: -5px; }
  .form-row > .col,
  .form-row > [class*="col-"] {
    padding-right: 5px;
    padding-left: 5px; }

.form-check {
  position: relative;
  display: block;
  padding-left: 1.25rem; }

.form-check-input {
  position: absolute;
  margin-top: 0.3rem;
  margin-left: -1.25rem; }
  .form-check-input:disabled ~ .form-check-label {
    color: #6c757d; }

.form-check-label {
  margin-bottom: 0; }

.form-check-inline {
  display: inline-flex;
  align-items: center;
  padding-left: 0;
  margin-right: 0.75rem; }
  .form-check-inline .form-check-input {
    position: static;
    margin-top: 0;
    margin-right: 0.3125rem;
    margin-left: 0; }

.valid-feedback {
  display: none;
  width: 100%;
  margin-top: 0.25rem;
  font-size: 80%;
  color: #20c997; }

.valid-tooltip {
  position: absolute;
  top: 100%;
  z-index: 5;
  display: none;
  max-width: 100%;
  padding: 0.25rem 0.5rem;
  margin-top: .1rem;
  font-size: 0.875rem;
  line-height: 1.5;
  color: #fff;
  background-color: rgba(32, 201, 151, 0.9);
  border-radius: 0.25rem; }

.was-validated .form-control:valid, .form-control.is-valid, .was-validated
.custom-select:valid,
.custom-select.is-valid {
  border-color: #20c997; }
  .was-validated .form-control:valid:focus, .form-control.is-valid:focus, .was-validated
  .custom-select:valid:focus,
  .custom-select.is-valid:focus {
    border-color: #20c997;
    box-shadow: 0 0 0 0.2rem rgba(32, 201, 151, 0.25); }
  .was-validated .form-control:valid ~ .valid-feedback,
  .was-validated .form-control:valid ~ .valid-tooltip, .form-control.is-valid ~ .valid-feedback,
  .form-control.is-valid ~ .valid-tooltip, .was-validated
  .custom-select:valid ~ .valid-feedback,
  .was-validated
  .custom-select:valid ~ .valid-tooltip,
  .custom-select.is-valid ~ .valid-feedback,
  .custom-select.is-valid ~ .valid-tooltip {
    display: block; }

.was-validated .form-control-file:valid ~ .valid-feedback,
.was-validated .form-control-file:valid ~ .valid-tooltip, .form-control-file.is-valid ~ .valid-feedback,
.form-control-file.is-valid ~ .valid-tooltip {
  display: block; }

.was-validated .form-check-input:valid ~ .form-check-label, .form-check-input.is-valid ~ .form-check-label {
  color: #20c997; }

.was-validated .form-check-input:valid ~ .valid-feedback,
.was-validated .form-check-input:valid ~ .valid-tooltip, .form-check-input.is-valid ~ .valid-feedback,
.form-check-input.is-valid ~ .valid-tooltip {
  display: block; }

.was-validated .custom-control-input:valid ~ .custom-control-label, .custom-control-input.is-valid ~ .custom-control-label {
  color: #20c997; }
  .was-validated .custom-control-input:valid ~ .custom-control-label::before, .custom-control-input.is-valid ~ .custom-control-label::before {
    background-color: #7eeaca; }

.was-validated .custom-control-input:valid ~ .valid-feedback,
.was-validated .custom-control-input:valid ~ .valid-tooltip, .custom-control-input.is-valid ~ .valid-feedback,
.custom-control-input.is-valid ~ .valid-tooltip {
  display: block; }

.was-validated .custom-control-input:valid:checked ~ .custom-control-label::before, .custom-control-input.is-valid:checked ~ .custom-control-label::before {
  background-color: #3ce0af; }

.was-validated .custom-control-input:valid:focus ~ .custom-control-label::before, .custom-control-input.is-valid:focus ~ .custom-control-label::before {
  box-shadow: 0 0 0 1px #fff, 0 0 0 0.2rem rgba(32, 201, 151, 0.25); }

.was-validated .custom-file-input:valid ~ .custom-file-label, .custom-file-input.is-valid ~ .custom-file-label {
  border-color: #20c997; }
  .was-validated .custom-file-input:valid ~ .custom-file-label::after, .custom-file-input.is-valid ~ .custom-file-label::after {
    border-color: inherit; }

.was-validated .custom-file-input:valid ~ .valid-feedback,
.was-validated .custom-file-input:valid ~ .valid-tooltip, .custom-file-input.is-valid ~ .valid-feedback,
.custom-file-input.is-valid ~ .valid-tooltip {
  display: block; }

.was-validated .custom-file-input:valid:focus ~ .custom-file-label, .custom-file-input.is-valid:focus ~ .custom-file-label {
  box-shadow: 0 0 0 0.2rem rgba(32, 201, 151, 0.25); }

.invalid-feedback {
  display: none;
  width: 100%;
  margin-top: 0.25rem;
  font-size: 80%;
  color: #e94646; }

.invalid-tooltip {
  position: absolute;
  top: 100%;
  z-index: 5;
  display: none;
  max-width: 100%;
  padding: 0.25rem 0.5rem;
  margin-top: .1rem;
  font-size: 0.875rem;
  line-height: 1.5;
  color: #fff;
  background-color: rgba(233, 70, 70, 0.9);
  border-radius: 0.25rem; }

.was-validated .form-control:invalid, .form-control.is-invalid, .was-validated
.custom-select:invalid,
.custom-select.is-invalid {
  border-color: #e94646; }
  .was-validated .form-control:invalid:focus, .form-control.is-invalid:focus, .was-validated
  .custom-select:invalid:focus,
  .custom-select.is-invalid:focus {
    border-color: #e94646;
    box-shadow: 0 0 0 0.2rem rgba(233, 70, 70, 0.25); }
  .was-validated .form-control:invalid ~ .invalid-feedback,
  .was-validated .form-control:invalid ~ .invalid-tooltip, .form-control.is-invalid ~ .invalid-feedback,
  .form-control.is-invalid ~ .invalid-tooltip, .was-validated
  .custom-select:invalid ~ .invalid-feedback,
  .was-validated
  .custom-select:invalid ~ .invalid-tooltip,
  .custom-select.is-invalid ~ .invalid-feedback,
  .custom-select.is-invalid ~ .invalid-tooltip {
    display: block; }

.was-validated .form-control-file:invalid ~ .invalid-feedback,
.was-validated .form-control-file:invalid ~ .invalid-tooltip, .form-control-file.is-invalid ~ .invalid-feedback,
.form-control-file.is-invalid ~ .invalid-tooltip {
  display: block; }

.was-validated .form-check-input:invalid ~ .form-check-label, .form-check-input.is-invalid ~ .form-check-label {
  color: #e94646; }

.was-validated .form-check-input:invalid ~ .invalid-feedback,
.was-validated .form-check-input:invalid ~ .invalid-tooltip, .form-check-input.is-invalid ~ .invalid-feedback,
.form-check-input.is-invalid ~ .invalid-tooltip {
  display: block; }

.was-validated .custom-control-input:invalid ~ .custom-control-label, .custom-control-input.is-invalid ~ .custom-control-label {
  color: #e94646; }
  .was-validated .custom-control-input:invalid ~ .custom-control-label::before, .custom-control-input.is-invalid ~ .custom-control-label::before {
    background-color: #f7b8b8; }

.was-validated .custom-control-input:invalid ~ .invalid-feedback,
.was-validated .custom-control-input:invalid ~ .invalid-tooltip, .custom-control-input.is-invalid ~ .invalid-feedback,
.custom-control-input.is-invalid ~ .invalid-tooltip {
  display: block; }

.was-validated .custom-control-input:invalid:checked ~ .custom-control-label::before, .custom-control-input.is-invalid:checked ~ .custom-control-label::before {
  background-color: #ee7474; }

.was-validated .custom-control-input:invalid:focus ~ .custom-control-label::before, .custom-control-input.is-invalid:focus ~ .custom-control-label::before {
  box-shadow: 0 0 0 1px #fff, 0 0 0 0.2rem rgba(233, 70, 70, 0.25); }

.was-validated .custom-file-input:invalid ~ .custom-file-label, .custom-file-input.is-invalid ~ .custom-file-label {
  border-color: #e94646; }
  .was-validated .custom-file-input:invalid ~ .custom-file-label::after, .custom-file-input.is-invalid ~ .custom-file-label::after {
    border-color: inherit; }

.was-validated .custom-file-input:invalid ~ .invalid-feedback,
.was-validated .custom-file-input:invalid ~ .invalid-tooltip, .custom-file-input.is-invalid ~ .invalid-feedback,
.custom-file-input.is-invalid ~ .invalid-tooltip {
  display: block; }

.was-validated .custom-file-input:invalid:focus ~ .custom-file-label, .custom-file-input.is-invalid:focus ~ .custom-file-label {
  box-shadow: 0 0 0 0.2rem rgba(233, 70, 70, 0.25); }

.form-inline {
  display: flex;
  flex-flow: row wrap;
  align-items: center; }
  .form-inline .form-check {
    width: 100%; }
  @media (min-width: 576px) {
    .form-inline label {
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 0; }
    .form-inline .form-group {
      display: flex;
      flex: 0 0 auto;
      flex-flow: row wrap;
      align-items: center;
      margin-bottom: 0; }
    .form-inline .form-control {
      display: inline-block;
      width: auto;
      vertical-align: middle; }
    .form-inline .form-control-plaintext {
      display: inline-block; }
    .form-inline .input-group,
    .form-inline .custom-select {
      width: auto; }
    .form-inline .form-check {
      display: flex;
      align-items: center;
      justify-content: center;
      width: auto;
      padding-left: 0; }
    .form-inline .form-check-input {
      position: relative;
      margin-top: 0;
      margin-right: 0.25rem;
      margin-left: 0; }
    .form-inline .custom-control {
      align-items: center;
      justify-content: center; }
    .form-inline .custom-control-label {
      margin-bottom: 0; } }

.btn {
  display: inline-block;
  font-weight: 400;
  text-align: center;
  white-space: nowrap;
  vertical-align: middle;
  user-select: none;
  border: 1px solid transparent;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  line-height: 1.5;
  border-radius: 0.25rem;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out; }
  @media screen and (prefers-reduced-motion: reduce) {
    .btn {
      transition: none; } }
  .btn:hover, .btn:focus {
    text-decoration: none; }
  .btn:focus, .btn.focus {
    outline: 0;
    box-shadow: 0 0 0 0.2rem rgba(16, 40, 78, 0.25); }
  .btn.disabled, .btn:disabled {
    opacity: 0.65; }
  .btn:not(:disabled):not(.disabled) {
    cursor: pointer; }

a.btn.disabled,
fieldset:disabled a.btn {
  pointer-events: none; }

.btn-primary {
  color: #fff;
  background-color: #10284e;
  border-color: #10284e; }
  .btn-primary:hover {
    color: #fff;
    background-color: #09182e;
    border-color: #071224; }
  .btn-primary:focus, .btn-primary.focus {
    box-shadow: 0 0 0 0.2rem rgba(16, 40, 78, 0.5); }
  .btn-primary.disabled, .btn-primary:disabled {
    color: #fff;
    background-color: #10284e;
    border-color: #10284e; }
  .btn-primary:not(:disabled):not(.disabled):active, .btn-primary:not(:disabled):not(.disabled).active,
  .show > .btn-primary.dropdown-toggle {
    color: #fff;
    background-color: #071224;
    border-color: #050d19; }
    .btn-primary:not(:disabled):not(.disabled):active:focus, .btn-primary:not(:disabled):not(.disabled).active:focus,
    .show > .btn-primary.dropdown-toggle:focus {
      box-shadow: 0 0 0 0.2rem rgba(16, 40, 78, 0.5); }

.btn-secondary {
  color: #212529;
  background-color: #30caa0;
  border-color: #30caa0; }
  .btn-secondary:hover {
    color: #fff;
    background-color: #29ab88;
    border-color: #26a17f; }
  .btn-secondary:focus, .btn-secondary.focus {
    box-shadow: 0 0 0 0.2rem rgba(48, 202, 160, 0.5); }
  .btn-secondary.disabled, .btn-secondary:disabled {
    color: #212529;
    background-color: #30caa0;
    border-color: #30caa0; }
  .btn-secondary:not(:disabled):not(.disabled):active, .btn-secondary:not(:disabled):not(.disabled).active,
  .show > .btn-secondary.dropdown-toggle {
    color: #fff;
    background-color: #26a17f;
    border-color: #249677; }
    .btn-secondary:not(:disabled):not(.disabled):active:focus, .btn-secondary:not(:disabled):not(.disabled).active:focus,
    .show > .btn-secondary.dropdown-toggle:focus {
      box-shadow: 0 0 0 0.2rem rgba(48, 202, 160, 0.5); }

.btn-success {
  color: #fff;
  background-color: #20c997;
  border-color: #20c997; }
  .btn-success:hover {
    color: #fff;
    background-color: #1ba87e;
    border-color: #199d76; }
  .btn-success:focus, .btn-success.focus {
    box-shadow: 0 0 0 0.2rem rgba(32, 201, 151, 0.5); }
  .btn-success.disabled, .btn-success:disabled {
    color: #fff;
    background-color: #20c997;
    border-color: #20c997; }
  .btn-success:not(:disabled):not(.disabled):active, .btn-success:not(:disabled):not(.disabled).active,
  .show > .btn-success.dropdown-toggle {
    color: #fff;
    background-color: #199d76;
    border-color: #17926e; }
    .btn-success:not(:disabled):not(.disabled):active:focus, .btn-success:not(:disabled):not(.disabled).active:focus,
    .show > .btn-success.dropdown-toggle:focus {
      box-shadow: 0 0 0 0.2rem rgba(32, 201, 151, 0.5); }

.btn-info {
  color: #fff;
  background-color: #17a2b8;
  border-color: #17a2b8; }
  .btn-info:hover {
    color: #fff;
    background-color: #138496;
    border-color: #117a8b; }
  .btn-info:focus, .btn-info.focus {
    box-shadow: 0 0 0 0.2rem rgba(23, 162, 184, 0.5); }
  .btn-info.disabled, .btn-info:disabled {
    color: #fff;
    background-color: #17a2b8;
    border-color: #17a2b8; }
  .btn-info:not(:disabled):not(.disabled):active, .btn-info:not(:disabled):not(.disabled).active,
  .show > .btn-info.dropdown-toggle {
    color: #fff;
    background-color: #117a8b;
    border-color: #10707f; }
    .btn-info:not(:disabled):not(.disabled):active:focus, .btn-info:not(:disabled):not(.disabled).active:focus,
    .show > .btn-info.dropdown-toggle:focus {
      box-shadow: 0 0 0 0.2rem rgba(23, 162, 184, 0.5); }

.btn-warning {
  color: #212529;
  background-color: #ffc107;
  border-color: #ffc107; }
  .btn-warning:hover {
    color: #212529;
    background-color: #e0a800;
    border-color: #d39e00; }
  .btn-warning:focus, .btn-warning.focus {
    box-shadow: 0 0 0 0.2rem rgba(255, 193, 7, 0.5); }
  .btn-warning.disabled, .btn-warning:disabled {
    color: #212529;
    background-color: #ffc107;
    border-color: #ffc107; }
  .btn-warning:not(:disabled):not(.disabled):active, .btn-warning:not(:disabled):not(.disabled).active,
  .show > .btn-warning.dropdown-toggle {
    color: #212529;
    background-color: #d39e00;
    border-color: #c69500; }
    .btn-warning:not(:disabled):not(.disabled):active:focus, .btn-warning:not(:disabled):not(.disabled).active:focus,
    .show > .btn-warning.dropdown-toggle:focus {
      box-shadow: 0 0 0 0.2rem rgba(255, 193, 7, 0.5); }

.btn-danger {
  color: #fff;
  background-color: #e94646;
  border-color: #e94646; }
  .btn-danger:hover {
    color: #fff;
    background-color: #e52424;
    border-color: #e11b1b; }
  .btn-danger:focus, .btn-danger.focus {
    box-shadow: 0 0 0 0.2rem rgba(233, 70, 70, 0.5); }
  .btn-danger.disabled, .btn-danger:disabled {
    color: #fff;
    background-color: #e94646;
    border-color: #e94646; }
  .btn-danger:not(:disabled):not(.disabled):active, .btn-danger:not(:disabled):not(.disabled).active,
  .show > .btn-danger.dropdown-toggle {
    color: #fff;
    background-color: #e11b1b;
    border-color: #d61919; }
    .btn-danger:not(:disabled):not(.disabled):active:focus, .btn-danger:not(:disabled):not(.disabled).active:focus,
    .show > .btn-danger.dropdown-toggle:focus {
      box-shadow: 0 0 0 0.2rem rgba(233, 70, 70, 0.5); }

.btn-light {
  color: #212529;
  background-color: #f8f9fa;
  border-color: #f8f9fa; }
  .btn-light:hover {
    color: #212529;
    background-color: #e2e6ea;
    border-color: #dae0e5; }
  .btn-light:focus, .btn-light.focus {
    box-shadow: 0 0 0 0.2rem rgba(248, 249, 250, 0.5); }
  .btn-light.disabled, .btn-light:disabled {
    color: #212529;
    background-color: #f8f9fa;
    border-color: #f8f9fa; }
  .btn-light:not(:disabled):not(.disabled):active, .btn-light:not(:disabled):not(.disabled).active,
  .show > .btn-light.dropdown-toggle {
    color: #212529;
    background-color: #dae0e5;
    border-color: #d3d9df; }
    .btn-light:not(:disabled):not(.disabled):active:focus, .btn-light:not(:disabled):not(.disabled).active:focus,
    .show > .btn-light.dropdown-toggle:focus {
      box-shadow: 0 0 0 0.2rem rgba(248, 249, 250, 0.5); }

.btn-dark {
  color: #fff;
  background-color: #343a40;
  border-color: #343a40; }
  .btn-dark:hover {
    color: #fff;
    background-color: #23272b;
    border-color: #1d2124; }
  .btn-dark:focus, .btn-dark.focus {
    box-shadow: 0 0 0 0.2rem rgba(52, 58, 64, 0.5); }
  .btn-dark.disabled, .btn-dark:disabled {
    color: #fff;
    background-color: #343a40;
    border-color: #343a40; }
  .btn-dark:not(:disabled):not(.disabled):active, .btn-dark:not(:disabled):not(.disabled).active,
  .show > .btn-dark.dropdown-toggle {
    color: #fff;
    background-color: #1d2124;
    border-color: #171a1d; }
    .btn-dark:not(:disabled):not(.disabled):active:focus, .btn-dark:not(:disabled):not(.disabled).active:focus,
    .show > .btn-dark.dropdown-toggle:focus {
      box-shadow: 0 0 0 0.2rem rgba(52, 58, 64, 0.5); }

.btn-outline-primary {
  color: #10284e;
  background-color: transparent;
  background-image: none;
  border-color: #10284e; }
  .btn-outline-primary:hover {
    color: #fff;
    background-color: #10284e;
    border-color: #10284e; }
  .btn-outline-primary:focus, .btn-outline-primary.focus {
    box-shadow: 0 0 0 0.2rem rgba(16, 40, 78, 0.5); }
  .btn-outline-primary.disabled, .btn-outline-primary:disabled {
    color: #10284e;
    background-color: transparent; }
  .btn-outline-primary:not(:disabled):not(.disabled):active, .btn-outline-primary:not(:disabled):not(.disabled).active,
  .show > .btn-outline-primary.dropdown-toggle {
    color: #fff;
    background-color: #10284e;
    border-color: #10284e; }
    .btn-outline-primary:not(:disabled):not(.disabled):active:focus, .btn-outline-primary:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-primary.dropdown-toggle:focus {
      box-shadow: 0 0 0 0.2rem rgba(16, 40, 78, 0.5); }

.btn-outline-secondary {
  color: #30caa0;
  background-color: transparent;
  background-image: none;
  border-color: #30caa0; }
  .btn-outline-secondary:hover {
    color: #212529;
    background-color: #30caa0;
    border-color: #30caa0; }
  .btn-outline-secondary:focus, .btn-outline-secondary.focus {
    box-shadow: 0 0 0 0.2rem rgba(48, 202, 160, 0.5); }
  .btn-outline-secondary.disabled, .btn-outline-secondary:disabled {
    color: #30caa0;
    background-color: transparent; }
  .btn-outline-secondary:not(:disabled):not(.disabled):active, .btn-outline-secondary:not(:disabled):not(.disabled).active,
  .show > .btn-outline-secondary.dropdown-toggle {
    color: #212529;
    background-color: #30caa0;
    border-color: #30caa0; }
    .btn-outline-secondary:not(:disabled):not(.disabled):active:focus, .btn-outline-secondary:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-secondary.dropdown-toggle:focus {
      box-shadow: 0 0 0 0.2rem rgba(48, 202, 160, 0.5); }

.btn-outline-success {
  color: #20c997;
  background-color: transparent;
  background-image: none;
  border-color: #20c997; }
  .btn-outline-success:hover {
    color: #fff;
    background-color: #20c997;
    border-color: #20c997; }
  .btn-outline-success:focus, .btn-outline-success.focus {
    box-shadow: 0 0 0 0.2rem rgba(32, 201, 151, 0.5); }
  .btn-outline-success.disabled, .btn-outline-success:disabled {
    color: #20c997;
    background-color: transparent; }
  .btn-outline-success:not(:disabled):not(.disabled):active, .btn-outline-success:not(:disabled):not(.disabled).active,
  .show > .btn-outline-success.dropdown-toggle {
    color: #fff;
    background-color: #20c997;
    border-color: #20c997; }
    .btn-outline-success:not(:disabled):not(.disabled):active:focus, .btn-outline-success:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-success.dropdown-toggle:focus {
      box-shadow: 0 0 0 0.2rem rgba(32, 201, 151, 0.5); }

.btn-outline-info {
  color: #17a2b8;
  background-color: transparent;
  background-image: none;
  border-color: #17a2b8; }
  .btn-outline-info:hover {
    color: #fff;
    background-color: #17a2b8;
    border-color: #17a2b8; }
  .btn-outline-info:focus, .btn-outline-info.focus {
    box-shadow: 0 0 0 0.2rem rgba(23, 162, 184, 0.5); }
  .btn-outline-info.disabled, .btn-outline-info:disabled {
    color: #17a2b8;
    background-color: transparent; }
  .btn-outline-info:not(:disabled):not(.disabled):active, .btn-outline-info:not(:disabled):not(.disabled).active,
  .show > .btn-outline-info.dropdown-toggle {
    color: #fff;
    background-color: #17a2b8;
    border-color: #17a2b8; }
    .btn-outline-info:not(:disabled):not(.disabled):active:focus, .btn-outline-info:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-info.dropdown-toggle:focus {
      box-shadow: 0 0 0 0.2rem rgba(23, 162, 184, 0.5); }

.btn-outline-warning {
  color: #ffc107;
  background-color: transparent;
  background-image: none;
  border-color: #ffc107; }
  .btn-outline-warning:hover {
    color: #212529;
    background-color: #ffc107;
    border-color: #ffc107; }
  .btn-outline-warning:focus, .btn-outline-warning.focus {
    box-shadow: 0 0 0 0.2rem rgba(255, 193, 7, 0.5); }
  .btn-outline-warning.disabled, .btn-outline-warning:disabled {
    color: #ffc107;
    background-color: transparent; }
  .btn-outline-warning:not(:disabled):not(.disabled):active, .btn-outline-warning:not(:disabled):not(.disabled).active,
  .show > .btn-outline-warning.dropdown-toggle {
    color: #212529;
    background-color: #ffc107;
    border-color: #ffc107; }
    .btn-outline-warning:not(:disabled):not(.disabled):active:focus, .btn-outline-warning:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-warning.dropdown-toggle:focus {
      box-shadow: 0 0 0 0.2rem rgba(255, 193, 7, 0.5); }

.btn-outline-danger {
  color: #e94646;
  background-color: transparent;
  background-image: none;
  border-color: #e94646; }
  .btn-outline-danger:hover {
    color: #fff;
    background-color: #e94646;
    border-color: #e94646; }
  .btn-outline-danger:focus, .btn-outline-danger.focus {
    box-shadow: 0 0 0 0.2rem rgba(233, 70, 70, 0.5); }
  .btn-outline-danger.disabled, .btn-outline-danger:disabled {
    color: #e94646;
    background-color: transparent; }
  .btn-outline-danger:not(:disabled):not(.disabled):active, .btn-outline-danger:not(:disabled):not(.disabled).active,
  .show > .btn-outline-danger.dropdown-toggle {
    color: #fff;
    background-color: #e94646;
    border-color: #e94646; }
    .btn-outline-danger:not(:disabled):not(.disabled):active:focus, .btn-outline-danger:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-danger.dropdown-toggle:focus {
      box-shadow: 0 0 0 0.2rem rgba(233, 70, 70, 0.5); }

.btn-outline-light {
  color: #f8f9fa;
  background-color: transparent;
  background-image: none;
  border-color: #f8f9fa; }
  .btn-outline-light:hover {
    color: #212529;
    background-color: #f8f9fa;
    border-color: #f8f9fa; }
  .btn-outline-light:focus, .btn-outline-light.focus {
    box-shadow: 0 0 0 0.2rem rgba(248, 249, 250, 0.5); }
  .btn-outline-light.disabled, .btn-outline-light:disabled {
    color: #f8f9fa;
    background-color: transparent; }
  .btn-outline-light:not(:disabled):not(.disabled):active, .btn-outline-light:not(:disabled):not(.disabled).active,
  .show > .btn-outline-light.dropdown-toggle {
    color: #212529;
    background-color: #f8f9fa;
    border-color: #f8f9fa; }
    .btn-outline-light:not(:disabled):not(.disabled):active:focus, .btn-outline-light:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-light.dropdown-toggle:focus {
      box-shadow: 0 0 0 0.2rem rgba(248, 249, 250, 0.5); }

.btn-outline-dark {
  color: #343a40;
  background-color: transparent;
  background-image: none;
  border-color: #343a40; }
  .btn-outline-dark:hover {
    color: #fff;
    background-color: #343a40;
    border-color: #343a40; }
  .btn-outline-dark:focus, .btn-outline-dark.focus {
    box-shadow: 0 0 0 0.2rem rgba(52, 58, 64, 0.5); }
  .btn-outline-dark.disabled, .btn-outline-dark:disabled {
    color: #343a40;
    background-color: transparent; }
  .btn-outline-dark:not(:disabled):not(.disabled):active, .btn-outline-dark:not(:disabled):not(.disabled).active,
  .show > .btn-outline-dark.dropdown-toggle {
    color: #fff;
    background-color: #343a40;
    border-color: #343a40; }
    .btn-outline-dark:not(:disabled):not(.disabled):active:focus, .btn-outline-dark:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-dark.dropdown-toggle:focus {
      box-shadow: 0 0 0 0.2rem rgba(52, 58, 64, 0.5); }

.btn-link {
  font-weight: 400;
  color: #10284e;
  background-color: transparent; }
  .btn-link:hover {
    color: #03070f;
    text-decoration: underline;
    background-color: transparent;
    border-color: transparent; }
  .btn-link:focus, .btn-link.focus {
    text-decoration: underline;
    border-color: transparent;
    box-shadow: none; }
  .btn-link:disabled, .btn-link.disabled {
    color: #6c757d;
    pointer-events: none; }

.btn-lg, .btn-group-lg > .btn {
  padding: 0.5rem 1rem;
  font-size: 1.25rem;
  line-height: 1.5;
  border-radius: 0.3rem; }

.btn-sm, .btn-group-sm > .btn {
  padding: 0.25rem 0.5rem;
  font-size: 0.875rem;
  line-height: 1.5;
  border-radius: 0.2rem; }

.btn-block {
  display: block;
  width: 100%; }
  .btn-block + .btn-block {
    margin-top: 0.5rem; }

input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%; }

.fade {
  transition: opacity 0.15s linear; }
  @media screen and (prefers-reduced-motion: reduce) {
    .fade {
      transition: none; } }
  .fade:not(.show) {
    opacity: 0; }

.collapse:not(.show) {
  display: none; }

.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  transition: height 0.35s ease; }
  @media screen and (prefers-reduced-motion: reduce) {
    .collapsing {
      transition: none; } }

.dropup,
.dropright,
.dropdown,
.dropleft {
  position: relative; }

.dropdown-toggle::after {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 0.255em;
  vertical-align: 0.255em;
  content: "";
  border-top: 0.3em solid;
  border-right: 0.3em solid transparent;
  border-bottom: 0;
  border-left: 0.3em solid transparent; }

.dropdown-toggle:empty::after {
  margin-left: 0; }

.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 10rem;
  padding: 0.5rem 0;
  margin: 0.125rem 0 0;
  font-size: 1rem;
  color: #212529;
  text-align: left;
  list-style: none;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 0.25rem; }

.dropdown-menu-right {
  right: 0;
  left: auto; }

.dropup .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-top: 0;
  margin-bottom: 0.125rem; }

.dropup .dropdown-toggle::after {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 0.255em;
  vertical-align: 0.255em;
  content: "";
  border-top: 0;
  border-right: 0.3em solid transparent;
  border-bottom: 0.3em solid;
  border-left: 0.3em solid transparent; }

.dropup .dropdown-toggle:empty::after {
  margin-left: 0; }

.dropright .dropdown-menu {
  top: 0;
  right: auto;
  left: 100%;
  margin-top: 0;
  margin-left: 0.125rem; }

.dropright .dropdown-toggle::after {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 0.255em;
  vertical-align: 0.255em;
  content: "";
  border-top: 0.3em solid transparent;
  border-right: 0;
  border-bottom: 0.3em solid transparent;
  border-left: 0.3em solid; }

.dropright .dropdown-toggle:empty::after {
  margin-left: 0; }

.dropright .dropdown-toggle::after {
  vertical-align: 0; }

.dropleft .dropdown-menu {
  top: 0;
  right: 100%;
  left: auto;
  margin-top: 0;
  margin-right: 0.125rem; }

.dropleft .dropdown-toggle::after {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 0.255em;
  vertical-align: 0.255em;
  content: ""; }

.dropleft .dropdown-toggle::after {
  display: none; }

.dropleft .dropdown-toggle::before {
  display: inline-block;
  width: 0;
  height: 0;
  margin-right: 0.255em;
  vertical-align: 0.255em;
  content: "";
  border-top: 0.3em solid transparent;
  border-right: 0.3em solid;
  border-bottom: 0.3em solid transparent; }

.dropleft .dropdown-toggle:empty::after {
  margin-left: 0; }

.dropleft .dropdown-toggle::before {
  vertical-align: 0; }

.dropdown-menu[x-placement^="top"], .dropdown-menu[x-placement^="right"], .dropdown-menu[x-placement^="bottom"], .dropdown-menu[x-placement^="left"] {
  right: auto;
  bottom: auto; }

.dropdown-divider {
  height: 0;
  margin: 0.5rem 0;
  overflow: hidden;
  border-top: 1px solid #e9ecef; }

.dropdown-item {
  display: block;
  width: 100%;
  padding: 0.25rem 1.5rem;
  clear: both;
  font-weight: 400;
  color: #212529;
  text-align: inherit;
  white-space: nowrap;
  background-color: transparent;
  border: 0; }
  .dropdown-item:hover, .dropdown-item:focus {
    color: #16181b;
    text-decoration: none;
    background-color: #f8f9fa; }
  .dropdown-item.active, .dropdown-item:active {
    color: #fff;
    text-decoration: none;
    background-color: #10284e; }
  .dropdown-item.disabled, .dropdown-item:disabled {
    color: #6c757d;
    background-color: transparent; }

.dropdown-menu.show {
  display: block; }

.dropdown-header {
  display: block;
  padding: 0.5rem 1.5rem;
  margin-bottom: 0;
  font-size: 0.875rem;
  color: #6c757d;
  white-space: nowrap; }

.dropdown-item-text {
  display: block;
  padding: 0.25rem 1.5rem;
  color: #212529; }

.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-flex;
  vertical-align: middle; }
  .btn-group > .btn,
  .btn-group-vertical > .btn {
    position: relative;
    flex: 0 1 auto; }
    .btn-group > .btn:hover,
    .btn-group-vertical > .btn:hover {
      z-index: 1; }
    .btn-group > .btn:focus, .btn-group > .btn:active, .btn-group > .btn.active,
    .btn-group-vertical > .btn:focus,
    .btn-group-vertical > .btn:active,
    .btn-group-vertical > .btn.active {
      z-index: 1; }
  .btn-group .btn + .btn,
  .btn-group .btn + .btn-group,
  .btn-group .btn-group + .btn,
  .btn-group .btn-group + .btn-group,
  .btn-group-vertical .btn + .btn,
  .btn-group-vertical .btn + .btn-group,
  .btn-group-vertical .btn-group + .btn,
  .btn-group-vertical .btn-group + .btn-group {
    margin-left: -1px; }

.btn-toolbar {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start; }
  .btn-toolbar .input-group {
    width: auto; }

.btn-group > .btn:first-child {
  margin-left: 0; }

.btn-group > .btn:not(:last-child):not(.dropdown-toggle),
.btn-group > .btn-group:not(:last-child) > .btn {
  border-top-right-radius: 0;
  border-bottom-right-radius: 0; }

.btn-group > .btn:not(:first-child),
.btn-group > .btn-group:not(:first-child) > .btn {
  border-top-left-radius: 0;
  border-bottom-left-radius: 0; }

.dropdown-toggle-split {
  padding-right: 0.5625rem;
  padding-left: 0.5625rem; }
  .dropdown-toggle-split::after,
  .dropup .dropdown-toggle-split::after,
  .dropright .dropdown-toggle-split::after {
    margin-left: 0; }
  .dropleft .dropdown-toggle-split::before {
    margin-right: 0; }

.btn-sm + .dropdown-toggle-split, .btn-group-sm > .btn + .dropdown-toggle-split {
  padding-right: 0.375rem;
  padding-left: 0.375rem; }

.btn-lg + .dropdown-toggle-split, .btn-group-lg > .btn + .dropdown-toggle-split {
  padding-right: 0.75rem;
  padding-left: 0.75rem; }

.btn-group-vertical {
  flex-direction: column;
  align-items: flex-start;
  justify-content: center; }
  .btn-group-vertical .btn,
  .btn-group-vertical .btn-group {
    width: 100%; }
  .btn-group-vertical > .btn + .btn,
  .btn-group-vertical > .btn + .btn-group,
  .btn-group-vertical > .btn-group + .btn,
  .btn-group-vertical > .btn-group + .btn-group {
    margin-top: -1px;
    margin-left: 0; }
  .btn-group-vertical > .btn:not(:last-child):not(.dropdown-toggle),
  .btn-group-vertical > .btn-group:not(:last-child) > .btn {
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0; }
  .btn-group-vertical > .btn:not(:first-child),
  .btn-group-vertical > .btn-group:not(:first-child) > .btn {
    border-top-left-radius: 0;
    border-top-right-radius: 0; }

.btn-group-toggle > .btn,
.btn-group-toggle > .btn-group > .btn {
  margin-bottom: 0; }
  .btn-group-toggle > .btn input[type="radio"],
  .btn-group-toggle > .btn input[type="checkbox"],
  .btn-group-toggle > .btn-group > .btn input[type="radio"],
  .btn-group-toggle > .btn-group > .btn input[type="checkbox"] {
    position: absolute;
    clip: rect(0, 0, 0, 0);
    pointer-events: none; }

.input-group {
  position: relative;
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%; }
  .input-group > .form-control,
  .input-group > .custom-select,
  .input-group > .custom-file {
    position: relative;
    flex: 1 1 auto;
    width: 1%;
    margin-bottom: 0; }
    .input-group > .form-control + .form-control,
    .input-group > .form-control + .custom-select,
    .input-group > .form-control + .custom-file,
    .input-group > .custom-select + .form-control,
    .input-group > .custom-select + .custom-select,
    .input-group > .custom-select + .custom-file,
    .input-group > .custom-file + .form-control,
    .input-group > .custom-file + .custom-select,
    .input-group > .custom-file + .custom-file {
      margin-left: -1px; }
  .input-group > .form-control:focus,
  .input-group > .custom-select:focus,
  .input-group > .custom-file .custom-file-input:focus ~ .custom-file-label {
    z-index: 3; }
  .input-group > .custom-file .custom-file-input:focus {
    z-index: 4; }
  .input-group > .form-control:not(:last-child),
  .input-group > .custom-select:not(:last-child) {
    border-top-right-radius: 0;
    border-bottom-right-radius: 0; }
  .input-group > .form-control:not(:first-child),
  .input-group > .custom-select:not(:first-child) {
    border-top-left-radius: 0;
    border-bottom-left-radius: 0; }
  .input-group > .custom-file {
    display: flex;
    align-items: center; }
    .input-group > .custom-file:not(:last-child) .custom-file-label,
    .input-group > .custom-file:not(:last-child) .custom-file-label::after {
      border-top-right-radius: 0;
      border-bottom-right-radius: 0; }
    .input-group > .custom-file:not(:first-child) .custom-file-label {
      border-top-left-radius: 0;
      border-bottom-left-radius: 0; }

.input-group-prepend,
.input-group-append {
  display: flex; }
  .input-group-prepend .btn,
  .input-group-append .btn {
    position: relative;
    z-index: 2; }
  .input-group-prepend .btn + .btn,
  .input-group-prepend .btn + .input-group-text,
  .input-group-prepend .input-group-text + .input-group-text,
  .input-group-prepend .input-group-text + .btn,
  .input-group-append .btn + .btn,
  .input-group-append .btn + .input-group-text,
  .input-group-append .input-group-text + .input-group-text,
  .input-group-append .input-group-text + .btn {
    margin-left: -1px; }

.input-group-prepend {
  margin-right: -1px; }

.input-group-append {
  margin-left: -1px; }

.input-group-text {
  display: flex;
  align-items: center;
  padding: 0.375rem 0.75rem;
  margin-bottom: 0;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #495057;
  text-align: center;
  white-space: nowrap;
  background-color: #e9ecef;
  border: 1px solid #ced4da;
  border-radius: 0.25rem; }
  .input-group-text input[type="radio"],
  .input-group-text input[type="checkbox"] {
    margin-top: 0; }

.input-group-lg > .form-control,
.input-group-lg > .input-group-prepend > .input-group-text,
.input-group-lg > .input-group-append > .input-group-text,
.input-group-lg > .input-group-prepend > .btn,
.input-group-lg > .input-group-append > .btn {
  height: calc( 2.875rem + 2px);
  padding: 0.5rem 1rem;
  font-size: 1.25rem;
  line-height: 1.5;
  border-radius: 0.3rem; }

.input-group-sm > .form-control,
.input-group-sm > .input-group-prepend > .input-group-text,
.input-group-sm > .input-group-append > .input-group-text,
.input-group-sm > .input-group-prepend > .btn,
.input-group-sm > .input-group-append > .btn {
  height: calc( 1.8125rem + 2px);
  padding: 0.25rem 0.5rem;
  font-size: 0.875rem;
  line-height: 1.5;
  border-radius: 0.2rem; }

.input-group > .input-group-prepend > .btn,
.input-group > .input-group-prepend > .input-group-text,
.input-group > .input-group-append:not(:last-child) > .btn,
.input-group > .input-group-append:not(:last-child) > .input-group-text,
.input-group > .input-group-append:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group > .input-group-append:last-child > .input-group-text:not(:last-child) {
  border-top-right-radius: 0;
  border-bottom-right-radius: 0; }

.input-group > .input-group-append > .btn,
.input-group > .input-group-append > .input-group-text,
.input-group > .input-group-prepend:not(:first-child) > .btn,
.input-group > .input-group-prepend:not(:first-child) > .input-group-text,
.input-group > .input-group-prepend:first-child > .btn:not(:first-child),
.input-group > .input-group-prepend:first-child > .input-group-text:not(:first-child) {
  border-top-left-radius: 0;
  border-bottom-left-radius: 0; }

.custom-control {
  position: relative;
  display: block;
  min-height: 1.5rem;
  padding-left: 1.5rem; }

.custom-control-inline {
  display: inline-flex;
  margin-right: 1rem; }

.custom-control-input {
  position: absolute;
  z-index: -1;
  opacity: 0; }
  .custom-control-input:checked ~ .custom-control-label::before {
    color: #fff;
    background-color: #10284e; }
  .custom-control-input:focus ~ .custom-control-label::before {
    box-shadow: 0 0 0 1px #fff, 0 0 0 0.2rem rgba(16, 40, 78, 0.25); }
  .custom-control-input:active ~ .custom-control-label::before {
    color: #fff;
    background-color: #3a77d7; }
  .custom-control-input:disabled ~ .custom-control-label {
    color: #6c757d; }
    .custom-control-input:disabled ~ .custom-control-label::before {
      background-color: #e9ecef; }

.custom-control-label {
  position: relative;
  margin-bottom: 0; }
  .custom-control-label::before {
    position: absolute;
    top: 0.25rem;
    left: -1.5rem;
    display: block;
    width: 1rem;
    height: 1rem;
    pointer-events: none;
    content: "";
    user-select: none;
    background-color: #dee2e6; }
  .custom-control-label::after {
    position: absolute;
    top: 0.25rem;
    left: -1.5rem;
    display: block;
    width: 1rem;
    height: 1rem;
    content: "";
    background-repeat: no-repeat;
    background-position: center center;
    background-size: 50% 50%; }

.custom-checkbox .custom-control-label::before {
  border-radius: 0.25rem; }

.custom-checkbox .custom-control-input:checked ~ .custom-control-label::before {
  background-color: #10284e; }

.custom-checkbox .custom-control-input:checked ~ .custom-control-label::after {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3E%3Cpath fill='%23fff' d='M6.564.75l-3.59 3.612-1.538-1.55L0 4.26 2.974 7.25 8 2.193z'/%3E%3C/svg%3E"); }

.custom-checkbox .custom-control-input:indeterminate ~ .custom-control-label::before {
  background-color: #10284e; }

.custom-checkbox .custom-control-input:indeterminate ~ .custom-control-label::after {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 4'%3E%3Cpath stroke='%23fff' d='M0 2h4'/%3E%3C/svg%3E"); }

.custom-checkbox .custom-control-input:disabled:checked ~ .custom-control-label::before {
  background-color: rgba(16, 40, 78, 0.5); }

.custom-checkbox .custom-control-input:disabled:indeterminate ~ .custom-control-label::before {
  background-color: rgba(16, 40, 78, 0.5); }

.custom-radio .custom-control-label::before {
  border-radius: 50%; }

.custom-radio .custom-control-input:checked ~ .custom-control-label::before {
  background-color: #10284e; }

.custom-radio .custom-control-input:checked ~ .custom-control-label::after {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3E%3Ccircle r='3' fill='%23fff'/%3E%3C/svg%3E"); }

.custom-radio .custom-control-input:disabled:checked ~ .custom-control-label::before {
  background-color: rgba(16, 40, 78, 0.5); }

.custom-select {
  display: inline-block;
  width: 100%;
  height: calc(2.25rem + 2px);
  padding: 0.375rem 1.75rem 0.375rem 0.75rem;
  line-height: 1.5;
  color: #495057;
  vertical-align: middle;
  background: #fff url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 5'%3E%3Cpath fill='%23343a40' d='M2 0L0 2h4zm0 5L0 3h4z'/%3E%3C/svg%3E") no-repeat right 0.75rem center;
  background-size: 8px 10px;
  border: 1px solid #ced4da;
  border-radius: 0.25rem;
  appearance: none; }
  .custom-select:focus {
    border-color: #265eb8;
    outline: 0;
    box-shadow: 0 0 0 0.2rem rgba(38, 94, 184, 0.5); }
    .custom-select:focus::-ms-value {
      color: #495057;
      background-color: #fff; }
  .custom-select[multiple], .custom-select[size]:not([size="1"]) {
    height: auto;
    padding-right: 0.75rem;
    background-image: none; }
  .custom-select:disabled {
    color: #6c757d;
    background-color: #e9ecef; }
  .custom-select::-ms-expand {
    opacity: 0; }

.custom-select-sm {
  height: calc( 1.8125rem + 2px);
  padding-top: 0.375rem;
  padding-bottom: 0.375rem;
  font-size: 75%; }

.custom-select-lg {
  height: calc( 2.875rem + 2px);
  padding-top: 0.375rem;
  padding-bottom: 0.375rem;
  font-size: 125%; }

.custom-file {
  position: relative;
  display: inline-block;
  width: 100%;
  height: calc(2.25rem + 2px);
  margin-bottom: 0; }

.custom-file-input {
  position: relative;
  z-index: 2;
  width: 100%;
  height: calc(2.25rem + 2px);
  margin: 0;
  opacity: 0; }
  .custom-file-input:focus ~ .custom-file-label {
    border-color: #265eb8;
    box-shadow: 0 0 0 0.2rem rgba(16, 40, 78, 0.25); }
    .custom-file-input:focus ~ .custom-file-label::after {
      border-color: #265eb8; }
  .custom-file-input:disabled ~ .custom-file-label {
    background-color: #e9ecef; }
  .custom-file-input:lang(en) ~ .custom-file-label::after {
    content: "Browse"; }

.custom-file-label {
  position: absolute;
  top: 0;
  right: 0;
  left: 0;
  z-index: 1;
  height: calc(2.25rem + 2px);
  padding: 0.375rem 0.75rem;
  line-height: 1.5;
  color: #495057;
  background-color: #fff;
  border: 1px solid #ced4da;
  border-radius: 0.25rem; }
  .custom-file-label::after {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    z-index: 3;
    display: block;
    height: 2.25rem;
    padding: 0.375rem 0.75rem;
    line-height: 1.5;
    color: #495057;
    content: "Browse";
    background-color: #e9ecef;
    border-left: 1px solid #ced4da;
    border-radius: 0 0.25rem 0.25rem 0; }

.custom-range {
  width: 100%;
  padding-left: 0;
  background-color: transparent;
  appearance: none; }
  .custom-range:focus {
    outline: none; }
    .custom-range:focus::-webkit-slider-thumb {
      box-shadow: 0 0 0 1px #fff, 0 0 0 0.2rem rgba(16, 40, 78, 0.25); }
    .custom-range:focus::-moz-range-thumb {
      box-shadow: 0 0 0 1px #fff, 0 0 0 0.2rem rgba(16, 40, 78, 0.25); }
    .custom-range:focus::-ms-thumb {
      box-shadow: 0 0 0 1px #fff, 0 0 0 0.2rem rgba(16, 40, 78, 0.25); }
  .custom-range::-moz-focus-outer {
    border: 0; }
  .custom-range::-webkit-slider-thumb {
    width: 1rem;
    height: 1rem;
    margin-top: -0.25rem;
    background-color: #10284e;
    border: 0;
    border-radius: 1rem;
    transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    appearance: none; }
    @media screen and (prefers-reduced-motion: reduce) {
      .custom-range::-webkit-slider-thumb {
        transition: none; } }
    .custom-range::-webkit-slider-thumb:active {
      background-color: #3a77d7; }
  .custom-range::-webkit-slider-runnable-track {
    width: 100%;
    height: 0.5rem;
    color: transparent;
    cursor: pointer;
    background-color: #dee2e6;
    border-color: transparent;
    border-radius: 1rem; }
  .custom-range::-moz-range-thumb {
    width: 1rem;
    height: 1rem;
    background-color: #10284e;
    border: 0;
    border-radius: 1rem;
    transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    appearance: none; }
    @media screen and (prefers-reduced-motion: reduce) {
      .custom-range::-moz-range-thumb {
        transition: none; } }
    .custom-range::-moz-range-thumb:active {
      background-color: #3a77d7; }
  .custom-range::-moz-range-track {
    width: 100%;
    height: 0.5rem;
    color: transparent;
    cursor: pointer;
    background-color: #dee2e6;
    border-color: transparent;
    border-radius: 1rem; }
  .custom-range::-ms-thumb {
    width: 1rem;
    height: 1rem;
    margin-top: 0;
    margin-right: 0.2rem;
    margin-left: 0.2rem;
    background-color: #10284e;
    border: 0;
    border-radius: 1rem;
    transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    appearance: none; }
    @media screen and (prefers-reduced-motion: reduce) {
      .custom-range::-ms-thumb {
        transition: none; } }
    .custom-range::-ms-thumb:active {
      background-color: #3a77d7; }
  .custom-range::-ms-track {
    width: 100%;
    height: 0.5rem;
    color: transparent;
    cursor: pointer;
    background-color: transparent;
    border-color: transparent;
    border-width: 0.5rem; }
  .custom-range::-ms-fill-lower {
    background-color: #dee2e6;
    border-radius: 1rem; }
  .custom-range::-ms-fill-upper {
    margin-right: 15px;
    background-color: #dee2e6;
    border-radius: 1rem; }

.custom-control-label::before,
.custom-file-label,
.custom-select {
  transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out; }
  @media screen and (prefers-reduced-motion: reduce) {
    .custom-control-label::before,
    .custom-file-label,
    .custom-select {
      transition: none; } }

.nav {
  display: flex;
  flex-wrap: wrap;
  padding-left: 0;
  margin-bottom: 0;
  list-style: none; }

.nav-link {
  display: block;
  padding: 0.5rem 1rem; }
  .nav-link:hover, .nav-link:focus {
    text-decoration: none; }
  .nav-link.disabled {
    color: #6c757d; }

.nav-tabs {
  border-bottom: 1px solid #dee2e6; }
  .nav-tabs .nav-item {
    margin-bottom: -1px; }
  .nav-tabs .nav-link {
    border: 1px solid transparent;
    border-top-left-radius: 0.25rem;
    border-top-right-radius: 0.25rem; }
    .nav-tabs .nav-link:hover, .nav-tabs .nav-link:focus {
      border-color: #e9ecef #e9ecef #dee2e6; }
    .nav-tabs .nav-link.disabled {
      color: #6c757d;
      background-color: transparent;
      border-color: transparent; }
  .nav-tabs .nav-link.active,
  .nav-tabs .nav-item.show .nav-link {
    color: #495057;
    background-color: #fff;
    border-color: #dee2e6 #dee2e6 #fff; }
  .nav-tabs .dropdown-menu {
    margin-top: -1px;
    border-top-left-radius: 0;
    border-top-right-radius: 0; }

.nav-pills .nav-link {
  border-radius: 0.25rem; }

.nav-pills .nav-link.active,
.nav-pills .show > .nav-link {
  color: #fff;
  background-color: #10284e; }

.nav-fill .nav-item {
  flex: 1 1 auto;
  text-align: center; }

.nav-justified .nav-item {
  flex-basis: 0;
  flex-grow: 1;
  text-align: center; }

.tab-content > .tab-pane {
  display: none; }

.tab-content > .active {
  display: block; }

.navbar {
  position: relative;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  padding: 0.5rem 1rem; }
  .navbar > .container,
  .navbar > .container-fluid {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between; }

.navbar-brand {
  display: inline-block;
  padding-top: 0.3125rem;
  padding-bottom: 0.3125rem;
  margin-right: 1rem;
  font-size: 1.25rem;
  line-height: inherit;
  white-space: nowrap; }
  .navbar-brand:hover, .navbar-brand:focus {
    text-decoration: none; }

.navbar-nav {
  display: flex;
  flex-direction: column;
  padding-left: 0;
  margin-bottom: 0;
  list-style: none; }
  .navbar-nav .nav-link {
    padding-right: 0;
    padding-left: 0; }
  .navbar-nav .dropdown-menu {
    position: static;
    float: none; }

.navbar-text {
  display: inline-block;
  padding-top: 0.5rem;
  padding-bottom: 0.5rem; }

.navbar-collapse {
  flex-basis: 100%;
  flex-grow: 1;
  align-items: center; }

.navbar-toggler {
  padding: 0.25rem 0.75rem;
  font-size: 1.25rem;
  line-height: 1;
  background-color: transparent;
  border: 1px solid transparent;
  border-radius: 0.25rem; }
  .navbar-toggler:hover, .navbar-toggler:focus {
    text-decoration: none; }
  .navbar-toggler:not(:disabled):not(.disabled) {
    cursor: pointer; }

.navbar-toggler-icon {
  display: inline-block;
  width: 1.5em;
  height: 1.5em;
  vertical-align: middle;
  content: "";
  background: no-repeat center center;
  background-size: 100% 100%; }

@media (max-width: 575.98px) {
  .navbar-expand-sm > .container,
  .navbar-expand-sm > .container-fluid {
    padding-right: 0;
    padding-left: 0; } }

@media (min-width: 576px) {
  .navbar-expand-sm {
    flex-flow: row nowrap;
    justify-content: flex-start; }
    .navbar-expand-sm .navbar-nav {
      flex-direction: row; }
      .navbar-expand-sm .navbar-nav .dropdown-menu {
        position: absolute; }
      .navbar-expand-sm .navbar-nav .nav-link {
        padding-right: 0.5rem;
        padding-left: 0.5rem; }
    .navbar-expand-sm > .container,
    .navbar-expand-sm > .container-fluid {
      flex-wrap: nowrap; }
    .navbar-expand-sm .navbar-collapse {
      display: flex !important;
      flex-basis: auto; }
    .navbar-expand-sm .navbar-toggler {
      display: none; } }

@media (max-width: 767.98px) {
  .navbar-expand-md > .container,
  .navbar-expand-md > .container-fluid {
    padding-right: 0;
    padding-left: 0; } }

@media (min-width: 768px) {
  .navbar-expand-md {
    flex-flow: row nowrap;
    justify-content: flex-start; }
    .navbar-expand-md .navbar-nav {
      flex-direction: row; }
      .navbar-expand-md .navbar-nav .dropdown-menu {
        position: absolute; }
      .navbar-expand-md .navbar-nav .nav-link {
        padding-right: 0.5rem;
        padding-left: 0.5rem; }
    .navbar-expand-md > .container,
    .navbar-expand-md > .container-fluid {
      flex-wrap: nowrap; }
    .navbar-expand-md .navbar-collapse {
      display: flex !important;
      flex-basis: auto; }
    .navbar-expand-md .navbar-toggler {
      display: none; } }

@media (max-width: 991.98px) {
  .navbar-expand-lg > .container,
  .navbar-expand-lg > .container-fluid {
    padding-right: 0;
    padding-left: 0; } }

@media (min-width: 992px) {
  .navbar-expand-lg {
    flex-flow: row nowrap;
    justify-content: flex-start; }
    .navbar-expand-lg .navbar-nav {
      flex-direction: row; }
      .navbar-expand-lg .navbar-nav .dropdown-menu {
        position: absolute; }
      .navbar-expand-lg .navbar-nav .nav-link {
        padding-right: 0.5rem;
        padding-left: 0.5rem; }
    .navbar-expand-lg > .container,
    .navbar-expand-lg > .container-fluid {
      flex-wrap: nowrap; }
    .navbar-expand-lg .navbar-collapse {
      display: flex !important;
      flex-basis: auto; }
    .navbar-expand-lg .navbar-toggler {
      display: none; } }

@media (max-width: 1199.98px) {
  .navbar-expand-xl > .container,
  .navbar-expand-xl > .container-fluid {
    padding-right: 0;
    padding-left: 0; } }

@media (min-width: 1200px) {
  .navbar-expand-xl {
    flex-flow: row nowrap;
    justify-content: flex-start; }
    .navbar-expand-xl .navbar-nav {
      flex-direction: row; }
      .navbar-expand-xl .navbar-nav .dropdown-menu {
        position: absolute; }
      .navbar-expand-xl .navbar-nav .nav-link {
        padding-right: 0.5rem;
        padding-left: 0.5rem; }
    .navbar-expand-xl > .container,
    .navbar-expand-xl > .container-fluid {
      flex-wrap: nowrap; }
    .navbar-expand-xl .navbar-collapse {
      display: flex !important;
      flex-basis: auto; }
    .navbar-expand-xl .navbar-toggler {
      display: none; } }

.navbar-expand {
  flex-flow: row nowrap;
  justify-content: flex-start; }
  .navbar-expand > .container,
  .navbar-expand > .container-fluid {
    padding-right: 0;
    padding-left: 0; }
  .navbar-expand .navbar-nav {
    flex-direction: row; }
    .navbar-expand .navbar-nav .dropdown-menu {
      position: absolute; }
    .navbar-expand .navbar-nav .nav-link {
      padding-right: 0.5rem;
      padding-left: 0.5rem; }
  .navbar-expand > .container,
  .navbar-expand > .container-fluid {
    flex-wrap: nowrap; }
  .navbar-expand .navbar-collapse {
    display: flex !important;
    flex-basis: auto; }
  .navbar-expand .navbar-toggler {
    display: none; }

.navbar-light .navbar-brand {
  color: rgba(0, 0, 0, 0.9); }
  .navbar-light .navbar-brand:hover, .navbar-light .navbar-brand:focus {
    color: rgba(0, 0, 0, 0.9); }

.navbar-light .navbar-nav .nav-link {
  color: rgba(0, 0, 0, 0.5); }
  .navbar-light .navbar-nav .nav-link:hover, .navbar-light .navbar-nav .nav-link:focus {
    color: rgba(0, 0, 0, 0.7); }
  .navbar-light .navbar-nav .nav-link.disabled {
    color: rgba(0, 0, 0, 0.3); }

.navbar-light .navbar-nav .show > .nav-link,
.navbar-light .navbar-nav .active > .nav-link,
.navbar-light .navbar-nav .nav-link.show,
.navbar-light .navbar-nav .nav-link.active {
  color: rgba(0, 0, 0, 0.9); }

.navbar-light .navbar-toggler {
  color: rgba(0, 0, 0, 0.5);
  border-color: rgba(0, 0, 0, 0.1); }

.navbar-light .navbar-toggler-icon {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath stroke='rgba(0, 0, 0, 0.5)' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 7h22M4 15h22M4 23h22'/%3E%3C/svg%3E"); }

.navbar-light .navbar-text {
  color: rgba(0, 0, 0, 0.5); }
  .navbar-light .navbar-text a {
    color: rgba(0, 0, 0, 0.9); }
    .navbar-light .navbar-text a:hover, .navbar-light .navbar-text a:focus {
      color: rgba(0, 0, 0, 0.9); }

.navbar-dark .navbar-brand {
  color: #fff; }
  .navbar-dark .navbar-brand:hover, .navbar-dark .navbar-brand:focus {
    color: #fff; }

.navbar-dark .navbar-nav .nav-link {
  color: rgba(255, 255, 255, 0.5); }
  .navbar-dark .navbar-nav .nav-link:hover, .navbar-dark .navbar-nav .nav-link:focus {
    color: rgba(255, 255, 255, 0.75); }
  .navbar-dark .navbar-nav .nav-link.disabled {
    color: rgba(255, 255, 255, 0.25); }

.navbar-dark .navbar-nav .show > .nav-link,
.navbar-dark .navbar-nav .active > .nav-link,
.navbar-dark .navbar-nav .nav-link.show,
.navbar-dark .navbar-nav .nav-link.active {
  color: #fff; }

.navbar-dark .navbar-toggler {
  color: rgba(255, 255, 255, 0.5);
  border-color: rgba(255, 255, 255, 0.1); }

.navbar-dark .navbar-toggler-icon {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath stroke='rgba(255, 255, 255, 0.5)' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 7h22M4 15h22M4 23h22'/%3E%3C/svg%3E"); }

.navbar-dark .navbar-text {
  color: rgba(255, 255, 255, 0.5); }
  .navbar-dark .navbar-text a {
    color: #fff; }
    .navbar-dark .navbar-text a:hover, .navbar-dark .navbar-text a:focus {
      color: #fff; }

.card {
  position: relative;
  display: flex;
  flex-direction: column;
  min-width: 0;
  word-wrap: break-word;
  background-color: #fff;
  background-clip: border-box;
  border: 1px solid rgba(0, 0, 0, 0.125);
  border-radius: 0.25rem; }
  .card > hr {
    margin-right: 0;
    margin-left: 0; }
  .card > .list-group:first-child .list-group-item:first-child {
    border-top-left-radius: 0.25rem;
    border-top-right-radius: 0.25rem; }
  .card > .list-group:last-child .list-group-item:last-child {
    border-bottom-right-radius: 0.25rem;
    border-bottom-left-radius: 0.25rem; }

.card-body {
  flex: 1 1 auto;
  padding: 1.25rem; }

.card-title {
  margin-bottom: 0.75rem; }

.card-subtitle {
  margin-top: -0.375rem;
  margin-bottom: 0; }

.card-text:last-child {
  margin-bottom: 0; }

.card-link:hover {
  text-decoration: none; }

.card-link + .card-link {
  margin-left: 1.25rem; }

.card-header {
  padding: 0.75rem 1.25rem;
  margin-bottom: 0;
  background-color: rgba(0, 0, 0, 0.03);
  border-bottom: 1px solid rgba(0, 0, 0, 0.125); }
  .card-header:first-child {
    border-radius: calc( 0.25rem - 1px) calc( 0.25rem - 1px) 0 0; }
  .card-header + .list-group .list-group-item:first-child {
    border-top: 0; }

.card-footer {
  padding: 0.75rem 1.25rem;
  background-color: rgba(0, 0, 0, 0.03);
  border-top: 1px solid rgba(0, 0, 0, 0.125); }
  .card-footer:last-child {
    border-radius: 0 0 calc( 0.25rem - 1px) calc( 0.25rem - 1px); }

.card-header-tabs {
  margin-right: -0.625rem;
  margin-bottom: -0.75rem;
  margin-left: -0.625rem;
  border-bottom: 0; }

.card-header-pills {
  margin-right: -0.625rem;
  margin-left: -0.625rem; }

.card-img-overlay {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  padding: 1.25rem; }

.card-img {
  width: 100%;
  border-radius: calc( 0.25rem - 1px); }

.card-img-top {
  width: 100%;
  border-top-left-radius: calc( 0.25rem - 1px);
  border-top-right-radius: calc( 0.25rem - 1px); }

.card-img-bottom {
  width: 100%;
  border-bottom-right-radius: calc( 0.25rem - 1px);
  border-bottom-left-radius: calc( 0.25rem - 1px); }

.card-deck {
  display: flex;
  flex-direction: column; }
  .card-deck .card {
    margin-bottom: 15px; }
  @media (min-width: 576px) {
    .card-deck {
      flex-flow: row wrap;
      margin-right: -15px;
      margin-left: -15px; }
      .card-deck .card {
        display: flex;
        flex: 1 0 0%;
        flex-direction: column;
        margin-right: 15px;
        margin-bottom: 0;
        margin-left: 15px; } }

.card-group {
  display: flex;
  flex-direction: column; }
  .card-group > .card {
    margin-bottom: 15px; }
  @media (min-width: 576px) {
    .card-group {
      flex-flow: row wrap; }
      .card-group > .card {
        flex: 1 0 0%;
        margin-bottom: 0; }
        .card-group > .card + .card {
          margin-left: 0;
          border-left: 0; }
        .card-group > .card:first-child {
          border-top-right-radius: 0;
          border-bottom-right-radius: 0; }
          .card-group > .card:first-child .card-img-top,
          .card-group > .card:first-child .card-header {
            border-top-right-radius: 0; }
          .card-group > .card:first-child .card-img-bottom,
          .card-group > .card:first-child .card-footer {
            border-bottom-right-radius: 0; }
        .card-group > .card:last-child {
          border-top-left-radius: 0;
          border-bottom-left-radius: 0; }
          .card-group > .card:last-child .card-img-top,
          .card-group > .card:last-child .card-header {
            border-top-left-radius: 0; }
          .card-group > .card:last-child .card-img-bottom,
          .card-group > .card:last-child .card-footer {
            border-bottom-left-radius: 0; }
        .card-group > .card:only-child {
          border-radius: 0.25rem; }
          .card-group > .card:only-child .card-img-top,
          .card-group > .card:only-child .card-header {
            border-top-left-radius: 0.25rem;
            border-top-right-radius: 0.25rem; }
          .card-group > .card:only-child .card-img-bottom,
          .card-group > .card:only-child .card-footer {
            border-bottom-right-radius: 0.25rem;
            border-bottom-left-radius: 0.25rem; }
        .card-group > .card:not(:first-child):not(:last-child):not(:only-child) {
          border-radius: 0; }
          .card-group > .card:not(:first-child):not(:last-child):not(:only-child) .card-img-top,
          .card-group > .card:not(:first-child):not(:last-child):not(:only-child) .card-img-bottom,
          .card-group > .card:not(:first-child):not(:last-child):not(:only-child) .card-header,
          .card-group > .card:not(:first-child):not(:last-child):not(:only-child) .card-footer {
            border-radius: 0; } }

.card-columns .card {
  margin-bottom: 0.75rem; }

@media (min-width: 576px) {
  .card-columns {
    column-count: 3;
    column-gap: 1.25rem;
    orphans: 1;
    widows: 1; }
    .card-columns .card {
      display: inline-block;
      width: 100%; } }

.accordion .card:not(:first-of-type):not(:last-of-type) {
  border-bottom: 0;
  border-radius: 0; }

.accordion .card:not(:first-of-type) .card-header:first-child {
  border-radius: 0; }

.accordion .card:first-of-type {
  border-bottom: 0;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0; }

.accordion .card:last-of-type {
  border-top-left-radius: 0;
  border-top-right-radius: 0; }

.breadcrumb {
  display: flex;
  flex-wrap: wrap;
  padding: 0.75rem 1rem;
  margin-bottom: 1rem;
  list-style: none;
  background-color: #e9ecef;
  border-radius: 0.25rem; }

.breadcrumb-item + .breadcrumb-item {
  padding-left: 0.5rem; }
  .breadcrumb-item + .breadcrumb-item::before {
    display: inline-block;
    padding-right: 0.5rem;
    color: #6c757d;
    content: "/"; }

.breadcrumb-item + .breadcrumb-item:hover::before {
  text-decoration: underline; }

.breadcrumb-item + .breadcrumb-item:hover::before {
  text-decoration: none; }

.breadcrumb-item.active {
  color: #6c757d; }

.pagination {
  display: flex;
  padding-left: 0;
  list-style: none;
  border-radius: 0.25rem; }

.page-link {
  position: relative;
  display: block;
  padding: 0.5rem 0.75rem;
  margin-left: -1px;
  line-height: 1.25;
  color: #10284e;
  background-color: #fff;
  border: 1px solid #dee2e6; }
  .page-link:hover {
    z-index: 2;
    color: #03070f;
    text-decoration: none;
    background-color: #e9ecef;
    border-color: #dee2e6; }
  .page-link:focus {
    z-index: 2;
    outline: 0;
    box-shadow: 0 0 0 0.2rem rgba(16, 40, 78, 0.25); }
  .page-link:not(:disabled):not(.disabled) {
    cursor: pointer; }

.page-item:first-child .page-link {
  margin-left: 0;
  border-top-left-radius: 0.25rem;
  border-bottom-left-radius: 0.25rem; }

.page-item:last-child .page-link {
  border-top-right-radius: 0.25rem;
  border-bottom-right-radius: 0.25rem; }

.page-item.active .page-link {
  z-index: 1;
  color: #fff;
  background-color: #10284e;
  border-color: #10284e; }

.page-item.disabled .page-link {
  color: #6c757d;
  pointer-events: none;
  cursor: auto;
  background-color: #fff;
  border-color: #dee2e6; }

.pagination-lg .page-link {
  padding: 0.75rem 1.5rem;
  font-size: 1.25rem;
  line-height: 1.5; }

.pagination-lg .page-item:first-child .page-link {
  border-top-left-radius: 0.3rem;
  border-bottom-left-radius: 0.3rem; }

.pagination-lg .page-item:last-child .page-link {
  border-top-right-radius: 0.3rem;
  border-bottom-right-radius: 0.3rem; }

.pagination-sm .page-link {
  padding: 0.25rem 0.5rem;
  font-size: 0.875rem;
  line-height: 1.5; }

.pagination-sm .page-item:first-child .page-link {
  border-top-left-radius: 0.2rem;
  border-bottom-left-radius: 0.2rem; }

.pagination-sm .page-item:last-child .page-link {
  border-top-right-radius: 0.2rem;
  border-bottom-right-radius: 0.2rem; }

.badge {
  display: inline-block;
  padding: 0.25em 0.4em;
  font-size: 75%;
  font-weight: 700;
  line-height: 1;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: 0.25rem; }
  .badge:empty {
    display: none; }

.btn .badge {
  position: relative;
  top: -1px; }

.badge-pill {
  padding-right: 0.6em;
  padding-left: 0.6em;
  border-radius: 10rem; }

.badge-primary {
  color: #fff;
  background-color: #10284e; }
  .badge-primary[href]:hover, .badge-primary[href]:focus {
    color: #fff;
    text-decoration: none;
    background-color: #071224; }

.badge-secondary {
  color: #212529;
  background-color: #30caa0; }
  .badge-secondary[href]:hover, .badge-secondary[href]:focus {
    color: #212529;
    text-decoration: none;
    background-color: #26a17f; }

.badge-success {
  color: #fff;
  background-color: #20c997; }
  .badge-success[href]:hover, .badge-success[href]:focus {
    color: #fff;
    text-decoration: none;
    background-color: #199d76; }

.badge-info {
  color: #fff;
  background-color: #17a2b8; }
  .badge-info[href]:hover, .badge-info[href]:focus {
    color: #fff;
    text-decoration: none;
    background-color: #117a8b; }

.badge-warning {
  color: #212529;
  background-color: #ffc107; }
  .badge-warning[href]:hover, .badge-warning[href]:focus {
    color: #212529;
    text-decoration: none;
    background-color: #d39e00; }

.badge-danger {
  color: #fff;
  background-color: #e94646; }
  .badge-danger[href]:hover, .badge-danger[href]:focus {
    color: #fff;
    text-decoration: none;
    background-color: #e11b1b; }

.badge-light {
  color: #212529;
  background-color: #f8f9fa; }
  .badge-light[href]:hover, .badge-light[href]:focus {
    color: #212529;
    text-decoration: none;
    background-color: #dae0e5; }

.badge-dark {
  color: #fff;
  background-color: #343a40; }
  .badge-dark[href]:hover, .badge-dark[href]:focus {
    color: #fff;
    text-decoration: none;
    background-color: #1d2124; }

.jumbotron {
  padding: 2rem 1rem;
  margin-bottom: 2rem;
  background-color: #e9ecef;
  border-radius: 0.3rem; }
  @media (min-width: 576px) {
    .jumbotron {
      padding: 4rem 2rem; } }

.jumbotron-fluid {
  padding-right: 0;
  padding-left: 0;
  border-radius: 0; }

.alert {
  position: relative;
  padding: 0.75rem 1.25rem;
  margin-bottom: 1rem;
  border: 1px solid transparent;
  border-radius: 0.25rem; }

.alert-heading {
  color: inherit; }

.alert-link {
  font-weight: 700; }

.alert-dismissible {
  padding-right: 4rem; }
  .alert-dismissible .close {
    position: absolute;
    top: 0;
    right: 0;
    padding: 0.75rem 1.25rem;
    color: inherit; }

.alert-primary {
  color: #081529;
  background-color: #cfd4dc;
  border-color: #bcc3cd; }
  .alert-primary hr {
    border-top-color: #adb6c2; }
  .alert-primary .alert-link {
    color: black; }

.alert-secondary {
  color: #196953;
  background-color: #d6f4ec;
  border-color: #c5f0e4; }
  .alert-secondary hr {
    border-top-color: #b1ebdb; }
  .alert-secondary .alert-link {
    color: #0f4032; }

.alert-success {
  color: #11694f;
  background-color: #d2f4ea;
  border-color: #c1f0e2; }
  .alert-success hr {
    border-top-color: #acebd8; }
  .alert-success .alert-link {
    color: #0a3d2e; }

.alert-info {
  color: #0c5460;
  background-color: #d1ecf1;
  border-color: #bee5eb; }
  .alert-info hr {
    border-top-color: #abdde5; }
  .alert-info .alert-link {
    color: #062c33; }

.alert-warning {
  color: #856404;
  background-color: #fff3cd;
  border-color: #ffeeba; }
  .alert-warning hr {
    border-top-color: #ffe8a1; }
  .alert-warning .alert-link {
    color: #533f03; }

.alert-danger {
  color: #792424;
  background-color: #fbdada;
  border-color: #f9cbcb; }
  .alert-danger hr {
    border-top-color: #f6b4b4; }
  .alert-danger .alert-link {
    color: #521818; }

.alert-light {
  color: #818182;
  background-color: #fefefe;
  border-color: #fdfdfe; }
  .alert-light hr {
    border-top-color: #ececf6; }
  .alert-light .alert-link {
    color: #686868; }

.alert-dark {
  color: #1b1e21;
  background-color: #d6d8d9;
  border-color: #c6c8ca; }
  .alert-dark hr {
    border-top-color: #b9bbbe; }
  .alert-dark .alert-link {
    color: #040505; }

@keyframes progress-bar-stripes {
  from {
    background-position: 1rem 0; }
  to {
    background-position: 0 0; } }

.progress {
  display: flex;
  height: 1rem;
  overflow: hidden;
  font-size: 0.75rem;
  background-color: #e9ecef;
  border-radius: 0.25rem; }

.progress-bar {
  display: flex;
  flex-direction: column;
  justify-content: center;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  background-color: #10284e;
  transition: width 0.6s ease; }
  @media screen and (prefers-reduced-motion: reduce) {
    .progress-bar {
      transition: none; } }

.progress-bar-striped {
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 1rem 1rem; }

.progress-bar-animated {
  animation: progress-bar-stripes 1s linear infinite; }

.media {
  display: flex;
  align-items: flex-start; }

.media-body {
  flex: 1; }

.list-group {
  display: flex;
  flex-direction: column;
  padding-left: 0;
  margin-bottom: 0; }

.list-group-item-action {
  width: 100%;
  color: #495057;
  text-align: inherit; }
  .list-group-item-action:hover, .list-group-item-action:focus {
    color: #495057;
    text-decoration: none;
    background-color: #f8f9fa; }
  .list-group-item-action:active {
    color: #212529;
    background-color: #e9ecef; }

.list-group-item {
  position: relative;
  display: block;
  padding: 0.75rem 1.25rem;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid rgba(0, 0, 0, 0.125); }
  .list-group-item:first-child {
    border-top-left-radius: 0.25rem;
    border-top-right-radius: 0.25rem; }
  .list-group-item:last-child {
    margin-bottom: 0;
    border-bottom-right-radius: 0.25rem;
    border-bottom-left-radius: 0.25rem; }
  .list-group-item:hover, .list-group-item:focus {
    z-index: 1;
    text-decoration: none; }
  .list-group-item.disabled, .list-group-item:disabled {
    color: #6c757d;
    background-color: #fff; }
  .list-group-item.active {
    z-index: 2;
    color: #fff;
    background-color: #10284e;
    border-color: #10284e; }

.list-group-flush .list-group-item {
  border-right: 0;
  border-left: 0;
  border-radius: 0; }

.list-group-flush:first-child .list-group-item:first-child {
  border-top: 0; }

.list-group-flush:last-child .list-group-item:last-child {
  border-bottom: 0; }

.list-group-item-primary {
  color: #081529;
  background-color: #bcc3cd; }
  .list-group-item-primary.list-group-item-action:hover, .list-group-item-primary.list-group-item-action:focus {
    color: #081529;
    background-color: #adb6c2; }
  .list-group-item-primary.list-group-item-action.active {
    color: #fff;
    background-color: #081529;
    border-color: #081529; }

.list-group-item-secondary {
  color: #196953;
  background-color: #c5f0e4; }
  .list-group-item-secondary.list-group-item-action:hover, .list-group-item-secondary.list-group-item-action:focus {
    color: #196953;
    background-color: #b1ebdb; }
  .list-group-item-secondary.list-group-item-action.active {
    color: #fff;
    background-color: #196953;
    border-color: #196953; }

.list-group-item-success {
  color: #11694f;
  background-color: #c1f0e2; }
  .list-group-item-success.list-group-item-action:hover, .list-group-item-success.list-group-item-action:focus {
    color: #11694f;
    background-color: #acebd8; }
  .list-group-item-success.list-group-item-action.active {
    color: #fff;
    background-color: #11694f;
    border-color: #11694f; }

.list-group-item-info {
  color: #0c5460;
  background-color: #bee5eb; }
  .list-group-item-info.list-group-item-action:hover, .list-group-item-info.list-group-item-action:focus {
    color: #0c5460;
    background-color: #abdde5; }
  .list-group-item-info.list-group-item-action.active {
    color: #fff;
    background-color: #0c5460;
    border-color: #0c5460; }

.list-group-item-warning {
  color: #856404;
  background-color: #ffeeba; }
  .list-group-item-warning.list-group-item-action:hover, .list-group-item-warning.list-group-item-action:focus {
    color: #856404;
    background-color: #ffe8a1; }
  .list-group-item-warning.list-group-item-action.active {
    color: #fff;
    background-color: #856404;
    border-color: #856404; }

.list-group-item-danger {
  color: #792424;
  background-color: #f9cbcb; }
  .list-group-item-danger.list-group-item-action:hover, .list-group-item-danger.list-group-item-action:focus {
    color: #792424;
    background-color: #f6b4b4; }
  .list-group-item-danger.list-group-item-action.active {
    color: #fff;
    background-color: #792424;
    border-color: #792424; }

.list-group-item-light {
  color: #818182;
  background-color: #fdfdfe; }
  .list-group-item-light.list-group-item-action:hover, .list-group-item-light.list-group-item-action:focus {
    color: #818182;
    background-color: #ececf6; }
  .list-group-item-light.list-group-item-action.active {
    color: #fff;
    background-color: #818182;
    border-color: #818182; }

.list-group-item-dark {
  color: #1b1e21;
  background-color: #c6c8ca; }
  .list-group-item-dark.list-group-item-action:hover, .list-group-item-dark.list-group-item-action:focus {
    color: #1b1e21;
    background-color: #b9bbbe; }
  .list-group-item-dark.list-group-item-action.active {
    color: #fff;
    background-color: #1b1e21;
    border-color: #1b1e21; }

.close {
  float: right;
  font-size: 1.5rem;
  font-weight: 700;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: .5; }
  .close:not(:disabled):not(.disabled) {
    cursor: pointer; }
    .close:not(:disabled):not(.disabled):hover, .close:not(:disabled):not(.disabled):focus {
      color: #000;
      text-decoration: none;
      opacity: .75; }

button.close {
  padding: 0;
  background-color: transparent;
  border: 0;
  -webkit-appearance: none; }

.modal-open {
  overflow: hidden; }
  .modal-open .modal {
    overflow-x: hidden;
    overflow-y: auto; }

.modal {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  display: none;
  overflow: hidden;
  outline: 0; }

.modal-dialog {
  position: relative;
  width: auto;
  margin: 0.5rem;
  pointer-events: none; }
  .modal.fade .modal-dialog {
    transition: transform 0.3s ease-out;
    transform: translate(0, -25%); }
    @media screen and (prefers-reduced-motion: reduce) {
      .modal.fade .modal-dialog {
        transition: none; } }
  .modal.show .modal-dialog {
    transform: translate(0, 0); }

.modal-dialog-centered {
  display: flex;
  align-items: center;
  min-height: calc(100% - (0.5rem * 2)); }
  .modal-dialog-centered::before {
    display: block;
    height: calc(100vh - (0.5rem * 2));
    content: ""; }

.modal-content {
  position: relative;
  display: flex;
  flex-direction: column;
  width: 100%;
  pointer-events: auto;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 0.3rem;
  outline: 0; }

.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000; }
  .modal-backdrop.fade {
    opacity: 0; }
  .modal-backdrop.show {
    opacity: 0.5; }

.modal-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  padding: 1rem;
  border-bottom: 1px solid #e9ecef;
  border-top-left-radius: 0.3rem;
  border-top-right-radius: 0.3rem; }
  .modal-header .close {
    padding: 1rem;
    margin: -1rem -1rem -1rem auto; }

.modal-title {
  margin-bottom: 0;
  line-height: 1.5; }

.modal-body {
  position: relative;
  flex: 1 1 auto;
  padding: 1rem; }

.modal-footer {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  padding: 1rem;
  border-top: 1px solid #e9ecef; }
  .modal-footer > :not(:first-child) {
    margin-left: .25rem; }
  .modal-footer > :not(:last-child) {
    margin-right: .25rem; }

.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll; }

@media (min-width: 576px) {
  .modal-dialog {
    max-width: 500px;
    margin: 1.75rem auto; }
  .modal-dialog-centered {
    min-height: calc(100% - (1.75rem * 2)); }
    .modal-dialog-centered::before {
      height: calc(100vh - (1.75rem * 2)); }
  .modal-sm {
    max-width: 300px; } }

@media (min-width: 992px) {
  .modal-lg {
    max-width: 800px; } }

.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  font-style: normal;
  font-weight: 400;
  line-height: 1.5;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  letter-spacing: normal;
  word-break: normal;
  word-spacing: normal;
  white-space: normal;
  line-break: auto;
  font-size: 0.875rem;
  word-wrap: break-word;
  opacity: 0; }
  .tooltip.show {
    opacity: 0.9; }
  .tooltip .arrow {
    position: absolute;
    display: block;
    width: 0.8rem;
    height: 0.4rem; }
    .tooltip .arrow::before {
      position: absolute;
      content: "";
      border-color: transparent;
      border-style: solid; }

.bs-tooltip-top, .bs-tooltip-auto[x-placement^="top"] {
  padding: 0.4rem 0; }
  .bs-tooltip-top .arrow, .bs-tooltip-auto[x-placement^="top"] .arrow {
    bottom: 0; }
    .bs-tooltip-top .arrow::before, .bs-tooltip-auto[x-placement^="top"] .arrow::before {
      top: 0;
      border-width: 0.4rem 0.4rem 0;
      border-top-color: #000; }

.bs-tooltip-right, .bs-tooltip-auto[x-placement^="right"] {
  padding: 0 0.4rem; }
  .bs-tooltip-right .arrow, .bs-tooltip-auto[x-placement^="right"] .arrow {
    left: 0;
    width: 0.4rem;
    height: 0.8rem; }
    .bs-tooltip-right .arrow::before, .bs-tooltip-auto[x-placement^="right"] .arrow::before {
      right: 0;
      border-width: 0.4rem 0.4rem 0.4rem 0;
      border-right-color: #000; }

.bs-tooltip-bottom, .bs-tooltip-auto[x-placement^="bottom"] {
  padding: 0.4rem 0; }
  .bs-tooltip-bottom .arrow, .bs-tooltip-auto[x-placement^="bottom"] .arrow {
    top: 0; }
    .bs-tooltip-bottom .arrow::before, .bs-tooltip-auto[x-placement^="bottom"] .arrow::before {
      bottom: 0;
      border-width: 0 0.4rem 0.4rem;
      border-bottom-color: #000; }

.bs-tooltip-left, .bs-tooltip-auto[x-placement^="left"] {
  padding: 0 0.4rem; }
  .bs-tooltip-left .arrow, .bs-tooltip-auto[x-placement^="left"] .arrow {
    right: 0;
    width: 0.4rem;
    height: 0.8rem; }
    .bs-tooltip-left .arrow::before, .bs-tooltip-auto[x-placement^="left"] .arrow::before {
      left: 0;
      border-width: 0.4rem 0 0.4rem 0.4rem;
      border-left-color: #000; }

.tooltip-inner {
  max-width: 200px;
  padding: 0.25rem 0.5rem;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 0.25rem; }

.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: block;
  max-width: 276px;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  font-style: normal;
  font-weight: 400;
  line-height: 1.5;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  letter-spacing: normal;
  word-break: normal;
  word-spacing: normal;
  white-space: normal;
  line-break: auto;
  font-size: 0.875rem;
  word-wrap: break-word;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 0.3rem; }
  .popover .arrow {
    position: absolute;
    display: block;
    width: 1rem;
    height: 0.5rem;
    margin: 0 0.3rem; }
    .popover .arrow::before, .popover .arrow::after {
      position: absolute;
      display: block;
      content: "";
      border-color: transparent;
      border-style: solid; }

.bs-popover-top, .bs-popover-auto[x-placement^="top"] {
  margin-bottom: 0.5rem; }
  .bs-popover-top .arrow, .bs-popover-auto[x-placement^="top"] .arrow {
    bottom: calc((0.5rem + 1px) * -1); }
  .bs-popover-top .arrow::before, .bs-popover-auto[x-placement^="top"] .arrow::before,
  .bs-popover-top .arrow::after,
  .bs-popover-auto[x-placement^="top"] .arrow::after {
    border-width: 0.5rem 0.5rem 0; }
  .bs-popover-top .arrow::before, .bs-popover-auto[x-placement^="top"] .arrow::before {
    bottom: 0;
    border-top-color: rgba(0, 0, 0, 0.25); }
  
  .bs-popover-top .arrow::after,
  .bs-popover-auto[x-placement^="top"] .arrow::after {
    bottom: 1px;
    border-top-color: #fff; }

.bs-popover-right, .bs-popover-auto[x-placement^="right"] {
  margin-left: 0.5rem; }
  .bs-popover-right .arrow, .bs-popover-auto[x-placement^="right"] .arrow {
    left: calc((0.5rem + 1px) * -1);
    width: 0.5rem;
    height: 1rem;
    margin: 0.3rem 0; }
  .bs-popover-right .arrow::before, .bs-popover-auto[x-placement^="right"] .arrow::before,
  .bs-popover-right .arrow::after,
  .bs-popover-auto[x-placement^="right"] .arrow::after {
    border-width: 0.5rem 0.5rem 0.5rem 0; }
  .bs-popover-right .arrow::before, .bs-popover-auto[x-placement^="right"] .arrow::before {
    left: 0;
    border-right-color: rgba(0, 0, 0, 0.25); }
  
  .bs-popover-right .arrow::after,
  .bs-popover-auto[x-placement^="right"] .arrow::after {
    left: 1px;
    border-right-color: #fff; }

.bs-popover-bottom, .bs-popover-auto[x-placement^="bottom"] {
  margin-top: 0.5rem; }
  .bs-popover-bottom .arrow, .bs-popover-auto[x-placement^="bottom"] .arrow {
    top: calc((0.5rem + 1px) * -1); }
  .bs-popover-bottom .arrow::before, .bs-popover-auto[x-placement^="bottom"] .arrow::before,
  .bs-popover-bottom .arrow::after,
  .bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-width: 0 0.5rem 0.5rem 0.5rem; }
  .bs-popover-bottom .arrow::before, .bs-popover-auto[x-placement^="bottom"] .arrow::before {
    top: 0;
    border-bottom-color: rgba(0, 0, 0, 0.25); }
  
  .bs-popover-bottom .arrow::after,
  .bs-popover-auto[x-placement^="bottom"] .arrow::after {
    top: 1px;
    border-bottom-color: #fff; }
  .bs-popover-bottom .popover-header::before, .bs-popover-auto[x-placement^="bottom"] .popover-header::before {
    position: absolute;
    top: 0;
    left: 50%;
    display: block;
    width: 1rem;
    margin-left: -0.5rem;
    content: "";
    border-bottom: 1px solid #f7f7f7; }

.bs-popover-left, .bs-popover-auto[x-placement^="left"] {
  margin-right: 0.5rem; }
  .bs-popover-left .arrow, .bs-popover-auto[x-placement^="left"] .arrow {
    right: calc((0.5rem + 1px) * -1);
    width: 0.5rem;
    height: 1rem;
    margin: 0.3rem 0; }
  .bs-popover-left .arrow::before, .bs-popover-auto[x-placement^="left"] .arrow::before,
  .bs-popover-left .arrow::after,
  .bs-popover-auto[x-placement^="left"] .arrow::after {
    border-width: 0.5rem 0 0.5rem 0.5rem; }
  .bs-popover-left .arrow::before, .bs-popover-auto[x-placement^="left"] .arrow::before {
    right: 0;
    border-left-color: rgba(0, 0, 0, 0.25); }
  
  .bs-popover-left .arrow::after,
  .bs-popover-auto[x-placement^="left"] .arrow::after {
    right: 1px;
    border-left-color: #fff; }

.popover-header {
  padding: 0.5rem 0.75rem;
  margin-bottom: 0;
  font-size: 1rem;
  color: inherit;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-top-left-radius: calc(0.3rem - 1px);
  border-top-right-radius: calc(0.3rem - 1px); }
  .popover-header:empty {
    display: none; }

.popover-body {
  padding: 0.5rem 0.75rem;
  color: #212529; }

.carousel {
  position: relative; }

.carousel-inner {
  position: relative;
  width: 100%;
  overflow: hidden; }

.carousel-item {
  position: relative;
  display: none;
  align-items: center;
  width: 100%;
  backface-visibility: hidden;
  perspective: 1000px; }

.carousel-item.active,
.carousel-item-next,
.carousel-item-prev {
  display: block;
  transition: transform 0.6s ease; }
  @media screen and (prefers-reduced-motion: reduce) {
    .carousel-item.active,
    .carousel-item-next,
    .carousel-item-prev {
      transition: none; } }

.carousel-item-next,
.carousel-item-prev {
  position: absolute;
  top: 0; }

.carousel-item-next.carousel-item-left,
.carousel-item-prev.carousel-item-right {
  transform: translateX(0); }
  @supports (transform-style: preserve-3d) {
    .carousel-item-next.carousel-item-left,
    .carousel-item-prev.carousel-item-right {
      transform: translate3d(0, 0, 0); } }

.carousel-item-next,
.active.carousel-item-right {
  transform: translateX(100%); }
  @supports (transform-style: preserve-3d) {
    .carousel-item-next,
    .active.carousel-item-right {
      transform: translate3d(100%, 0, 0); } }

.carousel-item-prev,
.active.carousel-item-left {
  transform: translateX(-100%); }
  @supports (transform-style: preserve-3d) {
    .carousel-item-prev,
    .active.carousel-item-left {
      transform: translate3d(-100%, 0, 0); } }

.carousel-fade .carousel-item {
  opacity: 0;
  transition-duration: .6s;
  transition-property: opacity; }

.carousel-fade .carousel-item.active,
.carousel-fade .carousel-item-next.carousel-item-left,
.carousel-fade .carousel-item-prev.carousel-item-right {
  opacity: 1; }

.carousel-fade .active.carousel-item-left,
.carousel-fade .active.carousel-item-right {
  opacity: 0; }

.carousel-fade .carousel-item-next,
.carousel-fade .carousel-item-prev,
.carousel-fade .carousel-item.active,
.carousel-fade .active.carousel-item-left,
.carousel-fade .active.carousel-item-prev {
  transform: translateX(0); }
  @supports (transform-style: preserve-3d) {
    .carousel-fade .carousel-item-next,
    .carousel-fade .carousel-item-prev,
    .carousel-fade .carousel-item.active,
    .carousel-fade .active.carousel-item-left,
    .carousel-fade .active.carousel-item-prev {
      transform: translate3d(0, 0, 0); } }

.carousel-control-prev,
.carousel-control-next {
  position: absolute;
  top: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 15%;
  color: #fff;
  text-align: center;
  opacity: 0.5; }
  .carousel-control-prev:hover, .carousel-control-prev:focus,
  .carousel-control-next:hover,
  .carousel-control-next:focus {
    color: #fff;
    text-decoration: none;
    outline: 0;
    opacity: .9; }

.carousel-control-prev {
  left: 0; }

.carousel-control-next {
  right: 0; }

.carousel-control-prev-icon,
.carousel-control-next-icon {
  display: inline-block;
  width: 20px;
  height: 20px;
  background: transparent no-repeat center center;
  background-size: 100% 100%; }

.carousel-control-prev-icon {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23fff' viewBox='0 0 8 8'%3E%3Cpath d='M5.25 0l-4 4 4 4 1.5-1.5-2.5-2.5 2.5-2.5-1.5-1.5z'/%3E%3C/svg%3E"); }

.carousel-control-next-icon {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23fff' viewBox='0 0 8 8'%3E%3Cpath d='M2.75 0l-1.5 1.5 2.5 2.5-2.5 2.5 1.5 1.5 4-4-4-4z'/%3E%3C/svg%3E"); }

.carousel-indicators {
  position: absolute;
  right: 0;
  bottom: 10px;
  left: 0;
  z-index: 15;
  display: flex;
  justify-content: center;
  padding-left: 0;
  margin-right: 15%;
  margin-left: 15%;
  list-style: none; }
  .carousel-indicators li {
    position: relative;
    flex: 0 1 auto;
    width: 30px;
    height: 3px;
    margin-right: 3px;
    margin-left: 3px;
    text-indent: -999px;
    cursor: pointer;
    background-color: rgba(255, 255, 255, 0.5); }
    .carousel-indicators li::before {
      position: absolute;
      top: -10px;
      left: 0;
      display: inline-block;
      width: 100%;
      height: 10px;
      content: ""; }
    .carousel-indicators li::after {
      position: absolute;
      bottom: -10px;
      left: 0;
      display: inline-block;
      width: 100%;
      height: 10px;
      content: ""; }
  .carousel-indicators .active {
    background-color: #fff; }

.carousel-caption {
  position: absolute;
  right: 15%;
  bottom: 20px;
  left: 15%;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center; }

.align-baseline {
  vertical-align: baseline !important; }

.align-top {
  vertical-align: top !important; }

.align-middle {
  vertical-align: middle !important; }

.align-bottom {
  vertical-align: bottom !important; }

.align-text-bottom {
  vertical-align: text-bottom !important; }

.align-text-top {
  vertical-align: text-top !important; }

.bg-primary {
  background-color: #10284e !important; }

a.bg-primary:hover, a.bg-primary:focus,
button.bg-primary:hover,
button.bg-primary:focus {
  background-color: #071224 !important; }

.bg-secondary {
  background-color: #30caa0 !important; }

a.bg-secondary:hover, a.bg-secondary:focus,
button.bg-secondary:hover,
button.bg-secondary:focus {
  background-color: #26a17f !important; }

.bg-success {
  background-color: #20c997 !important; }

a.bg-success:hover, a.bg-success:focus,
button.bg-success:hover,
button.bg-success:focus {
  background-color: #199d76 !important; }

.bg-info {
  background-color: #17a2b8 !important; }

a.bg-info:hover, a.bg-info:focus,
button.bg-info:hover,
button.bg-info:focus {
  background-color: #117a8b !important; }

.bg-warning {
  background-color: #ffc107 !important; }

a.bg-warning:hover, a.bg-warning:focus,
button.bg-warning:hover,
button.bg-warning:focus {
  background-color: #d39e00 !important; }

.bg-danger {
  background-color: #e94646 !important; }

a.bg-danger:hover, a.bg-danger:focus,
button.bg-danger:hover,
button.bg-danger:focus {
  background-color: #e11b1b !important; }

.bg-light {
  background-color: #f8f9fa !important; }

a.bg-light:hover, a.bg-light:focus,
button.bg-light:hover,
button.bg-light:focus {
  background-color: #dae0e5 !important; }

.bg-dark {
  background-color: #343a40 !important; }

a.bg-dark:hover, a.bg-dark:focus,
button.bg-dark:hover,
button.bg-dark:focus {
  background-color: #1d2124 !important; }

.bg-white {
  background-color: #fff !important; }

.bg-transparent {
  background-color: transparent !important; }

.border {
  border: 1px solid #dee2e6 !important; }

.border-top {
  border-top: 1px solid #dee2e6 !important; }

.border-right {
  border-right: 1px solid #dee2e6 !important; }

.border-bottom {
  border-bottom: 1px solid #dee2e6 !important; }

.border-left {
  border-left: 1px solid #dee2e6 !important; }

.border-0 {
  border: 0 !important; }

.border-top-0 {
  border-top: 0 !important; }

.border-right-0 {
  border-right: 0 !important; }

.border-bottom-0 {
  border-bottom: 0 !important; }

.border-left-0 {
  border-left: 0 !important; }

.border-primary {
  border-color: #10284e !important; }

.border-secondary {
  border-color: #30caa0 !important; }

.border-success {
  border-color: #20c997 !important; }

.border-info {
  border-color: #17a2b8 !important; }

.border-warning {
  border-color: #ffc107 !important; }

.border-danger {
  border-color: #e94646 !important; }

.border-light {
  border-color: #f8f9fa !important; }

.border-dark {
  border-color: #343a40 !important; }

.border-white {
  border-color: #fff !important; }

.rounded {
  border-radius: 0.25rem !important; }

.rounded-top {
  border-top-left-radius: 0.25rem !important;
  border-top-right-radius: 0.25rem !important; }

.rounded-right {
  border-top-right-radius: 0.25rem !important;
  border-bottom-right-radius: 0.25rem !important; }

.rounded-bottom {
  border-bottom-right-radius: 0.25rem !important;
  border-bottom-left-radius: 0.25rem !important; }

.rounded-left {
  border-top-left-radius: 0.25rem !important;
  border-bottom-left-radius: 0.25rem !important; }

.rounded-circle {
  border-radius: 50% !important; }

.rounded-0 {
  border-radius: 0 !important; }

.clearfix::after {
  display: block;
  clear: both;
  content: ""; }

.d-none {
  display: none !important; }

.d-inline {
  display: inline !important; }

.d-inline-block {
  display: inline-block !important; }

.d-block {
  display: block !important; }

.d-table {
  display: table !important; }

.d-table-row {
  display: table-row !important; }

.d-table-cell {
  display: table-cell !important; }

.d-flex {
  display: flex !important; }

.d-inline-flex {
  display: inline-flex !important; }

@media (min-width: 576px) {
  .d-sm-none {
    display: none !important; }
  .d-sm-inline {
    display: inline !important; }
  .d-sm-inline-block {
    display: inline-block !important; }
  .d-sm-block {
    display: block !important; }
  .d-sm-table {
    display: table !important; }
  .d-sm-table-row {
    display: table-row !important; }
  .d-sm-table-cell {
    display: table-cell !important; }
  .d-sm-flex {
    display: flex !important; }
  .d-sm-inline-flex {
    display: inline-flex !important; } }

@media (min-width: 768px) {
  .d-md-none {
    display: none !important; }
  .d-md-inline {
    display: inline !important; }
  .d-md-inline-block {
    display: inline-block !important; }
  .d-md-block {
    display: block !important; }
  .d-md-table {
    display: table !important; }
  .d-md-table-row {
    display: table-row !important; }
  .d-md-table-cell {
    display: table-cell !important; }
  .d-md-flex {
    display: flex !important; }
  .d-md-inline-flex {
    display: inline-flex !important; } }

@media (min-width: 992px) {
  .d-lg-none {
    display: none !important; }
  .d-lg-inline {
    display: inline !important; }
  .d-lg-inline-block {
    display: inline-block !important; }
  .d-lg-block {
    display: block !important; }
  .d-lg-table {
    display: table !important; }
  .d-lg-table-row {
    display: table-row !important; }
  .d-lg-table-cell {
    display: table-cell !important; }
  .d-lg-flex {
    display: flex !important; }
  .d-lg-inline-flex {
    display: inline-flex !important; } }

@media (min-width: 1200px) {
  .d-xl-none {
    display: none !important; }
  .d-xl-inline {
    display: inline !important; }
  .d-xl-inline-block {
    display: inline-block !important; }
  .d-xl-block {
    display: block !important; }
  .d-xl-table {
    display: table !important; }
  .d-xl-table-row {
    display: table-row !important; }
  .d-xl-table-cell {
    display: table-cell !important; }
  .d-xl-flex {
    display: flex !important; }
  .d-xl-inline-flex {
    display: inline-flex !important; } }

@media print {
  .d-print-none {
    display: none !important; }
  .d-print-inline {
    display: inline !important; }
  .d-print-inline-block {
    display: inline-block !important; }
  .d-print-block {
    display: block !important; }
  .d-print-table {
    display: table !important; }
  .d-print-table-row {
    display: table-row !important; }
  .d-print-table-cell {
    display: table-cell !important; }
  .d-print-flex {
    display: flex !important; }
  .d-print-inline-flex {
    display: inline-flex !important; } }

.embed-responsive {
  position: relative;
  display: block;
  width: 100%;
  padding: 0;
  overflow: hidden; }
  .embed-responsive::before {
    display: block;
    content: ""; }
  .embed-responsive .embed-responsive-item,
  .embed-responsive iframe,
  .embed-responsive embed,
  .embed-responsive object,
  .embed-responsive video {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border: 0; }

.embed-responsive-21by9::before {
  padding-top: 42.85714%; }

.embed-responsive-16by9::before {
  padding-top: 56.25%; }

.embed-responsive-4by3::before {
  padding-top: 75%; }

.embed-responsive-1by1::before {
  padding-top: 100%; }

.flex-row {
  flex-direction: row !important; }

.flex-column {
  flex-direction: column !important; }

.flex-row-reverse {
  flex-direction: row-reverse !important; }

.flex-column-reverse {
  flex-direction: column-reverse !important; }

.flex-wrap {
  flex-wrap: wrap !important; }

.flex-nowrap {
  flex-wrap: nowrap !important; }

.flex-wrap-reverse {
  flex-wrap: wrap-reverse !important; }

.flex-fill {
  flex: 1 1 auto !important; }

.flex-grow-0 {
  flex-grow: 0 !important; }

.flex-grow-1 {
  flex-grow: 1 !important; }

.flex-shrink-0 {
  flex-shrink: 0 !important; }

.flex-shrink-1 {
  flex-shrink: 1 !important; }

.justify-content-start {
  justify-content: flex-start !important; }

.justify-content-end {
  justify-content: flex-end !important; }

.justify-content-center {
  justify-content: center !important; }

.justify-content-between {
  justify-content: space-between !important; }

.justify-content-around {
  justify-content: space-around !important; }

.align-items-start {
  align-items: flex-start !important; }

.align-items-end {
  align-items: flex-end !important; }

.align-items-center {
  align-items: center !important; }

.align-items-baseline {
  align-items: baseline !important; }

.align-items-stretch {
  align-items: stretch !important; }

.align-content-start {
  align-content: flex-start !important; }

.align-content-end {
  align-content: flex-end !important; }

.align-content-center {
  align-content: center !important; }

.align-content-between {
  align-content: space-between !important; }

.align-content-around {
  align-content: space-around !important; }

.align-content-stretch {
  align-content: stretch !important; }

.align-self-auto {
  align-self: auto !important; }

.align-self-start {
  align-self: flex-start !important; }

.align-self-end {
  align-self: flex-end !important; }

.align-self-center {
  align-self: center !important; }

.align-self-baseline {
  align-self: baseline !important; }

.align-self-stretch {
  align-self: stretch !important; }

@media (min-width: 576px) {
  .flex-sm-row {
    flex-direction: row !important; }
  .flex-sm-column {
    flex-direction: column !important; }
  .flex-sm-row-reverse {
    flex-direction: row-reverse !important; }
  .flex-sm-column-reverse {
    flex-direction: column-reverse !important; }
  .flex-sm-wrap {
    flex-wrap: wrap !important; }
  .flex-sm-nowrap {
    flex-wrap: nowrap !important; }
  .flex-sm-wrap-reverse {
    flex-wrap: wrap-reverse !important; }
  .flex-sm-fill {
    flex: 1 1 auto !important; }
  .flex-sm-grow-0 {
    flex-grow: 0 !important; }
  .flex-sm-grow-1 {
    flex-grow: 1 !important; }
  .flex-sm-shrink-0 {
    flex-shrink: 0 !important; }
  .flex-sm-shrink-1 {
    flex-shrink: 1 !important; }
  .justify-content-sm-start {
    justify-content: flex-start !important; }
  .justify-content-sm-end {
    justify-content: flex-end !important; }
  .justify-content-sm-center {
    justify-content: center !important; }
  .justify-content-sm-between {
    justify-content: space-between !important; }
  .justify-content-sm-around {
    justify-content: space-around !important; }
  .align-items-sm-start {
    align-items: flex-start !important; }
  .align-items-sm-end {
    align-items: flex-end !important; }
  .align-items-sm-center {
    align-items: center !important; }
  .align-items-sm-baseline {
    align-items: baseline !important; }
  .align-items-sm-stretch {
    align-items: stretch !important; }
  .align-content-sm-start {
    align-content: flex-start !important; }
  .align-content-sm-end {
    align-content: flex-end !important; }
  .align-content-sm-center {
    align-content: center !important; }
  .align-content-sm-between {
    align-content: space-between !important; }
  .align-content-sm-around {
    align-content: space-around !important; }
  .align-content-sm-stretch {
    align-content: stretch !important; }
  .align-self-sm-auto {
    align-self: auto !important; }
  .align-self-sm-start {
    align-self: flex-start !important; }
  .align-self-sm-end {
    align-self: flex-end !important; }
  .align-self-sm-center {
    align-self: center !important; }
  .align-self-sm-baseline {
    align-self: baseline !important; }
  .align-self-sm-stretch {
    align-self: stretch !important; } }

@media (min-width: 768px) {
  .flex-md-row {
    flex-direction: row !important; }
  .flex-md-column {
    flex-direction: column !important; }
  .flex-md-row-reverse {
    flex-direction: row-reverse !important; }
  .flex-md-column-reverse {
    flex-direction: column-reverse !important; }
  .flex-md-wrap {
    flex-wrap: wrap !important; }
  .flex-md-nowrap {
    flex-wrap: nowrap !important; }
  .flex-md-wrap-reverse {
    flex-wrap: wrap-reverse !important; }
  .flex-md-fill {
    flex: 1 1 auto !important; }
  .flex-md-grow-0 {
    flex-grow: 0 !important; }
  .flex-md-grow-1 {
    flex-grow: 1 !important; }
  .flex-md-shrink-0 {
    flex-shrink: 0 !important; }
  .flex-md-shrink-1 {
    flex-shrink: 1 !important; }
  .justify-content-md-start {
    justify-content: flex-start !important; }
  .justify-content-md-end {
    justify-content: flex-end !important; }
  .justify-content-md-center {
    justify-content: center !important; }
  .justify-content-md-between {
    justify-content: space-between !important; }
  .justify-content-md-around {
    justify-content: space-around !important; }
  .align-items-md-start {
    align-items: flex-start !important; }
  .align-items-md-end {
    align-items: flex-end !important; }
  .align-items-md-center {
    align-items: center !important; }
  .align-items-md-baseline {
    align-items: baseline !important; }
  .align-items-md-stretch {
    align-items: stretch !important; }
  .align-content-md-start {
    align-content: flex-start !important; }
  .align-content-md-end {
    align-content: flex-end !important; }
  .align-content-md-center {
    align-content: center !important; }
  .align-content-md-between {
    align-content: space-between !important; }
  .align-content-md-around {
    align-content: space-around !important; }
  .align-content-md-stretch {
    align-content: stretch !important; }
  .align-self-md-auto {
    align-self: auto !important; }
  .align-self-md-start {
    align-self: flex-start !important; }
  .align-self-md-end {
    align-self: flex-end !important; }
  .align-self-md-center {
    align-self: center !important; }
  .align-self-md-baseline {
    align-self: baseline !important; }
  .align-self-md-stretch {
    align-self: stretch !important; } }

@media (min-width: 992px) {
  .flex-lg-row {
    flex-direction: row !important; }
  .flex-lg-column {
    flex-direction: column !important; }
  .flex-lg-row-reverse {
    flex-direction: row-reverse !important; }
  .flex-lg-column-reverse {
    flex-direction: column-reverse !important; }
  .flex-lg-wrap {
    flex-wrap: wrap !important; }
  .flex-lg-nowrap {
    flex-wrap: nowrap !important; }
  .flex-lg-wrap-reverse {
    flex-wrap: wrap-reverse !important; }
  .flex-lg-fill {
    flex: 1 1 auto !important; }
  .flex-lg-grow-0 {
    flex-grow: 0 !important; }
  .flex-lg-grow-1 {
    flex-grow: 1 !important; }
  .flex-lg-shrink-0 {
    flex-shrink: 0 !important; }
  .flex-lg-shrink-1 {
    flex-shrink: 1 !important; }
  .justify-content-lg-start {
    justify-content: flex-start !important; }
  .justify-content-lg-end {
    justify-content: flex-end !important; }
  .justify-content-lg-center {
    justify-content: center !important; }
  .justify-content-lg-between {
    justify-content: space-between !important; }
  .justify-content-lg-around {
    justify-content: space-around !important; }
  .align-items-lg-start {
    align-items: flex-start !important; }
  .align-items-lg-end {
    align-items: flex-end !important; }
  .align-items-lg-center {
    align-items: center !important; }
  .align-items-lg-baseline {
    align-items: baseline !important; }
  .align-items-lg-stretch {
    align-items: stretch !important; }
  .align-content-lg-start {
    align-content: flex-start !important; }
  .align-content-lg-end {
    align-content: flex-end !important; }
  .align-content-lg-center {
    align-content: center !important; }
  .align-content-lg-between {
    align-content: space-between !important; }
  .align-content-lg-around {
    align-content: space-around !important; }
  .align-content-lg-stretch {
    align-content: stretch !important; }
  .align-self-lg-auto {
    align-self: auto !important; }
  .align-self-lg-start {
    align-self: flex-start !important; }
  .align-self-lg-end {
    align-self: flex-end !important; }
  .align-self-lg-center {
    align-self: center !important; }
  .align-self-lg-baseline {
    align-self: baseline !important; }
  .align-self-lg-stretch {
    align-self: stretch !important; } }

@media (min-width: 1200px) {
  .flex-xl-row {
    flex-direction: row !important; }
  .flex-xl-column {
    flex-direction: column !important; }
  .flex-xl-row-reverse {
    flex-direction: row-reverse !important; }
  .flex-xl-column-reverse {
    flex-direction: column-reverse !important; }
  .flex-xl-wrap {
    flex-wrap: wrap !important; }
  .flex-xl-nowrap {
    flex-wrap: nowrap !important; }
  .flex-xl-wrap-reverse {
    flex-wrap: wrap-reverse !important; }
  .flex-xl-fill {
    flex: 1 1 auto !important; }
  .flex-xl-grow-0 {
    flex-grow: 0 !important; }
  .flex-xl-grow-1 {
    flex-grow: 1 !important; }
  .flex-xl-shrink-0 {
    flex-shrink: 0 !important; }
  .flex-xl-shrink-1 {
    flex-shrink: 1 !important; }
  .justify-content-xl-start {
    justify-content: flex-start !important; }
  .justify-content-xl-end {
    justify-content: flex-end !important; }
  .justify-content-xl-center {
    justify-content: center !important; }
  .justify-content-xl-between {
    justify-content: space-between !important; }
  .justify-content-xl-around {
    justify-content: space-around !important; }
  .align-items-xl-start {
    align-items: flex-start !important; }
  .align-items-xl-end {
    align-items: flex-end !important; }
  .align-items-xl-center {
    align-items: center !important; }
  .align-items-xl-baseline {
    align-items: baseline !important; }
  .align-items-xl-stretch {
    align-items: stretch !important; }
  .align-content-xl-start {
    align-content: flex-start !important; }
  .align-content-xl-end {
    align-content: flex-end !important; }
  .align-content-xl-center {
    align-content: center !important; }
  .align-content-xl-between {
    align-content: space-between !important; }
  .align-content-xl-around {
    align-content: space-around !important; }
  .align-content-xl-stretch {
    align-content: stretch !important; }
  .align-self-xl-auto {
    align-self: auto !important; }
  .align-self-xl-start {
    align-self: flex-start !important; }
  .align-self-xl-end {
    align-self: flex-end !important; }
  .align-self-xl-center {
    align-self: center !important; }
  .align-self-xl-baseline {
    align-self: baseline !important; }
  .align-self-xl-stretch {
    align-self: stretch !important; } }

.float-left {
  float: left !important; }

.float-right {
  float: right !important; }

.float-none {
  float: none !important; }

@media (min-width: 576px) {
  .float-sm-left {
    float: left !important; }
  .float-sm-right {
    float: right !important; }
  .float-sm-none {
    float: none !important; } }

@media (min-width: 768px) {
  .float-md-left {
    float: left !important; }
  .float-md-right {
    float: right !important; }
  .float-md-none {
    float: none !important; } }

@media (min-width: 992px) {
  .float-lg-left {
    float: left !important; }
  .float-lg-right {
    float: right !important; }
  .float-lg-none {
    float: none !important; } }

@media (min-width: 1200px) {
  .float-xl-left {
    float: left !important; }
  .float-xl-right {
    float: right !important; }
  .float-xl-none {
    float: none !important; } }

.position-static {
  position: static !important; }

.position-relative {
  position: relative !important; }

.position-absolute {
  position: absolute !important; }

.position-fixed {
  position: fixed !important; }

.position-sticky {
  position: sticky !important; }

.fixed-top {
  position: fixed;
  top: 0;
  right: 0;
  left: 0;
  z-index: 1030; }

.fixed-bottom {
  position: fixed;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1030; }

@supports (position: sticky) {
  .sticky-top {
    position: sticky;
    top: 0;
    z-index: 1020; } }

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0; }

.sr-only-focusable:active, .sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  overflow: visible;
  clip: auto;
  white-space: normal; }

.shadow-sm {
  box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075) !important; }

.shadow {
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15) !important; }

.shadow-lg {
  box-shadow: 0 1rem 3rem rgba(0, 0, 0, 0.175) !important; }

.shadow-none {
  box-shadow: none !important; }

.w-25 {
  width: 25% !important; }

.w-50 {
  width: 50% !important; }

.w-75 {
  width: 75% !important; }

.w-100 {
  width: 100% !important; }

.w-auto {
  width: auto !important; }

.h-25 {
  height: 25% !important; }

.h-50 {
  height: 50% !important; }

.h-75 {
  height: 75% !important; }

.h-100 {
  height: 100% !important; }

.h-auto {
  height: auto !important; }

.mw-100 {
  max-width: 100% !important; }

.mh-100 {
  max-height: 100% !important; }

.m-0 {
  margin: 0 !important; }

.mt-0,
.my-0 {
  margin-top: 0 !important; }

.mr-0,
.mx-0 {
  margin-right: 0 !important; }

.mb-0,
.my-0 {
  margin-bottom: 0 !important; }

.ml-0,
.mx-0 {
  margin-left: 0 !important; }

.m-1 {
  margin: 0.25rem !important; }

.mt-1,
.my-1 {
  margin-top: 0.25rem !important; }

.mr-1,
.mx-1 {
  margin-right: 0.25rem !important; }

.mb-1,
.my-1 {
  margin-bottom: 0.25rem !important; }

.ml-1,
.mx-1 {
  margin-left: 0.25rem !important; }

.m-2 {
  margin: 0.5rem !important; }

.mt-2,
.my-2 {
  margin-top: 0.5rem !important; }

.mr-2,
.mx-2 {
  margin-right: 0.5rem !important; }

.mb-2,
.my-2 {
  margin-bottom: 0.5rem !important; }

.ml-2,
.mx-2 {
  margin-left: 0.5rem !important; }

.m-3 {
  margin: 1rem !important; }

.mt-3,
.my-3 {
  margin-top: 1rem !important; }

.mr-3,
.mx-3 {
  margin-right: 1rem !important; }

.mb-3,
.my-3 {
  margin-bottom: 1rem !important; }

.ml-3,
.mx-3 {
  margin-left: 1rem !important; }

.m-4 {
  margin: 1.5rem !important; }

.mt-4,
.my-4 {
  margin-top: 1.5rem !important; }

.mr-4,
.mx-4 {
  margin-right: 1.5rem !important; }

.mb-4,
.my-4 {
  margin-bottom: 1.5rem !important; }

.ml-4,
.mx-4 {
  margin-left: 1.5rem !important; }

.m-5 {
  margin: 3rem !important; }

.mt-5,
.my-5 {
  margin-top: 3rem !important; }

.mr-5,
.mx-5 {
  margin-right: 3rem !important; }

.mb-5,
.my-5 {
  margin-bottom: 3rem !important; }

.ml-5,
.mx-5 {
  margin-left: 3rem !important; }

.p-0 {
  padding: 0 !important; }

.pt-0,
.py-0 {
  padding-top: 0 !important; }

.pr-0,
.px-0 {
  padding-right: 0 !important; }

.pb-0,
.py-0 {
  padding-bottom: 0 !important; }

.pl-0,
.px-0 {
  padding-left: 0 !important; }

.p-1 {
  padding: 0.25rem !important; }

.pt-1,
.py-1 {
  padding-top: 0.25rem !important; }

.pr-1,
.px-1 {
  padding-right: 0.25rem !important; }

.pb-1,
.py-1 {
  padding-bottom: 0.25rem !important; }

.pl-1,
.px-1 {
  padding-left: 0.25rem !important; }

.p-2 {
  padding: 0.5rem !important; }

.pt-2,
.py-2 {
  padding-top: 0.5rem !important; }

.pr-2,
.px-2 {
  padding-right: 0.5rem !important; }

.pb-2,
.py-2 {
  padding-bottom: 0.5rem !important; }

.pl-2,
.px-2 {
  padding-left: 0.5rem !important; }

.p-3 {
  padding: 1rem !important; }

.pt-3,
.py-3 {
  padding-top: 1rem !important; }

.pr-3,
.px-3 {
  padding-right: 1rem !important; }

.pb-3,
.py-3 {
  padding-bottom: 1rem !important; }

.pl-3,
.px-3 {
  padding-left: 1rem !important; }

.p-4 {
  padding: 1.5rem !important; }

.pt-4,
.py-4 {
  padding-top: 1.5rem !important; }

.pr-4,
.px-4 {
  padding-right: 1.5rem !important; }

.pb-4,
.py-4 {
  padding-bottom: 1.5rem !important; }

.pl-4,
.px-4 {
  padding-left: 1.5rem !important; }

.p-5 {
  padding: 3rem !important; }

.pt-5,
.py-5 {
  padding-top: 3rem !important; }

.pr-5,
.px-5 {
  padding-right: 3rem !important; }

.pb-5,
.py-5 {
  padding-bottom: 3rem !important; }

.pl-5,
.px-5 {
  padding-left: 3rem !important; }

.m-auto {
  margin: auto !important; }

.mt-auto,
.my-auto {
  margin-top: auto !important; }

.mr-auto,
.mx-auto {
  margin-right: auto !important; }

.mb-auto,
.my-auto {
  margin-bottom: auto !important; }

.ml-auto,
.mx-auto {
  margin-left: auto !important; }

@media (min-width: 576px) {
  .m-sm-0 {
    margin: 0 !important; }
  .mt-sm-0,
  .my-sm-0 {
    margin-top: 0 !important; }
  .mr-sm-0,
  .mx-sm-0 {
    margin-right: 0 !important; }
  .mb-sm-0,
  .my-sm-0 {
    margin-bottom: 0 !important; }
  .ml-sm-0,
  .mx-sm-0 {
    margin-left: 0 !important; }
  .m-sm-1 {
    margin: 0.25rem !important; }
  .mt-sm-1,
  .my-sm-1 {
    margin-top: 0.25rem !important; }
  .mr-sm-1,
  .mx-sm-1 {
    margin-right: 0.25rem !important; }
  .mb-sm-1,
  .my-sm-1 {
    margin-bottom: 0.25rem !important; }
  .ml-sm-1,
  .mx-sm-1 {
    margin-left: 0.25rem !important; }
  .m-sm-2 {
    margin: 0.5rem !important; }
  .mt-sm-2,
  .my-sm-2 {
    margin-top: 0.5rem !important; }
  .mr-sm-2,
  .mx-sm-2 {
    margin-right: 0.5rem !important; }
  .mb-sm-2,
  .my-sm-2 {
    margin-bottom: 0.5rem !important; }
  .ml-sm-2,
  .mx-sm-2 {
    margin-left: 0.5rem !important; }
  .m-sm-3 {
    margin: 1rem !important; }
  .mt-sm-3,
  .my-sm-3 {
    margin-top: 1rem !important; }
  .mr-sm-3,
  .mx-sm-3 {
    margin-right: 1rem !important; }
  .mb-sm-3,
  .my-sm-3 {
    margin-bottom: 1rem !important; }
  .ml-sm-3,
  .mx-sm-3 {
    margin-left: 1rem !important; }
  .m-sm-4 {
    margin: 1.5rem !important; }
  .mt-sm-4,
  .my-sm-4 {
    margin-top: 1.5rem !important; }
  .mr-sm-4,
  .mx-sm-4 {
    margin-right: 1.5rem !important; }
  .mb-sm-4,
  .my-sm-4 {
    margin-bottom: 1.5rem !important; }
  .ml-sm-4,
  .mx-sm-4 {
    margin-left: 1.5rem !important; }
  .m-sm-5 {
    margin: 3rem !important; }
  .mt-sm-5,
  .my-sm-5 {
    margin-top: 3rem !important; }
  .mr-sm-5,
  .mx-sm-5 {
    margin-right: 3rem !important; }
  .mb-sm-5,
  .my-sm-5 {
    margin-bottom: 3rem !important; }
  .ml-sm-5,
  .mx-sm-5 {
    margin-left: 3rem !important; }
  .p-sm-0 {
    padding: 0 !important; }
  .pt-sm-0,
  .py-sm-0 {
    padding-top: 0 !important; }
  .pr-sm-0,
  .px-sm-0 {
    padding-right: 0 !important; }
  .pb-sm-0,
  .py-sm-0 {
    padding-bottom: 0 !important; }
  .pl-sm-0,
  .px-sm-0 {
    padding-left: 0 !important; }
  .p-sm-1 {
    padding: 0.25rem !important; }
  .pt-sm-1,
  .py-sm-1 {
    padding-top: 0.25rem !important; }
  .pr-sm-1,
  .px-sm-1 {
    padding-right: 0.25rem !important; }
  .pb-sm-1,
  .py-sm-1 {
    padding-bottom: 0.25rem !important; }
  .pl-sm-1,
  .px-sm-1 {
    padding-left: 0.25rem !important; }
  .p-sm-2 {
    padding: 0.5rem !important; }
  .pt-sm-2,
  .py-sm-2 {
    padding-top: 0.5rem !important; }
  .pr-sm-2,
  .px-sm-2 {
    padding-right: 0.5rem !important; }
  .pb-sm-2,
  .py-sm-2 {
    padding-bottom: 0.5rem !important; }
  .pl-sm-2,
  .px-sm-2 {
    padding-left: 0.5rem !important; }
  .p-sm-3 {
    padding: 1rem !important; }
  .pt-sm-3,
  .py-sm-3 {
    padding-top: 1rem !important; }
  .pr-sm-3,
  .px-sm-3 {
    padding-right: 1rem !important; }
  .pb-sm-3,
  .py-sm-3 {
    padding-bottom: 1rem !important; }
  .pl-sm-3,
  .px-sm-3 {
    padding-left: 1rem !important; }
  .p-sm-4 {
    padding: 1.5rem !important; }
  .pt-sm-4,
  .py-sm-4 {
    padding-top: 1.5rem !important; }
  .pr-sm-4,
  .px-sm-4 {
    padding-right: 1.5rem !important; }
  .pb-sm-4,
  .py-sm-4 {
    padding-bottom: 1.5rem !important; }
  .pl-sm-4,
  .px-sm-4 {
    padding-left: 1.5rem !important; }
  .p-sm-5 {
    padding: 3rem !important; }
  .pt-sm-5,
  .py-sm-5 {
    padding-top: 3rem !important; }
  .pr-sm-5,
  .px-sm-5 {
    padding-right: 3rem !important; }
  .pb-sm-5,
  .py-sm-5 {
    padding-bottom: 3rem !important; }
  .pl-sm-5,
  .px-sm-5 {
    padding-left: 3rem !important; }
  .m-sm-auto {
    margin: auto !important; }
  .mt-sm-auto,
  .my-sm-auto {
    margin-top: auto !important; }
  .mr-sm-auto,
  .mx-sm-auto {
    margin-right: auto !important; }
  .mb-sm-auto,
  .my-sm-auto {
    margin-bottom: auto !important; }
  .ml-sm-auto,
  .mx-sm-auto {
    margin-left: auto !important; } }

@media (min-width: 768px) {
  .m-md-0 {
    margin: 0 !important; }
  .mt-md-0,
  .my-md-0 {
    margin-top: 0 !important; }
  .mr-md-0,
  .mx-md-0 {
    margin-right: 0 !important; }
  .mb-md-0,
  .my-md-0 {
    margin-bottom: 0 !important; }
  .ml-md-0,
  .mx-md-0 {
    margin-left: 0 !important; }
  .m-md-1 {
    margin: 0.25rem !important; }
  .mt-md-1,
  .my-md-1 {
    margin-top: 0.25rem !important; }
  .mr-md-1,
  .mx-md-1 {
    margin-right: 0.25rem !important; }
  .mb-md-1,
  .my-md-1 {
    margin-bottom: 0.25rem !important; }
  .ml-md-1,
  .mx-md-1 {
    margin-left: 0.25rem !important; }
  .m-md-2 {
    margin: 0.5rem !important; }
  .mt-md-2,
  .my-md-2 {
    margin-top: 0.5rem !important; }
  .mr-md-2,
  .mx-md-2 {
    margin-right: 0.5rem !important; }
  .mb-md-2,
  .my-md-2 {
    margin-bottom: 0.5rem !important; }
  .ml-md-2,
  .mx-md-2 {
    margin-left: 0.5rem !important; }
  .m-md-3 {
    margin: 1rem !important; }
  .mt-md-3,
  .my-md-3 {
    margin-top: 1rem !important; }
  .mr-md-3,
  .mx-md-3 {
    margin-right: 1rem !important; }
  .mb-md-3,
  .my-md-3 {
    margin-bottom: 1rem !important; }
  .ml-md-3,
  .mx-md-3 {
    margin-left: 1rem !important; }
  .m-md-4 {
    margin: 1.5rem !important; }
  .mt-md-4,
  .my-md-4 {
    margin-top: 1.5rem !important; }
  .mr-md-4,
  .mx-md-4 {
    margin-right: 1.5rem !important; }
  .mb-md-4,
  .my-md-4 {
    margin-bottom: 1.5rem !important; }
  .ml-md-4,
  .mx-md-4 {
    margin-left: 1.5rem !important; }
  .m-md-5 {
    margin: 3rem !important; }
  .mt-md-5,
  .my-md-5 {
    margin-top: 3rem !important; }
  .mr-md-5,
  .mx-md-5 {
    margin-right: 3rem !important; }
  .mb-md-5,
  .my-md-5 {
    margin-bottom: 3rem !important; }
  .ml-md-5,
  .mx-md-5 {
    margin-left: 3rem !important; }
  .p-md-0 {
    padding: 0 !important; }
  .pt-md-0,
  .py-md-0 {
    padding-top: 0 !important; }
  .pr-md-0,
  .px-md-0 {
    padding-right: 0 !important; }
  .pb-md-0,
  .py-md-0 {
    padding-bottom: 0 !important; }
  .pl-md-0,
  .px-md-0 {
    padding-left: 0 !important; }
  .p-md-1 {
    padding: 0.25rem !important; }
  .pt-md-1,
  .py-md-1 {
    padding-top: 0.25rem !important; }
  .pr-md-1,
  .px-md-1 {
    padding-right: 0.25rem !important; }
  .pb-md-1,
  .py-md-1 {
    padding-bottom: 0.25rem !important; }
  .pl-md-1,
  .px-md-1 {
    padding-left: 0.25rem !important; }
  .p-md-2 {
    padding: 0.5rem !important; }
  .pt-md-2,
  .py-md-2 {
    padding-top: 0.5rem !important; }
  .pr-md-2,
  .px-md-2 {
    padding-right: 0.5rem !important; }
  .pb-md-2,
  .py-md-2 {
    padding-bottom: 0.5rem !important; }
  .pl-md-2,
  .px-md-2 {
    padding-left: 0.5rem !important; }
  .p-md-3 {
    padding: 1rem !important; }
  .pt-md-3,
  .py-md-3 {
    padding-top: 1rem !important; }
  .pr-md-3,
  .px-md-3 {
    padding-right: 1rem !important; }
  .pb-md-3,
  .py-md-3 {
    padding-bottom: 1rem !important; }
  .pl-md-3,
  .px-md-3 {
    padding-left: 1rem !important; }
  .p-md-4 {
    padding: 1.5rem !important; }
  .pt-md-4,
  .py-md-4 {
    padding-top: 1.5rem !important; }
  .pr-md-4,
  .px-md-4 {
    padding-right: 1.5rem !important; }
  .pb-md-4,
  .py-md-4 {
    padding-bottom: 1.5rem !important; }
  .pl-md-4,
  .px-md-4 {
    padding-left: 1.5rem !important; }
  .p-md-5 {
    padding: 3rem !important; }
  .pt-md-5,
  .py-md-5 {
    padding-top: 3rem !important; }
  .pr-md-5,
  .px-md-5 {
    padding-right: 3rem !important; }
  .pb-md-5,
  .py-md-5 {
    padding-bottom: 3rem !important; }
  .pl-md-5,
  .px-md-5 {
    padding-left: 3rem !important; }
  .m-md-auto {
    margin: auto !important; }
  .mt-md-auto,
  .my-md-auto {
    margin-top: auto !important; }
  .mr-md-auto,
  .mx-md-auto {
    margin-right: auto !important; }
  .mb-md-auto,
  .my-md-auto {
    margin-bottom: auto !important; }
  .ml-md-auto,
  .mx-md-auto {
    margin-left: auto !important; } }

@media (min-width: 992px) {
  .m-lg-0 {
    margin: 0 !important; }
  .mt-lg-0,
  .my-lg-0 {
    margin-top: 0 !important; }
  .mr-lg-0,
  .mx-lg-0 {
    margin-right: 0 !important; }
  .mb-lg-0,
  .my-lg-0 {
    margin-bottom: 0 !important; }
  .ml-lg-0,
  .mx-lg-0 {
    margin-left: 0 !important; }
  .m-lg-1 {
    margin: 0.25rem !important; }
  .mt-lg-1,
  .my-lg-1 {
    margin-top: 0.25rem !important; }
  .mr-lg-1,
  .mx-lg-1 {
    margin-right: 0.25rem !important; }
  .mb-lg-1,
  .my-lg-1 {
    margin-bottom: 0.25rem !important; }
  .ml-lg-1,
  .mx-lg-1 {
    margin-left: 0.25rem !important; }
  .m-lg-2 {
    margin: 0.5rem !important; }
  .mt-lg-2,
  .my-lg-2 {
    margin-top: 0.5rem !important; }
  .mr-lg-2,
  .mx-lg-2 {
    margin-right: 0.5rem !important; }
  .mb-lg-2,
  .my-lg-2 {
    margin-bottom: 0.5rem !important; }
  .ml-lg-2,
  .mx-lg-2 {
    margin-left: 0.5rem !important; }
  .m-lg-3 {
    margin: 1rem !important; }
  .mt-lg-3,
  .my-lg-3 {
    margin-top: 1rem !important; }
  .mr-lg-3,
  .mx-lg-3 {
    margin-right: 1rem !important; }
  .mb-lg-3,
  .my-lg-3 {
    margin-bottom: 1rem !important; }
  .ml-lg-3,
  .mx-lg-3 {
    margin-left: 1rem !important; }
  .m-lg-4 {
    margin: 1.5rem !important; }
  .mt-lg-4,
  .my-lg-4 {
    margin-top: 1.5rem !important; }
  .mr-lg-4,
  .mx-lg-4 {
    margin-right: 1.5rem !important; }
  .mb-lg-4,
  .my-lg-4 {
    margin-bottom: 1.5rem !important; }
  .ml-lg-4,
  .mx-lg-4 {
    margin-left: 1.5rem !important; }
  .m-lg-5 {
    margin: 3rem !important; }
  .mt-lg-5,
  .my-lg-5 {
    margin-top: 3rem !important; }
  .mr-lg-5,
  .mx-lg-5 {
    margin-right: 3rem !important; }
  .mb-lg-5,
  .my-lg-5 {
    margin-bottom: 3rem !important; }
  .ml-lg-5,
  .mx-lg-5 {
    margin-left: 3rem !important; }
  .p-lg-0 {
    padding: 0 !important; }
  .pt-lg-0,
  .py-lg-0 {
    padding-top: 0 !important; }
  .pr-lg-0,
  .px-lg-0 {
    padding-right: 0 !important; }
  .pb-lg-0,
  .py-lg-0 {
    padding-bottom: 0 !important; }
  .pl-lg-0,
  .px-lg-0 {
    padding-left: 0 !important; }
  .p-lg-1 {
    padding: 0.25rem !important; }
  .pt-lg-1,
  .py-lg-1 {
    padding-top: 0.25rem !important; }
  .pr-lg-1,
  .px-lg-1 {
    padding-right: 0.25rem !important; }
  .pb-lg-1,
  .py-lg-1 {
    padding-bottom: 0.25rem !important; }
  .pl-lg-1,
  .px-lg-1 {
    padding-left: 0.25rem !important; }
  .p-lg-2 {
    padding: 0.5rem !important; }
  .pt-lg-2,
  .py-lg-2 {
    padding-top: 0.5rem !important; }
  .pr-lg-2,
  .px-lg-2 {
    padding-right: 0.5rem !important; }
  .pb-lg-2,
  .py-lg-2 {
    padding-bottom: 0.5rem !important; }
  .pl-lg-2,
  .px-lg-2 {
    padding-left: 0.5rem !important; }
  .p-lg-3 {
    padding: 1rem !important; }
  .pt-lg-3,
  .py-lg-3 {
    padding-top: 1rem !important; }
  .pr-lg-3,
  .px-lg-3 {
    padding-right: 1rem !important; }
  .pb-lg-3,
  .py-lg-3 {
    padding-bottom: 1rem !important; }
  .pl-lg-3,
  .px-lg-3 {
    padding-left: 1rem !important; }
  .p-lg-4 {
    padding: 1.5rem !important; }
  .pt-lg-4,
  .py-lg-4 {
    padding-top: 1.5rem !important; }
  .pr-lg-4,
  .px-lg-4 {
    padding-right: 1.5rem !important; }
  .pb-lg-4,
  .py-lg-4 {
    padding-bottom: 1.5rem !important; }
  .pl-lg-4,
  .px-lg-4 {
    padding-left: 1.5rem !important; }
  .p-lg-5 {
    padding: 3rem !important; }
  .pt-lg-5,
  .py-lg-5 {
    padding-top: 3rem !important; }
  .pr-lg-5,
  .px-lg-5 {
    padding-right: 3rem !important; }
  .pb-lg-5,
  .py-lg-5 {
    padding-bottom: 3rem !important; }
  .pl-lg-5,
  .px-lg-5 {
    padding-left: 3rem !important; }
  .m-lg-auto {
    margin: auto !important; }
  .mt-lg-auto,
  .my-lg-auto {
    margin-top: auto !important; }
  .mr-lg-auto,
  .mx-lg-auto {
    margin-right: auto !important; }
  .mb-lg-auto,
  .my-lg-auto {
    margin-bottom: auto !important; }
  .ml-lg-auto,
  .mx-lg-auto {
    margin-left: auto !important; } }

@media (min-width: 1200px) {
  .m-xl-0 {
    margin: 0 !important; }
  .mt-xl-0,
  .my-xl-0 {
    margin-top: 0 !important; }
  .mr-xl-0,
  .mx-xl-0 {
    margin-right: 0 !important; }
  .mb-xl-0,
  .my-xl-0 {
    margin-bottom: 0 !important; }
  .ml-xl-0,
  .mx-xl-0 {
    margin-left: 0 !important; }
  .m-xl-1 {
    margin: 0.25rem !important; }
  .mt-xl-1,
  .my-xl-1 {
    margin-top: 0.25rem !important; }
  .mr-xl-1,
  .mx-xl-1 {
    margin-right: 0.25rem !important; }
  .mb-xl-1,
  .my-xl-1 {
    margin-bottom: 0.25rem !important; }
  .ml-xl-1,
  .mx-xl-1 {
    margin-left: 0.25rem !important; }
  .m-xl-2 {
    margin: 0.5rem !important; }
  .mt-xl-2,
  .my-xl-2 {
    margin-top: 0.5rem !important; }
  .mr-xl-2,
  .mx-xl-2 {
    margin-right: 0.5rem !important; }
  .mb-xl-2,
  .my-xl-2 {
    margin-bottom: 0.5rem !important; }
  .ml-xl-2,
  .mx-xl-2 {
    margin-left: 0.5rem !important; }
  .m-xl-3 {
    margin: 1rem !important; }
  .mt-xl-3,
  .my-xl-3 {
    margin-top: 1rem !important; }
  .mr-xl-3,
  .mx-xl-3 {
    margin-right: 1rem !important; }
  .mb-xl-3,
  .my-xl-3 {
    margin-bottom: 1rem !important; }
  .ml-xl-3,
  .mx-xl-3 {
    margin-left: 1rem !important; }
  .m-xl-4 {
    margin: 1.5rem !important; }
  .mt-xl-4,
  .my-xl-4 {
    margin-top: 1.5rem !important; }
  .mr-xl-4,
  .mx-xl-4 {
    margin-right: 1.5rem !important; }
  .mb-xl-4,
  .my-xl-4 {
    margin-bottom: 1.5rem !important; }
  .ml-xl-4,
  .mx-xl-4 {
    margin-left: 1.5rem !important; }
  .m-xl-5 {
    margin: 3rem !important; }
  .mt-xl-5,
  .my-xl-5 {
    margin-top: 3rem !important; }
  .mr-xl-5,
  .mx-xl-5 {
    margin-right: 3rem !important; }
  .mb-xl-5,
  .my-xl-5 {
    margin-bottom: 3rem !important; }
  .ml-xl-5,
  .mx-xl-5 {
    margin-left: 3rem !important; }
  .p-xl-0 {
    padding: 0 !important; }
  .pt-xl-0,
  .py-xl-0 {
    padding-top: 0 !important; }
  .pr-xl-0,
  .px-xl-0 {
    padding-right: 0 !important; }
  .pb-xl-0,
  .py-xl-0 {
    padding-bottom: 0 !important; }
  .pl-xl-0,
  .px-xl-0 {
    padding-left: 0 !important; }
  .p-xl-1 {
    padding: 0.25rem !important; }
  .pt-xl-1,
  .py-xl-1 {
    padding-top: 0.25rem !important; }
  .pr-xl-1,
  .px-xl-1 {
    padding-right: 0.25rem !important; }
  .pb-xl-1,
  .py-xl-1 {
    padding-bottom: 0.25rem !important; }
  .pl-xl-1,
  .px-xl-1 {
    padding-left: 0.25rem !important; }
  .p-xl-2 {
    padding: 0.5rem !important; }
  .pt-xl-2,
  .py-xl-2 {
    padding-top: 0.5rem !important; }
  .pr-xl-2,
  .px-xl-2 {
    padding-right: 0.5rem !important; }
  .pb-xl-2,
  .py-xl-2 {
    padding-bottom: 0.5rem !important; }
  .pl-xl-2,
  .px-xl-2 {
    padding-left: 0.5rem !important; }
  .p-xl-3 {
    padding: 1rem !important; }
  .pt-xl-3,
  .py-xl-3 {
    padding-top: 1rem !important; }
  .pr-xl-3,
  .px-xl-3 {
    padding-right: 1rem !important; }
  .pb-xl-3,
  .py-xl-3 {
    padding-bottom: 1rem !important; }
  .pl-xl-3,
  .px-xl-3 {
    padding-left: 1rem !important; }
  .p-xl-4 {
    padding: 1.5rem !important; }
  .pt-xl-4,
  .py-xl-4 {
    padding-top: 1.5rem !important; }
  .pr-xl-4,
  .px-xl-4 {
    padding-right: 1.5rem !important; }
  .pb-xl-4,
  .py-xl-4 {
    padding-bottom: 1.5rem !important; }
  .pl-xl-4,
  .px-xl-4 {
    padding-left: 1.5rem !important; }
  .p-xl-5 {
    padding: 3rem !important; }
  .pt-xl-5,
  .py-xl-5 {
    padding-top: 3rem !important; }
  .pr-xl-5,
  .px-xl-5 {
    padding-right: 3rem !important; }
  .pb-xl-5,
  .py-xl-5 {
    padding-bottom: 3rem !important; }
  .pl-xl-5,
  .px-xl-5 {
    padding-left: 3rem !important; }
  .m-xl-auto {
    margin: auto !important; }
  .mt-xl-auto,
  .my-xl-auto {
    margin-top: auto !important; }
  .mr-xl-auto,
  .mx-xl-auto {
    margin-right: auto !important; }
  .mb-xl-auto,
  .my-xl-auto {
    margin-bottom: auto !important; }
  .ml-xl-auto,
  .mx-xl-auto {
    margin-left: auto !important; } }

.text-monospace {
  font-family: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; }

.text-justify {
  text-align: justify !important; }

.text-nowrap {
  white-space: nowrap !important; }

.text-truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap; }

.text-left {
  text-align: left !important; }

.text-right {
  text-align: right !important; }

.text-center {
  text-align: center !important; }

@media (min-width: 576px) {
  .text-sm-left {
    text-align: left !important; }
  .text-sm-right {
    text-align: right !important; }
  .text-sm-center {
    text-align: center !important; } }

@media (min-width: 768px) {
  .text-md-left {
    text-align: left !important; }
  .text-md-right {
    text-align: right !important; }
  .text-md-center {
    text-align: center !important; } }

@media (min-width: 992px) {
  .text-lg-left {
    text-align: left !important; }
  .text-lg-right {
    text-align: right !important; }
  .text-lg-center {
    text-align: center !important; } }

@media (min-width: 1200px) {
  .text-xl-left {
    text-align: left !important; }
  .text-xl-right {
    text-align: right !important; }
  .text-xl-center {
    text-align: center !important; } }

.text-lowercase {
  text-transform: lowercase !important; }

.text-uppercase {
  text-transform: uppercase !important; }

.text-capitalize {
  text-transform: capitalize !important; }

.font-weight-light {
  font-weight: 300 !important; }

.font-weight-normal {
  font-weight: 400 !important; }

.font-weight-bold {
  font-weight: 700 !important; }

.font-italic {
  font-style: italic !important; }

.text-white {
  color: #fff !important; }

.text-primary {
  color: #10284e !important; }

a.text-primary:hover, a.text-primary:focus {
  color: #071224 !important; }

.text-secondary {
  color: #30caa0 !important; }

a.text-secondary:hover, a.text-secondary:focus {
  color: #26a17f !important; }

.text-success {
  color: #20c997 !important; }

a.text-success:hover, a.text-success:focus {
  color: #199d76 !important; }

.text-info {
  color: #17a2b8 !important; }

a.text-info:hover, a.text-info:focus {
  color: #117a8b !important; }

.text-warning {
  color: #ffc107 !important; }

a.text-warning:hover, a.text-warning:focus {
  color: #d39e00 !important; }

.text-danger {
  color: #e94646 !important; }

a.text-danger:hover, a.text-danger:focus {
  color: #e11b1b !important; }

.text-light {
  color: #f8f9fa !important; }

a.text-light:hover, a.text-light:focus {
  color: #dae0e5 !important; }

.text-dark {
  color: #343a40 !important; }

a.text-dark:hover, a.text-dark:focus {
  color: #1d2124 !important; }

.text-body {
  color: #212529 !important; }

.text-muted {
  color: #6c757d !important; }

.text-black-50 {
  color: rgba(0, 0, 0, 0.5) !important; }

.text-white-50 {
  color: rgba(255, 255, 255, 0.5) !important; }

.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0; }

.visible {
  visibility: visible !important; }

.invisible {
  visibility: hidden !important; }

@media print {
  *,
  *::before,
  *::after {
    text-shadow: none !important;
    box-shadow: none !important; }
  a:not(.btn) {
    text-decoration: underline; }
  abbr[title]::after {
    content: " (" attr(title) ")"; }
  pre {
    white-space: pre-wrap !important; }
  pre,
  blockquote {
    border: 1px solid #adb5bd;
    page-break-inside: avoid; }
  thead {
    display: table-header-group; }
  tr,
  img {
    page-break-inside: avoid; }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3; }
  h2,
  h3 {
    page-break-after: avoid; }
  @page {
    size: a3; }
  body {
    min-width: 992px !important; }
  .container {
    min-width: 992px !important; }
  .navbar {
    display: none; }
  .badge {
    border: 1px solid #000; }
  .table {
    border-collapse: collapse !important; }
    .table td,
    .table th {
      background-color: #fff !important; }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #dee2e6 !important; }
  .table-dark {
    color: inherit; }
    .table-dark th,
    .table-dark td,
    .table-dark thead th,
    .table-dark tbody + tbody {
      border-color: #dee2e6; }
  .table .thead-dark th {
    color: inherit;
    border-color: #dee2e6; } }

```  
3. btre/static/css/lightbox.min.css  
```
.lb-loader,
.lightbox {
  text-align: center;
  line-height: 0;
}
.lb-dataContainer:after,
.lb-outerContainer:after {
  content: '';
  clear: both;
}
html.lb-disable-scrolling {
  overflow: hidden;
  position: fixed;
  height: 100vh;
  width: 100vw;
}
.lightboxOverlay {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 9999;
  background-color: #000;
  filter: alpha(Opacity=80);
  opacity: 0.8;
  display: none;
}
.lightbox {
  position: absolute;
  left: 0;
  width: 100%;
  z-index: 10000;
  font-weight: 400;
}
.lightbox .lb-image {
  display: block;
  height: auto;
  max-width: inherit;
  max-height: none;
  border-radius: 3px;
  border: 4px solid #fff;
}
.lightbox a img {
  border: none;
}
.lb-outerContainer {
  position: relative;
  width: 250px;
  height: 250px;
  margin: 0 auto;
  border-radius: 4px;
  background-color: #fff;
}
.lb-loader,
.lb-nav {
  position: absolute;
  left: 0;
}
.lb-outerContainer:after {
  display: table;
}
.lb-loader {
  top: 43%;
  height: 25%;
  width: 100%;
}
.lb-cancel {
  display: block;
  width: 32px;
  height: 32px;
  margin: 0 auto;
  background: url(../images/loading.gif) no-repeat;
}
.lb-nav {
  top: 0;
  height: 100%;
  width: 100%;
  z-index: 10;
}
.lb-container > .nav {
  left: 0;
}
.lb-nav a {
  outline: 0;
  background-image: url(data:image/gif;base64,R0lGODlhAQABAPAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==);
}
.lb-next,
.lb-prev {
  height: 100%;
  cursor: pointer;
  display: block;
}
.lb-nav a.lb-prev {
  width: 34%;
  left: 0;
  float: left;
  background: url(../img/lightbox/prev.png) left 48% no-repeat;
  filter: alpha(Opacity=0);
  opacity: 0;
  -webkit-transition: opacity 0.6s;
  -moz-transition: opacity 0.6s;
  -o-transition: opacity 0.6s;
  transition: opacity 0.6s;
}
.lb-nav a.lb-prev:hover {
  filter: alpha(Opacity=100);
  opacity: 1;
}
.lb-nav a.lb-next {
  width: 64%;
  right: 0;
  float: right;
  background: url(../img/lightbox/next.png) right 48% no-repeat;
  filter: alpha(Opacity=0);
  opacity: 0;
  -webkit-transition: opacity 0.6s;
  -moz-transition: opacity 0.6s;
  -o-transition: opacity 0.6s;
  transition: opacity 0.6s;
}
.lb-nav a.lb-next:hover {
  filter: alpha(Opacity=100);
  opacity: 1;
}
.lb-dataContainer {
  margin: 0 auto;
  padding-top: 5px;
  width: 100%;
  border-bottom-left-radius: 4px;
  border-bottom-right-radius: 4px;
}
.lb-dataContainer:after {
  display: table;
}
.lb-data {
  padding: 0 4px;
  color: #ccc;
}
.lb-data .lb-details {
  width: 85%;
  float: left;
  text-align: left;
  line-height: 1.1em;
}
.lb-data .lb-caption {
  font-size: 13px;
  font-weight: 700;
  line-height: 1em;
}
.lb-data .lb-caption a {
  color: #4ae;
}
.lb-data .lb-number {
  display: block;
  clear: left;
  padding-bottom: 1em;
  font-size: 12px;
  color: #999;
}
.lb-data .lb-close {
  display: block;
  float: right;
  width: 30px;
  height: 30px;
  background: url(../img/lightbox/close.png) top right no-repeat;
  text-align: right;
  outline: 0;
  filter: alpha(Opacity=70);
  opacity: 0.7;
  -webkit-transition: opacity 0.2s;
  -moz-transition: opacity 0.2s;
  -o-transition: opacity 0.2s;
  transition: opacity 0.2s;
}
.lb-data .lb-close:hover {
  cursor: pointer;
  filter: alpha(Opacity=100);
  opacity: 1;
}

```
4. btre/static/css/style.css  
```
.btn-secondary {
  color: #fff !important; }

img {
  width: 100%; }

.logo {
  width: 80px; }

.navbar {
  opacity: 0.9;
  text-transform: uppercase; }

.social a {
  margin-right: 0.4rem; }

#showcase {
  background: url(../img/showcase.jpg) no-repeat top center fixed/cover;
  position: relative;
  min-height: 650px;
  color: #fff;
  padding-top: 6rem; }
  #showcase .home-search {
    min-height: 400px;
    position: relative;
    border-radius: 5px; }
  #showcase .overlay {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    min-height: 400px;
    width: 100%;
    background: rgba(51, 51, 51, 0.8); }

#services {
  background: url(../img/building.jpg) no-repeat top center fixed/cover;
  min-height: 300px;
  position: relative;
  overflow: hidden; }
  #services::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    min-height: 100%;
    width: 100%;
    background: rgba(32, 134, 107, 0.8); }

#showcase-inner {
  background: url(../img/building.jpg) no-repeat top center fixed/cover;
  position: relative;
  overflow: hidden;
  min-height: 200px; }
  #showcase-inner::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    min-height: 100%;
    width: 100%;
    background: rgba(32, 134, 107, 0.8); }
  #showcase-inner.showcase-search {
    min-height: 270px; }

#work {
  padding: 6rem 0; }

.listing-preview a {
  position: relative; }

@media (max-width: 991px) {
  #showcase {
    padding-top: 4rem; }
    #showcase h1 {
      font-size: 40px; }
  .hide-md-down {
    display: none; } }

@media (max-width: 768px) {
  #showcase {
    padding-top: 3rem; }
    #showcase h1 {
      font-size: 40px; }
    #showcase p {
      display: none; }
  #top-bar {
    text-align: center; }
    #top-bar .social {
      text-align: center !important; } }

@media (max-width: 576px) {
  #showcase h1 {
    font-size: 30px; }
  #showcase-inner h1 {
    font-size: 40px; } }

```

----

####  listings.html 最後修改  - 12549

1.  listings/views.py  
```
from django.shortcuts import render
from django.core.paginator import EmptyPage , PageNotAnInteger , Paginator  //增加
from .models import Listing
# Create your views here.


def index(request):
    listings = Listing.objects.all()  
    paginator = Paginator(listings, 3)  //增加
    page = request.GET.get('page')  //增加
    paged_listings = paginator.get_page(page)  //增加
    context = {
        'listings': paged_listings  //改了 paged_listings
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id): //改了 listing_id
    return render(request,'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html') 
```

2. templates/listings/listings.html  
```
{% extends 'base.html' %}
{% load humanize %}
{% block title %} | Browse Property Listings{% endblock %} //加了
{% block content %}
<section id="showcase-inner" class="py-5 text-white">
  <div class="container">
    <div class="row text-center">
      <div class="col-md-12">
        <h1 class="display-4">Browse Our Properties</h1>
        <p class="lead">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Sunt, pariatur!</p>
      </div>
    </div>
  </div>
</section>

<!-- Breadcrumb -->
<section id="bc" class="mt-3">
  <div class="container">
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item">
          <a href="{% url 'index' %}">
            <i class="fas fa-home"></i> Home</a>
        </li>
        <li class="breadcrumb-item active"> Browse Listings</li>
      </ol>
    </nav>
  </div>
</section>

<!-- Listings -->

<section id="listings" class="py-4">
  <div class="container">
    <div class="row">

      <!-- Listing 1 -->
{% if listings %}

{% for listing in listings %}

      <div class="col-md-6 col-lg-4 mb-4">
        <div class="card listing-preview">
          <img class="card-img-top" src="{{listing.photo_main.url}}" alt="">
          <div class="card-img-overlay">
            <h2>
              <span class="badge badge-secondary text-white">${{listing.price | intcomma}}</span>
            </h2>
          </div>
          <div class="card-body">
            <div class="listing-heading text-center">
              <h4 class="text-primary">{{listing.title}}</h4>
              <p>
                <i class="fas fa-map-marker text-secondary"></i>{{listing.city}}  {{listing.state}}  {{listing.zipcode}}</p>  加了空白
            </div>
            <hr>
            <div class="row py-2 text-secondary">
              <div class="col-6">
                <i class="fas fa-th-large"></i> Sqft: {{listing.zipcode}}</div>
              <div class="col-6">
                <i class="fas fa-car"></i> Garage: {{listing.garage}}</div>
            </div>
            <div class="row py-2 text-secondary">
              <div class="col-6">
                <i class="fas fa-bed"></i> Bedrooms: {{listing.bedrooms}}</div>
              <div class="col-6">
                <i class="fas fa-bath"></i> Bathrooms: {{listing.bathrooms}}</div> // bathroom 改了 bathrooms
            </div>
            <hr>
            <div class="row py-2 text-secondary">
              <div class="col-12">
                <i class="fas fa-user"></i> {{listing.realtor}}</div>
            </div>
            <div class="row text-secondary pb-2">
              <div class="col-6">
                <i c2 days agolass="fas fa-clock"></i> {{ listing.list_date | timesince }}</div>
            </div>
            <hr>
            <a href="{% url 'listing' listing.id %}" class="btn btn-primary btn-block">More Info</a>
          </div>
        </div>
      </div>
      {% endfor %} {% else %}
      <div class="col-md-12">
        <!--No data then display no data message -->
        <p>No Listings Available</p>
        </div>
        {% endif %}
        </div>
   

    <div class="row">
      <div class="col-md-12">
        {% if listings.has_other_pages %} //增加
        <ul class="pagination">
          {% if listings.has_previous %} //增加
          <li class="page-items">
            <a
            href="?page={{listings.previous_page_number}}" //增加
            class="page-link"
            >&laquo;</a>
            </li>
            {% else %} //增加

          <li class="page-item disabled">
            <a class="page-link">&laquo;</a>
          </li>
          {% endif %}
          {% for i in listings.paginator.gage_range %} //增加
          {% if listings.number == i %} //增加
          <li class="page-item active">
            <a class="page-link">{{i}}</a> //增加
          </li>
          {% else %} //增加
          <li class="page-item">
            <a href="?page={{i}}" class="page-link">{{i}}</a> //增加
            </li>
            {% endif %} //增加
            {% endfor %} //增加

            {% if listings.has_next %}   //增加         

          <li class="page-item">
            <a class="page-link" href="?page={{listings.next_page_number}} ">&raquo;</a> //改了
          </li>
          {% else %} //增加
          <li class="page-item disabled">
            <a class="page-link">&raquo;</a>
            </li>
            {% endif %} //增加
        </ul>
        {% endif %}
      </div>
    </div>
  </div>
</section>
{% endblock content %}
```
---

