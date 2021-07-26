import random
import string

contra = ''
for i in range(1):
    #GENERADORES CARACTERES
    cara=string.ascii_letters+string.digits+string.whitespace+string.__cached__+string.octdigits+string.printable  # whitspaces genera espacios en la contraseña
    #contra = contra + random.choice(usua)
    contra=("").join(random.choice(cara) for i in range(15))
    print("")
    print("Tu contraseña es : "+ contra)
    print("")