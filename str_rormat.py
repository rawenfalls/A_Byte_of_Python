age = 26
name = 'Swaroop'

print('Ворзраст {0} -- {1} лет.'.format(name, age))
print('Почему {0} забовляется с этим Python?'.format(name))
#десяточно число (.) с точностью в 3 знака для плавающих:
print('{0:.3}'.format(1/3))
print('{0:.5}'.format(1/3))
#заполнить подчёркиваниями (_) с центровкой текста(^) по ширине 11:
print('{0:_^11}'.format('hello'))
# по ключевым словам:
print('{name} написал {book}'.format(name= 'Swaroop', book='A byte of Python'))