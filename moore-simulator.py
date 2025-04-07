import json

def simulate_moore_machine(states, transitions, init_state, test_string):
    curr_state = init_state
    path = [curr_state]
    output = [states[curr_state]]

    for symbol in test_string:
        curr_state = transitions[curr_state][symbol]
        path.append(curr_state)
        output.append(states[curr_state])

    return path, output


data = {}

with open ("input.json", "r") as file:
    data = json.load(file)

states = data["states"]
transitions = data["transitions"]

init_state = data["initial_state"]
test_string = data["test_string"]

result = simulate_moore_machine(states, transitions, init_state, test_string)
path = result[0]
output = result[1]

print("\nPath: " + " ➔ ".join(path))
print("Output:", "".join(output))