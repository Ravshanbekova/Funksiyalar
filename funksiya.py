# def yigindi(son1, son2):
#     natija = son1 + son2
#     return f"Yig'indi: {natija}"
#
# son1 = int(input("Son 1 ni kiriting: "))
# son2 = int(input("Son 2 ni kiriting: "))
#
# print(yigindi(son1, son2))


def calculator(son1, son2, belgi):
    if belgi == "+":
        return f"Yig'indi: {son1 + son2}"
    elif belgi == "-":
        return f"Ayirma: {son1 - son2}"
    elif belgi == "*":
        return f"Ko'paytma: {son1 * son2}"
    elif belgi == "/":
        return f"Bo'linma: {son1 / son2}"
    else:
        return f"Qiymat xato kiritildi"

son1 = float(input("1 - sonni kiriting: "))
son2 = float(input("2 - sonni kiriting: "))
belgi = input("Belgini kiriting(+, -, *, /): ")

print(calculator(son1, son2, belgi))







