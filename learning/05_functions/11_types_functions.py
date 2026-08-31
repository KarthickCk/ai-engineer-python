# def pure_chai(cups):
#     return cups * 2

# total_chai = 0

# # not recommended to use global variables, but it is possible to do so
# def impure_chai(cups):
#     global total_chai
#     total_chai += cups * 2
#     return total_chai

# def pour_chai(n):
#     if n == 0:
#         return "No cups to pour."
#     return pour_chai(n-1)

# print(pour_chai(5))

def chai_report():
    print("Generating chai report...")

chai_types = ["green", "black", "white", "green"]

strong_chai = list(filter(lambda chai: chai == "green", chai_types))
print(strong_chai)