import tkinter as tk
from tkinter import filedialog

class FileUpload:
    """
    Class to manage the file upload functions
    """

    def __init__(self, frame):
        self.frame = frame
        self.upload_label = None
        self.select_file_button = None
        self.selected_file_path = None
        self.create_file_dialog()

    def create_file_dialog(self):
        self.add_label_upload_file()
        self.add_select_file_button()

    def add_label_upload_file(self):
        self.upload_label = tk.Label(self.frame, text="Upload File")
        self.upload_label.pack(pady=10)

    def add_select_file_button(self):
        self.select_file_button = tk.Button(
            self.frame,
            text="Select file",
            command=self.prompt_user_for_files
        )
        self.select_file_button.pack(pady=10)

    def prompt_user_for_files(self):
        file_path = filedialog.askopenfile(
            title="Select a file",
            filetypes=[
                ("Excel files", "*.xlsx *.xls"),
                ("CSV files", "*.csv"),
                ("All files", "*.*")
            ]
        )
        if file_path:
            self.selected_file_path = file_path
            self.upload_label.config(
                text=f"Selected: {file_path.name}"
            )

    def show_file_upload_screen_frame(self) -> None:
        """Show the file upload screen frame"""
        self.frame.pack(fill="both", expand=True)