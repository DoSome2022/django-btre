## python django 指南

part2 - 181  
part3 - 223  
part4 - 272  
part5 - 377  
part6 - 568    
part7 - 729  
part8 - 1355  




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

