
# ==========================================================
# PROYECTO: SISTEMA INTEGRAL SOFTWARE FJ
# ARCHIVO: entidades.py
# DESCRIPCION: Clases abstractas y gestion de clientes
# ==========================================================

from abc import ABC, abstractmethod

from excepciones import (
    DatosInvalidosError,
    registrar_evento
)


# ==========================================================
# CLASE ABSTRACTA GENERAL
# ==========================================================

class Entidad(ABC):
    """
    Clase abstracta que representa las entidades generales
    del sistema Software FJ.
    """

    def __init__(self, identificacion, nombre):

        if not identificacion or not str(identificacion).strip():
            raise DatosInvalidosError(
                "La identificacion no puede estar vacia."
            )

        if not nombre or not nombre.strip():
            raise DatosInvalidosError(
                "El nombre no puede estar vacio."
            )

        self._identificacion = str(identificacion).strip()
        self._nombre = nombre.strip()

    @property
    def identificacion(self):
        return self._identificacion

    @property
    def nombre(self):
        return self._nombre

    @abstractmethod
    def mostrar_informacion(self):
        """
        Metodo abstracto que deben implementar
        las clases que hereden de Entidad.
        """
        pass


# ==========================================================
# CLASE CLIENTE
# ==========================================================

class Cliente(Entidad):
    """
    Representa un cliente de Software FJ.
    Hereda de Entidad y aplica encapsulacion.
    """

    def __init__(self, identificacion, nombre, correo, telefono):

        # Validar correo electronico
        if not isinstance(correo, str) or "@" not in correo:
            raise DatosInvalidosError(
                "El correo electronico no es valido."
            )

        partes_correo = correo.split("@")

        if (
            len(partes_correo) != 2
            or not partes_correo[0].strip()
            or "." not in partes_correo[1]
            or partes_correo[1].startswith(".")
            or partes_correo[1].endswith(".")
        ):
            raise DatosInvalidosError(
                "El formato del correo electronico es incorrecto."
            )

        # Validar telefono
        if not str(telefono).isdigit() or len(str(telefono)) < 7:
            raise DatosInvalidosError(
                "El telefono debe tener al menos 7 digitos."
            )

        # Inicializar los atributos de la clase padre
        super().__init__(identificacion, nombre)

        # Atributos privados del cliente
        self.__correo = correo.strip()
        self.__telefono = str(telefono)

        registrar_evento(
            f"Cliente registrado: {self.nombre}"
        )

    # Propiedad para consultar el correo
    @property
    def correo(self):
        return self.__correo

    # Propiedad para consultar el telefono
    @property
    def telefono(self):
        return self.__telefono

    # Metodo para mostrar informacion del cliente
    def mostrar_informacion(self):

        return (
            f"Identificacion: {self.identificacion}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}\n"
            f"Telefono: {self.telefono}"
        )

    # Metodo para representar el objeto
    def __str__(self):
        return (
            f"Cliente: {self.nombre} | "
            f"ID: {self.identificacion} | "
            f"Correo: {self.correo}"
        )

