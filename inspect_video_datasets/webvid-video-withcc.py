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
        
        caption = "Caption unavailable" # Default caption in case unable to find corresponding caption 
                
        for _, row in df.iterrows(): # Iterate through each row in df to match up video id with the caption
    
            if str(row["videoid"]) == os.path.splitext(os.path.split(video)[1])[0]:
                caption = row["name"]
            
        
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
        font_scale = .45
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
            
            
            overlay = frame.copy()

            # # Draw a rectangle background
            cv2.rectangle(frame, (0, frame_height - 10), (frame_width, frame_height - 95), background_color, cv2.FILLED)
            # Overlay caption on the frame
            
            cv2.addWeighted(overlay, opacity, frame, 1 - opacity, 0, frame)
            
            text_size, _ = cv2.getTextSize(caption, font, font_scale, thickness)
            text_x = (frame_width - text_size[0]) // 2
            
            cv2.putText(frame, caption,(text_x, frame_height - 50), font, font_scale, font_color, thickness, cv2.LINE_AA)# Get text size and calculate the rectangle position
            
            

            # Display the frame with caption
            cv2.imshow(f'{os.path.splitext(os.path.split(video)[1])[0]}', frame)

            # Exit if 'q' is pressed
            if cv2.waitKey(delay) & 0xFF == ord('q'):
                break

        # Release the video capture object
        cap.release()
        cv2.destroyAllWindows()
        
def main():
    
    master_video_dir = "/Volumes/proj/hnl_downloaded_public_data/weakly_labeled/webvid-10M/data/train/videos" # The directory with all the video directories

    master_video_path_list = [f for f in os.listdir(master_video_dir) if not f.startswith(".")] # Make a list of all the non-hidden video directories to be used for a random selection

    random_index = random.randint(0, len(master_video_path_list) - 1) # Randomly select an index to be called in the paths

    video_directory = f"/Volumes/proj/hnl_downloaded_public_data/weakly_labeled/webvid-10M/data/train/videos/{master_video_path_list[random_index]}" # Call video directory path using random index from list

    caption_csv = f"/Volumes/proj/hnl_downloaded_public_data/weakly_labeled/webvid-10M/data/train/partitions/{master_video_path_list[random_index]}" + ".csv" # Call partition path using random index from list

    video_caption(video_directory, caption_csv) # Execute function with paths
    
if __name__ == "__main__":
    main()
