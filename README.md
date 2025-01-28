
## **How to Run the Application**

1. Start the server with:
   ```bash
   uvicorn app.main:app --reload
   ```

2. The application will be accessible at:
   - Swagger UI (API documentation): `http://127.0.0.1:8000/docs`
   - Redoc: `http://127.0.0.1:8000/redoc`

--- 

### Docker
  To build the Docker image of the application, run the following command:
  ```bash
  docker-compose up --build
  docker-compose down
  docker-compose logs -f


