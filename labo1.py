# Texto cifrado
mensaje_cifrado = '''RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE
AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.
AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ
TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX
DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936,
PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN
TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE,
HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK
HKCZJOI OKEJSZCNHE.'''

def contar_apariciones(texto):
    frecuencias = {}
    for caracter in texto:
        if caracter != " " and caracter != "\n" and caracter != "." and caracter != ",":
            if caracter in frecuencias:
                frecuencias[caracter] = frecuencias[caracter] + 1
            else:
                frecuencias[caracter] = 1
    frecuencias_ordenadas = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)
    # Imprimir la frecuencia de cada caracter
    for caracter, frecuencia in frecuencias_ordenadas:
        print(f"{caracter}: {frecuencia}")

    contar_apariciones(mensaje_cifrado)

# Diccionario de reemplazos
reemplazos = {
    "V": "Y", "v": "V", "Q": "B", "S": "Q", "N": "S", "J": "N", "G": "J",
    "U": "G", "Z": "U", "K": "R", "R": "C", "C": "I", "I": "O", "O": "F",
    "F": "X", "X": "E", "E": "A", "A": "D", "D": "P", "P": "M", "M": "H",
    "H": "T", "T": "L", "L": "Z"
}
# Variable para almacenar el mensaje descifrado
mensaje_descifrado = ""
# Recorrer el texto cifrado y reemplazar caracteres según el diccionario
for caracter in mensaje_cifrado:
    if caracter in reemplazos:
        mensaje_descifrado += reemplazos[caracter]
    else:
        mensaje_descifrado += caracter
# Imprimir el resultado final
print(mensaje_descifrado)

