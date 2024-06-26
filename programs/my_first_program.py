from nada_dsl import *

def nada_main():
    
    party1 = Party(name="Party1")

   
    secret_int1 = SecretInteger(Input(name="my_int1", party=party1))
    secret_int2 = SecretInteger(Input(name="my_int2", party=party1))

    
    addition_result = secret_int1 + secret_int2

    
    return [Output(value=addition_result, name="addition_output", party=party1)]

if __name__ == "__main__":
    result = nada_main()
    print("Result:", result)