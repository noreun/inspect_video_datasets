import cv2
import os
import pandas as pd
import ast
import random
from dotenv import load_dotenv

load_dotenv()

def video_caption(video_directory, caption_csv):
    """Displays a random video from dataset with corresponding caption with a translucent black background for visibility
    Parameters
    ---------
    video_directory: str
    Path of directory where all the videos are contained
    caption_csv: str
    Path of where the csv file is contained
    """


    list_ = [os.path.join(video_directory, f) for f in os.listdir(video_directory) if f.endswith('.mp4')] # Make a list of video paths from the inputted video directory
    
    random.shuffle(list_) # Another aspect of ramdonmess
    
    df = pd.read_csv(caption_csv) # Convert csv to df
    
    
    for video in list_:
        captions = ['Caption unavailable', 'Caption unavailable', 'Caption unavailable'] # Default list of captions in case unable to find corresponding captions for video
        
        for _, row in df.iterrows(): # Iterate through each row in df to find corresponding captions video
            
            if "vid_" + row["url"][-11:] == os.path.splitext(os.path.split(video)[1])[0][:15]:
                caption = row["caption"]
                captions = ast.literal_eval(caption)
                timestamps = ast.literal_eval(row["timestamp"])
            
        
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
        font_scale = .35
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
            text_size, _ = cv2.getTextSize(captions[0] + " " + str(timestamps[2]).strip('[]'), font, font_scale, thickness)
            text_x = (frame_width - text_size[0]) // 2
            
            overlay = frame.copy()

            # # Draw a rectangle background
            cv2.rectangle(frame, (0, frame_height - 10), (frame_width, frame_height - 95), background_color, cv2.FILLED)
            # Overlay caption on the frame
            
            cv2.addWeighted(overlay, opacity, frame, 1 - opacity, 0, frame)
            cv2.putText(frame, captions[0] + str(timestamps[0]).strip('[]'),(text_x, frame_height - 75), font, font_scale, font_color, thickness, cv2.LINE_AA)# Get text size and calculate the rectangle position
            
            text_size, _ = cv2.getTextSize(captions[1] + " " + str(timestamps[2]).strip("[]"), font, font_scale, thickness)
            text_x = (frame_width - text_size[0]) // 2
            
            cv2.putText(frame, captions[1] + str(timestamps[1]).strip('[]'),(text_x, frame_height - 50), font, font_scale, font_color, thickness, cv2.LINE_AA)# Get text size and calculate the rectangle position
            
            text_size, _ = cv2.getTextSize(captions[2] + " " + str(timestamps[2]).strip("[]"), font, font_scale, thickness)
            text_x = (frame_width - text_size[0]) // 2
            
            cv2.putText(frame, captions[2] + " " + str(timestamps[2]).strip("[]"),(text_x, frame_height - 25), font, font_scale, font_color, thickness, cv2.LINE_AA)# Get text size and calculate the rectangle position

            # Display the frame with caption
            cv2.imshow(f'{os.path.splitext(os.path.split(video)[1])[0]}', frame)

            # Exit if 'q' is pressed
            if cv2.waitKey(delay) & 0xFF == ord('q'):
                break

        # Release the video capture object
        cap.release()
        cv2.destroyAllWindows()

def main():

    proj_root = os.getenv('PROJ_ROOT', '/Volumes/proj')  # Use environment variable or default path
 
    file_num = random.randint(1, 40) # Select a random number between 1 and 40 to be used as which videos to caption

    video_directory = f"{proj_root}/hnl_downloaded_public_data/weakly_labeled/pandas-70M/data/Training/Video_Whole/Pandas-Training_{file_num}"

    caption_csv = f"{proj_root}/hnl_downloaded_public_data/weakly_labeled/pandas-70M/data/Training/Partitions_Cut/Pandas-Training_{file_num}.csv"

    video_caption(video_directory, caption_csv) # Execute code with video and csv path

if __name__ == "__main__":
    main()
