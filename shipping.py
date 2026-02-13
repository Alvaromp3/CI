def calculate_shipping(weight_kg: float, is_express: bool, destination: str) -> float:
    # R1: validar inputs

    if weight_kg <= 0 or weight_kg > 50:
        raise ValueError("weight_kg out of range")

    if destination not in ("US", "CA", "MX"):
        raise ValueError("invalid destination")

    ## R2 hacemos base por destino


    base = {"US": 5.00, "CA": 8.00, "MX": 10.00}[destination]

    ## R3 hacemos recargo por peso

    if weight_kg <= 1.0:
        surcharge = 0.00
    elif weight_kg <= 5.0:
        surcharge = 3.00
    elif weight_kg <= 20.0:
        surcharge = 7.00
    else:
        surcharge = 12.00

    subtotal = base + surcharge

    # R4 vamos a hacer express

    
    if is_express:
        subtotal *= 1.6

    ## R5 solo redondeamos
    return round(subtotal, 2)
