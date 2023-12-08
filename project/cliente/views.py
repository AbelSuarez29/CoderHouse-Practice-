from django.shortcuts import render, redirect

def cliente_view(request):
    if request.method == "GET":
        print("+" * 90) #  Imprimimos esto para ver por consola
        print("+" * 90) #  Imprimimos esto para ver por consola
        return render(
            request,
            "cliente/cliente_formulario_basico.html",
        )
    else:
        print("*" * 90)     #  Imprimimos esto para ver por consola
        print(request.POST) #  Imprimimos esto para ver por consola
        print("*" * 90)     #  Imprimimos esto para ver por consola
        return redirect("cliente:index")
        

def home(request):
    return render(request, "cliente/index.html")