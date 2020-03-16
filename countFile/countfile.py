def nhapFile(i):
    print(i)
    print("Moi ban nhap ten file ")
    b = a.append(input('Nhap: '))
    return b


def nhapFoler():
    print("so phan tu cua file la: ");
    m = int(input())
    for i in range(m):
        print('phan tu thu i la file or folder: 0===> file , 1 ====> folder ');
        val = int(input())
        if val == 0:
            return nhapFile(i)
        else:
            return nhapFoler()


try:
    n = int(input("Nhap n: "))
    if n <= 0:
        exit()
except:
    print('Phai nhap so tu nhien')
    exit()
a = []

for i in range(n):
    print('phan tu thu i la file or folder: 0===> file , 1 ====> folder ');
    values = int(input())
    if values == 0:
        nhapFile(i)
    else:
        nhapFoler()
print(a)
print(len(a))
