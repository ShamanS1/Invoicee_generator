document.getElementById("add_item").addEventListener("click", function() {
    var itemsContainer = document.getElementById("items");
    var itemDiv = document.createElement("div");
    itemDiv.classList.add("item");

    var itemCount = itemsContainer.getElementsByClassName("item").length;
    var itemHtml = `
        <div class="form-group">
            <label for="item">Item:</label>
            <input type="text" name="item[]" required>
        </div>
        <div class="form-group">
            <label for="quantity">Quantity:</label>
            <input type="number" name="qty[]" required>
        </div>
        <div class="form-group">
            <label for="price">Rate:</label>
            <input type="number" name="price[]" required>
        </div>
    `;
    itemDiv.innerHTML = itemHtml;
    itemsContainer.appendChild(itemDiv);
});
