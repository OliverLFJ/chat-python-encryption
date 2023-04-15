#Jorge Oliver López Fierro client.py 27/Septiembre/2020 "Comunicación en red"
import socket
class Cifrado:
    def encriptacion(self,mensaje):
        mensajeParseado=str(mensaje.lower())
        listaMensaje=list(mensajeParseado)
        alfabeto=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','¿','?','á','é','í','ó','ú']
        alfabetoSustitucion=list(reversed(alfabeto))
        indices = [[i for i in range(len(alfabeto)) if item1 == alfabeto[i]]for item1 in listaMensaje]

        listaPlanaIndices = []
        for i in indices:
            listaPlanaIndices+=i
        palabraCifrada=[ alfabetoSustitucion[i] for i in listaPlanaIndices ]
        mensajeDescifrado = ""
        for f in palabraCifrada:  
            mensajeDescifrado += f 
        return(mensajeDescifrado)
       
    def desencriptar(self,mensaje):
        mensajeParseado=str(mensaje.lower())
        listaMensaje=list(mensajeParseado)
        alfabeto=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','¿','?','á','é','í','ó','ú']
        alfabetoSustitucion=list(reversed(alfabeto))
        indices = [[i for i in range(len(alfabetoSustitucion)) if item1 == alfabetoSustitucion[i]]for item1 in listaMensaje]
        listaPlanaIndices = []
        for i in indices:
            listaPlanaIndices+=i
        listaDescrifrada=[ alfabeto[i] for i in listaPlanaIndices ]
        mensajeEncriptado = ""
        for g in mensaje:  
            mensajeEncriptado += g
        mensajeDescifrado = ""
        for f in listaDescrifrada:  
            mensajeDescifrado += f 
        return(mensajeDescifrado)
        
try:
    objeto=Cifrado()
    host = ''
    puerto = 0
    usuario=""
    client_socket = socket.socket()
    print("Bienvenido al chat indica tu nombre de usuario:")
    usuario=input()
    print("¿A que Host se conectará? (Ejemplo: localhost) :")
    host=input()
    print("¿A que puerto se conectará?:")
    puerto=input()
    client_socket.connect((host, int(puerto)))
    print("Para salir del chat escriba 'salir' :")
    print("Conexión establecida! Inicia la comunicación:")
    client_socket.send(usuario.encode('UTF-8'))
    usuarioServidor = client_socket.recv(1024)
    while True:
        mensaje = input(usuario+':')
        if mensaje == 'salir':
            client_socket.send(mensaje.encode('UTF-8'))
            break;
        enviar=objeto.encriptacion(mensaje)
        client_socket.send(enviar.encode('UTF-8'))
        recibido = client_socket.recv(1024)
        mensajeRecib=recibido.decode()
        print(usuarioServidor.decode(),':',objeto.desencriptar(mensajeRecib),'>',mensajeRecib) 
    client_socket.close()
    print("Conexión cerrada")
except:
    print("El Host o puerto no coinciden con alguno cercano")

    
