import serial
import serial.tools.list_ports
import time
import re

def extraer_numero(texto_crudo):
    # Busca uno o más números, seguidos de un punto, seguidos de uno o más números
    match = re.search(r'([0-9]+\.[0-9]+)', texto_crudo)
    if match:
        return float(match.group(1))
    return 0.0

def buscar_balanza(baudrate=9600, timeout=2):
    puertos_disponibles = serial.tools.list_ports.comports()
    
    if not puertos_disponibles:
        return None, 0.0

    for puerto in puertos_disponibles:
        try:
            with serial.Serial(puerto.device, baudrate=baudrate, timeout=timeout) as ser:
                time.sleep(0.5) 
                lectura_cruda = ser.readline()
                
                if lectura_cruda:
                    texto = lectura_cruda.decode('ascii', errors='ignore').strip()
                    peso_limpio = extraer_numero(texto)
                    return puerto.device, peso_limpio
                    
        except serial.SerialException:
            continue
            
    return None, 0.0

# Bloque de prueba
if __name__ == "__main__":
    puerto, peso = buscar_balanza()
    if puerto:
        print(f"\n[ÉXITO] Balanza en {puerto}. Peso extraído para Odoo: {peso}")
    else:
        print("\n[ERROR] No se detectó la balanza.")