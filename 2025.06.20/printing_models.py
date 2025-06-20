import printing_model_functions
from printing_model_functions import print_models, show_completed_models
import printing_model_functions as pmf
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_model_functions.print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
pmf.show_completed_models(completed_models)
print(unprinted_designs)