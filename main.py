from pyscript import document

def create_order(event):
    items = document.querySelectorAll('input[type="checkbox"]:checked')
    subtotal = 0
    for item in items:
        subtotal = subtotal + float(item.value)
    vat = subtotal * 0.12
    total = subtotal + vat

    receipt = document.querySelector('#receipt')
    receipt.innerHTML = f"""
       <h2>==== Receipt ====</h2>
       <p>Subtotal: {subtotal:.2f}</p>
       <p>VAT: ₱{vat:.2f}</p>
       <p class="total">Total: ₱{total:.2f}</p>
    """