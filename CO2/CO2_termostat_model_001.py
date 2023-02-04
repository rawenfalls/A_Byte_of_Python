from decimal import Decimal

import numpy as np
import matplotlib.pyplot as plt

TempCabinet = 25				#начальная температура.
'''начальная температура.'''
TempUstavka = 30				#целевая температура, которую должен поддерживать термостат.
'''целевая температура, которую должен поддерживать термостат.'''
TimeMod = 20					#длительность моделирования.
'''длительность моделирования.'''
TimeStep = 0.1					#шаг изменеиня времени, значение должно быть кратно целым числам.
'''шаг изменеиня времени, значение должно быть кратно целым числам.'''
t = 0							#переменная времени.
'''переменная времени.'''
Temp = TempCabinet				#текущая температура термостата.
'''текущая температура термостата.'''
TempDiff = 0
'''ошибка управления по температуре'''
Number_of_decimals = 2
'''количество знаков после запятой'''
K_proportionally = 10			#коэффициэкнт пропорциональной составляющей.
'''коэффициэкнт пропорциональной составляющей.'''
Integral = 60					#время интегрирования ПИД регулятора в секундах.
'''время интегрирования ПИД регулятора в секундах'''
arr_Temp_Integral = [(TempUstavka - TempCabinet)] * Integral	#массив предыдущих температур за время интегрирования.
'''массив предыдущих температур за время интегрирования'''
K_integral = 1e-2					#коэффициэнт интегральной составляющей.
'''коэффициэнт интегральной составляющей.'''
Differential = 1					#смещение по массиву температур: difTemp=Temp(i)-Temp(i-3)
'''смещение по массиву температур: difTemp=Temp(i)-Temp(i-3)'''
K_differential = 0.1				#коэффициэнт дифференциальной составляющей.
'''коэффициэнт дифференциальной составляющей.'''
while t <= TimeMod:
	TempDiff = TempUstavka - Temp
	PID_proportionally =- K_proportionally * TempDiff
	PID_integral = K_integral * sum(arr_Temp_Integral)
	PID_differential = K_differential*(TempDiff - arr_Temp_Integral[-1 * Differential])
	PID = PID_proportionally + PID_integral + PID_differential
	if int(t) == t:
		arr_Temp_Integral.append(round(TempDiff,Number_of_decimals))
		del arr_Temp_Integral[0]
	t = round((t + TimeStep),Number_of_decimals)
	print(arr_Temp_Integral)
	print(t)
	Temp = Temp + TimeStep
	


