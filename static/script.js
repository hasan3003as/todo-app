// Confirm before deleting a task
document.querySelectorAll(".delete-form").forEach(function (form) {
    form.addEventListener("submit", function (event) {
        var confirmed = confirm("Delete this task?");
        if (!confirmed) {
            event.preventDefault();
        }
    });
});

// Let the user press Enter to submit (already works, but this
// adds a small animation when a task is added)
document.querySelector(".add-task-form form").addEventListener("submit", function () {
    var button = this.querySelector("button");
    button.textContent = "Adding...";
    button.disabled = true;
});