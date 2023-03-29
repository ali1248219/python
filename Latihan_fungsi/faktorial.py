def faktorial(bil):
    hasil_faktorial = 1
    for x in range(2, bil+1):
        hasil_faktorial = hasil_faktorial * x
    return hasil_faktorial


for f in range(1, 10):
    print('{} faktorial = {}'.format(f, faktorial(f)))
