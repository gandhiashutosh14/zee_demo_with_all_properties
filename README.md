# Zee Demo with All Properties

This repository contains a demo project showcasing the integration of various cloud services for video processing and analysis. In this project, we utilize Azure Transcription for subtitle generation, AWS Rekognition for content moderation and celebrity recognition, and FFmpeg commands for video segmentation. The purpose of segmentation is to accommodate AWS Rekognition's limitation of processing a minimum video duration at a time. Therefore, we segment the video and store the segments in an AWS S3 bucket.

## Features

- **Azure Transcription:** Utilize Azure's powerful transcription service to automatically generate subtitles for videos.

- **AWS Rekognition:**
  - **Content Moderation:** Employ AWS Rekognition's content moderation capabilities to analyze and filter out objectionable content within videos.
  - **Celebrity Recognition:** Leverage AWS Rekognition's celebrity recognition feature to identify and tag celebrities present in the video.

- **FFmpeg Command for Segmentation:** Use FFmpeg commands to segment the video into smaller chunks. This is essential to ensure compatibility with AWS Rekognition's processing limitations.

- **AWS S3 Bucket Storage:** Store the segmented video chunks in an AWS S3 bucket for efficient and scalable storage.

## Getting Started

Follow these steps to get started with the Zee Demo project:

1. Clone this repository to your local machine using the following command:

2. Set up your cloud service accounts:
- **Azure Transcription:** Obtain the necessary API keys and configure them in the project.
- **AWS Rekognition:** Set up AWS credentials and configure the required permissions.
- **AWS S3 Bucket:** Create an S3 bucket to store the segmented video chunks.

3. Install the required dependencies. You can use the provided `requirements.txt` file to install Python dependencies using:

4. Customize the project as needed to suit your use case, including adjusting the segmentation duration and integration logic.

5. Run the project by executing the main script:

## Notes

- Ensure that you handle cloud service credentials and sensitive information securely, using environment variables or other secure methods.

- This project serves as a demonstration of integrating cloud services for video processing. It can be extended and adapted for various applications, such as video analysis, content moderation, and transcription.

- For more detailed information and usage instructions, refer to the code comments and documentation provided within the repository.

## License

This project is licensed under the [MIT License](LICENSE).
