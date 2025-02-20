""" 1.- Gestión de Notificaciones
    Programa que utiliza el Principio de Responsabilidad Única (SRP) y el Principio de Inversión de Dependencias (DIP)
    para implementar un sistema de notificaciones 
 """
 
from abc import ABC, abstractmethod
 
class Notification(ABC):
    @abstractmethod
    def body(self):
        pass

    @abstractmethod
    def send(self):
        pass

class Receiver(ABC):
    @abstractmethod
    def getReceiver(self):
        pass
 
class EmailNotification(Notification):        
    def body(self):
        return "Some important email body"
        
    def send(self):
        return "Sending email notification..."
    
    def getReceiver(self):
        return "john.doe@email.com"
        
class SMSNotification(Notification):
    def body(self):
        return "SPAM SMS body"
        
    def send(self):
        return "Sending SMS notification..."
    
    def getReceiver(self):
        return "555-555-5555"
 
class NotificationService():
    def notify(self):
        return [EmailNotification(), SMSNotification()]


def main():
    notificationService = NotificationService()
    
    for notification in notificationService.notify():
        print(f"\nSending to: ", notification.getReceiver())
        print(notification.body())
        print(notification.send())
    


if __name__ == "__main__":
    main()
 