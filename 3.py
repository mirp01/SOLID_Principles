class Trackable:
    def trackPackage(self):
        pass

class Deliverable:
    def manageDeliveries(self):
        pass

    def manageTransportation(self):
        pass

class Routable:
    def optimizeRoute(self):
        pass

    def manageLogistics(self):
        pass

class Transportista(Deliverable):
    def manageDeliveries(self):
        print("Managing deliveries...")

    def manageTransportation(self):
        print("Managing transportation...")

class AdministradorDeRutas(Routable, Trackable):
    def optimizeRoute(self):
        print("Optimizing route...")

    def manageLogistics(self):
        print("Managing logistics...")

    def trackPackage(self):
        print("Tracking package as a route admin...")

class SoporteAlCliente(Trackable):
    def trackPackage(self):
        print("Tracking package as client support...")

def main():
    transportista = Transportista()
    admin_rutas = AdministradorDeRutas()
    soporte_cliente = SoporteAlCliente()

    transportista.manageDeliveries()
    transportista.manageTransportation()

    admin_rutas.optimizeRoute()
    admin_rutas.manageLogistics()
    admin_rutas.trackPackage()

    soporte_cliente.trackPackage()

if __name__ == "__main__":
    main()