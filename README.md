90 North Assignment 
============================

This repository contains the completed tasks for the assignment involving **Frontend Development**, **Django**, and **AWS Lambda Functions**. The project is divided into three main parts, each designed to meet the requirements specified in the assignment.

Project Overview
----------------

### **Frontend Development**

A responsive webpage was created with the following features:

1.  **Fixed Navbar**: The navigation bar remains stationary while scrolling.
    
2.  **Three-Section Layout**:
    
    *   Left collapsible menu.
        
    *   Main content area.
        
    *   Right-side panel.
        
3.  **Footer**: Positioned at the bottom of the page.
    
4.  **Responsive JavaScript Functionality**: The layout adjusts based on screen width.
    

### **Django Chat Application**

A fully functional chat application was developed with these features:

1.  **User Registration and Login**: Users can sign up and log in securely.
    
2.  **User List Display**: A collapsible left menu lists all registered users.
    
3.  **Chat Functionality**: Users can initiate one-on-one chats, send messages, and retrieve previous messages.
    
4.  **Database Integration**: Chat messages and user data are stored in a PostgreSQL database.
    
5.  **WebSocket Integration**: Enables real-time communication in the chat interface.
    
6.  **User-Friendly Interface**: Clean, responsive design for optimal user experience.
    

### **AWS Lambda Functions**

1.  **Addition Function**: Adds two numbers and returns the result.
    
2.  **Document Storage**: Uploads a document or PDF file to an S3 bucket.
    

Technologies Used
-----------------

*   **Frontend**: HTML, CSS, JavaScript
    
*   **Backend**: Django Framework
    
*   **Database**: PostgreSQL
    
*   **AWS**: Lambda, S3
    
*   **Hosting**: PythonAnywhere (for Django app)
    

Folder Structure
----------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   arduinoCopyEditproject/  ├── frontend/  │   ├── index.html  │   ├── styles.css  │   ├── scripts.js  ├── django_app/  │   ├── chat/  │   ├── templates/  │   ├── static/  │   ├── db.sqlite3  │   ├── manage.py  ├── aws/  │   ├── addition_function.py  │   ├── upload_to_s3.py  ├── requirements.txt  ├── README.md   `

Setup and Installation
----------------------

### **Step 1: Clone the Repository**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   bashCopyEditgit clone https://github.com/yourusername/assignment_repo.git  cd assignment_repo   `

### **Step 2: Frontend**

Open the frontend/index.html file in a web browser to view the webpage.

### **Step 3: Django Application**

1.  bashCopyEditcd django\_app
    
2.  bashCopyEditpip install -r requirements.txt
    
3.  bashCopyEditpython manage.py runserver
    
4.  Access the app at http://127.0.0.1:8000.
    

### **Step 4: AWS Lambda**

1.  Deploy addition\_function.py and upload\_to\_s3.py to AWS Lambda.
    
2.  Configure triggers as needed (API Gateway or S3 events).
    

Usage Instructions
------------------

### **Frontend**

*   The webpage adjusts its layout based on screen size using the implemented JavaScript logic.
    
*   Interact with the collapsible menu, explore the main content, and view the footer.
    

### **Django Chat App**

1.  Register a new user or log in with an existing account.
    
2.  Select a user from the collapsible menu to initiate a chat.
    
3.  Send messages and view old messages in real time.
    

### **AWS Lambda**

1.  Trigger the addition function via an API Gateway or directly from the AWS Lambda console.
    
2.  Upload files to S3 using the upload\_to\_s3.py function.
    
License
-------

This project is licensed under the **MIT License**.
