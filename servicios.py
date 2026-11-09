
# ==========================================================
# PROYECTO: SISTEMA INTEGRAL SOFTWARE FJ
# ARCHIVO: servicios.py
# DESCRIPCION: Servicios especializados de la empresa
# ==========================================================

from abc import ABC, abstractmethod

from entidades import Entidad
from excepciones import (
    DatosInvalidosError,
    ServicioNoDisponibleError,
    registrar_evento
)


# ==========================================================
# CLASE ABSTRACTA SERVICIO
# ==========================================================

class Servicio(Entidad, ABC):
    """
    Clase abstracta que representa los servicios
    ofrecidos por Software FJ.
    """

    def __init__(self, identificacion, nombre, precio_base,
                 disponible=True):

        super().__init__(identificacion, nombre)

        if isinstance(precio_base, bool) or not isinstance(
            precio_base, (int, float)
        ) or precio_base <= 0:
            raise DatosInvalidosError(
                "El precio base debe ser un numero mayor que cero."
            )

        if not isinstance(disponible, bool):
            raise DatosInvalidosError(
                "La disponibilidad debe ser verdadera o falsa."
            )

        self._precio_base = float(precio_base)
        self._disponible = disponible

    @property
    def precio_base(self):
        return self._precio_base

    @property
    def disponible(self):
        return self._disponible

    def verificar_disponibilidad(self):
        if not self._disponible:
            raise ServicioNoDisponibleError(
                f"El servicio {self.nombre} no esta disponible."
            )

    def validar_costo(self, duracion, descuento, impuesto):
        """Valida los parametros utilizados en los costos."""

        if isinstance(duracion, bool) or not isinstance(
            duracion, (int, float)
        ) or duracion <= 0:
            raise DatosInvalidosError(
                "La duracion debe ser mayor que cero."
            )

        if isinstance(descuento, bool) or not isinstance(
            descuento, (int, float)
        ) or not 0 <= descuento <= 100:
            raise DatosInvalidosError(
                "El descuento debe estar entre 0 y 100."
            )

        if isinstance(impuesto, bool) or not isinstance(
            impuesto, (int, float)
        ) or not 0 <= impuesto <= 1:
            raise DatosInvalidosError(
                "El impuesto debe estar entre 0 y 1."
            )

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0.0):
        """Calcula el costo especifico de cada servicio."""
        pass

    @abstractmethod
    def validar_parametros(self, **kwargs):
        """Valida los parametros propios de cada servicio."""
        pass

    @abstractmethod
    def describir_servicio(self):
        """Devuelve la descripcion del servicio."""
        pass

    def mostrar_informacion(self):
        return self.describir_servicio()


# ==========================================================
# SERVICIO 1: RESERVA DE SALAS
# ==========================================================

class ReservaSala(Servicio):
    """Servicio para reservar salas de reuniones."""

    def __init__(self, identificacion, nombre, precio_hora,
                 capacidad_maxima, disponible=True):

        super().__init__(
            identificacion, nombre, precio_hora, disponible
        )

        if isinstance(capacidad_maxima, bool) or not isinstance(
            capacidad_maxima, int
        ) or capacidad_maxima <= 0:
            raise DatosInvalidosError(
                "La capacidad debe ser un entero positivo."
            )

        self.capacidad_maxima = capacidad_maxima

    def validar_parametros(self, **kwargs):

        asistentes = kwargs.get("asistentes")

        if isinstance(asistentes, bool) or not isinstance(
            asistentes, int
        ) or asistentes <= 0:
            raise DatosInvalidosError(
                "El numero de asistentes debe ser positivo."
            )

        if asistentes > self.capacidad_maxima:
            raise DatosInvalidosError(
                "La sala no tiene capacidad suficiente."
            )

        self.verificar_disponibilidad()
        return True

    def calcular_costo(self, duracion, descuento=0, impuesto=0.0):

        self.validar_costo(duracion, descuento, impuesto)
        self.verificar_disponibilidad()

        subtotal = self.precio_base * duracion
        subtotal -= subtotal * descuento / 100
        total = subtotal * (1 + impuesto)

        return round(total, 2)

    def describir_servicio(self):

        return (
            f"Reserva de sala: {self.nombre}\n"
            f"Precio por hora: {self.precio_base}\n"
            f"Capacidad maxima: {self.capacidad_maxima} personas"
        )


# ==========================================================
# SERVICIO 2: ALQUILER DE EQUIPOS
# ==========================================================

class AlquilerEquipo(Servicio):
    """Servicio para alquilar equipos tecnologicos."""

    def __init__(self, identificacion, nombre, precio_dia,
                 cantidad_disponible, disponible=True):

        super().__init__(
            identificacion, nombre, precio_dia, disponible
        )

        if isinstance(cantidad_disponible, bool) or not isinstance(
            cantidad_disponible, int
        ) or cantidad_disponible < 0:
            raise DatosInvalidosError(
                "La cantidad disponible debe ser un entero no negativo."
            )

        self.cantidad_disponible = cantidad_disponible

    def validar_parametros(self, **kwargs):

        cantidad = kwargs.get("cantidad")

        if isinstance(cantidad, bool) or not isinstance(
            cantidad, int
        ) or cantidad <= 0:
            raise DatosInvalidosError(
                "La cantidad de equipos debe ser positiva."
            )

        if cantidad > self.cantidad_disponible:
            raise DatosInvalidosError(
                "No hay suficientes equipos disponibles."
            )

        self.verificar_disponibilidad()
        return True

    def calcular_costo(self, duracion, descuento=0, impuesto=0.0):

        self.validar_costo(duracion, descuento, impuesto)
        self.verificar_disponibilidad()

        subtotal = self.precio_base * duracion
        subtotal -= subtotal * descuento / 100
        total = subtotal * (1 + impuesto)

        return round(total, 2)

    def describir_servicio(self):

        return (
            f"Alquiler de equipos: {self.nombre}\n"
            f"Precio por dia: {self.precio_base}\n"
            f"Cantidad disponible: {self.cantidad_disponible}"
        )


# ==========================================================
# SERVICIO 3: ASESORIAS ESPECIALIZADAS
# ==========================================================

class AsesoriaEspecializada(Servicio):
    """Servicio de asesoria profesional especializada."""

    def __init__(self, identificacion, nombre, precio_hora,
                 especialidad, disponible=True):

        super().__init__(
            identificacion, nombre, precio_hora, disponible
        )

        if not isinstance(especialidad, str) or not especialidad.strip():
            raise DatosInvalidosError(
                "La especialidad no puede estar vacia."
            )

        self.especialidad = especialidad.strip()

    def validar_parametros(self, **kwargs):

        modalidad = kwargs.get("modalidad")

        modalidades_validas = ["presencial", "virtual"]

        if not isinstance(modalidad, str) or (
            modalidad.lower() not in modalidades_validas
        ):
            raise DatosInvalidosError(
                "La modalidad debe ser presencial o virtual."
            )

        self.verificar_disponibilidad()
        return True

    def calcular_costo(self, duracion, descuento=0, impuesto=0.0):

        self.validar_costo(duracion, descuento, impuesto)
        self.verificar_disponibilidad()

        subtotal = self.precio_base * duracion
        subtotal -= subtotal * descuento / 100
        total = subtotal * (1 + impuesto)

        return round(total, 2)

    def describir_servicio(self):

        return (
            f"Asesoria especializada: {self.nombre}\n"
            f"Precio por hora: {self.precio_base}\n"
            f"Especialidad: {self.especialidad}"
        )


# ==========================================================
# FIN DEL MODULO DE SERVICIOS
# ==========================================================

registrar_evento(
    "Modulo de servicios cargado correctamente."
)
