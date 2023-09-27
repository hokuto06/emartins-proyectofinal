from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class SimplePasswordValidator:
    
    def simple_password_validator(value):
        # Aquí puedes definir tu propia lógica de validación personalizada para contraseñas
        if len(value) < 6:
            raise ValidationError(
                _("La contraseña es demasiado corta. Debe tener al menos 6 caracteres."),
                code='password_too_short',
            )