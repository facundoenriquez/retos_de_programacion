import re

def detector_handles(text):
    # Expresión regular para detectar handles de usuario
    user_handles = re.findall(r'@(\w+)', text)

    # Expresión regular para detectar handles de hashtag
    hashtag_handles = re.findall(r'#(\w+)', text)

    # Expresión regular para detectar handles web
    web_handles = re.findall(r'(www\.|http:\/\/|https:\/\/)([\w\.-]+)', text)

    return {
        "user_handles": user_handles,
        "hashtag_handles": hashtag_handles,
        "web_handles": web_handles
    }

print(detector_handles("¡Hola @usuario1! ¿Has visto el #nuevoProducto en www.ejemplo.com? #lanzamiento"))