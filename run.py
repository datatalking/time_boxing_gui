# run.py

import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar


class TaskManagerGUI:
    """
    Class to create a GUI for task management system.

    Attributes:
    - root: tk.Tk
            The root window of the GUI.
    - task_name_entry: tk.Entry
            Entry widget for entering task name.
    - task_details_text: tk.Text
            Text widget for entering task details or description.
    - deadline_calendar: Calendar
            Calendar widget for selecting task deadline.
    - canvas: tk.Canvas
            Canvas widget for drawing graphical representation of tasks.
    """

    def __init__(self):
        """
        Constructor to instantiate the TaskManagerGUI class and create the GUI.

        Initializes all the required widgets and sets up the layout.
        """

        # Creating the root window
        self.root = tk.Tk()
        self.root.title("Task Manager")

        # Creating the task name entry widget
        self.task_name_entry = tk.Entry(self.root)
        self.task_name_entry.pack()

        # Creating the task details text widget
        self.task_details_text = tk.Text(self.root)
        self.task_details_text.pack()

        # Creating the deadline calendar widget
        self.deadline_calendar = Calendar(
            self.root, selectmode="day", year=2023, month=1, day=1
        )
        self.deadline_calendar.pack()

        # Creating the canvas widget
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        # Creating the add task button
        add_task_button = tk.Button(self.root, text="Add a task", command=self.add_task)
        add_task_button.pack()

    def add_task(self):
        """
        Function to handle the add task button click event.

        Retrieves the task name, details, and deadline from the widgets,
        and performs the necessary actions to add the task.
        """

        # Get the task name from the entry widget
        task_name = self.task_name_entry.get()

        # Get the task details from the text widget
        task_details = self.task_details_text.get("1.0", tk.END)

        # Get the selected deadline from the calendar widget
        selected_date = self.deadline_calendar.selection_get()

        # Display a message box with the task information
        messagebox.showinfo(
            "Task Added",
            f"Task Name: {task_name}\nTask Details: {task_details}\nDeadline: {selected_date}",
        )

    def run(self):
        """
        Function to start the GUI event loop.
        """
        self.root.mainloop()


# Create an instance of the TaskManagerGUI class and run the GUI
task_manager_gui = TaskManagerGUI()
task_manager_gui.run()
