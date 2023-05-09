# Youtube Upload Automation

This is a Python code that automates the uploading process of YouTube videos using the Selenium WebDriver library. The code provides the option to upload either a single video multiple times or multiple videos at once. It also allows scheduling of the videos for a specific date.

Here's a breakdown of the code:

The code starts by importing the necessary modules: time, os, selenium, and tkinter. Then, it sets some constants for the XPaths of various elements on the YouTube Studio website.

Next, the code sets up the Selenium WebDriver by creating a ChromeOptions object, setting the logging level to 3, and providing the path to the Chrome user data directory and binary location.

The user is then prompted to choose whether they want to upload a single video multiple times or multiple videos at once. Based on the user's input, the code proceeds with the corresponding logic.

If the user chooses to upload a single video multiple times, they are prompted to enter the name of the video they want to upload and how many times they want to upload it. The code then starts a loop that uploads the video as many times as specified by the user.

If the user chooses to upload multiple videos at once, the code searches the videos folder for video files and uploads them one by one.

For each video, the code navigates to the YouTube Studio website, clicks the upload button, selects the file to upload, and clicks through the various screens until the video is scheduled for upload. The code also waits for the upload to complete before proceeding to the next video.

Finally, the code prints a message indicating that the upload process has completed.
