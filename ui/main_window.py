import tkinter as tk

class MainWindow:
    """
    Class to manage the main UI window.
    """

    def __init__(self):
        try:
            self.root = None
            self.close_button = None
            self.build_base_dialog()
            self.initial_frame = None
            self.file_upload_frame = None
            self.create_frames()
        except Exception as e:
            print(f"Unable to initiliaze main window class, error:{e}")

    def create_root_window(self) -> None:
        """Creates the root app window"""
        self.root = tk.Tk()
        self.root.title("MoneyAssistant")
        self.root.geometry("600x400")

    def add_close_button(self) -> None:
        """Add a close button to the main app window"""
        self.close_button = tk.Button(
            self.root, 
            text="Close",
            command=self.root.destroy
        )
    
    def build_base_dialog(self) -> None:
        """Builds the base dialog window"""
        self.create_root_window()
        self.add_close_button()
    
    def start_ui_loop(self) -> None:
        """Starts the UI loop"""
        self.root.mainloop()

    def create_frames(self) -> None:
        """Create UI frames"""
        self.initial_frame = tk.Frame(self.root)
        self.file_upload_frame = tk.Frame(self.root)

    def clear_frames(self) -> None:
        """Remove frames from window"""
        self.initial_frame.pack_forget()
        self.file_upload_frame.pack_forget()

if __name__ == "__main__":
    main_window = MainWindow()
