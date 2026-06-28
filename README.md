🚀 Django Lead Generation System

A professional Django-based Lead Generation System that scrapes publicly available company information, stores it in a database, and provides a modern dashboard with search, CSV export, and Excel export functionality.

📌 Features
Scrape company information from public sources
Store leads in a Django database
Company Name
Website URL
Location
Search Leads
Responsive Bootstrap 5 Dashboard
CSV Export
Excel Export
Django Admin Panel
Duplicate Prevention using get_or_create()
🛠️ Tech Stack
Python 3
Django
Selenium
BeautifulSoup4
SQLite
Bootstrap 5
OpenPyXL
HTML5
CSS3
📂 Project Structure
django-lead-generation-system/
│
├── manage.py
├── db.sqlite3
│
├── config/
│
├── leads/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   │
│   ├── management/
│   │   └── commands/
│   │       └── scraper.py
│   │
│   └── templates/
│       └── leads/
│           └── lead_list.html
│
└── requirements.txt
⚙️ Installation
Clone Repository
git clone https://github.com/Anisjamiloffical1/django-lead-generation-system.git

cd django-lead-generation-system
Create Virtual Environment
python -m venv venv
Activate Virtual Environment
macOS/Linux
source venv/bin/activate
Windows
venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
Database Setup
python manage.py makemigrations

python manage.py migrate
Create Admin User
python manage.py createsuperuser
Run Development Server
python manage.py runserver

Open:

http://127.0.0.1:8000/

Admin Panel:

http://127.0.0.1:8000/admin/
🕷️ Scrape Leads

Run the custom Django management command:

python manage.py scraper

Example Output:

Successfully scraped leads
🔍 Search Leads

Use the search bar to filter companies by:

Company Name
Location
📄 Export CSV

Download all leads as CSV:

Export CSV Button
📊 Export Excel

Download all leads as Excel:

Export Excel Button
🗄️ Lead Model
class Lead(models.Model):
    company_name = models.CharField(max_length=255)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.company_name
📈 Future Improvements
User Authentication
Lead Notes
Lead Status Tracking
REST API
Pagination
Scheduled Scraping
PostgreSQL Support
Analytics Dashboard
Email Notifications
Advanced Filters
🎯 Learning Outcomes

This project demonstrates:

Django Development
Web Scraping with Selenium
Data Extraction
Database Management
Django ORM
Search Functionality
CSV Export
Excel Export
Bootstrap Dashboard Design
Git & GitHub Workflow
📜 License

This project is open source and available for educational and portfolio purposes.

👨‍💻 Author

Anis Jamil

Python Developer | Django Developer | Web Scraping Enthusiast
