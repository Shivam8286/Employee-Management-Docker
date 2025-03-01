
# Employee Management System with CRUD Operations using Docker

This project is a **Docker-based Employee Management System** that performs CRUD (Create, Read, Update, Delete) operations with **MySQL** as the backend database and **Flask** as the web framework.

---

## 🔥 Project Description
The Employee Management System is designed to perform employee data management, including:
- Adding new employees
- Viewing employee details
- Updating employee information
- Deleting employee records

The system is entirely containerized using Docker and follows **microservices architecture**.

---

## 🎯 Technologies Used
| Technology      | Purpose               |
|----------------|-----------------------|
| Python         | Backend Logic        |
| Flask          | Web Framework       |
| MySQL         | Database            |
| Docker        | Containerization    |
| Docker Compose | Multi-container Orchestration |

---

## 📁 Folder Structure
```plaintext
📁 employee_management
├── 📄 Dockerfile           # Docker Image Creation
├── 📄 docker-compose.yml   # Service Orchestration
├── 📁 app                 # App Source Code
│   ├── 📄 app.py          # Flask Backend
│   ├── 📄 requirements.txt # Python Dependencies
│   ├── 📁 templates       # HTML Templates
│   │   ├── index.html    # Home Page
│   │   ├── create.html   # Employee Creation Page
│   │   ├── update.html   # Employee Update Page
│   │   └── base.html     # Base HTML Layout
│   └── 📁 static         # CSS & Static Files
│       └── style.css    # Styling
└── 📄 init.sql           # Database Initialization Script
```

---

## ⚙️ How to Run the Project
### 1. Clone the Repository
```bash
git clone https://github.com/Shivam8286/employee_management.git
cd employee_management
```

### 2. Build and Start Docker Containers
```bash
docker-compose up --build
```

### 3. Access Application
- Open your browser and go to: http://localhost:5000

---

## Docker Hub Image
Pull the Docker Image directly from Docker Hub:
```bash
docker pull Shivamattri741/employee_management:latest
docker run -p 5000:5000 Shivamattri741/employee_management:latest
```

---

## Features
✅ Add Employees  
✅ View Employee List  
✅ Update Employee Details  
✅ Delete Employee Records  
✅ Fully Dockerized Setup  
✅ Automatic Database Creation  
✅ Modern User Interface  

---

## Screenshots
| Feature        
| Employee List 
| Create Employee 
| Update Employee 
| Delete Employee 


---

## 🛠️ Built With
- Flask  
- MySQL  
- Docker  
- Docker Compose  
- HTML/CSS  

---

## 🔗 Connect with Me
- LinkedIn: [Your LinkedIn Profile](linkedin.com/in/shivam-attri23)  
- GitHub: [Your GitHub Profile](https://github.com/Shivam8286)  
- Docker Hub: [Your Docker Hub Profile](https://hub.docker.com/u/Shivamattri741)  



## Author
👤 Shivam attri 
