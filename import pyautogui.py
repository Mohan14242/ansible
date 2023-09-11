import pyautogui
import cv2
import numpy as np
import threading

# Set the screen resolution (you may need to adjust this)
screen_width, screen_height = pyautogui.size()

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('screen_record.avi', fourcc, 20.0, (screen_width, screen_height))

# Flag to indicate whether recording is in progress
recording = True

def record_screen():
    global recording
    try:
        while recording:
            # Capture the screen as an image
            img = pyautogui.screenshot()

            # Convert the image to a numpy array
            frame = np.array(img)

            # Convert RGB to BGR (required for OpenCV)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            # Write the frame to the video file
            out.write(frame)
    except Exception as e:
        print("An error occurred while recording:", str(e))

# Create a thread for screen recording
record_thread = threading.Thread(target=record_screen)

try:
    # Start recording
    record_thread.start()

    # Wait for the user to press the "q" key to stop recording
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    # Stop recording when you press Ctrl+C
    pass
finally:
    # Stop the recording thread and release the VideoWriter
    recording = False
    record_thread.join()
    out.release()
    cv2.destroyAllWindows()
