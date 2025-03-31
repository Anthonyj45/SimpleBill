document.addEventListener("DOMContentLoaded", function () {
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

})