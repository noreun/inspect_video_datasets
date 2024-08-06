import cv2
import os
import pandas as pd
import ast
import random


def video_caption(video_directory, caption_csv):
    """Displays a video with corresponding caption with a translucent black background for visibility
    Parameters
    ---------
    video_directory: str
    Path of directory where all the videos are contained
    caption_csv: str
    Path of where the csv file is contained
    """
    
    list_ = [os.path.join(video_directory, f) for f in os.listdir(video_directory) if f.endswith('.mp4')] # Make a list of video paths from the inputted video directory
    
    random.shuffle(list_) # Another aspect of randomess
    
    df = pd.read_csv(caption_csv) # Convert csv to pandas df
    
    
    for video in list_:
        start_timestamp = "ST Unavailable" # Default start_timestamp, end_timestamp, and caption in case unable to find corresponding values for video
        end_timestamp = "ET Unavailable"
        caption = "Caption Unavailable"
        
        for _, row in df.iterrows(): # Iterate through entire df until finding the corresponding values for a video
            
    
            if "vid_" + row["YoutubeID"][-11:] == os.path.splitext(os.path.split(video)[1])[0][:15]:
                caption = row["Caption"]
                start_timestamp = row["Start_timestamp"]
                end_timestamp = row["End_timestamp"]
            
        
        cap = cv2.VideoCapture(video)


        # Check if the video opened successfully
        if not cap.isOpened():
            print("Error: Could not open video.")
            exit()
            
        # Get the frame rate of the video
        fps = cap.get(cv2.CAP_PROP_FPS)
        delay = int(865 / fps)  # Delay in milliseconds

        # Caption text properties
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = .5
        font_color = (255, 255, 255)  # White color
        thickness = 1

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Calculate position for the caption
            frame_height = frame.shape[0]
            frame_width = frame.shape[1]
            
            background_color = (0, 0, 0)
            opacity = 0.5
            
            # Get text size and calculate the rectangle position
            text_size_caption, _ = cv2.getTextSize(caption, font, font_scale, thickness)
            text_size_timestamp, _ = cv2.getTextSize(start_timestamp + " " + end_timestamp, font, font_scale, thickness)
            text_x_caption = (frame_width - text_size_caption[0]) // 2
            text_x_timestamp = (frame_width - text_size_timestamp[0]) // 2
            
            overlay = frame.copy()

            # # Draw a rectangle background
            cv2.rectangle(frame, (0, frame_height - 10), (frame_width, frame_height - 95), background_color, cv2.FILLED)
            # Overlay caption on the frame
            
            cv2.addWeighted(overlay, opacity, frame, 1 - opacity, 0, frame)
            cv2.putText(frame, caption,(text_x_caption, frame_height - 63), font, font_scale, font_color, thickness, cv2.LINE_AA)# Get text size and calculate the rectangle position
            cv2.putText(frame, start_timestamp + " " + end_timestamp,(text_x_timestamp, frame_height - 38), font, font_scale, font_color, thickness, cv2.LINE_AA)

            # Display the frame with caption
            cv2.imshow(f'{os.path.splitext(os.path.split(video)[1])[0]}', frame)

            # Exit if 'q' is pressed
            if cv2.waitKey(delay) & 0xFF == ord('q'):
                break

        # Release the video capture object
        cap.release()
        cv2.destroyAllWindows()
        
def main():   
    file_num = random.randint(1, 40) # Generate a random number for the csv file and the video directory

    caption_csv = f"Intern_{file_num}.csv"

    part_cut_path = "/Volumes/proj/hnl_downloaded_public_data/weakly_labeled/InternVid/data/training/Partitions-Cut"

    for folder in os.listdir(part_cut_path): # Iterate through all the split up partition directories to find corresponding partition file to video directory
        if not folder.startswith("."):

            for csv_file in os.listdir(os.path.join(part_cut_path, folder)):
                if csv_file == caption_csv:
                    caption_csv_path = os.path.join(os.path.join(part_cut_path, folder), caption_csv)


    video_directory = f"/Volumes/proj/hnl_downloaded_public_data/weakly_labeled/InternVid/data/training/Videos/Intern_{file_num}"

    video_caption(video_directory, caption_csv_path)
    
if __name__ == "__main__":
    main()
