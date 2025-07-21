# Employee_Management_System

# create in a github new Repository and the Repository name is Employee_Management_System.

# uskai baad go to the code and copy HTTPS link https://github.com/GYANENDRA8080/Employee_Management_System.git and then paste in vs code clone git repository.

# for django project create virtual environment folder using command python -m venv envfoldername.

# and then activate env folder using command in terminal env\Scripts\activate env folder is activated.

# now uskai baad create kiya maine Employee_Management_System  folder mai .gitignore file aur usmai apne env folder ko daal diya *myenv ese.

# ab maine Employee_Management_System is directory kai pass aa kar maine ek command chalaya terminal mai pip install django yeh command chalane sai django install ho gya mere virtual envirnoment mai.

# ab muje dekhna hai kie mere virtual environment mai kaun kaun sa package install hai toh use karunga command in terminal pip freeze yeh command run karne si muje pta chal jayega kie kun kun sa package install hai mere virtual environment mai.

# ab mai chahat hu kie jitna bhi package install hai mere virtual environment mai wo ek file crete ho jaye aur usmai sabhi package ka naam as a version chala jaye uskai liye command use karunga pip freeze>requirements.txt yeh command run karne sai automatically mere folder mai ek requirements.txt naam ka folder ban jayega aur usmai sabi package chale jayenge 

# pip freeze > requirements.txt is command ko as it is run karna karna hai ab ismai jitne packages hai ab mai jab kabi dure system par yeh project run karunga toh    pip install -r requirements.txt yeh command likh dene sai bas mera sabi kuch install ho jayega jo ish project kai liye jaruri hai lekin pahle hame virtual environmenent create karna hoga aur use activate karna hoga then hum ish command ko use karenge.

# ab hum apna project create karenge using this command django-admin startproject project_name . => hum project_name kai baad . isliye lagayege kie hamene jo naam sai pale ek folder banaya hai same ushi folder mai bane na kie ush folder mai ek aur folder mai project bane.

# django-admin startproject employeemanagement . yeh command use karne sai mera project ban jayega ish Employee_Management_System folder mai.

# ab hum dekhege kie mera django project run kar raha hai kie nhi uskai liye hum command use karenge python manage.py runserver lekin hum apna command wahi run karge jaha hamare yeh file hoga iskai liye hame ush directory mai jana hoga jaha hamara django ka project hai.

# python manage.py runserver, agar hame apne project ko kisi specific port par run kar karna hi toh python manage.py runserver 4000 yaha jo port likhenge ush port par chalnne lagega yeh command chalane sai mera django ka server run ho jata hai hai aur db.sqlite3 ka file automatich chal jata hai http://127.0.0.1:8000/ ish url par jane sai mera project ka start dikhta hai.

# hame apne project folder kai jitne file hai usmai kuch nhi karna hai bas hame settings.py file aur urls.py file inh dono mai jo karna hai wo karna hai baki kisi aur file mai nhi.

# agar hum apne ish project ko next day run karna chahta hu toh mai pale ish project ko apne vs - code mai open karunga aur virtualenv ko activate karunga aur python manage.py runserver kar dunga mera project run ho jayega.

# ab hum apne project mai kai saare aplication bana sakte hai using manage.py file ish file mai hum kuch nhi karte hai yeh file as it is rakhte hai. ab hame apne project mai ek application create karna hai toh use karenge command python manage,py startapp appname

# manage.py file is a django command-line utility for administrative task jiska use kar kai hum log sara kaam karte hai apne project ka, jaise {static file, server run, application create karna} ish file sai karte hai.

# Django application group of application mil kar django project banata hai. ek django project mai ek ya ek sai adkin application bana sakte hai apne requirement kai behalf par.

# python manage.py startapp emp_app ish command ko run karne sai terminal par ek app create ho jayega hamre project mai yeh command run karte hie hamare project mai ek app create ho jata hai.

# emp_app ek hamara app create ho gya hamre project mai. ab ish app ko hame pahle apne project kai settings.py file mai register karna hoga INSTALLED_APPS mai hum emp_app ek list mai mention kar denge.

# project mai jo settings.py file hai aur urls.py file hai isko hum apne jarurat kai behalf par change karte hai. 

# setting.py - this file contains all the information or data about project settings. ex- database configuration information, templates, installed application, validators etc.

# urls.py - this file contains informations of url attached with application.

# urls.py - yeh file hame apne har application mai banaa padat hai manually. apne appliaction kai folder mai jaaa kar create new file karte hai aur uska naam urls.py file hie dete hai. aur apne application wale urls.py file ko apne django project kai urls.py file sai isko map karte hai.

# urls.py- urls.py file mapping hoti hai kie kun sa url fire karne par kaun sa views function chalega.

# apne project kai urls.py file mai yeh line rahat hai pahle sai bas ismai hum {aage inclue likh dete hai cooma laga kar} from django.urls import path,include [include lets you connect your main project's URLs to your app's URLs, so you can organize routes for each app separately.] ab hum uskai nice yeh wala line likhte hai,[ path('', include('emp_app.urls'))] This line connects your main project’s root URL to all the routes defined in your emp_app app.

# ab hum jo apne app mai urls banaye hai usmai bhi yeh linke likhte hai [from django.urls import path, include] [ from emp_app import views] aur usmai ek urlpatterns [] iski list bana kar usmai apan urls ka path dete hai. apan jo view function banate hai usko apne app wale urls sai map karte hai.

#
