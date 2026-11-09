
# ==========================================================
# PROYECTO: SISTEMA INTEGRAL SOFTWARE FJ
# ARCHIVO: reservas.py
# DESCRIPCION: Gestion de reservas y procesamiento
# ==========================================================

from excepciones import (
    DatosInvalidosError,
    ReservaInvalidaError,
    OperacionNoPermitidaError,
    ErrorSistema,
    registrar_evento
)

from entidades import Cliente
from servicios import Servicio


# ==========================================================
# CLASE RESERVA
# ==========================================================

class Reserva:
    """
    Clase encargada de gestionar las reservas
    realizadas por los clientes de Software FJ.
    """

    contador_reservas = 0

    def __init__(self, cliente, servicio, duracion,
                 **parametros_servicio):

        # Validar el cliente
        if not isinstance(cliente, Cliente):
            raise DatosInvalidosError(
                "La reserva necesita un cliente valido."
            )

        # Validar el servicio
        if not isinstance(servicio, Servicio):
            raise DatosInvalidosError(
                "La reserva necesita un servicio valido."
            )

        # Validar la duracion
        if isinstance(duracion, bool) or not isinstance(
            duracion, (int, float)
        ) or duracion <= 0:
            raise DatosInvalidosError(
                "La duracion debe ser mayor que cero."
            )

        # Asignar identificador automatico
        Reserva.contador_reservas += 1
        self.__identificador = Reserva.contador_reservas

        # Datos privados de la reserva
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"
        self.__parametros_servicio = parametros_servicio.copy()
        self.__costo = None

        registrar_evento(
            f"Reserva {self.__identificador} creada para "
            f"{self.__cliente.nombre}."
        )

    # ======================================================
    # PROPIEDADES
    # ======================================================

    @property
    def identificador(self):
        return self.__identificador

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    @property
    def costo(self):
        return self.__costo

    # ======================================================
    # CONFIRMAR RESERVA
    # ======================================================

    def confirmar(self):

        if self.__estado != "Pendiente":
            raise OperacionNoPermitidaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        try:
            # Validar los parametros del servicio
            self.__servicio.validar_parametros(
                **self.__parametros_servicio
            )

            self.__estado = "Confirmada"

        except Exception as error:
            registrar_evento(
                f"Error al confirmar reserva "
                f"{self.__identificador}: {error}",
                "error"
            )
            raise ReservaInvalidaError(
                "No fue posible confirmar la reserva."
            ) from error

        else:
            registrar_evento(
                f"Reserva {self.__identificador} confirmada."
            )
            return True

    # ======================================================
    # CANCELAR RESERVA
    # ======================================================

    def cancelar(self):

        if self.__estado not in ("Pendiente", "Confirmada"):
            raise OperacionNoPermitidaError(
                "La reserva no se puede cancelar en su estado actual."
            )

        self.__estado = "Cancelada"

        registrar_evento(
            f"Reserva {self.__identificador} cancelada."
        )

        return True

    # ======================================================
    # PROCESAR RESERVA
    # ======================================================

    def procesar(self, descuento=0, impuesto=0.0):

        if self.__estado != "Confirmada":
            raise OperacionNoPermitidaError(
                "La reserva debe estar confirmada para procesarse."
            )

        try:
            # Calcular el costo mediante polimorfismo
            total = self.__servicio.calcular_costo(
                self.__duracion,
                descuento,
                impuesto
            )

            if total < 0:
                raise DatosInvalidosError(
                    "El costo calculado no puede ser negativo."
                )

            self.__costo = total
            self.__estado = "Procesada"

        except Exception as error:
            registrar_evento(
                f"Error al procesar reserva "
                f"{self.__identificador}: {error}",
                "error"
            )

            raise ErrorSistema(
                "Se produjo un error durante el procesamiento."
            ) from error

        else:
            registrar_evento(
                f"Reserva {self.__identificador} procesada. "
                f"Costo total: {self.__costo}"
            )

            return self.__costo

        finally:
            registrar_evento(
                f"Finalizo el intento de procesamiento "
                f"de la reserva {self.__identificador}."
            )

    # ======================================================
    # MOSTRAR INFORMACION
    # ======================================================

    def mostrar_informacion(self):

        informacion = (
            f"\n========== RESERVA ==========\n"
            f"Numero: {self.identificador}\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Duracion: {self.duracion}\n"
            f"Estado: {self.estado}\n"
        )

        if self.costo is not None:
            informacion += f"Costo total: {self.costo}\n"

        informacion += "============================="

        return informacion

    def __str__(self):
        return (
            f"Reserva {self.identificador} - "
            f"{self.cliente.nombre} - "
            f"{self.servicio.nombre} - "
            f"{self.estado}"
        )
