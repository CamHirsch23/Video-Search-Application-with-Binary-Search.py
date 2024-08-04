from flask import Flask, request, jsonify

# List of video titles
video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

# Binary search function
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Sort the list of video titles
video_titles.sort()

# Flask application
app = Flask(__name__)

# API endpoint for searching a video by title
@app.route('/search', methods=['GET'])
def search_video():
    query = request.args.get('title')
    index = binary_search(video_titles, query)
    if index != -1:
        return jsonify({"message": "Video found", "title": video_titles[index]})
    else:
        return jsonify({"message": "Video not found"}), 404

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
