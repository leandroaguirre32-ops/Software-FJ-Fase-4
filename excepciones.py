
# ==========================================================
# PROYECTO: SISTEMA INTEGRAL SOFTWARE FJ
# ARCHIVO: excepciones.py
# DESCRIPCION: Manejo de errores personalizados y registros
# ==========================================================

import logging


# Configuracion del sistema de registros (logs)
logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Logger principal del sistema
logger = logging.getLogger("SoftwareFJ")


# Funcion para registrar eventos y errores
def registrar_evento(mensaje, nivel="info"):
    if nivel == "error":
        logger.error(mensaje)
    elif nivel == "warning":
        logger.warning(mensaje)
    else:
        logger.info(mensaje)


# ==========================================================
# EXCEPCIONES PERSONALIZADAS
# ==========================================================

class ErrorSistema(Exception):
    """Excepcion general del sistema Software FJ."""
    pass


class DatosInvalidosError(ErrorSistema):
    """Se produce cuando los datos ingresados no son validos."""
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """Se produce cuando un servicio no esta disponible."""
    pass


class ReservaInvalidaError(ErrorSistema):
    """Se produce cuando una reserva no cumple los requisitos."""
    pass


class OperacionNoPermitidaError(ErrorSistema):
    """Se produce cuando se intenta una operacion no permitida."""
    pass


# Registro de carga del modulo
registrar_evento("Modulo de excepciones cargado correctamente.")

