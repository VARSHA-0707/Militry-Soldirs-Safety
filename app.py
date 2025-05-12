import cv2

# Load the video file
video_path = video_path = "C:\\Users\\anna_students\\Downloads\\video.png.mp4"
  # Replace with your actual video file path
cap = cv2.VideoCapture(video_path)

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Loop through each frame
while True:
    ret, frame = cap.read()  # Read a frame
   
    if not ret:  # If video ended, break loop
        break

    cv2.imshow("Soldier Safety Video", frame)  # Display frame

    if cv2.waitKey(25) & 0xFF == ord('q'):  # Exit on 'q' key press
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
