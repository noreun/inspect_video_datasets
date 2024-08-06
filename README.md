# HNL_DOWNLOADED_PUBLIC_DATA

## Table of Contents

## Datasets:

**WebVid10M**

*Description*
Large-scale text-video dataset, **containing 10 million video-text pairs** scraped from the stock footage sites. This dataset was used for large-scale pretraining to achieve state-of-the-art end-to-end retrieval in our frozen-in-time work: the code of which can be found [here](https://github.com/m-bain/frozen-in-time)
[Link to Dataset](https://huggingface.co/datasets/TempoFunk/webvid-10M)

*Download Log*
STATUS - FUll VIDEOS DOWNLOADED
7/29/2024 - 10,727,500 .mp4 files


*Training*

Train Partitions (.csv) - weakly_labeled > webvid-10M > data > train > partitions
Train Videos (.mp4) - weakly_labeled > webvid-10M > data > train > videos

*Validation*

Val Partitions (.csv) - weakly_labeled > webvid-10M > data > val > partitions
Val Videos (.mp4) - weakly_labeled > webvid-10M > data > val > videos

*Scripts*

Download-Script (.py) - weakly_labeled > webvid-10M > pfc > scripts > download_webvid-10M.py

**Pandas70M**

*Description*
Panda-70M is a large-scale dataset with 70M high-quality video-caption pairs. ***Note:*** *A 2.4M subset was used*
[Link to Dataset](https://github.com/snap-research/Panda-70M)

*Download Log*
STATUS - FULL VIDEOS DOWNLOADED (2.4M Subset)
7/29/20024 - 772878 .mp4 files | 1006816 files

*Training*

Training Whole Partition (.csv) - weakly_labeled > pandas-70M > data > Training > Partitions
Training 40-Part Partitions (.csv) - weakly_labeled > pandas-70M > data > Training > Partitions_Cut
Training Whole Videos (.mp4 & .m4a) - weakly_labeled > pandas-70M > data > Training > Video_Whole
Training Spliced Videos (.mp4) - weakly_labeled - pandas-70M > data > Training > Videos_Cut

*Validation*

Validation Partition (.csv) - weakly_labeled > pandas-70M > data > Validation > Partitions
Validation Whole Videos (.mp4) - weakly_labeled > pandas-70M > data > Validation > Videos_Whole > panda70m_validation ***Note:*** *May not contain all videos*
Validation Cut Videos (.mp4) - weakly_labeled > pandas-70M > data > Validation > Videos_Cut > panda70m_validation ***Note:*** *May not contain all videos*

*Scripts*

No-splice Script (.py) - weakly_labeled > pandas-70M > scripts > pandas70m-script-nocut.py
Download Videos and Splice Script (.py) - weakly_labeled > pandas-70M > scripts > pandas70m-scriptV2.py

**InternVid**

*Description*
InternVid-10M-FLT, a subset of InternVid-10M, consists of 10 million video clips, with generated high-quality captions for publicly available web videos.
[Link to Dataset](https://huggingface.co/datasets/OpenGVLab/InternVid)

*Download Log*
STATUS - DOWNLOADING FULL VIDEOS
7/29/2024 - 503408 .mp4 files | 758714 files

*Training*

Training Json files (.json) - weakly_labeled > InternVid > training-json
Whole Training Partition (.csv) - weakly_labeled > InternVid > data > training > Partitions-Full ***Note:*** *csv file was converted from InternVid-10M-flt.jsonl*
Training 40-Part Partitions (.csv) - weakly_labeled > InternVid > data > training > Partitions-Cut

*Scripts*

No-splice Script (.py) - weakly_labeled > pandas-70M > scripts > pandas70m-script-nocut.py
Download Videos and Splice Script (.py) - weakly_labeled > pandas-70M > scripts > pandas70m-scriptV2.py

**VIDAL-10M**

*Description*
Vidal-10M is a large video dataset which contains videos, text from various sources, depth, and infrared.
[Link to Dataset](https://github.com/PKU-YuanGroup/LanguageBind/blob/main/DATASETS.md)

*Training*

Training Partitions (.json) - weakly_labeled > VIDAL-10M > Train > Partitions
Training Data (.json, .mp4, .wav, .m4a, .png, etc.) - weakly_labeled > VIDAL-10M > Train > Videos

*Other*

Sample Data (.json, .mp4, .wav, .m4a, .png, etc.) - weakly_labeled > VIDAL-10M > coco_vat_test

*Scripts*

Download Dataset Content (.py) - weakly_labeled > VIDAL-10M > scripts


## Video-Captioning Demo:

*Description*
We have provided a live demo matching up the respective captioning and timestamps in each video. Currently we are only able to demonstrate this upon the InternVid, Pandas70M, and WebVid datasets. Each script will randomly select a video directory and randomly caption a video from the directory. The captions are all displayed with a translucent black box behind them for visibility. Some captions also have timestamps depending on the datasets. Press "q" on your keyboard to automatically go to the next video. Please refer to the scripts below to use the demos.  ***Note:*** *Certain video-caption pairs will contain captions that run off the screen or be too small to read. This is fine, this is only for demonstrative purposes. Go to the next video if captioning errors hinder your viewing.*

*Scripts*

Pandas-70M Captioning Demo (.py) - inspect_video_datasets > pandas-video-withcc.py

InternVid Captioning Demo (.py) - inspect_video_datasets > internvid-video-withcc.py

WebVid Captioning Demo (.py) - inspect_video_datasets > webvid-video-withcc.py

