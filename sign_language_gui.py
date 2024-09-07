import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
from PIL import Image, ImageTk
import datetime

# Function to check if the current time is within the allowed operation time
def is_within_operation_time():
    current_time = datetime.datetime.now().time()
    start_time = datetime.time(18, 0)  # 6:00 PM
    end_time = datetime.time(22, 0)    # 10:00 PM
    return start_time <= current_time <= end_time

# Function to upload and display an image
def upload_image():
    if not is_within_operation_time():
        messagebox.showwarning("Time Restriction", "This application only works between 6 PM and 10 PM.")
        return

    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        image_label.config(image=image)
        image_label.image = image

# Function to start the video detection
def start_video_detection():
    if not is_within_operation_time():
        messagebox.showwarning("Time Restriction", "This application only works between 6 PM and 10 PM.")
        return

    # Implement video detection logic here
    cap = cv2.VideoCapture(0)  # Start video capture from the webcam
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Here you can add your model's prediction on each frame

        # Convert the frame to display it in Tkinter
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        video_label.imgtk = imgtk
        video_label.configure(image=imgtk)
        video_label.update()

    cap.release()

# Main GUI application
app = tk.Tk()
app.title("Sign Language Detection")

# Image upload button
upload_button = tk.Button(app, text="Upload Image", command=upload_image)
upload_button.pack()

# Image display label
image_label = tk.Label(app)
image_label.pack()

# Start video detection button
video_button = tk.Button(app, text="Start Video Detection", command=start_video_detection)
video_button.pack()

# Video display label
video_label = tk.Label(app)
video_label.pack()

app.mainloop()
