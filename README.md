# Continuous Integration and Continuous Delivery (CI/CD) – Final Project - Peer Reviewed - IBM

This project demonstrates a complete **CI/CD pipeline** using GitHub Actions, Tekton, and OpenShift. It is part of the **IBM Hands-on Lab: Continuous Integration and Continuous Delivery (CI/CD)** and showcases best practices for automating testing, building, and deployment of applications.

---

## 📂 Project Structure

├── .github/workflows/
│ └── workflow.yml # GitHub Actions CI pipeline for linting and unit testing
├── .tekton/
│ └── tasks.yml # Tekton tasks for linting, unit testing, and building images
├── tests/
│ └── test_app.py # Unit tests for the sample application
├── app.py # Sample application code
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## 🔑 Objectives Achieved

1. **CI Pipeline with GitHub Actions**
   - Configured a pipeline that automatically runs **linting** and **unit tests** on code commits and pull requests.
   - Ensures code quality and test coverage before deployment.

2. **Tekton Pipeline Tasks**
   - Created reusable **Tekton tasks** for linting, unit testing, and building container images.
   - Modular tasks that can be integrated into any OpenShift pipeline.

3. **OpenShift CI Pipeline**
   - Integrated Tekton tasks into a complete **OpenShift CI pipeline**.
   - Automated build, test, and deploy process using Tekton pipelines.

4. **Deployment to OpenShift Cluster**
   - Configured deployment steps in the pipeline to **automatically deploy the application** to the lab OpenShift environment.
   - Ensures the latest tested version of the application is always deployed.

---

## ⚙️ Technologies Used

- **GitHub Actions** – Continuous Integration pipeline
- **Tekton** – CI/CD task automation
- **OpenShift** – Container orchestration and deployment
- **Python** – Application code and unit testing
- **Pytest** – Unit test framework
- **Flake8 / Linting** – Code quality checks

---

## 🏗️ Project Workflow

1. **Code Commit**
   - Developer pushes code changes to the GitHub repository.

2. **GitHub Actions**
   - Automatically triggers linting and unit tests.
   - Prevents faulty code from merging.

3. **Tekton Tasks**
   - Runs linting, testing, and container image build tasks.
   - Produces container image ready for deployment.

4. **OpenShift CI Pipeline**
   - Uses Tekton tasks to build, test, and deploy the application to the OpenShift cluster.
   - Verifies the application runs successfully in a production-like environment.

---
<img width="956" height="510" alt="2" src="https://github.com/user-attachments/assets/aac01f04-1c2e-4cc3-a6cf-b928137ef96c" />

<img width="956" height="511" alt="4" src="https://github.com/user-attachments/assets/6d24fd4d-c680-4bc1-a072-1a71ba268824" />

## 🚀 How to Run

1. **Clone the repository**

```bash
git clone https://github.com/Shaunak-Kunde/Continuous-Integration-Continuous-Delivery-Peer-Graded-IBM-Final-Project-of-Shaunak.git
cd Continuous-Integration-Continuous-Delivery-Peer-Graded-IBM-Final-Project-of-Shaunak
Install Python dependencies (optional, for local testing)

bash
Copy code
pip install -r requirements.txt
Run the sample application locally

bash
Copy code
python app.py
Execute unit tests

bash
Copy code
pytest tests/test_app.py
Note: CI/CD pipelines are fully automated via GitHub Actions, Tekton, and OpenShift. Manual execution is optional for local verification.
```

## 🌟 Learning Outcomes
Gained hands-on experience creating CI/CD pipelines from scratch.

Learned to integrate GitHub Actions, Tekton tasks, and OpenShift pipelines.

Applied best practices in unit testing, linting, and automated deployment.

Understood modular pipeline design for scalability and maintainability.

<img width="485" height="377" alt="10" src="https://github.com/user-attachments/assets/1c7329f0-e030-4479-8522-556a0b86ad5c" />

## 🙌 Acknowledgements
IBM Skills Network Hands-on Lab: Continuous Integration and Continuous Delivery (CI/CD)

OpenShift Container Platform

Tekton Pipelines and GitHub Actions documentation
