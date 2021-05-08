import os

tiposdeplaca = ['AB01', 'AB02', 'AC01', 'AC02']

for placa in tiposdeplaca:
    for file in os.listdir('../results/'+placa+'/iguais/'):
        os.remove('../results/'+placa+'/iguais/' + file)

    for file in os.listdir('../results/'+placa+'/diferentes/'):
        os.remove('../results/'+placa+'/diferentes/' + file)
