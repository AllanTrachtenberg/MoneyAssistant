import tkinter as tk

class InitialScreen:
    """Class to manage the initial screen"""
    def __init__(self, frame, file_upload_command):
        self.frame = frame
        self.file_upload_command = file_upload_command
        self.build_initial_screen()
        
    def build_initial_screen(self) -> None:
        self.add_welcome_text()
        self.add_assistant_image()
        self.add_subtitle_text()
        self.add_file_upload_button()
    
    def add_welcome_text(self) -> None:
        title = tk.Label(
            self.frame, 
            text="Welcome to your personal Money Assistant App",
            font=("Arial", 16)
        )
        title.pack(side="top", pady=(20, 10))
        title.pack_configure(anchor="n")

    def show_initial_screen_frame(self) -> None:
        """Show the initial screen frame"""
        self.frame.pack(fill="both", expand=True)

    def add_subtitle_text(self) -> None:
        subtitle = tk.Label(
            self.frame,
            text="How can we help you today",
            font=("Arial", 12),
            fg="gray"
        )
        subtitle.pack(side="top", pady=(10, 20))
        subtitle.pack_configure(anchor="n")

    def add_assistant_image(self) -> None:
        self.image = tk.PhotoImage(file="ui/assistant.png")
        img_label = tk.Label(self.frame, image=self.image)
        img_label.pack(side="top", pady=(0, 10))
        img_label.pack_configure(anchor="n")

    def add_file_upload_button(self) -> None:
        upload_button = tk.Button(
            self.frame,
            text="Upload Bank Statement",
            command=self.file_upload_command
        )
        upload_button.pack(side="top", pady=(10, 10), padx=(20, 20))
        upload_button.pack_configure(anchor="w")
        