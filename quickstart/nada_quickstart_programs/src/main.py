from nada_dsl import *

def nada_main():
    # Define the parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")
    party4 = Party(name="Party4")  # New party to receive the output

    # Define the secret inputs for each party
    a = SecretInteger(Input(name="A", party=party1))
    b = SecretInteger(Input(name="B", party=party2))
    c = SecretInteger(Input(name="C", party=party3))  # New secret input

    # Compute the sum of the three secret integers
    result = a + b + c

    # Output the result to the fourth party
    return [Output(result, "sum_output", party4)]
