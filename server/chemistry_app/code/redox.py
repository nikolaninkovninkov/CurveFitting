import re
from chempy import Equilibrium
from chempy import balance_stoichiometry
from chempy import Substance
import fuckit
def create_acidic_equilibrium(form1, form2, K):
    @fuckit
    def helper(oxidant, reductor, eq_const):
        return Equilibrium(*balance_stoichiometry({'H+', 'e-', oxidant}, {'H2O', reductor}), eq_const)
        return Equilibrium(*balance_stoichiometry({'e-', oxidant}, {reductor}), eq_const)
        return Equilibrium(*balance_stoichiometry({'H+', 'e-', oxidant, 'H2O'}, {reductor}), eq_const)
        return Equilibrium(*balance_stoichiometry({'H+', 'e-', oxidant}, {reductor}), eq_const)
        return Equilibrium(*balance_stoichiometry({'e-', oxidant}, {reductor}), eq_const)
        return None
    helper_return = helper(form1, form2, K)
    if helper_return:
        return helper_return
    raise ValueError("Acidic equilibrium cannot be created")