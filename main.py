from pyscript import document

def search_element(event):
    # Dictionary storing non-metal elements: (Name, Atomic Number, Atomic Mass)
    non_metals = {
        "H": ("Hydrogen", "1", "1.008"),
        "C": ("Carbon", "6", "12.011"),
        "N": ("Nitrogen", "7", "14.007"),
        "O": ("Oxygen", "8", "15.999"),
        "F": ("Fluorine", "9", "18.998"),
        "P": ("Phosphorus", "15", "30.974"),
        "S": ("Sulfur", "16", "32.06"),
        "Cl": ("Chlorine", "17", "35.45"),
        "Se": ("Selenium", "34", "78.971"),
        "Br": ("Bromine", "35", "79.904"),
        "I": ("Iodine", "53", "126.90"),
        "He": ("Helium", "2", "4.0026"),
        "Ne": ("Neon", "10", "20.180"),
        "Ar": ("Argon", "18", "39.95"),
        "Kr": ("Krypton", "36", "83.80"),
        "Xe": ("Xenon", "54", "131.29"),
        "Rn": ("Radon", "86", "222")
    }
    
    # Get user input from the text field
    raw_input = document.getElementById("Element1").value.strip()
    
    # Capitalize input appropriately to match dictionary keys
    if raw_input in non_metals:
        symbol = raw_input
    elif raw_input.capitalize() in non_metals:
        symbol = raw_input.capitalize()
    elif raw_input.upper() in non_metals:
        symbol = raw_input.upper()
    else:
        symbol = raw_input

    # Retrieve element data using the required .get() syntax
    result = non_metals.get(symbol, ("Element not found", "-", "-"))
    
    output_div = document.getElementById("output")
    
    # Display result OR error message
    if result[0] == "Element not found":
        output_div.innerHTML = """
            <div class="alert alert-danger mb-0 py-2 px-3 border-0 small">
                Element does not exist in the non-metals list.
            </div>
        """
    else:
        output_div.innerHTML = f"""
            <div class="row g-2 font-monospace small">
                <div class="col-6"><strong>Symbol:</strong> {symbol}</div>
                <div class="col-6"><strong>Element:</strong> {result[0]}</div>
                <div class="col-6"><strong>Atomic No:</strong> {result[1]}</div>
                <div class="col-6"><strong>Atomic Mass:</strong> {result[2]}</div>
            </div>
        """