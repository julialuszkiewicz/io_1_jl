def oblicz_pole_trojkata(podstawa, wysokosc):
    pole = 0.5 * podstawa * wysokosc
    return pole

try:
    podstawa = float(input("Podaj długość podstawy trójkąta: "))
    wysokosc = float(input("Podaj wysokość trójkąta: "))
    
    pole = oblicz_pole_trojkata(podstawa, wysokosc)
    print("Pole trójkąta wynosi:", pole)
    
except ValueError:
    print("Podano nieprawidłową wartość. Wprowadź liczbę.")

def oblicz_pole_prostokata(bok_a, bok_b):
    pole_p = bok_a*bok_b
    return pole_p
try:
    bok_a = float(input("podaj długość boku a"))
    bok_b = float(input("podaj dlugosc boku b"))

    pole_p = oblicz_pole_prostokata(bok_a, bok_b)
    print("pole prostokąta wynosi:", pole_p)

except ValueError:
    print("Podano nieprawidłową wartość. Wprowadź liczbę.")

def oblicz_pole_kw(bok_kw):
    pole_k = bok_kw * bok_kw
    return pole_k

try:
    bok_kw = float(input("Podaj długość boku kwadratu: "))
    bok_kw = float(input("Podaj długość boku kwadratu: "))

    pole_k = oblicz_pole_kw(bok_kw)
    print("Pole kwadratu wynosi:", pole_k)

except ValueError:
    print("Podano nieprawidłową wartość. Wprowadź liczbę.")



 