#functions.py

def handle_uploaded_file(f,email):  
    with open('app1/static/'+email+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)