import locale as __locale

if 'es' in __locale.getdefaultlocale()[0]:
    from spanish_message import *
else:
    from english_message import *
    
    
C_BLACK = 'black'
C_RED = 'red'
C_DARKRED = 'darkred'
C_BLUE = 'blue'
C_DARKBLUE = 'darkblue'
C_GREEN = 'green'
C_DARKGREEN = 'darkgreen'
C_YELLOW = 'yellow'
C_DARKYELLOW = 'darkyellow'
C_WHITE = 'white'

SOLID = 'solid'

# Alignment
TOP = 'top'
LEFT = 'left'
