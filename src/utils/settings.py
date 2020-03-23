import os
import sys
import platform

try:
    # Si se ejecuta desde allure, se toma este path
    path= os.path.abspath(sys.argv[1])
except IndexError:
    # Si se ejecuta localmente, se usa este path
    path = os.path.abspath(sys.path[0])

splitpath = path.split('\\')
index = splitpath.index('proyectos')
proyecto = splitpath[index+1]

if platform.system() == 'Windows':
    path_evidence = os.path.join('C:\evidencias\some_test',
                                 proyecto, 'screenshots')
else:
    print('Definir el path de la evidencia')
