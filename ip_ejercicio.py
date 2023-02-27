def validar_ip(ip):
    try:
        primeros3 = int(ip.split('.')[0])
        if primeros3 == 10:
            return 'A, ip  privada'
        elif primeros3 == 172 and 16 <= int(ip.split('.')[1]) <= 31:
            return 'B, ip privada'
        elif primeros3 == 192 and int(ip.split('.')[1]) == 168:
            return 'C, ip privada'
        else:
            if primeros3 >= 1 and primeros3 <= 126:
                return 'A, ip publica'
            elif primeros3 >= 128 and primeros3 <= 191:
                return 'B, ip publica'
            elif primeros3 >= 192 and primeros3 <= 223:
                return 'C, ip publica'
            elif primeros3 >= 224 and primeros3 <= 239:
                return 'D, ip publica'
            elif primeros3 >= 240 and primeros3 <= 255:
                return 'E, ip publica'
            else:
                return 'Ninguna, direccion IP inválida'  # Dirección IP inválida
    except:
        print("String no válido para hacer la validación de ip")
    

ip_usuario = input("Ingrese su IP: " )
ip_clase = validar_ip(ip_usuario)
if ip_clase != None:
    print(f'La dirección IP {ip_usuario} pertenece a la clase {ip_clase}')