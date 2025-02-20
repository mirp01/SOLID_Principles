#include <iostream>
using namespace std;

// Superclase

class PaymentSystem {
    public:
        // Constructor, recibe un método de pago
        PaymentSystem(PaymentMethod* method) : paymentMethod(method) {}

        void processPayment(string& userInfo) {
            paymentMethod->pay(userInfo);
        }
    
    private:
        PaymentMethod* paymentMethod;
};

// Interfaz de pago

class PaymentMethod{
    public:
        virtual void pay(string) = 0;
        virtual ~PaymentMethod() = default;
};

// Implementación en otras clases

class Paypal: public PaymentMethod{
    public:
        void pay(string email) override{
            cout << "Charging though Paypal's API the user's email: " << email << " ..." << endl;
        }
};

class CreditCard: public PaymentMethod{
    public:
        void pay(string ID) override{
            cout << "Charging the user with the ID number of: " << ID << " ..." << endl;
        }
};

int main(){

}