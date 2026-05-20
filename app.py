from flask import Flask, render_template, request, redirect, url_for, jsonify
from database import create_table, get_all_tasks, add_task, toggle_task, delete_task

app = Flask(__name__)

# Create the database table when the server starts
create_table()


@app.route("/")
def index():
    """Serve the main page with all tasks."""
    tasks = get_all_tasks()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add():
    """Handle adding a new task."""
    title = request.form.get("title", "").strip()
    if title:
        add_task(title)
    return redirect(url_for("index"))


@app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle(task_id):
    """Handle marking a task complete/incomplete."""
    toggle_task(task_id)
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    """Handle deleting a task."""
    delete_task(task_id)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)