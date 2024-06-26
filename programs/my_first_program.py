from nada_dsl import *

def nada_main():
    # Define the party
    party1 = Party(name="Party1")

    # Define secret integer inputs for the party
    secret_int1 = SecretInteger(Input(name="my_int1", party=party1))
    secret_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Perform the addition of the two secret integers
    addition_result = secret_int1 + secret_int2

    # Return the result as an output for the party
    return [Output(addition_result, "addition_output", party1)]
