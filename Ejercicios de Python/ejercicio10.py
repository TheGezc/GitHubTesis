Numero_llamadas= int(input("Ingrese el numero de llamadas: "))
Promedio_duracion=float(input("Ingrese el promedio de duración de llamadas: "))
usuarios=int(input("Ingrese el numero de usuarios: "))
t=3600

while True:
    trafico_actual=round((Numero_llamadas*Promedio_duracion)/t,2)
    Densidad_TraficoEmpresarial=round(trafico_actual/usuarios,2)
    Densidad_TraficoResidencial=round(Densidad_TraficoEmpresarial/2,3)
    print("El resultado es: ",trafico_actual, "Erlangs")
    print("El resultado de densidad de trafico empresarial es: ",Densidad_TraficoEmpresarial, "Erlang/usuario")
    print("El resultado de densidad de trafico residencial es: ",Densidad_TraficoResidencial, "Erlang/usuario")
    n_canales=int(input("Ingrese el número de canales: "))
    canales=[]
    x=1
    for x in range(n_canales):
        valor=int(input(f"Ingrese el numero de usuarios del canal {x}: "))   
        canales.append(valor)
    print(canales)
    

