import streamlit as st

def main():
    st.set_page_config(page_title="Unit Converter", page_icon="📏", layout="wide")
    
    st.title("📏 Unit Converter")
    st.write("A simple tool to convert between different units of measurement")
    
    # Define conversion functions for different categories
    def convert_length(value, from_unit, to_unit):
        # Convert to meters first
        to_meter = {
            'nanometer': 1e-9,
            'micrometer': 1e-6,
            'millimeter': 0.001,
            'centimeter': 0.01,
            'meter': 1.0,
            'kilometer': 1000.0,
            'inch': 0.0254,
            'foot': 0.3048,
            'yard': 0.9144,
            'mile': 1609.344,
            'nautical mile': 1852.0
        }
        
        meters = value * to_meter[from_unit]
        # Convert to target unit
        return meters / to_meter[to_unit]
    
    def convert_weight(value, from_unit, to_unit):
        # Convert to grams first
        to_gram = {
            'microgram': 1e-6,
            'milligram': 0.001,
            'gram': 1.0,
            'kilogram': 1000.0,
            'tonne': 1e6,
            'ounce': 28.3495,
            'pound': 453.592,
            'stone': 6350.29,
            'ton (US)': 907185.0,
            'ton (UK)': 1016050.0
        }
        
        grams = value * to_gram[from_unit]
        return grams / to_gram[to_unit]
    
    def convert_temperature(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        
        # Convert to Celsius first
        if from_unit == 'celsius':
            celsius = value
        elif from_unit == 'fahrenheit':
            celsius = (value - 32) * 5/9
        elif from_unit == 'kelvin':
            celsius = value - 273.15
        
        # Convert from Celsius to target unit
        if to_unit == 'celsius':
            return celsius
        elif to_unit == 'fahrenheit':
            return (celsius * 9/5) + 32
        elif to_unit == 'kelvin':
            return celsius + 273.15
    
    def convert_area(value, from_unit, to_unit):
        # Convert to square meters first
        to_sq_meter = {
            'square millimeter': 1e-6,
            'square centimeter': 1e-4,
            'square meter': 1.0,
            'hectare': 10000.0,
            'square kilometer': 1e6,
            'square inch': 0.00064516,
            'square foot': 0.092903,
            'square yard': 0.836127,
            'acre': 4046.86,
            'square mile': 2.59e6
        }
        
        sq_meters = value * to_sq_meter[from_unit]
        return sq_meters / to_sq_meter[to_unit]
    
    def convert_volume(value, from_unit, to_unit):
        # Convert to liters first
        to_liter = {
            'milliliter': 0.001,
            'centiliter': 0.01,
            'deciliter': 0.1,
            'liter': 1.0,
            'kiloliter': 1000.0,
            'cubic centimeter': 0.001,
            'cubic meter': 1000.0,
            'teaspoon (US)': 0.00492892,
            'tablespoon (US)': 0.0147868,
            'fluid ounce (US)': 0.0295735,
            'cup (US)': 0.236588,
            'pint (US)': 0.473176,
            'quart (US)': 0.946353,
            'gallon (US)': 3.78541,
            'cubic inch': 0.0163871,
            'cubic foot': 28.3168
        }
        
        liters = value * to_liter[from_unit]
        return liters / to_liter[to_unit]
    
    def convert_time(value, from_unit, to_unit):
        # Convert to seconds first
        to_second = {
            'nanosecond': 1e-9,
            'microsecond': 1e-6,
            'millisecond': 0.001,
            'second': 1.0,
            'minute': 60.0,
            'hour': 3600.0,
            'day': 86400.0,
            'week': 604800.0,
            'month': 2629800.0,  # Approximate
            'year': 31557600.0,  # Approximate
            'decade': 315576000.0,
            'century': 3155760000.0
        }
        
        seconds = value * to_second[from_unit]
        return seconds / to_second[to_unit]
    
    def convert_speed(value, from_unit, to_unit):
        # Convert to m/s first
        to_mps = {
            'meter per second': 1.0,
            'kilometer per hour': 0.277778,
            'mile per hour': 0.44704,
            'knot': 0.514444,
            'foot per second': 0.3048
        }
        
        mps = value * to_mps[from_unit]
        return mps / to_mps[to_unit]
    
    # Define categories and their units
    categories = {
        'Length': {
            'units': ['meter', 'kilometer', 'centimeter', 'millimeter', 'micrometer', 'nanometer', 
                     'mile', 'yard', 'foot', 'inch', 'nautical mile'],
            'function': convert_length
        },
        'Weight': {
            'units': ['kilogram', 'gram', 'milligram', 'microgram', 'tonne', 
                     'pound', 'ounce', 'stone', 'ton (US)', 'ton (UK)'],
            'function': convert_weight
        },
        'Temperature': {
            'units': ['celsius', 'fahrenheit', 'kelvin'],
            'function': convert_temperature
        },
        'Area': {
            'units': ['square meter', 'square kilometer', 'square centimeter', 'square millimeter', 
                      'hectare', 'acre', 'square mile', 'square yard', 'square foot', 'square inch'],
            'function': convert_area
        },
        'Volume': {
            'units': ['liter', 'milliliter', 'centiliter', 'deciliter', 'kiloliter', 
                     'cubic meter', 'cubic centimeter', 'gallon (US)', 'quart (US)', 
                     'pint (US)', 'cup (US)', 'fluid ounce (US)', 'tablespoon (US)', 
                     'teaspoon (US)', 'cubic foot', 'cubic inch'],
            'function': convert_volume
        },
        'Time': {
            'units': ['second', 'millisecond', 'microsecond', 'nanosecond', 
                     'minute', 'hour', 'day', 'week', 'month', 'year', 'decade', 'century'],
            'function': convert_time
        },
        'Speed': {
            'units': ['meter per second', 'kilometer per hour', 'mile per hour', 'knot', 'foot per second'],
            'function': convert_speed
        }
    }
    
    # Sidebar for category selection
    category = st.sidebar.selectbox("Select Category", list(categories.keys()))
    
    # Get the units and conversion function for the selected category
    units = categories[category]['units']
    conversion_function = categories[category]['function']
    
    # Main conversion interface
    col1, col2, col3 = st.columns(3)
    
    with col1:
        from_unit = st.selectbox("From", units, key='from_unit')
        value = st.number_input("Value", value=1.0, step=0.1, key='value')
    
    with col2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        if st.button("⇄ Swap Units"):
            # Swap the units
            current_from = st.session_state.from_unit
            current_to = st.session_state.to_unit
            st.session_state.from_unit = current_to
            st.session_state.to_unit = current_from
    
    with col3:
        to_unit = st.selectbox("To", units, key='to_unit')
        try:
            if from_unit not in units or to_unit not in units:
                st.error("Invalid unit selected. Please choose valid units.")
            else:
                result = conversion_function(value, from_unit, to_unit)


            st.metric("Result", f"{result:.6g}", delta=None)
        except Exception as e:
            st.error(f"Conversion not possible: {e}")

    
    # Add some space and attribution
    st.markdown("---")
    st.markdown("""
    **Unit Converter** - Created with Python and Streamlit  
    For educational purposes
    """)

if __name__ == "__main__":
    main()
