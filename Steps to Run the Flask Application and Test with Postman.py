Step 1: Run the Flask Application

Install Flask: Ensure you have Flask installed in your Python environment. You can install Flask using pip:
bash


pip install Flask
Save the Code: Save the provided Flask application code to a file, for example, app.py.
Run the Application: Open a terminal, navigate to the directory containing app.py, and run the application:
bash


python app.py
This will start the Flask development server, typically accessible at http://127.0.0.1:5000/.
Step 2: Test the API Endpoint Using Postman

Open Postman: Ensure you have the Postman desktop app installed and open it 
.
Create a New Request:
Click on "New" and select "Request".
Name your request and save it to a collection if desired 
.
Set the Request URL:
Enter the URL of the Flask API endpoint: http://127.0.0.1:5000/sorted_videos 
.
Select the HTTP Method:
Choose the GET method for this request 
.
Send the Request:
Click the "Send" button to execute the request 
.
Verify the Response:
The API response, including the sorted video titles, will appear in the lower pane of Postman. You should see a JSON response with the sorted list of video titles 
.
Example of a Successful Request

Request URL: http://127.0.0.1:5000/sorted_videos
HTTP Method: GET
Response:
json


{
    "sorted_videos": [
        "Artificial Intelligence Revolution",
        "Cooking Masterclass: Italian Cuisine",
        "Digital Photography Essentials",
        "Exploring the Cosmos",
        "Financial Planning for Beginners",
        "Fitness Fundamentals: Strength Training",
        "History Uncovered: Ancient Civilizations",
        "Nature's Wonders: National Geographic",
        "The Art of Coding",
        "Travel Diaries: Discovering Europe"
    ]
}
