import pickle
import bz2
user_string = """Per me si va ne la città dolente, 
per me si va ne l'etterno dolore, 
per me si va tra la perduta gente. 
Giustizia mosse il mio alto fattore: 
fecemi la divina podestate, 
la somma sapienza e 'l primo amore; 
dinanzi a me non fuor cose create 
se non etterne, e io etterno duro. 
Lasciate ogne speranza, voi ch'intrate."""
pickling = pickle.dumps( user_string )
compressed = bz2.compress( pickling )
len( user_string )  