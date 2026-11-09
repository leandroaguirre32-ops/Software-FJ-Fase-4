
# ==========================================================
# PROYECTO: SISTEMA INTEGRAL SOFTWARE FJ
# ARCHIVO: main.py
# DESCRIPCION: Programa principal y pruebas del sistema
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
# FUNCION PARA MOSTRAR TITULOS
# ==========================================================

def mostrar_titulo(texto):

    print("\n" + "=" * 65)
    print(texto.center(65))
    print("=" * 65)


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

def ejecutar_sistema():

    mostrar_titulo("SISTEMA INTEGRAL SOFTWARE FJ")

    print("Bienvenido al sistema de gestion de clientes,")
    print("servicios y reservas de Software FJ.")

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

        print("Cliente registrado correctamente.")
        print(cliente1.mostrar_informacion())

    except DatosInvalidosError as error:
        print("Error al registrar cliente:", error)

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
        registrar_evento(
            f"Registro de cliente invalido: {error}",
            "error"
        )

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

        print("Servicio creado correctamente.")
        print(sala.describir_servicio())

    except DatosInvalidosError as error:
        print("Error al crear sala:", error)

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

        print("Servicio creado correctamente.")
        print(equipo.describir_servicio())

    except DatosInvalidosError as error:
        print("Error al crear equipo:", error)

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

        print("Servicio creado correctamente.")
        print(asesoria.describir_servicio())

    except DatosInvalidosError as error:
        print("Error al crear asesoria:", error)

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
        registrar_evento(
            f"Creacion de servicio invalido: {error}",
            "error"
        )

    # ------------------------------------------------------
    # OPERACION 7: RESERVA EXITOSA DE SALA
    # ------------------------------------------------------

    mostrar_titulo("OPERACION 7: RESERVA EXITOSA DE SALA")

    try:
        reserva1 = Reserva(
            cliente1,
            sala,
            3,
            asistentes=10
        )

        reservas.append(reserva1)

        reserva1.confirmar()

        costo1 = reserva1.procesar(
            descuento=10,
            impuesto=0.21
        )

        print("Reserva realizada correctamente.")
        print(reserva1.mostrar_informacion())

    except ErrorSistema as error:
        print("Error en la reserva:", error)

    # ------------------------------------------------------
    # OPERACION 8: RESERVA CON PARAMETROS INCORRECTOS
    # ------------------------------------------------------

    mostrar_titulo("OPERACION 8: RESERVA FALLIDA")

    try:
        reserva2 = Reserva(
            cliente1,
            sala,
            2,
            asistentes=50
        )

        reservas.append(reserva2)

        reserva2.confirmar()

    except ReservaInvalidaError as error:
        print("No fue posible confirmar la reserva.")
        print("Motivo:", error)

    except ErrorSistema as error:
        print("Error:", error)

    # ------------------------------------------------------
    # OPERACION 9: RESERVA DE EQUIPOS
    # ------------------------------------------------------

    mostrar_titulo("OPERACION 9: RESERVA DE EQUIPOS")

    try:
        reserva3 = Reserva(
            cliente1,
            equipo,
            2,
            cantidad=3
        )

        reservas.append(reserva3)

        reserva3.confirmar()

        costo3 = reserva3.procesar(
            descuento=5,
            impuesto=0.21
        )

        print("Alquiler procesado correctamente.")
        print(reserva3.mostrar_informacion())

    except ErrorSistema as error:
        print("Error en alquiler:", error)

    # ------------------------------------------------------
    # OPERACION 10: RESERVA DE ASESORIA
    # ------------------------------------------------------

    mostrar_titulo("OPERACION 10: RESERVA DE ASESORIA")

    try:
        reserva4 = Reserva(
            cliente1,
            asesoria,
            2,
            modalidad="virtual"
        )

        reservas.append(reserva4)

        reserva4.confirmar()

        costo4 = reserva4.procesar(
            descuento=0,
            impuesto=0.21
        )

        print("Asesoria procesada correctamente.")
        print(reserva4.mostrar_informacion())

    except ErrorSistema as error:
        print("Error en asesoria:", error)

    # ------------------------------------------------------
    # OPERACION 11: CANCELACION DE RESERVA
    # ------------------------------------------------------

    mostrar_titulo("OPERACION 11: CANCELACION DE RESERVA")

    try:
        reserva_cancelacion = Reserva(
            cliente1,
            sala,
            1,
            asistentes=5
        )

        reservas.append(reserva_cancelacion)

        reserva_cancelacion.confirmar()
        reserva_cancelacion.cancelar()

        print("Reserva cancelada correctamente.")
        print(reserva_cancelacion.mostrar_informacion())

    except ErrorSistema as error:
        print("Error al cancelar:", error)

    # ------------------------------------------------------
    # RESUMEN GENERAL DEL SISTEMA
    # ------------------------------------------------------

    mostrar_titulo("RESUMEN GENERAL DEL SISTEMA")

    print("Total de clientes registrados:", len(clientes))
    print("Total de servicios creados:", len(servicios))
    print("Total de reservas realizadas:", len(reservas))

    print("\nLISTADO DE CLIENTES:")

    for cliente in clientes:
        print(cliente)

    print("\nLISTADO DE SERVICIOS:")

    for servicio in servicios:
        print(servicio.describir_servicio())

    print("\nLISTADO DE RESERVAS:")

    for reserva in reservas:
        print(reserva)

    registrar_evento(
        "Ejecucion del sistema Software FJ finalizada."
    )

    mostrar_titulo("FIN DEL PROGRAMA")

    print("Gracias por utilizar Software FJ.")


# ==========================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ==========================================================

if __name__ == "__main__":

    try:
        ejecutar_sistema()

    except Exception as error:
        print("Se produjo un error inesperado:", error)

        registrar_evento(
            f"Error general del sistema: {error}",
            "error"
        )
