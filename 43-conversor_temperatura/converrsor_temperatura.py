import re


def conversor_temperatura(temp):
    if "°" in temp and "C" in temp or "F" in temp:

        match = re.search(r'(\d+)[°CF]', temp)
        if match:
            temperature = int(match.group(1))
        else:
            return None

        if "C" in temp:
            fahrenheit = (temperature * 9/5) + 32
            return f"La temperatura en Farenheit es de {fahrenheit}"
        if "F" in temp:
            celsius = (temperature - 32) * 5/9
            return f"La temperatura en Farenheit es de {celsius}"
    else:
        return f"Error de temperatura debe contener un °C u °F"


print(conversor_temperatura("27°F"))
