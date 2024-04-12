from abc import ABC, abstractmethod


class Membresia(ABC):
    def __init__(self, email, tarjeta):
        self._email = email
        self._tarjeta = tarjeta

    @abstractmethod
    def cambiar_suscripcion(self, nuevo_tipo):
        pass

    def _crear_nueva_membresia(self, tipo):
        clases = {
            1: Basica,
            2: Familiar,
            3: SinConexion,
            4: Pro,
        }
        return clases[tipo](self._email, self._tarjeta)

    def cancelar_suscripcion(self):
        return Gratis(self._email, self._tarjeta)

    @property
    def email(self):
        return self._email

    @property
    def tarjeta(self):
        return self._tarjeta

    @email.setter
    def email(self, value):
        self._email = value

    @tarjeta.setter
    def tarjeta(self, value):
        self._tarjeta = value


class Gratis(Membresia):
    def __init__(self, email, tarjeta):
        super().__init__(email, tarjeta)
        self._costo = 0
        self._dispositivos_max = 1

    @property
    def costo(self):
        return self._costo

    @property
    def dispositivos_max(self):
        return self._dispositivos_max

    def cambiar_suscripcion(self, nuevo_tipo):
        if 1 <= nuevo_tipo <= 4:
            return self._crear_nueva_membresia(nuevo_tipo)
        return self


class Basica(Membresia):
    def __init__(self, email, tarjeta):
        super().__init__(email, tarjeta)
        self._costo = 3000
        self._dispositivos_max = 2

    @property
    def costo(self):
        return self._costo

    @property
    def dispositivos_max(self):
        return self._dispositivos_max

    def cambiar_suscripcion(self, nuevo_tipo):
        if 2 <= nuevo_tipo <= 4:
            return self._crear_nueva_membresia(nuevo_tipo)
        return self


class Familiar(Basica):
    def __init__(self, email, tarjeta):
        super().__init__(email, tarjeta)
        self._dias_regalo = 7

    @property
    def dias_regalo(self):
        return self._dias_regalo

    def cambiar_suscripcion(self, nuevo_tipo):
        if nuevo_tipo in [1, 3, 4]:
            return self._crear_nueva_membresia(nuevo_tipo)
        return self

    def modificar_control_parental(self):
        pass


class SinConexion(Basica):
    def __init__(self, email, tarjeta):
        super().__init__(email, tarjeta)
        self._dias_regalo = 7

    @property
    def dias_regalo(self):
        return self._dias_regalo

    def cambiar_suscripcion(self, nuevo_tipo):
        if nuevo_tipo in [1, 2, 4]:
            return self._crear_nueva_membresia(nuevo_tipo)
        return self

    def incrementar_contenido_offline(self):
        pass


class Pro(Familiar, SinConexion):
    def __init__(self, email, tarjeta):
        Familiar.__init__(self, email, tarjeta)
        self._costo = 7000
        self._dispositivos_max = 6
        self._dias_regalo = 15

    def cambiar_suscripcion(self, nuevo_tipo):
        if nuevo_tipo in [1, 2, 3]:
            return self._crear_nueva_membresia(nuevo_tipo)
        return self

    def modificar_control_parental(self):
        pass

    def incrementar_contenido_offline(self):
        pass


# Contexto de prueba:
g = Gratis("correo@prueba.cl", "123 456 789")
print(type(g))
b = g.cambiar_suscripcion(1)
print(type(b))
f = b.cambiar_suscripcion(2)
print(type(f))
sc = f.cambiar_suscripcion(3)
print(type(sc))
pro = sc.cambiar_suscripcion(4)
print(type(pro))
g2 = pro.cancelar_suscripcion()
print(type(g2))
