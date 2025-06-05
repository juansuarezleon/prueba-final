"""Simple command line calculator."""

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


OPERATIONS = {
    '1': ('Sumar', add),
    '2': ('Restar', subtract),
    '3': ('Multiplicar', multiply),
    '4': ('Dividir', divide),
}


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Por favor ingrese un número válido.")


def main():
    print("Calculadora básica")
    for key, (name, _) in OPERATIONS.items():
        print(f"{key}. {name}")

    choice = input("Seleccione una operación: ")
    if choice not in OPERATIONS:
        print("Opción no válida")
        return

    a = get_number("Ingrese el primer número: ")
    b = get_number("Ingrese el segundo número: ")

    name, func = OPERATIONS[choice]
    try:
        result = func(a, b)
        print(f"Resultado: {result}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
