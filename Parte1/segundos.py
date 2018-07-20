segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

horas = segundos // 3600

segundos_restantes = segundos % 3600

minutos = segundos_restantes // 60

segundos_restantes_final = segundos_restantes % 60

dias = horas // 24

horas_final = horas % 24
print(dias,"dias,",horas_final,"horas,",minutos,"minutos e",segundos_restantes_final,"segundos")