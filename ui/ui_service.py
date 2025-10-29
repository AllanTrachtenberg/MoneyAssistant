from ui.main_window import MainWindow
from ui.file_upload_screen import FileUpload
from ui.initial_screen import InitialScreen

class UiService:
    """
    Class to manage UI operations.
    """
    def __init__(self):
        try:
            self.main_window = MainWindow()
            self.file_upload = FileUpload(self.main_window.file_upload_frame)
            self.initial_screen = InitialScreen(
                self.main_window.initial_frame,
                self.open_file_upload_screen
            )
        except Exception as e:
            print(f"Unable to start UiService, error: {e}")

    def start_app(self) -> None:
        """Start the app"""
        self.main_window.clear_frames()
        self.initial_screen.show_initial_screen_frame()
        self.main_window.start_ui_loop()

    def open_file_upload_screen(self) -> None:
        """Open the file upload screen"""
        self.main_window.clear_frames()
        self.file_upload.show_file_upload_screen_frame()
        