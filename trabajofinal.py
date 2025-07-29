
N = int(input("¿Cuántos números quieres ingresar? "))
numeros = []

while len(numeros) < N:
    nuevo = int(input(f"Ingrese el número #{len(numeros)+1}: "))

    if len(numeros) >= 2:
        suma_ultimos = numeros[-1] + numeros[-2]
        
        while nuevo == suma_ultimos:
            print("❌ No se puede ingresar ese número. Es igual a la suma de los dos anteriores.")
            nuevo = int(input("Ingrese un número diferente: "))
            suma_ultimos = numeros[-1] + numeros[-2]

    numeros.append(nuevo)

print("✅ Números ingresados:", numeros)
