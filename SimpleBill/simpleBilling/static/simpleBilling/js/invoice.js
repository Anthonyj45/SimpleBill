document.addEventListener("DOMContentLoaded", function () {
    const showFormBtn = document.getElementById("show-form-btn");
    const formContainer = document.getElementById("form-container");

    showFormBtn.addEventListener("click", function() {
        formContainer.style.display = "block";
        showFormBtn.style.display = "none";
    });

    const form = document.getElementById("invoice-form");
    const invoiceBox = document.getElementById("invoices-list");

    const serviceFeeInput = document.getElementById("service-fee");
    const travelExpensesInput = document.getElementById("travel-expenses");
    const taxPercentInput = document.getElementById("tax-percent");
    const totalAmountDisplay = document.getElementById("total_amount");

    function calculateTotal() {
        const serviceFee = parseFloat(serviceFeeInput.value) || 0;
        const travelExpenses = parseFloat(travelExpensesInput.value) || 0;
        const taxPercent = parseFloat(taxPercentInput.value) || 0;
        
        const subtotal = serviceFee + travelExpenses;
        const tax = subtotal * (taxPercent / 100);
        const total = subtotal + tax;

        totalAmountDisplay.textContent = `$${total.toFixed(2)}`;
    }

    serviceFeeInput.addEventListener("input", calculateTotal);
    travelExpensesInput.addEventListener("input", calculateTotal);
    taxPercentInput.addEventListener("input", calculateTotal);

    form.addEventListener("submit", function (e) {
        e.preventDefault();

        const formData = new FormData(form);

        fetch("", {
            method: "POST",
            headers: {
                "X-Requested-With": "XMLHttpRequest"
            },
            body: formData
        })
        .then(res => res.json())
        .then(data => {
            if(data.success) {
                const newCard =`
                <div class="invoice-card">
                <h3>${data.invoice.client}</h3>
                <p>
                    Service Fee: $${data.invoice.service_fee}<br>
                    Travel_Expenses: $${data.invoice.travel_expenses}<br>
                    Tax: ${data.invoice.tax_percent}%<br>
                    Total: $${data.invoice.total}<br>
                </p>
                </div>
                `;

                invoiceBox.insertAdjacentHTML("afterbegin", newCard);
                form.reset();
                totalAmountDisplay.textContent = "$0.00";
            } else {
                alert("Error. Invoice could not be created");
            }
        });
    });
});