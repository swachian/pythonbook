from collections import deque

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

def print_models(unprinted_designs, completed_models):
    my_deque = deque(unprinted_designs)
    while my_deque:
        design = my_deque.popleft()
        print(f"print {design}")
        completed_models.append(design)

def show_completed_models(completed_list):
    for design in completed_list:
        print(design)

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(unprinted_designs)

def print_messages(messages, sent_messages):
    while messages:
        message = messages.pop()
        print(f"sent {message}")
        sent_messages.append(message)
messages = ['Love', "Duo", "Cuo"]
sent_messages = []
print_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)

