from django.shortcuts import render, HttpResponse, redirect
from radientapp.models import Inquiry,Smallinq

# Create your views here.


def index(request):
    return HttpResponse("Hello this is the best web app")


def form(request):
    if request.method == 'POST':
        country = request.POST.getlist('Country[]')
        firstname = request.POST.get('firstname')
        middlename = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        mobile = request.POST.get('mobile')
        wmobile = request.POST.get('wmobile')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        isPassport = request.POST.get('isPassport')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        instaid = request.POST.get('instaid')
        fbid = request.POST.get('fbid')
        marital_status = request.POST.get('marital_status')
        no_child = request.POST.get('no_child')
        fdate1 = request.POST.get('fdate1')
        tdate1 = request.POST.get('tdate1')
        qual1 = request.POST.get('qual1')
        ctype1 = request.POST.get('ctype1')
        marks1 = request.POST.get('marks1')
        school1 = request.POST.get('school1')
        fdate2 = request.POST.get('fdate2')
        tdate2 = request.POST.get('tdate2')
        qual2 = request.POST.get('qual2')
        ctype2 = request.POST.get('ctype2')
        marks2 = request.POST.get('marks2')
        school2 = request.POST.get('school2')
        fdate3 = request.POST.get('fdate3')
        tdate3 = request.POST.get('tdate3')
        qual3 = request.POST.get('qual3')
        ctype3 = request.POST.get('ctype3')
        marks3 = request.POST.get('marks3')
        school3 = request.POST.get('school3')
        fdate4 = request.POST.get('fdate4')
        tdate4 = request.POST.get('tdate4')
        qual4 = request.POST.get('qual4')
        ctype4 = request.POST.get('ctype4')
        marks4 = request.POST.get('marks4')
        school4 = request.POST.get('school4')
        fdate5 = request.POST.get('fdate5')
        tdate5 = request.POST.get('tdate5')
        role1 = request.POST.get('role1')
        org1 = request.POST.get('org1')
        fdate6 = request.POST.get('fdate6')
        tdate6 = request.POST.get('tdate6')
        org2 = request.POST.get('org2')
        role2 = request.POST.get('role2')
        fname = request.POST.get('fname')
        occupation_type = request.POST.get('occupation_type')
        occupation_name = request.POST.get('occupation_name')
        english_test = request.POST.get('english_test')
        english_test_date = request.POST.get('english_test_date')
        lband = request.POST.get('lband')
        rband = request.POST.get('rband')
        wband = request.POST.get('wband')
        sband = request.POST.get('sband')
        oband = request.POST.get('oband')
        General_test_date = request.POST.get('General_test_date')
        General_test_score = request.POST.get('gs')
        rejected = request.POST.get('rejected')
        rejectedcountry = request.POST.get('rejectedcountry')
        ref = request.POST.get('ref')

        obj = Inquiry(country=country,firstname=firstname,
                        middlename=middlename, lastname=lastname, mobile=mobile, wmobile=wmobile,
                        email=email, dob=dob, gender=gender, isPassport=isPassport, address=address,
                        city=city, state=state, pincode=pincode, instaid=instaid, fbid=fbid, marital_status=marital_status,no_child=no_child,
                        fdate1=fdate1, tdate1=tdate1,qual1=qual1, ctype1=ctype1, marks1=marks1, school1=school1,
                        fdate2=fdate2, tdate2=tdate2, qual2=qual2, ctype2=ctype2,marks2=marks2, school2=school2,
                        fdate3=fdate3, tdate3=tdate3,qual3=qual3,ctype3=ctype3, marks3=marks3, school3=school3, 
                        fdate4=fdate4, tdate4=tdate4,qual4=qual4, ctype4=ctype4, marks4=marks4, school4=school4,
                        fdate5=fdate5,tdate5=tdate5,org1=org1,role1=role1,
                        fdate6=fdate6,tdate6=tdate6, org2=org2,role2=role2,
                        fname=fname,occupation_name=occupation_name,occupation_type=occupation_type,
                        english_test=english_test,english_test_date=english_test_date,lband=lband,rband=rband,wband=wband,sband=sband,oband=oband,
                        General_test_date=General_test_date,General_test_score=General_test_score,rejected=rejected,rejectedcountry=rejectedcountry,ref=ref
                        )

        obj.save()
        return redirect('form')
    return render(request, 'form.html')


def dashboard(request):
    return render(request, 'dashboard.html')

def show_inquiry(request):
    inquiry=Smallinq.objects.all();
    context={
        "inquiry":inquiry,
    }
    return render(request, 'inquiry.html',context)

def mini_inq(request):
    if request.method == 'POST':
        country = request.POST.getlist('Country[]')
        name=request.POST.get('fullname')
        mobile=request.POST.get('mobile')
        wmobile=request.POST.get('wmobile')
        email=request.POST.get('email')
        dob = request.POST.get('dob')
        ref=request.POST.get('ref')
        gender=request.POST.get('gender')
        print(country,name,mobile,wmobile,email,dob,ref)
        smallinq=Smallinq(name=name,mobile=mobile,wmobile=wmobile,email=email,dob=dob,ref=ref,gender=gender,country=country)
        smallinq.save()
        return redirect('mini_inq')
    return render(request, 'mini_inq.html')

def show(request,pk):
    inq=Smallinq.objects.get(id=pk)
    context={"inq":inq}
    return render(request, 'show.html',context)

