
# Security Tool

## Overview
<<<<<<< HEAD
This security tool offers comprehensive scanning for network, web, cloud infrastructure, and containers. It features machine learning for detecting potential future threats based on past vulnerabilities.

### Key Features:
- **JWT Authentication**: Secure your API endpoints with token-based authentication.
- **Cloud Scanning**: Supports scanning AWS ECS, GCP Cloud Run, and Azure AKS.
- **Network and Web Scanners**: Uses Nmap and OWASP ZAP for vulnerability detection.
- **Machine Learning**: Predict future vulnerabilities based on past scan data.
- **Graphical Reports**: Generate detailed reports with visualized charts in PDF.
- **Scan Scheduling**: Automatically schedule scans for periodic assessments.
- **Rate Limiting**: Protect sensitive endpoints from abuse with rate-limiting.
=======
This security tool offers comprehensive scanning for network, web, cloud infrastructure, and containers. It now features machine learning for detecting potential future threats and supports OAuth2 authentication with refresh tokens.

### Key Features:
- **OAuth2 Authentication**: Secure login with token refresh functionality for long-lived sessions.
- **JWT Authentication**: Secure your API endpoints with token-based authentication.
- **Cloud Scanning**: Supports scanning AWS ECS, GCP Cloud Run, Azure AKS, GCP IAM, and Azure Storage.
- **Network and Web Scanners**: Uses Nmap and OWASP ZAP for vulnerability detection.
- **Machine Learning**: Predict future vulnerabilities based on past scan data.
- **Graphical Reports**: Generate detailed reports with visualized charts in PDF, including vulnerability trends and comparison charts.
- **Scan Scheduling**: Automatically schedule scans for periodic assessments.
- **Rate Limiting**: Protect sensitive endpoints from abuse with rate-limiting.
- **Role-Based Access Control (RBAC)**: Differentiates between admin and regular users.
>>>>>>> 5bc60ec (push)

## How to Run the Project

### Prerequisites:
1. **Docker**: Ensure Docker is installed on your system.
2. **Python 3.9+**: The application requires Python 3.9 or later.

### Installation Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/security_tool.git
   cd security_tool
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the Docker services:
   ```bash
   docker-compose up --build
   ```

### Running the Application:
- The backend API will be available on `http://localhost:8000`.
- The GUI is accessible on `http://localhost:3000`.

### How to Use:
1. **Authentication**:
   - Login to the system using `/login` endpoint by providing your username and password.
   - Obtain a JWT token, which must be used to authenticate API requests.
<<<<<<< HEAD

2. **Network Scanning**:
   - You can perform a network scan by sending a POST request to `/scan` with the target IP address.
=======
   - **Token Refresh**: Use the `/refresh_token` endpoint to refresh your token using a refresh token.

2. **Network Scanning**:
   - Perform a network scan by sending a POST request to `/scan` with the target IP address.
>>>>>>> 5bc60ec (push)
   - Example:
     ```bash
     curl -X POST "http://localhost:8001/scan" -d '{"target_ip": "192.168.1.1"}' -H "Authorization: Bearer <your_token>"
     ```

3. **Cloud Scanning**:
<<<<<<< HEAD
   - Cloud scans are available for AWS ECS, GCP Cloud Run, and Azure AKS.
   - Example for AWS ECS scan:
     ```bash
     curl -X POST "http://localhost:8003/aws/scan" -H "Authorization: Bearer <your_token>"
=======
   - Cloud scans are available for AWS ECS, GCP Cloud Run, Azure AKS, GCP IAM, and Azure Storage.
   - Example for GCP IAM scan:
     ```bash
     curl -X POST "http://localhost:8003/gcp/scan" -H "Authorization: Bearer <your_token>"
>>>>>>> 5bc60ec (push)
     ```

4. **Machine Learning Predictions**:
   - The machine learning model can predict future vulnerabilities based on scan data.
   - Example:
     ```bash
     curl -X POST "http://localhost:8000/predict" -d '{"open_ports": 3, "services_running": 5, "configurations": 2, "cloud_provider": "aws"}' -H "Authorization: Bearer <your_token>"
     ```

5. **Report Generation**:
<<<<<<< HEAD
   - After a scan is completed, generate a PDF report:
=======
   - Generate PDF reports with vulnerability trends and comparison charts:
>>>>>>> 5bc60ec (push)
     ```bash
     curl -X POST "http://localhost:8000/generate_pdf" -H "Authorization: Bearer <your_token>"
     ```

<<<<<<< HEAD
6. **Scan Scheduling**:
   - Schedule scans to run periodically using the scheduler in `scheduler.py`.

## Future Enhancements
- OAuth2 authentication integration.
- Expanded cloud service coverage.
- More advanced machine learning models for better prediction accuracy.
- Role-based access control for administrators and regular users.
=======
6. **Role-Based Access Control**:
   - Admin routes require an admin token.
   - Example for accessing the admin dashboard:
     ```bash
     curl -X GET "http://localhost:8000/admin/dashboard" -H "Authorization: Bearer <admin_token>"
     ```

7. **Scan Scheduling**:
   - Schedule scans to run periodically using the scheduler in `scheduler.py`.

## Future Enhancements
- Further optimization of the machine learning model for better prediction accuracy.
- Expansion of container scanning to more platforms.
- Improved CI/CD integration for automated scans during deployment.
>>>>>>> 5bc60ec (push)

