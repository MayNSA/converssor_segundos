print("\033[35m--- Converssor de Segundos ---")
print()

segundos = float(input("\033[31mSegundos a ser convertido: "))

hora = segundos // 3600
segundos_restantes = segundos % 3600

minuto = segundos_restantes // 60
segundos_final = segundos_restantes % 60

print("\033[34m{} hora, {} minutos e {} segundos".format(hora, minuto, segundos_final))