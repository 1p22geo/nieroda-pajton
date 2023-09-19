def sil(x):
    if(x<2):
        return 1
    return sil(x-1)*x

print(sil(5))