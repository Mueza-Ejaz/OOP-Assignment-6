# Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        """
         Convert Celsius to Fahrenheit.

        """
        return (c * 9/5) + 32

# Example usage:
temp_1 = TemperatureConverter
print(f"Temperature in Fahrenheit: {temp_1.celsius_to_fahrenheit(25)}F")  

# output:
# Temperature in Fahrenheit: 77.0F



