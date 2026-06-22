# HR Nexus — Django Employee Management & HR Dashboard

HR Nexus is a modern, responsive, and aesthetically polished HR dashboard and Employee Management System built using **Django** and **Bootstrap 5**. It features a dark-themed user interface, database-driven analytics dashboards, payroll breakdown reports, and full CRUD capabilities for handling employee records.

---

## 🌟 Key Features

1. **Dashboard & Employee Directory (CRUD)**
   - View, search, create, update, and delete employee records.
   - Live analytics cards (Headcount, Departments, Average Salary, Total Payroll) computed dynamically.
   - Real-time search filter for employee directory.

2. **Interactive Analytics Report**
   - **Department Distribution Chart**: A doughnut chart visualizing employee counts per department.
   - **Average Salary Chart**: A bar chart comparing compensation budgets.
   - **Top Earners List**: Renders a table of the highest compensated team members.

3. **Payroll Administration**
   - Monthly and annual salary breakdowns per employee.
   - **Budget Allocation Chart**: A pie chart showing payroll distribution per department.
   - Total payroll expenditure metrics.

4. **Attendance Tracking (Demo Dashboard)**
   - Daily sign-in logs with clock-in/out timestamps and duration.
   - Present, Absent, and On-Leave split metrics.
   - **Weekly Attendance Trend**: Line chart tracking participation percentages.

5. **Preferences & Settings Panel**
   - Clean UI controls for appearance (Dark/Compact modes), system notifications, regional formatting (Date formats, Currencies, Languages).

---

## 🛠️ Technology Stack

- **Backend Framework**: Django 5.2 (Python)
- **Database**: SQLite 3
- **Frontend Styling**: Bootstrap 5.3.3 (Dark Theme enabled)
- **Charts & Data Visualization**: Chart.js (via CDN)
- **Icons**: Bootstrap Icons
- **Typography**: Google Fonts (Inter)

---

## 📁 Directory Structure

```text
employee_management/
│
├── employee_management/           # Project Configuration
│   ├── settings.py                # Django Settings (Apps, DB, Templates)
│   └── urls.py                    # Root URL router
│
├── employees/                     # Employee Application
│   ├── admin.py                   # Model registration for admin panel
│   ├── forms.py                   # Employee ModelForm
│   ├── models.py                  # Employee Database Model
│   ├── urls.py                    # App-specific URL paths
│   └── views.py                   # Controllers (CRUD + Analytics backend)
│
├── templates/                     # Global HTML templates
│   ├── base.html                  # Shared layout, styles & sidebar nav
│   ├── employee_list.html         # Main dashboard directory
│   ├── employee_form.html         # Add & Edit form
│   ├── employee_delete.html       # Confirm delete layout
│   ├── analytics.html             # Chart.js analytics dashboard
│   ├── payroll.html               # Compensation & budget analysis
│   ├── attendance.html            # Attendance logs simulation
│   └── preferences.html           # Settings layout
│
├── db.sqlite3                     # SQLite database file
└── manage.py                      # Django CLI utility
```

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have **Python 3.10+** installed on your system.

### 2. Clone and Setup
1. Navigate to the project root directory:
   ```bash
   cd employee_management
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   * **Windows (PowerShell)**:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   * **macOS / Linux**:
     ```bash
     source venv/bin/activate
     ```

4. Install Django:
   ```bash
   pip install django
   ```

### 3. Run Migrations & Server
1. Apply the database migrations:
   ```bash
   python manage.py migrate
   ```

2. Start the development server:
   ```bash
   python manage.py runserver
   ```

3. Open your browser and navigate to:
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### 4. Admin Access (Optional)
To access Django's built-in administration site at `/admin/`:
1. Create a superuser account:
   ```bash
   python manage.py createsuperuser
   ```
2. Follow the prompts to set your username, email, and password.
3. Log in at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).
