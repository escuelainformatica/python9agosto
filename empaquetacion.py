def mifuncion(arg1,arg2,arg3,arg4):
    pass
def mifuncion2(*arg):
    print("{0} {1} {2} {3}".format(arg[0],arg[1],arg[2],arg[3]))


def mifuncion3(**kwargs):
    print("{0} {1}".format(kwargs['arg1'],kwargs['arg2']))


mifuncion(1,2,3,4,)

tuple=(1,2,3,4)

mifuncion2( *tuple )   # mifuncion2( 1,2,3,4)

# kwargs (argumentos con nombre)

dic={"arg1":"hola","arg2":"mundo"}

mifuncion3(**dic)  # mifuncion3(arg1="hola",arg2="mundo")
mifuncion3(arg1="hola",arg2="mundo")

