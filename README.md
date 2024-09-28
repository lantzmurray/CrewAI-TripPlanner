CrewAI Trip Planner
This project is a more advanced version of the trip planner based on TylerProgramming's project on YouTube. This AI-powered trip planner expands upon the original by including features for multiple travelers and special requirements, making it a robust tool for planning personalized trips.

Features
Traveler Input: Users can input the total number of adults, children, and infants traveling.
Special Information Section: Users can add specific details, such as:
Teens or children with disabilities.
Special interests (e.g., historical sites, adventure parks, or special needs).
Critical medical or travel considerations.
This information will alert CrewAI to customize the trip accordingly, ensuring all traveler needs and preferences are addressed.
How It Works
The user inputs the number of adults, children, and infants.
The user can provide additional special information, including disabilities or interests that may impact the trip.
CrewAI uses the input data to plan a tailored itinerary, factoring in any special considerations.
Setup
Prerequisites
Python 3.8+
CrewAI
OpenAI GPT-4.0  (or another version)

Installation
Clone the repository:
Download or clone the repository from https://github.com/lantzmurray/CrewAI-TripPlanner.git.

Navigate to the project directory:
Open your terminal or command prompt and navigate to the project folder, CrewAI-TripPlanner.

Set up a virtual environment (optional but recommended):
Create a virtual environment using your preferred method.

Activate the virtual environment:

For Windows: Activate the virtual environment by running the activate script located in the Scripts folder.
For macOS/Linux: Activate the virtual environment by sourcing the activate script located in the bin folder.
Install dependencies:
Install the necessary dependencies listed in the requirements.txt file using your package manager.

Configure API keys:
Make sure to have your OpenAI API key and Serper key in your .env file. These can be stored as environment variables or configured within the project settings.


How to Use
Input the number of adults, children, and infants.
Add any special information such as travel preferences, special needs, or critical requirements.
The AI will generate a personalized trip plan that caters to your specific needs.
Future Enhancements
Destination Suggestions: Automatically suggest destinations based on the users' interests and special requirements.
Accommodation and Activity Recommendations: Provide options for hotels and activities suited to the group's specific needs.
Real-time Updates: Introduce notifications or updates to adapt the trip plan in real-time.
Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests. If you're planning major changes, please open an issue to discuss them first.

License
This project is licensed under the MIT License.



