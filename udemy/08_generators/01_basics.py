def serve_chai():
    yield "Cup 1: Masala chai"
    yield "Cup 2: Green tea"
    yield "Cup 3: Elaichi chai"

stall = serve_chai()

# for cup in stall:
#     print(cup)

def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"

chai = get_chai_gen()
print(next(chai))
print(next(chai))
# print(next(chai)) // error