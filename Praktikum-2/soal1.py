# program kalkulator sederhana 
print("=== kalkulator sederhana ===")
angka1 = float(input("masukan angka pertama: "))
operator = input("masukan operator (+, -, *, /): ")
angka2 = float(input("masukan angka kedua: "))

if operator == "+":
    hasil = angka1 + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "*":
    hasil = angka1 * angka2
elif operator == "/":
    hasil = angka1 / angka2
else:
    hasil = "operator tidak dikenali"
    
