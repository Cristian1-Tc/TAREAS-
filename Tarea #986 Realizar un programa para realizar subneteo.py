import ipaddress

def subnet_calc(ip_address, subnet_mask):
    network = ipaddress.IPv4Network(ip_address + '/' + subnet_mask, strict=False)
    subnet_list = list(network.subnets())

    print("Dirección IP de red: {}".format(network.network_address))
    print("Máscara de subred: {}".format(network.netmask))

    print("\nSubredes generadas:")
    for subnet in subnet_list:
        print("Subred: {}".format(subnet.network_address))
        print("Máscara de subred: {}".format(subnet.netmask))
        print("Rango de direcciones IP utilizables: {} - {}".format(subnet.network_address + 1, subnet.broadcast_address - 1))
        print("Cantidad de direcciones IP utilizables: {}\n".format(subnet.num_addresses - 2))

# Tenemos un ejemplo de uso:
ip_address = input("Ingrese la dirección IP: ")
subnet_mask = input("Ingrese la máscara de subred en formato CIDR (ejemplo: 24): ")

subnet_calc(ip_address, subnet_mask)
