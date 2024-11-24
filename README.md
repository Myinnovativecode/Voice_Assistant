Myra - Personal Voice Assistant
Myra is a Python-based personal voice assistant designed to perform various tasks through voice commands. The assistant uses speech recognition and text-to-speech synthesis to provide an interactive experience for the user. Myra is capable of performing a variety of tasks, such as sending emails, opening applications, fetching information from the web, playing music, and more.

Features
As of now, Myra supports the following tasks:

Send Email
Myra can send emails to any email address using Gmail's SMTP server. Simply provide the message content and the recipient’s address.

Open Applications
Myra can open commonly used applications like Visual Studio Code by voice command. You can add more application commands to suit your needs.

Open Websites
Myra can open websites such as Google and YouTube. You can add more website commands to customize the experience.

Wikipedia Search
Myra allows you to search Wikipedia by speaking the query, and it will read the summary of the search results.

Play Music
Myra can play music from a local directory. It selects a random MP3 file and plays it using the pygame library.

what's the Time
Myra can tell you the current time upon request.

Installation
To run Myra, you’ll need to set up a Python environment and install the required dependencies. Follow these steps to get started:

Step 1: Clone the Repository
bash
Copy code
git clone https://github.com/Myinnovativecode/Voice_Assistant.git
cd myra_voice_assistant
Step 2: Create a Virtual Environment (Optional but Recommended)
Create a virtual environment to keep the dependencies isolated:

bash
Copy code
python -m venv .venv
Activate the virtual environment:

On Windows:
bash
Copy code
.venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source .venv/bin/activate
Step 3: Install Dependencies
Install the required libraries using pip:

bash
Copy code
pip install -r requirements.txt
The requirements.txt file contains all necessary dependencies, including:

pyttsx3 (for text-to-speech)
speech_recognition (for voice recognition)
pygame (for playing music)
wikipedia (for Wikipedia search)
requests (for fetching news via News API)
smtplib (for sending emails)
Step 4: Configure Email Sending (Optional)
To enable the email functionality, you need to add your email credentials. Create a file named pass.txt in the root directory of the project and store your Gmail password in it (this is used for sending emails via Gmail’s SMTP server).

Step 5: Run the Program
Once everything is set up, run the myra.py script:

bash
Copy code
python myra.py
The assistant will greet you and start listening for commands.

Usage
You can interact with Myra by speaking commands. Here are some examples of what you can say:

"Send an email" – Myra will ask for the recipient’s email address and the content of the message.
"Open VS Code" – Myra will open Visual Studio Code (make sure it’s installed on your system).
"Open Google" – Myra will open the Google website in your default browser.
"Search Wikipedia" – Myra will search for the term on Wikipedia and read the result.
"Play music" – Myra will play a random song from your music folder.
"What’s the time?" – Myra will tell you the current time.
Example Interaction:
User: "Play music"
Myra: "Now playing: [Song Name]"

User: "Open Google"
Myra: "Opening Google"

User: "Send email"
Myra: "What should I say?" (After the user responds)
Myra: "Email sent successfully!"

User: "What’s the time?"
Myra: "It is 3:30 PM."

Future Features
In the future, Myra will support additional features like:

Reading News – Fetch and read news articles from sources like News API.
Reminders – Set and manage reminders for tasks and events.
Weather Information – Get real-time weather updates from various services.
Control Smart Devices – Integrate with smart home devices (e.g., controlling lights, thermostat, etc.).
Task Automation – Automate everyday tasks like turning off the computer, shutting down applications, etc.
Contributing
Feel free to fork the repository and create a pull request for any bug fixes, improvements, or new features. Please follow the guidelines for clean and well-commented code.

How to Contribute:
Fork the repository.
Create a new branch for your changes.
Commit your changes and push them to your fork.
Open a pull request to the main repository.
License
This project is licensed under the MIT License – see the LICENSE file for details.
