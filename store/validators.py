from django.core.exceptions import ValidationError

def max_size_kb(image):
    max_size = 300  # size in KB
    if image.size > max_size * 1024:
        raise ValidationError(f"Max file size is {max_size} KB")
