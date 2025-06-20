from collections import deque

def print_models(unprinted_designs, completed_models):
    my_deque = deque(unprinted_designs)
    while my_deque:
        design = my_deque.popleft()
        print(f"print {design}")
        completed_models.append(design)

def show_completed_models(completed_list):
    print("\nThe followings have been completed")
    for design in completed_list:
        print(design)
    print()

