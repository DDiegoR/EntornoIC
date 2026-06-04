from behave import given, when, then
from app import app

@given('que ingreso el numero "{numero_a}"')
def step_impl_a(context, numero_a):
    context.numero_a = numero_a
    # Configuramos un cliente de pruebas para nuestra app Flask
    context.client = app.test_client()

@given('el numero "{numero_b}"')
def step_impl_b(context, numero_b):
    context.numero_b = numero_b

@when('solicito realizar la suma')
def step_impl_suma(context):
    # Simulamos que un usuario entra a la URL de suma
    url = f"/add/{context.numero_a}/{context.numero_b}"
    context.response = context.client.get(url)

@then('el resultado en pantalla debe ser "{resultado_esperado}"')
def step_impl_resultado(context, resultado_esperado):
    # Verificamos que el texto de la respuesta contenga el resultado esperado
    respuesta_texto = context.response.data.decode('utf-8')
    assert resultado_esperado in respuesta_texto, f"Esperaba '{resultado_esperado}' pero obtuve '{respuesta_texto}'"
