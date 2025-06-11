print("verificando si el servicio ejecutado esta activo")

import os 
import sys

if os.name == 'nt':
    print("Windows")
elif os.name == 'posix':
    print("Linux")
elif os.name == 'mac':
    print("macOS")
else:
    print("otro sistema operativo")

print("Gracias por la verificacion")