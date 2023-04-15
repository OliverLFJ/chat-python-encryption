#Jorge Oliver López Fierro server.py 27/Septiembre/2020 "Comunicación en red"
import socket 
server_socket = socket.socket()
usuario="Servidor"
server_socket.bind(('localhost', 8000))
print("Servidor conectado")
print("Esperando usuario....")
server_socket.listen(1)
cliente, addr = server_socket.accept()
usuarioCliente=cliente.recv(1024)
usuarioCliente1=usuarioCliente.decode()
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
        indices = [[i for i in range(len(alfabetoSustitucion)) if item1 == alfabetoSustitucion[i]]for item1 in mensaje]
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
    cliente.send(usuario.encode('UTF-8'))
    print("Usuario conectado:",usuarioCliente1)
    while True:
        recibido = cliente.recv(1024)
        mensajeRecib=recibido.decode()
        if mensajeRecib == 'salir':
            break;
        print(usuarioCliente1,':',objeto.desencriptar(mensajeRecib),'>',mensajeRecib)
        mensaje=input(usuario+':')
        enviar=objeto.encriptacion(mensaje)
        cliente.send(enviar.encode('UTF-8'))
    print("El usuario cerró el chat")
    cliente.close()
    server_socket.close()
except:
    print("Ocurrió un error")
    
