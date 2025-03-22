from  django.shortcuts import render,redirect
from django.db import connection

def admin(request):
    template = 'Admin.html'
    context = {}
    return render(request, template, context)

def general(request):
    id_user = None
    template = 'General.html'
    context = {}
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM credits.status_get();")
        status = dictfetchall(cursor)
        context['status'] = status
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM credits.application_get(%s);", (id_user,))
            apps = dictfetchall(cursor)
            # pprint(apps)
            applications = []
        ids = []
        for app in apps:
            if app['id'] not in ids:
                application = {}
                application['fk_credit'] = app['fk_credit']
                application['id'] = app['id']
                application['date'] = app['date']
                application['sum'] = app['sum']
                application['fk_status'] = app['fk_status']
                application['term'] = app['term']
                application['fk_user'] = app['fk_user']
                application['fk_user'] = app['fk_user']
                application['bank'] = app['bank']  # Дублирование строки
                application['purpose'] = app['purpose']
        pprint(applications)
        context['applications'] = applications
        return render(request, template, context)

def login(request):
    template = 'Login.html'
    context = {}
    return render(request, template, context)

def my_applications(request):
    template = 'My_applications.html'
    context = {}
    return render(request, template, context)
def registration(request):
    template = 'Registration.html'
    context = {}
    return render(request, template, context)
def logout(request):
    return redirect('registration')

def dictfetchall(cursor):
    """
    Return all rows from a cursor as a dict.
    Assume the column names are unique.
    """
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

# Create your views here.
