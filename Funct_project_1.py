inputs = input("Input any hypen seperated colour : ")

def sort_inputs(inputs):
    inputs_list = inputs.split('-')

    sorted_input = sorted(inputs_list)

    final = "-".join(term for term in sorted_input)

    return final

final = sort_inputs(inputs)

print(final)
