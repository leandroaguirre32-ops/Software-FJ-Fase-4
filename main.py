# ==========================================================
# PROYECTO: SISTEMA INTEGRAL SOFTWARE FJ
# ARCHIVO: main.py
# DESCRIPCION: Programa principal y simulacion de operaciones
# ==========================================================

from entidades import Cliente
from servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from reservas import Reserva

from excepciones import (
    DatosInvalidosError,
    ReservaInvalidaError,
    ErrorSistema,
    registrar_evento
)


# ==========================================================
# LISTAS INTERNAS DEL SISTEMA
# ==========================================================

clientes = []
servicios = []
reservas = []


# ==========================================================
# FUNCIONES AUXILIARES
# ==========================================================

def mostrar_titulo(texto):
    print("\\n" + "=" * 65)
    print(texto.center(65))
    print("=" * 65)


def registrar_log(mensaje, tipo="info"):
    """
    Centraliza el registro de eventos y errores.
    Si el propio archivo de logs falla, el programa informa
    el inconveniente sin ocultar el error original.
    """
    try:
        registrar_evento(mensaje, tipo)
    except TypeError:
        # Compatibilidad si registrar_evento acepta un solo argumento.
        registrar_evento(mensaje)
    except Exception as error_log:
        print(f"ADVERTENCIA: no fue posible escribir en el log: {error_log}")


def mostrar_error(nombre_operacion, error):
    print(f"{nombre_operacion}: {error}")
    registrar_log(f"{nombre_operacion}: {error}", "error")


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

def ejecutar_sistema():

    # CAMBIO 1: inicializar las referencias para evitar NameError
    # si alguna creacion falla.
    cliente1 = None
    sala = None
    equipo = None
    asesoria = None

    mostrar_titulo("SISTEMA INTEGRAL SOFTWARE FJ")
    print("Bienvenido al sistema de gestion de clientes,")
    print("servicios y reservas de Software FJ.")

    registrar_log("Inicio de ejecucion del sistema Software FJ.")

    # ------------------------------------------------------
    # OPERACION 1: REGISTRO DE CLIENTE VALIDO
    # ------------------------------------------------------
    mostrar_titulo("OPERACION 1: REGISTRO DE CLIENTE")

    try:
        cliente1 = Cliente(
            "1001",
            "Carlos Ramirez",
            "carlos@gmail.com",
            "600123456"
        )
        clientes.append(cliente1)

    except DatosInvalidosError as error:
        mostrar_error("Error al registrar cliente", error)

    except Exception as error:
        mostrar_error("Error inesperado al registrar cliente", error)

    else:
        print("Cliente registrado correctamente.")
        print(cliente1.mostrar_informacion())
        registrar_log("Cliente 1001 registrado correctamente.")

    finally:
        print("Operacion 1 finalizada.")

    # ------------------------------------------------------
    # OPERACION 2: REGISTRO DE CLIENTE INVALIDO
    # ------------------------------------------------------
    mostrar_titulo("OPERACION 2: CLIENTE CON DATOS INVALIDOS")

    try:
        cliente_invalido = Cliente(
            "1002",
            "Maria Lopez",
            "correo_incorrecto",
            "123"
        )
        clientes.append(cliente_invalido)

    except DatosInvalidosError as error:
        print("Registro rechazado:", error)
        registrar_log(f"Registro de cliente invalido: {error}", "error")

    except Exception as error:
        mostrar_error("Error inesperado en el registro invalido", error)

    else:
        print("El cliente fue registrado.")
        registrar_log("Registro de cliente de la operacion 2 completado.")

    finally:
        print("Operacion 2 finalizada.")

    # ------------------------------------------------------
    # OPERACION 3: CREAR SERVICIO DE SALA
    # ------------------------------------------------------
    mostrar_titulo("OPERACION 3: CREACION DE SALA")

    try:
        sala = ReservaSala(
            "S001",
            "Sala de reuniones",
            50,
            20
        )
        servicios.append(sala)

    except DatosInvalidosError as error:
        mostrar_error("Error al crear sala", error)

    except Exception as error:
        mostrar_error("Error inesperado al crear sala", error)

    else:
        print("Servicio creado correctamente.")
        print(sala.describir_servicio())
        registrar_log("Servicio de sala S001 creado correctamente.")

    finally:
        print("Operacion 3 finalizada.")

    # ------------------------------------------------------
    # OPERACION 4: CREAR SERVICIO DE ALQUILER
    # ------------------------------------------------------
    mostrar_titulo("OPERACION 4: ALQUILER DE EQUIPOS")

    try:
        equipo = AlquilerEquipo(
            "E001",
            "Proyector multimedia",
            30,
            10
        )
        servicios.append(equipo)

    except DatosInvalidosError as error:
        mostrar_error("Error al crear equipo", error)

    except Exception as error:
        mostrar_error("Error inesperado al crear equipo", error)

    else:
        print("Servicio creado correctamente.")
        print(equipo.describir_servicio())
        registrar_log("Servicio de equipo E001 creado correctamente.")

    finally:
        print("Operacion 4 finalizada.")

    # ------------------------------------------------------
    # OPERACION 5: CREAR SERVICIO DE ASESORIA
    # ------------------------------------------------------
    mostrar_titulo("OPERACION 5: ASESORIA ESPECIALIZADA")

    try:
        asesoria = AsesoriaEspecializada(
            "A001",
            "Asesoria en programacion",
            60,
            "Desarrollo de software"
        )
        servicios.append(asesoria)

    except DatosInvalidosError as error:
        mostrar_error("Error al crear asesoria", error)

    except Exception as error:
        mostrar_error("Error inesperado al crear asesoria", error)

    else:
        print("Servicio creado correctamente.")
        print(asesoria.describir_servicio())
        registrar_log("Servicio de asesoria A001 creado correctamente.")

    finally:
        print("Operacion 5 finalizada.")

    # ------------------------------------------------------
    # OPERACION 6: CREAR SERVICIO INVALIDO
    # ------------------------------------------------------
    mostrar_titulo("OPERACION 6: SERVICIO INVALIDO")

    try:
        servicio_invalido = ReservaSala(
            "S002",
            "Sala incorrecta",
            -50,
            10
        )
        servicios.append(servicio_invalido)

    except DatosInvalidosError as error:
        print("Servicio rechazado:", error)
        registrar_log(f"Creacion de servicio invalido: {error}", "error")

    except Exception as error:
        mostrar_error("Error inesperado al crear servicio invalido", error)

    else:
        print("El servicio fue creado.")
        registrar_log("Servicio de la operacion 6 creado.")

    finally:
        print("Operacion 6 finalizada.")

    # ------------------------------------------------------
    # OPERACION 7: RESERVA EXITOSA DE SALA
    # ------------------------------------------------------
    mostrar_titulo("OPERACION 7: RESERVA EXITOSA DE SALA")

    try:
        # CAMBIO 2: comprobar dependencias antes de usarlas.
        if cliente1 is None or sala is None:
            raise ErrorSistema(
                "No se puede reservar: el cliente o la sala no estan disponibles."
            )

        reserva1 = Reserva(cliente1, sala, 3, asistentes=10)
        reserva1.confirmar()

        # CAMBIO 3: guardar solamente despues de confirmar.
        reservas.append(reserva1)

        costo1 = reserva1.procesar(descuento=10, impuesto=0.21)

    except ErrorSistema as error:
        mostrar_error("Error en la reserva de sala", error)

    except Exception as error:
        mostrar_error("Error inesperado en la reserva de sala", error)

    else:
        print("Reserva realizada correctamente.")
        print(reserva1.mostrar_informacion())
        print("Costo calculado:", costo1)
        registrar_log("Reserva de sala confirmada y procesada.")

    finally:
        print("Operacion 7 finalizada.")

    # ------------------------------------------------------
    # OPERACION 8: RESERVA CON PARAMETROS INCORRECTOS
    # ------------------------------------------------------
    mostrar_titulo("OPERACION 8: RESERVA FALLIDA")

    try:
        if cliente1 is None or sala is None:
            raise ErrorSistema(
                "No se puede probar la reserva: falta el cliente o la sala."
            )

        reserva2 = Reserva(cliente1, sala, 2, asistentes=50)
        reserva2.confirmar()

        # Una reserva fallida no se agrega a la lista de confirmadas.
        reservas.append(reserva2)

    except ReservaInvalidaError as error:
        print("No fue posible confirmar la reserva.")
        print("Motivo:", error)
        registrar_log(f"Reserva rechazada por parametros incorrectos: {error}", "error")

    except ErrorSistema as error:
        mostrar_error("Error del sistema en la reserva fallida", error)

    except Exception as error:
        mostrar_error("Error inesperado en la operacion 8", error)

    else:
        print("La reserva fue confirmada.")
        registrar_log("Reserva de la operacion 8 confirmada.")

    finally:
        print("Operacion 8 finalizada.")

    # ------------------------------------------------------
    # OPERACION 9: RESERVA DE EQUIPOS
    # ------------------------------------------------------
    mostrar_titulo("OPERACION 9: RESERVA DE EQUIPOS")

    try:
        if cliente1 is None or equipo is None:
            raise ErrorSistema(
                "No se puede alquilar: el cliente o el equipo no estan disponibles."
            )

        reserva3 = Reserva(cliente1, equipo, 2, cantidad=3)
        reserva3.confirmar()
        reservas.append(reserva3)

        costo3 = reserva3.procesar(descuento=5, impuesto=0.21)

    except ErrorSistema as error:
        mostrar_error("Error en alquiler de equipos", error)

    except Exception as error:
        mostrar_error("Error inesperado en alquiler de equipos", error)

    else:
        print("Alquiler procesado correctamente.")
        print(reserva3.mostrar_informacion())
        print("Costo calculado:", costo3)
        registrar_log("Reserva de equipos confirmada y procesada.")

    finally:
        print("Operacion 9 finalizada.")

    # ------------------------------------------------------
    # OPERACION 10: RESERVA DE ASESORIA
    # ------------------------------------------------------
    mostrar_titulo("OPERACION 10: RESERVA DE ASESORIA")

    try:
        if cliente1 is None or asesoria is None:
            raise ErrorSistema(
                "No se puede reservar la asesoria: faltan datos del cliente o servicio."
            )

        reserva4 = Reserva(
            cliente1,
            asesoria,
            2,
            modalidad="virtual"
        )
        reserva4.confirmar()
        reservas.append(reserva4)

        costo4 = reserva4.procesar(descuento=0, impuesto=0.21)

    except ErrorSistema as error:
        mostrar_error("Error en reserva de asesoria", error)

    except Exception as error:
        mostrar_error("Error inesperado en reserva de asesoria", error)

    else:
        print("Asesoria procesada correctamente.")
        print(reserva4.mostrar_informacion())
        print("Costo calculado:", costo4)
        registrar_log("Reserva de asesoria confirmada y procesada.")

    finally:
        print("Operacion 10 finalizada.")

    # ------------------------------------------------------
    # OPERACION 11: CANCELACION DE RESERVA
    # ------------------------------------------------------
    mostrar_titulo("OPERACION 11: CANCELACION DE RESERVA")

    try:
        if cliente1 is None or sala is None:
            raise ErrorSistema(
                "No se puede cancelar una reserva: faltan el cliente o la sala."
            )

        reserva_cancelacion = Reserva(
            cliente1,
            sala,
            1,
            asistentes=5
        )
        reserva_cancelacion.confirmar()
        reservas.append(reserva_cancelacion)
        reserva_cancelacion.cancelar()

    except ErrorSistema as error:
        mostrar_error("Error al cancelar reserva", error)

    except Exception as error:
        mostrar_error("Error inesperado al cancelar reserva", error)

    else:
        print("Reserva cancelada correctamente.")
        print(reserva_cancelacion.mostrar_informacion())
        registrar_log("Reserva confirmada y posteriormente cancelada.")

    finally:
        print("Operacion 11 finalizada.")

    # ------------------------------------------------------
    # RESUMEN GENERAL DEL SISTEMA
    # ------------------------------------------------------
    mostrar_titulo("RESUMEN GENERAL DEL SISTEMA")

    print("Total de clientes registrados:", len(clientes))
    print("Total de servicios creados:", len(servicios))
    print("Total de reservas confirmadas:", len(reservas))

    print("\\nLISTADO DE CLIENTES:")
    for cliente in clientes:
        print(cliente.mostrar_informacion())

    print("\\nLISTADO DE SERVICIOS:")
    for servicio in servicios:
        print(servicio.describir_servicio())

    print("\\nLISTADO DE RESERVAS:")
    for reserva in reservas:
        print(reserva.mostrar_informacion())

    registrar_log("Ejecucion del sistema Software FJ finalizada.")

    mostrar_titulo("FIN DEL PROGRAMA")
    print("Gracias por utilizar Software FJ.")


# ==========================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ==========================================================

if __name__ == "__main__":
    try:
        ejecutar_sistema()

    except Exception as error:
        # Ultima barrera de seguridad: registra errores no controlados.
        print("Se produjo un error inesperado:", error)
        registrar_log(f"Error general del sistema: {error}", "error")

    finally:
        print("\\nCierre de la ejecucion del programa.")

