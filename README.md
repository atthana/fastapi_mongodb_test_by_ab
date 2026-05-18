## FastAPI + MongoDB Async: โลกของ Non-blocking + ทดสอบด้วย ab

1. source ./venv/bin/activate
2. pip install -r requirements.txt
3. docker run -d --name local-mongo -p 27017:27017 mongo:latest     # Install mongo in Docker
4. cd order_service
5. python -m uvicorn app.main:app --reload                          # Force to use uvicorn from venv na

