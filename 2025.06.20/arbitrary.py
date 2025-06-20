def make_sandwich(*args):
    for sandwitch in args:
        print(f"-{sandwitch}")
make_sandwich('tuna')
make_sandwich('tuna', 'pork')
make_sandwich('tuna', 'pork', 'chicken')