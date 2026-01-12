from pyscript import document

def convert_temp(event):
    f_input = document.querySelector("#f-input")
    f_val = f_input.value
    
    if not f_val:
        document.querySelector("#output-area").innerText = "Please enter a number."
        return

    fahrenheit = float(f_val)
    celsius = (fahrenheit - 32) * 5 / 9

    status = "Fever detected." if celsius >= 37.8 else "No fever."
    
    result_text = f"Temperature: {celsius:.2f}°C. {status}"
    document.querySelector("#output-area").innerText = result_text