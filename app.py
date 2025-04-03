import streamlit as st

def unit_converter():
    st.title("Unit Converter")
    unit_type = st.selectbox("Choose a unit type", ["Length", "Weight", "Temperature"])
    
    if unit_type == "Length":
        value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
        from_unit = st.selectbox("From:", ["Meters", "Kilometers", "Miles", "Feet"])
        to_unit = st.selectbox("To:", ["Meters", "Kilometers", "Miles", "Feet"])
        
        conversion_factors = {
            ("Meters", "Kilometers"): 0.001, ("Meters", "Miles"): 0.000621371, ("Meters", "Feet"): 3.28084,
            ("Kilometers", "Meters"): 1000, ("Kilometers", "Miles"): 0.621371, ("Kilometers", "Feet"): 3280.84,
            ("Miles", "Meters"): 1609.34, ("Miles", "Kilometers"): 1.60934, ("Miles", "Feet"): 5280,
            ("Feet", "Meters"): 0.3048, ("Feet", "Kilometers"): 0.0003048, ("Feet", "Miles"): 0.000189394
        }
        
        if from_unit != to_unit:
            result = value * conversion_factors.get((from_unit, to_unit), 1)
            st.success(f"Converted Value: {result:.4f} {to_unit}")
    
    elif unit_type == "Weight":
        value = st.number_input("Enter weight:", min_value=0.0, format="%.2f")
        from_unit = st.selectbox("From:", ["Kilograms", "Grams", "Pounds"])
        to_unit = st.selectbox("To:", ["Kilograms", "Grams", "Pounds"])
        
        weight_factors = {
            ("Kilograms", "Grams"): 1000, ("Kilograms", "Pounds"): 2.20462,
            ("Grams", "Kilograms"): 0.001, ("Grams", "Pounds"): 0.00220462,
            ("Pounds", "Kilograms"): 0.453592, ("Pounds", "Grams"): 453.592
        }
        
        if from_unit != to_unit:
            result = value * weight_factors.get((from_unit, to_unit), 1)
            st.success(f"Converted Value: {result:.4f} {to_unit}")
    
    elif unit_type == "Temperature":
        value = st.number_input("Enter temperature:", format="%.2f")
        from_unit = st.selectbox("From:", ["Celsius", "Fahrenheit", "Kelvin"])
        to_unit = st.selectbox("To:", ["Celsius", "Fahrenheit", "Kelvin"])
        
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = (value - 273.15) * 9/5 + 32
        else:
            result = value
        
        st.success(f"Converted Value: {result:.2f} {to_unit}")

if __name__ == "__main__":
    unit_converter()
