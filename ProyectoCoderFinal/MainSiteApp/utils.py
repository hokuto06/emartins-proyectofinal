import random

def get_user_color(user_id):
    # Seed aleatoria basada en el ID del usuario para mantener los mismos colores para un usuario dado
    random.seed(user_id)
    
    # Genera un color hexadecimal aleatorio
    color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    return color
