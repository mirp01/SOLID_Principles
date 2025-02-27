""" 
4. Calculadora de Descuentos
    Programa que utiliza el Principio Abierto/Cerrado (OCP) para permitir agregar nuevos tipos de descuentos sin alterar el código existente 
    y el Principio de Responsabilidad Única (SRP) para que cada tipo de descuento se encarga de su propio cálculo. 
"""
from abc import ABC, abstractmethod

#Clase PaymentProcessor
class PaymentProcessor():
    def __init__(self, discount_type):
        self.discount_type = discount_type
    
    def process_payment(self, amount):
        final = self.discount_type.apply_discount(amount)
        print(f"${final:.2f}")

#Interfaz de descuento
class Discount():
    @abstractmethod
    def apply_discount(self, amount):
        return amount

#Tipos de descuentos
class NoDiscount(Discount):
    def apply_discount(self, amount):
        return amount

class VIPDiscount(Discount):
    def apply_discount(self, amount):
        return amount * 0.6

def main():
    #Cantidad inicial
    amount = 1000

    #Sin descuento
    print("Pago sin descuento:")
    payment1 = PaymentProcessor(NoDiscount())
    payment1.process_payment(amount)
    
    #Descuento VIP     
    print("Pago con descuento VIP:")
    payment2 = PaymentProcessor(VIPDiscount())
    payment2.process_payment(amount)

if __name__ == "__main__":
    main()