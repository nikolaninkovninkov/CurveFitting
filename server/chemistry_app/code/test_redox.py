from chempy import Equilibrium, balance_stoichiometry
from redox import create_acidic_equilibrium
def test_create_acidic_equilibrium():
    with open('testdata/forms.txt', 'r') as f:
        oxidants_and_reductors = [line.strip().split('=') for line in list(filter(lambda x: '#' not in x, f.readlines()))]
    with open('testdata/equilibria.txt', 'r') as f:
        equilibria_lines = list(filter(lambda x: '#' not in x, f.readlines()))
    assert len(equilibria_lines) == len(oxidants_and_reductors)
    length = len(equilibria_lines)
    for i in range(length):
        try:
            form1, form2 = oxidants_and_reductors[i]
            print(form1, form2)
            try:
                created_equilibrium = create_acidic_equilibrium(form1, form2, 1)
            except ValueError:
                print("Error 1")
            print(created_equilibrium)
            test_equilibrium = Equilibrium.from_string(equilibria_lines[i])
            print(test_equilibrium)
            assert dict(created_equilibrium.reac) == dict(test_equilibrium.reac)
            assert dict(created_equilibrium.prod) == dict(test_equilibrium.prod)
        except:
            print('Error 2')
            return
test_create_acidic_equilibrium()
