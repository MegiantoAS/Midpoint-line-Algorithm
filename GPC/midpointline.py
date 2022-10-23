import matplotlib.pyplot as plt
plt.title("Menggambar Garis dengan Menggunakan Algoritma Midpoint")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")

def line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    #Decision parameter
    d = dy - (dx/2)
    x = x1
    y = y1
    
    print ('x = %s, y = %s' % (x,y))

    #plotting points
    x_koordinat = [x]
    y_koordinat = [y]

    while(x < x2):
        x = x + 1
        if (d < 0):
            d = d + dy

        else: 
            d = d + (dy - dx)
            y = y + 1

        x_koordinat.append(x)
        y_koordinat.append(y)
        print('x =%s, y =%s' % (x, y))
    plt.plot(x_koordinat, y_koordinat)
    plt.show()
    
if __name__ == "__main__":
    x1 = int(input("Masukan Nilai x1: "))
    y1 = int(input("Masukan Nilai y1: "))                
    x2 = int(input("Masukan Nilai x2: "))              
    y2 = int(input("Masukan Nilai y2: "))    

    line(x1, y1, x2, y2)