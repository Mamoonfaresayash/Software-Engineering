from django.shortcuts import render

# Create your views here.

def index(request):
    context={
    "students":[
    {
        "FirstName" : "أحمد",
        "LastName" : "الهاشمي",
        "Age" : 21,
        "Gender" : "ذكر",
        "Level" : "السنة الثالثة",
        "Status" : "نعم"
    },
    {
        "FirstName" : "محمد",
        "LastName" : "الحضرمي",
        "Age" : 22,
        "Gender" : "ذكر",
        "Level" : "السنة الرابعة",
        "Status" : "نعم"
    },
    {
        "FirstName" : "ليلى",
        "LastName" : "الشريف",
        "Age" : 19,
        "Gender" : "أنثى",
        "Level" : "السنة الأولى",
        "Status" : "نعم"
    },
    {
        "FirstName" : "فهد",
        "LastName" : "القاسمي",
        "Age" : 23,
        "Gender" : "ذكر",
        "Level" : "السنة الخامسة",
        "Status" : "لا"
    },
    {
        "FirstName" : "سارة",
        "LastName" : "الزهري",
        "Age" : 20,
        "Gender" : "أنثى",
        "Level" : "السنة الثانية",
        "Status" : "نعم"
    },
    {
        "FirstName" : "عبدالله",
        "LastName" : "النعيمي",
        "Age" : 24,
        "Gender" : "ذكر",
        "Level" : "السنة الخامسة",
        "Status" : "لا"
    },
    {
        "FirstName" : "مريم",
        "LastName" : "العسيري",
        "Age" : 18,
        "Gender" : "أنثى",
        "Level" : "السنة الأولى",
        "Status" : "نعم"
    },
    {
        "FirstName" : "خالد",
        "LastName" : "المري",
        "Age" : 22,
        "Gender" : "ذكر",
        "Level" : "السنة الرابعة",
        "Status" : "نعم"
    },
    {
        "FirstName" : "هدى",
        "LastName" : "القرشي",
        "Age" : 21,
        "Gender" : "أنثى",
        "Level" : "السنة الثالثة",
        "Status" : "نعم"
    },
    {
        "FirstName" : "بدر",
        "LastName" : "التميمي",
        "Age" : 23,
        "Gender" : "ذكر",
        "Level" : "السنة الخامسة",
        "Status" : "لا"
    }
    ]
    }
    return render(request,'index.html',context)
    

   
def deletstudent(request):
    return render(request,'deletstudent.html')

def home(request):
    return render(request,'home.html')

    
def showstudent(request):
    studentsEdit={
        "total":300,
        "eachsub":{"Software":100,
                   "clints and serever program":100,
                   "Image proproceesing":100
                   }
    }
    return render(request,'showstudent.html',studentsEdit)


def editstudent(request):
    studentsEdit={
        "totle":300,
        "eachsub":{"Software":100,
                   "clints and serever program":100,
                   "Image proproceesing":100
                   }
    }
    return render(request,'editstudent.html',studentsEdit)
