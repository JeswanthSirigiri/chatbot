# chatbotA chatbot that provides answers to "how-to" questions related to Segment, mParticle, Lytics, and Zeotap by extracting information from their official documentation.

📌 Features
✅ Answers queries dynamically from official documentation
✅ Supports Segment, mParticle, Lytics, and Zeotap
✅ Extracts relevant sections using web scraping
✅ Provides real-time responses
✅ Simple web-based UI

🏗 Tech Stack
Backend: Django (Python)
Frontend: HTML, CSS, jQuery (AJAX)
Database: SQLite (default, can be changed)
Libraries: requests, BeautifulSoup, difflib (fuzzy matching)
⚡ Installation & Setup
🔹 Step 1: Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/cdp-chatbot.git
cd cdp-chatbot
🔹 Step 2: Set Up Virtual Environment
bash
Copy
Edit
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
🔹 Step 3: Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🔹 Step 4: Run Migrations
bash
Copy
Edit
python manage.py migrate
🔹 Step 5: Start the Development Server
bash
Copy
Edit
python manage.py runserver
Now, open http://127.0.0.1:8000/chatbot/ in your browser.

🎯 How to Use
Open the chatbot UI
Type a question (e.g., "How do I set up event tracking in Segment?")
The chatbot will retrieve relevant information from the official documentation
If no exact match is found, it provides a link to the relevant documentation
🛠 Project Structure
csharp
Copy
Edit
cdp-chatbot/
│── chatbot/                    # Django Project
│   │── chatbotapp/              # Main App
│   │   ├── migrations/          # Database Migrations
│   │   ├── static/              # Static Files (CSS, JS)
│   │   ├── templates/           # HTML Templates
│   │   ├── views.py             # Backend Logic
│   │   ├── models.py            # Database Models
│   │   ├── urls.py              # App URL Routes
│   │── chatbot/                 # Main Django Project
│   │   ├── settings.py          # Django Settings
│   │   ├── urls.py              # Project URL Routes
│   ├── manage.py                # Django Management Script
│   ├── requirements.txt         # Dependencies
│   ├── README.md                # Documentation
📜 Endpoints
Method	Endpoint	Description
GET	/chatbot/	Loads the chatbot UI
POST	/api/chatbot/	Handles chatbot queries
