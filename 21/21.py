def bmi(weight, height):
    return weight / (height ** 2)


def print_bmi(bmi):
    if bmi < 18.5:
        print("Underweight")
        return
    if bmi < 25:
        print("Normal weight")
        return
    if bmi < 30:
        print("Overweight")
        return
    print("Obesity")


weight, height = map(float, input("weight height = ").split())
height /= 100
bmi = bmi(weight, height)
print_bmi(bmi)
