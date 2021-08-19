from django.shortcuts import render
from django.shortcuts import redirect
from .models import Note
from .models import User
# Create your views here.
user_id = 0
note_id = 0

def homepage(request):
    print('this is the request',request)
    if user_id == 0:
        response = redirect('/login-template/')
        return response
    else:
        response = redirect('/login-success/')
        return response

def register_template(request):
    return render(request,'register.html',{
        'user':False
    })
def register(request):
    print("this is register request")

    user_name = request.POST["name"]
    user_pwd = request.POST["pwd"]

    try:
        User.objects.get(name=user_name)
        print("am gasit")
        return render(request,'register.html',{
            'duplicate': True,
        })
    except:
        new_user = User(name=user_name,password=user_pwd)
        new_user.save()

        return render(request,'login.html', {
            'framework_name': 'Django',
            'user': False,
        })
def login_template(request):
    return render(request, 'login.html', {
        'login': True,
        'user': False
    })
def login_error(request):
    return render(request, 'login.html', {
        'login': False,
        'user': False
    })
def login(request):
    user_name = request.POST["name"]
    user_pwd = request.POST["pwd"]

    try:
        user_logged = User.objects.get(name=user_name,password=user_pwd)
        global user_id
        user_id= user_logged.id
        response = redirect('/login-success/')
        return response
    except:
        response = redirect('/login-error/')
        return response


def login_succes(request):
    note_id = 0
    if user_id == 0:
        return render(request,'login.html', {
            'framework_name': 'Django',
            'user': False
        })
    else:
        user_logged = User.objects.get(id=user_id)
        all_notes_qs = Note.objects.filter(user_id=user_logged.id)
        return render(request, 'index.html', {
            'framework_name': 'Django',
            'notes': all_notes_qs,
            'user': user_logged
        })
def logout(request):
    global user_id
    user_id = 0;
    return render(request, 'login.html', {
        'user': False
    })
def addTemplate(request):
    global user_id
    user_logged = User.objects.get(id=user_id)
    return render(request,'addNote.html',{
        'user':user_logged
    })
def add(request):
    print("this is add request")

    note_summary = request.POST["summary"]
    note_content = request.POST["note"]

    print(note_summary)
    print(note_content)

    new_note = Note(user_id=user_id, summary=note_summary, content=note_content)
    new_note.save()
    user_logged = User.objects.get(id=user_id)
    all_notes_qs = Note.objects.filter(user_id = user_id)
    return render(request, 'index.html', {
            'framework_name': 'Django',
            'notes': all_notes_qs,
            'user': user_logged

    })
def see_note(request):
    print("note request")

    try:
        note_flag = request.POST["flag"]

        if user_id !=0:
            try:
                global note_id
                note_id = note_flag
                response = redirect('/show-note/')
                return response
            except:
                print("ajung si aici")
                response = redirect('/login-success/')
                return response
        else:
            response = redirect('/login-success/')
            return response
    except:
        response = redirect('/login-success/')
        return response

def show_note(request):
    if user_id != 0:
        user_logged = User.objects.get(id=user_id)
        if note_id != 0:
            note = Note.objects.get(id=note_id)
            return render(request, 'showNote.html', {
                'note': note,
                'user': user_logged
            })
        else:
            response = redirect('/login-success/')
            return response
    else:
        response = redirect('/login-template/')
        return response
