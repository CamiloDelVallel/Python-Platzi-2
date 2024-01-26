def message_creator(text):
   # Escribe tu solución 👇
   if text == "computadora":
      response = "Con mi computadora puedo programar usando Python"
   elif text == "celular":
     response = "En mi celular puedo aprender usando la app de Platzi"
   elif text == "cable":
      response = "¡Hay un cable en mi bota!"
   else:
      response = "Artículo no encontrado"

   return response

text = 'computadora'
response = message_creator(text)
print(response)