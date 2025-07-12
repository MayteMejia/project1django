from django.core.exceptions import ValidationError

def validate_rating(value):
    if value < 1 or value > 10:
        raise ValidationError('Rating must be between 1 and 10')
    
def validate_price_positive(value):
    if value <= 0:
        raise ValidationError('Price must be greater than 0')
    