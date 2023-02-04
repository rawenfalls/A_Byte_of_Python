x = 50

def func():
    global x

    print('x равен', x)
    x = 2
    print('Замена локального x на', x)

func ()
print('x по прежнему ', x)