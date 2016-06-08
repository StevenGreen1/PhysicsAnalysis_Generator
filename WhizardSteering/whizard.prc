# WHIZARD configuration file

# The selected model
model	SM_km

# Processes
#  Methods: chep=CompHEP, mad=MadGraph, omega=O'Mega, test=trivial)
#  Options: s      selected diagrams (CompHEP/MadGraph)
#           r      restricted intermediate state (O'Mega)
#           c      apply exact color algebra (O'Mega)
#           d      Feynman diagram option (O'Mega)
#           n:XXX  coupling order (MadGraph)
#           w:XXX  width scheme (O'Mega)
#           p      transfer polarization (test)
#           u      unit matrix element (test)
#
# Tag    	In      Out     	Method	Option
#=====================================================
alias up u:c
alias down d:s:b
alias anti_up U:C
alias anti_down D:S:B

vbswwww	e1,E1	n1,N1,up,anti_down,down,anti_up		omega	r: 5+6~W+ && 7+8~W- && 1+3~W- && 2+4~W+ 
vbswwzz	e1,E1	n1,N1,up,anti_up,down,anti_down		omega	r: 5+6~Z && 7+8~Z && 1+3~W- && 2+4~W+ 

