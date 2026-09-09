# Filtra hostnames de servidores a partir de uma lista de inventario

hostnames = ["SRV-FILE-01", "SRV-DC-02", "WKS-RH-115", "SW-CORE-01", "PRN-ADM-03"]

contador = 0

for hostname in hostnames:
    partes = hostname.split("-")
    tipo = partes[0]
    numero = partes[-1]
    if tipo == "SRV":
        print("Servidor:", numero)
        contador = contador + 1    
    elif tipo == "WKS":
        print("Workstation:", numero)
    elif tipo == "SW":
        print("Switch:", numero)
    else:
        print("Desconhecido:", tipo, numero)

print("Total de Servidores:", contador)