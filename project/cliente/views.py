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

        from .models import cliente 

        mi_cliente = cliente(nombre=request.POST["nombre"] , apellido=request.POST["apellido"], pais_origen = request.POST["pais_origen"], fecha_nacimiento= request.POST["fecha_nacimiento"])
        mi_cliente.save()
        return redirect("cliente:index")
        

def home(request):
    return render(request, "cliente/index.html")