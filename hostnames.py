# Filtra hostnames de servidores a partir de uma lista de inventario

hostnames = ["SRV-FILE-01", "SRV-DC-02", "WKS-RH-115"]

for hostname in hostnames: 
    partes = hostname.split("-")
    tipo = partes[0]
    numero = partes[-1]
    if tipo == "SRV":
        print(tipo, numero)