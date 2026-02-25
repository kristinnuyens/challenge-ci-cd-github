# CI/CD Pipeline Challenge

## Project Overview
This project was a GitHub Actions CI/CD challenge designed to simulate a Dev → QA → Prod deployment for a sample Python Streamlit application. We started from the Movie Recommender (https://github.com/kristinnuyens/movie-recommender) we created earlier.

**Objectives:**
- Practice CI/CD with GitHub Actions
- Run automated build and test jobs (CI)
- Simulate deployments to multiple environments (CD) 
- Use GitHub Environments & approvals
- Work with branches and branch protections
  
## Repository Structure
```text
.
├── README.md
├── app
│   ├── __init__.py
│   ├── inference.py
│   └── main.py
├── data
│   └── movie-recommender-final.csv
├── requirements.txt
├── runtime.txt
└── tests
    └── test_inference.py
```
## Step-by-Step Project Implementation

### 1. Set Up Python Environment
* Ensured Python 3.10 was used to avoid `imghdr` issues with Streamlit to create a virtual environment:

    ```bash
    /Library/Frameworks/Python.framework/Versions/3.10/bin/python3 -m venv venv
    source venv/bin/activate
    ```

* Installed dependencies:

    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

### 2. Streamlit App Development

* Created `main.py` to display content per environment (`dev`, `qa`, `prod`)
* Added `inference.py` and `data/movie-recommender-final.csv` for sample recommendations
* Implemented environment logic using:

    ```python
    ENV = os.getenv("ENVIRONMENT", "dev").lower()
    ```

* Streamlit displays:

  * **Dev** → green background, "Dev Environment"
  * **QA** → yellow background, "QA Environment"
  * **Prod** → red background, "Production Environment"

### 3. Continuous Integration (CI)

* Created `.github/workflows/ci.yml`
* Configured to run unit tests in `tests/test_inference.py` on pull requests → main
* Confirmed CI ran successfully for test PRs

### 4. Continuous Delivery (CD)

* Created `.github/workflows/cd.yml`
* Separate jobs for each branch:

    | Job         | Branch | Environment | Behavior                                      |
    | ----------- | ------ | ----------- | --------------------------------------------- |
    | deploy-dev  | `dev`  | Dev         | Echo deployment log                           |
    | deploy-qa   | `qa`   | QA          | Echo deployment log                           |
    | deploy-prod | `main` | Prod        | Manual approval required, echo deployment log |

* Verified CD pipeline logs for Dev, QA, and Prod
  
  ![Different Environments](<assets/Screenshot 2026-02-25 at 09.45.26.png>)

  ![Prod Deployment Steps](<assets/Screenshot 2026-02-25 at 09.45.42.png>)
  
* Prod workflow triggered **manual approval step** as required
  
  ![Deployment Log Showing Approval Step](<assets/Screenshot 2026-02-25 at 09.46.13.png>)

### 5. Local Testing

* Ran Streamlit locally with different environments:

    ```bash
    ENVIRONMENT=dev streamlit run app/main.py
    ENVIRONMENT=qa streamlit run app/main.py
    ENVIRONMENT=prod streamlit run app/main.py
    ```

* Verified page title and background color change correctly
* Verified recommendations displayed for sample user IDs

🧑‍💻 Contributors

Kristin Nuyens

⏰ Timeline

1 working day