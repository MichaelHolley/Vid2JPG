from tkinter import filedialog, messagebox
from tkinter.ttk import *
from tkinter import *
import cv2
import time
from pathlib import Path
from tkinter import Tk, Label, Button, filedialog, messagebox
from tkinter.ttk import Progressbar
import cv2


class VideoToJpgConverter:
    def __init__(self):
        self.file_path = ""
        self.output_folder_path = ""
        self.root = Tk()
        self.progress = None
        self.select_video_btn = None
        self.select_folder_btn = None
        self.start_btn = None
        self.video_path_label = None
        self.folder_path_label = None
        self.setup_ui()
        self.update_button_states()

    def setup_ui(self):
        """Initialize the user interface"""
        # Configure root window padding
        self.root.configure(padx=10, pady=10)

        # Video selection
        Label(self.root, text="Video:", width=20).grid(row=0, column=0, padx=5, pady=5)
        self.select_video_btn = Button(
            self.root, text="Select", command=self.select_video, width=10
        )
        self.select_video_btn.grid(row=0, column=1, padx=5, pady=5)
        # Add video path label
        self.video_path_label = Label(self.root, text="No video selected", fg="red")
        self.video_path_label.grid(row=0, column=2, sticky="w", padx=(5, 20), pady=5)

        # Output folder selection
        Label(self.root, text="Output-Folder:", width=20).grid(
            row=1, column=0, padx=5, pady=5
        )
        self.select_folder_btn = Button(
            self.root, text="Select", command=self.select_output_folder, width=10
        )
        self.select_folder_btn.grid(row=1, column=1, padx=5, pady=5)
        # Add folder path label
        self.folder_path_label = Label(self.root, text="No folder selected", fg="red")
        self.folder_path_label.grid(row=1, column=2, sticky="w", padx=(5, 20), pady=5)

        # Convert button
        self.start_btn = Button(
            self.root, text="Start", command=self.convert_video_to_images, width=10
        )
        self.start_btn.grid(row=2, column=0, padx=5, pady=5)
        self.start_btn["state"] = "disabled"

        # Progress bar
        self.progress = Progressbar(
            self.root, orient="horizontal", length=100, mode="determinate"
        )

        self.progress.grid(row=2, column=1, columnspan=2, sticky="ew", padx=5, pady=5)

    def update_button_states(self):
        """Update the state of buttons based on current conditions"""
        if self.file_path and self.output_folder_path:
            self.start_btn["state"] = "normal"
        else:
            self.start_btn["state"] = "disabled"

    def select_video(self) -> None:
        """Open file dialog to select input video"""
        self.file_path = filedialog.askopenfilename(
            initialdir=str(Path.home()),
            title="Select input video",
            filetypes=(("Video files", "*.mp4 *.avi *.wmv"), ("All files", "*.*")),
        )

        if self.file_path:
            self.video_path_label.config(text=Path(self.file_path).name, fg="green")
        else:
            self.video_path_label.config(text="No video selected", fg="red")
        print(f"Selected Video: {self.file_path}")
        self.update_button_states()

    def select_output_folder(self) -> None:
        """Open directory dialog to select output folder"""
        self.output_folder_path = filedialog.askdirectory(title="Select output folder")

        if self.output_folder_path:
            self.folder_path_label.config(
                text=Path(self.output_folder_path).name, fg="green"
            )
        else:
            self.folder_path_label.config(text="No folder selected", fg="red")

        print(f"Selected Folder: {self.output_folder_path}")
        self.update_button_states()

    def convert_video_to_images(self) -> None:
        """Convert video to sequence of JPG images"""
        try:
            # Disable all buttons during conversion
            self.select_video_btn["state"] = "disabled"
            self.select_folder_btn["state"] = "disabled"
            self.start_btn["state"] = "disabled"
            self.root.update()

            # Validate inputs
            if not self.file_path:
                messagebox.showerror("Error", "Please select a video file first")
                return
            if not self.output_folder_path:
                messagebox.showerror("Error", "Please select an output folder first")
                return

            # Open video file
            video = cv2.VideoCapture(self.file_path)
            if not video.isOpened():
                messagebox.showerror("Error", "Could not open video file")
                return

            # Create output directory
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            output_dir = Path(self.output_folder_path) / timestamp
            output_dir.mkdir(parents=True, exist_ok=True)

            # Get video properties
            total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
            frame_count = 0

            # Reset progress bar
            self.progress["value"] = 0
            self.root.update()

            while True:
                success, frame = video.read()
                if not success:
                    break

                # Save frame as JPG
                output_path = output_dir / f"frame_{frame_count:04d}.jpg"
                cv2.imwrite(str(output_path), frame)

                # Update progress bar
                frame_count += 1
                progress_value = int((frame_count / total_frames) * 100)
                self.progress["value"] = progress_value
                self.root.update()  # Update the entire UI

            video.release()
            messagebox.showinfo("Success", f"Converted {frame_count} frames to JPG")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            # Re-enable all buttons after conversion
            self.select_video_btn["state"] = "normal"
            self.select_folder_btn["state"] = "normal"
            self.update_button_states()

    def run(self):
        """Start the application"""
        self.root.title("Video to JPG Converter")
        self.root.mainloop()


def main():
    app = VideoToJpgConverter()
    app.run()


if __name__ == "__main__":
    main()
