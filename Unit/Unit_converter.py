import streamlit as st
from pint import UnitRegistry

ureg = UnitRegistry()

st.title("🌍 Unit Converter ")

unit_categories = {
    "Length": ["meter", "kilometer", "mile", "foot", "inch", "centimeter"],
    "Weight": ["gram", "kilogram", "pound", "ounce", "ton"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Speed": ["meter per second", "kilometer per hour", "mile per hour", "knot"],
    "Time": ["second", "minute", "hour", "day", "week", "month", "year"],
    "Volume": ["liter", "milliliter", "gallon", "cup", "fluid ounce"],
    "Energy": ["joule", "calorie", "kilowatt hour"],
    "Pressure": ["pascal", "bar", "atmosphere"],
    "Power": ["watt", "kilowatt", "horsepower"],
}

category = st.selectbox("Choice Your Category:", list(unit_categories.keys()))

from_unit = st.selectbox("From Unit:", unit_categories[category])
to_unit = st.selectbox("To Unit:", unit_categories[category])

value = st.number_input("Enter Your Value:", format = "%.5f")

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "kelvin":
            return value + 273.15
    elif from_unit == "fahrenheit":
        if to_unit == "celsius":
            return (value - 32) * 5/9
        elif to_unit == "kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin":
        if to_unit == "celsius":
            return value - 273.15
        elif to_unit == "fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return None

if st.button("Convert Now 🚀"):
    try:
        if category == "Temperature":
            result = convert_temperature(value, from_unit, to_unit)
            if result is None:
                raise ValueError("Invalid temperature conversion")
        else:
            result = (value * ureg(from_unit)).to(to_unit).magnitude

        st.success(f"{value} {from_unit} = {round(result, 2)} {to_unit}".replace("  ", " "))

    except Exception as e:
        st.error(f"Conversion Error: {e}")
