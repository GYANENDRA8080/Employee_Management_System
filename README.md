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

# apne app mai ek url banaye uskai baad uska view function banaye and then maine apne project kai app mai ja kar ek folder banaya templates naam ka aur uskmai ek file banaya html kai index.html ab project ko run kiya tho toh mera app ka url hit ho gya aur uska jo bhi view function tha wo chal gaya.

# itna sab kuch karne kai baad ab hum models.py file mai kaam karenge apna database banayenge. apna sabhi fileld banane kai baad ab hum python manage.py makemigrations yeh command run karne sai hamre app mai ek migration ka file bn jayega python manage.py migrate yeh command run karne sai hamara table bn jayega.

# modal create karne kai baad yeh optionl bhi hoti hai kar bhi skate ho nhi bhi kar skte ho lekin karne sai hum apna data save kar sakte hai admin panal sai bhi. admin.py file mai apna modal register karne sai hum apna data admin interface kai throw data daal sakte hai.

# admin.py file mai apna sabil modal ka class register karna hota hai. ab register karne kai baad hum usko acces karne kai liye super user create karte hai. using command in terminal python manage.py createsuperuser yeh command use karte hai. 

# super create karne kai baad aur usmai jo cradiantial managa hai usko dene kai baad ab apna project run karte hai usmai uskai baad apne url ko open karte hai and then usmai apna cradiantioal dalte hai toh mera djano admin ka dashboard open ho jata hai ab hum apne db mai user interface kie help sai data insert kar sakte hai.

# mera modal ban gya admin panal open ho raha hai aur manuualy data save kar diya hu bahut saare.

# now jo muje display karwana hai apne web page mai uska kaam karna hai templates mai. uskai liye hum use karenge bootstrap 5.1 ka starter templates usko copy karenge and usko index.html wale file mai copy kr denge ab hum container ka use karenge. aur us container mai hie hum PN header footer button ka ue karenge. 

# href="/"  jo button mai yaha / hai iskai wajah si hame ye pta chalta hai kie yeh root folder ko hie target kr raha hai. isko change karene kai liye hame urls.py filemai apne urls ko change karte hai.

# pahle maine urls banaya and then uska view banaya aur uskai baad ush view ka html file banaya templaes folder mai. 

# ab href="/" ismai mai apna urls ka view dai dunga. ab page ko refresh karunga and then usko dekhne par sbhi button aa jayenge aur ush button par click karne par blank page open hoga kyuki ush file mai kuch hai hie nhi.

# {% block content %}{% endblock %} maine DTL ka use kiya pale link par click karne par blank page open hota tha lein ab jo jo index.html page ka view tha wahi sabhi page par kr diya hu click karne par wahi page open hoga. 

# {% extends "index.html" %} {% block content %} <!-- Add Employee form or content here -->{% endblock %} yeh lanagna padta hai sabhi html file mai to extends index.html file.

# ab litna bhi logic hota hai usko hum views.py file mai agate hai. aur jish jish file kie jarurat hogi views.py file mai ush file ko hum import karte hai.

# object.all ka use kiye apne all_emp wale api mai taki sab kuch view ho jaye. yeh jitene bhi values hai wo sb kuch print mai dikh rahi hai ab usko hum frontend par dekhna chahte hai to usko kaise dekhnege.

# ab hum view_all_emp.html wale file mai hum apna pura html ka code likhenge jo hame dikhana hoga apne UI mai uska loop likenge aur table banayege aur table hum uska class likhenge table ka format acca dikhne kai liye.ab jitna bhi db mai data hai wo dikhne lagega

# ab hum add_emp.html wale file ko dekhnege aur usmai apna UI banayege aur iska use karenge  <form action="/add_emp" method="post"> aur  {% csrf_token %} iska use karenge. uskai baad hum views.py file mai apna logic likhenge. yeh wala kaam bhi ho gya jyada toush nhi tha yeh concept this is easy.

# remove_emp ab hum ish template par kaam akrenge yeh kaam karega emp_id kai behalf par. yeh bhi ban gya remove employee wala bhi id kie help sai.

# filter_emp.html ab hum ish module par kaam karege.