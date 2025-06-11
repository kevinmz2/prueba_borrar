#include <iostream>

int main() {
    double numero1, numero2, suma;

    std::cout << "Ingrese el primer número: ";
    std::cin >> numero1;

    std::cout << "Ingrese el segundo número: ";
    std::cin >> numero2;

    suma = numero1 + numero2;

    std::cout << "La suma es: " << suma << std::endl;

    return 0;
}
