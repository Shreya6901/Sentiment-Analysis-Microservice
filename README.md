# Sentiment Analysis Microservice

This project implements a microservice for sentiment analysis using **FastAPI**. The microservice is built following the **MVC (Model-View-Controller)** architectural pattern and exposes two main endpoints:

1. **`/predict`**: Uses a custom-trained sentiment analysis model to predict the sentiment of the input text.
2. **`/predict_external`**: Sends the input text to an external AI API (e.g., Hugging Face) for sentiment prediction.

The API can be tested through the interactive **Swagger UI** or by using tools such as **curl** and **Postman**.

---

## **Project Structure (Following MVC Pattern)**

```
.
├── app
│   ├── __init__.py               # Initialize the 'app' package (empty file)
│   ├── model.py                  # Model logic (loads and uses the sentiment model) - [Model Layer]
│   ├── controller.py             # Controller logic (API routing and logic) - [Controller Layer]
│   └── main.py                   # Entry point to run the API server (starts the application) - [Controller Layer]
├── model
│   ├── sentiment_model.pkl       # Saved trained sentiment model - [Model Layer]
│   └── vectorizer.pkl            # Saved vectorizer for text data - [Model Layer]
├── train_model.py                # Script to train and save the model - [Model Layer]
├── tests
│   └── test_api.py               # Unit tests for the API - [Tests]
├── README.md                     # Instructions for setup and usage
└── requirements.txt              # Python dependencies
```

---

## **MVC Pattern in This Project**

The **MVC (Model-View-Controller)** pattern organizes the project into three main components:

1. **Model**:
   - Handles the logic of loading, training, and saving models for sentiment analysis.
   - In this project, the **Model** layer consists of:
     - `model/sentiment_model.pkl`: Pre-trained sentiment analysis model.
     - `model/vectorizer.pkl`: TF-IDF vectorizer for transforming input text.
     - `train_model.py`: Script to train the sentiment analysis model.
     - `app/model.py`: Contains the `SentimentModel` class which loads and interacts with the trained model.
2. **View**:
   - In this API-based microservice, there is no traditional "View" layer (such as HTML templates). The **API responses** act as the "view" by returning the output (sentiment prediction) to the user.
   - **Swagger UI** (`http://127.0.0.1:8000/docs`) serves as the front-end for testing and visualizing the API responses.
3. **Controller**:
   - Controls the flow of the application, handling user requests and providing appropriate responses.
   - The **Controller** layer consists of:
     - `app/controller.py`: Contains the API endpoints (`/predict`, `/predict_external`, `/health`) and routing logic for processing requests.
     - `app/main.py`: The entry point that runs the FastAPI server and ties together the routes defined in `controller.py`.

---

## **Installation and Setup**

### **1. Clone the Repository**

```bash
git clone <repository_url>
cd Sentiment-Analysis-Microservice
```

### **2. Create and Activate a Virtual Environment**

- On **macOS/Linux**:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```
- On **Windows**:
  ```bash
  python -m venv .venv
  .venv\Scripts\activate
  ```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4. Train the Model**

Make sure you have **IMDB Dataset.csv** in the project folder. Then run the following command to train the sentiment analysis model and save it:

```bash
python train_model.py
```

The trained model and vectorizer will be saved in the `model/` folder as `sentiment_model.pkl` and `vectorizer.pkl`.

---

## **Running the API**

### **1. Start the FastAPI Server**

Run the following command to start the FastAPI server using **Uvicorn**:

```bash
python -m app.main
```

- The API will be available at **`http://127.0.0.1:8000`**.
- **Swagger UI** will be available at **`http://127.0.0.1:8000/docs`**.

---

## **API Endpoints**

### **1. Health Check**

- **URL**: `/health`
- **Method**: `GET`
- **Description**: Checks if the API service is running.

**Example Request (curl)**:

```bash
curl http://127.0.0.1:8000/health
```

**Example Response**:

```json
{
  "status": "running"
}
```

---

### **2. Sentiment Prediction Using Custom Model**

- **URL**: `/predict`
- **Method**: `POST`
- **Description**: Takes a JSON object with a `"text"` key and predicts the sentiment using a custom-trained model.

**Request Example** (JSON):

```json
{
  "text": "I love this product!"
}
```

**Example Request (curl)**:

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{"text": "I love this product!"}'
```

**Example Response**:

```json
{
  "sentiment": "positive"
}
```

---

### **3. Sentiment Prediction Using External AI API**

- **URL**: `/predict_external`
- **Method**: `POST`
- **Description**: Takes a JSON object with a `"text"` key, sends the input to an external AI API (e.g., Hugging Face), and returns the prediction.

**Request Example** (JSON):

```json
{
  "text": "I love this product!"
}
```

**Example Request (curl)**:

```bash
curl -X POST "http://127.0.0.1:8000/predict_external" \
-H "Content-Type: application/json" \
-d '{"text": "I love this product!"}'
```

**Example Response**:

```json
{
  "label": "POSITIVE",
  "score": 0.999865
}
```

The labels in the external model might be represented as:

- **LABEL_0**: Negative
- **LABEL_1**: Neutral
- **LABEL_2**: Positive

---

## **Testing with Swagger UI**

FastAPI automatically generates an interactive **Swagger UI** where you can test the API without needing external tools like Postman or curl.

### **Steps to Use Swagger UI**:

1. **Access Swagger UI**:

   - Open your browser and go to **`http://127.0.0.1:8000/docs`**.

2. **Test the `/predict` Endpoint**:

   - Find the **`POST /predict`** endpoint in the Swagger UI.
   - Click on **"Try it out"**.
   - Enter the following JSON in the input box:
     ```json
     {
       "text": "I love this product!"
     }
     ```
   - Click **"Execute"**.
   - You will see the predicted sentiment in the response section below the input form.

3. **Test the `/predict_external` Endpoint**:

   - Scroll down to the **`POST /predict_external`** endpoint.
   - Click **"Try it out"**.
   - Enter the same JSON input:
     ```json
     {
       "text": "I love this product!"
     }
     ```
   - Click **"Execute"** to send the request to the external AI API.
   - The predicted sentiment and confidence score from the external model will appear in the response section.

---

## **Running Unit Tests**

Unit tests are provided to verify the correctness of the API. To run the tests, use the following command:

```bash
pytest tests/
```

This will run the test cases located in the `tests/test_api.py` file.

---

## **Conclusion**

This sentiment analysis microservice is structured following the **MVC** pattern. The project separates the concerns of data handling, control logic, and view (API responses). It provides two main endpoints: one that uses a custom-trained model and another that uses an external AI API for sentiment predictions. You can interact with the API through **Swagger UI**, **curl**, or **Postman**.
