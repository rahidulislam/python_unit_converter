# Python Unit Converter

This project provides a simple unit conversion tool implemented in Python. It includes both class-based and function-based approaches to perform various unit conversions.

## Class-Based Unit Converter

The class-based approach uses a `UnitConverter` class to handle different unit conversions. This approach is useful for maintaining state and organizing related conversion methods.

### Example

```python
class UnitConverter:
    def __init__(self):
        self.conversion_factors = {
            'meters_to_feet': 3.28084,
            'feet_to_meters': 0.3048,
            'kilograms_to_pounds': 2.20462,
            'pounds_to_kilograms': 0.453592
        }

    def convert(self, value, from_unit, to_unit):
        key = f'{from_unit}_to_{to_unit}'
        if key in self.conversion_factors:
            return value * self.conversion_factors[key]
        else:
            raise ValueError(f'Conversion from {from_unit} to {to_unit} not supported.')

# Usage
converter = UnitConverter()
print(converter.convert(10, 'meters', 'feet'))  # Output: 32.8084
print(converter.convert(5, 'kilograms', 'pounds'))  # Output: 11.0231
```

## Function-Based Unit Converter

The function-based approach uses standalone functions to perform unit conversions. This approach is simpler and more straightforward for small scripts or one-off conversions.

### Example

```python
def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet * 0.3048

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds * 0.453592

# Usage
print(meters_to_feet(10))  # Output: 32.8084
print(kilograms_to_pounds(5))  # Output: 11.0231
```

## Conclusion

Both class-based and function-based approaches have their own advantages. The class-based approach is more suitable for complex applications where maintaining state and organizing methods is important. The function-based approach is simpler and more suitable for small scripts or one-off conversions. Choose the approach that best fits your needs.