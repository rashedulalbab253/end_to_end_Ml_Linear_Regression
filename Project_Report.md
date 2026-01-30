# Project Report: End-to-End House Price Prediction

## 1. Project Overview
This project is an end-to-end Machine Learning implementation designed to predict house prices based on socio-economic and geographical features. It encompasses the entire lifecycle of a data science project, from Exploratory Data Analysis (EDA) and model training to deployment as a web application using FastAPI and containerization with Docker.

### Key Objectives:
- Implement a robust Linear Regression model for real estate valuation.
- Build a production-ready API for real-time predictions.
- Containerize the application for consistent environment deployment.
- Integrate CI/CD for automated building and pushing to Docker Hub.

---

## 2. Technical Stack
- **Languages:** Python (3.12)
- **Data Science:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- **API Framework:** FastAPI (Uvicorn as ASGI server)
- **Web Interface:** HTML5, Jinja2 Templates
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Registry:** Docker Hub

---

## 3. Data Source & Preparation
- **Dataset:** California Housing Dataset (Scikit-learn).
- **Features:** 
    - `MedInc`: Median income in block.
    - `HouseAge`: Median house age in block.
    - `AveRooms`: Average number of rooms.
    - `AveBedrms`: Average number of bedrooms.
    - `Population`: Block population.
    - `AveOccup`: Average house occupancy.
    - `Latitude`: Block latitude.
    - `Longitude`: Block longitude.
- **Pre-processing:**
    - Standard Scaling (`StandardScaler`) was applied to normalize features, ensuring that the gradient descent (used in Linear Regression internally) converges faster and features are on the same scale.
    - Data split into Training (70%) and Testing (30%) sets.

---

## 4. Modeling & Performance
- **Algorithm:** Linear Regression.
- **Training:** The model learns coefficients for each feature to find the best-fit hyperplane that minimizes the Mean Squared Error (MSE).
- **Artifacts:**
    - `regmodel.pkl`: The serialized scikit-learn model.
    - `scaling.pkl`: The serialized scaler to ensure consistent preprocessing of inference data.

---

## 5. Deployment Architecture
- **Web App:** Built with **FastAPI** for its high performance and automatic documentation.
- **Endpoints:**
    - `GET /`: Serves the user interface.
    - `POST /predict`: Accepts form input from the UI and returns the predicted price.
    - `POST /predict_api`: Accepts JSON input for programmatic access.
- **Dockerization:**
    - Multi-platform support via Docker.
    - Exposed on port 8000.
- **CI/CD:**
    - Automated workflow triggers on every push to `main` branch.
    - Builds the image and pushes it to **Docker Hub** (`rashedulalbab1234/end-to-end-ml-linear-regression`).

---

## 6. Interview Q&A (Preparation)

### Q1: Why did you choose Linear Regression for this project?
**A:** Linear Regression serves as a strong baseline model. Given the California Housing dataset has linear relationships between features (like income) and price, it provides a highly interpretable result. It’s also computationally efficient for real-time inference.

### Q2: Why is feature scaling necessary here?
**A:** Since features like `Population` and `MedInc` have vastly different ranges, the model coefficients would be biased towards larger numbers. `StandardScaler` ensures all features contribute equally to the final prediction and improves the stability of the regression.

### Q3: How do you handle "pickling" and what are the risks?
**A:** I used `pickle` to serialize the model and scaler. While convenient, it requires the same Python and library versions in both training and production environments. This is exactly why I used Docker—it ensures the environment remains identical, mitigating the "it works on my machine" problem.

### Q4: Explain your CI/CD pipeline.
**A:** I used GitHub Actions to automate the deployment. On every push to the main branch, the runner logs into Docker Hub, builds the image from the latest source code, and pushes it. This ensures that the production image is always up-to-date with the latest model or code changes.

### Q5: How would you improve this model?
**A:** I would explore:
1.  **Feature Engineering:** Creating new features like "Rooms per person".
2.  **Regularization:** Using Lasso or Ridge regression to prevent overfitting.
3.  **Advanced Regressors:** Testing ensemble methods like Random Forest or XGBoost for better accuracy on non-linear patterns.

---

## 7. How to Run
```bash
# Pull from Docker Hub
docker pull rashedulalbab1234/end-to-end-ml-linear-regression:latest

# Run the container
docker run -p 8000:8000 rashedulalbab1234/end-to-end-ml-linear-regression
```
