
# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from prediction import make_predictions

# app = FastAPI()

# # Define the custom function `ai_process` to convert input string to uppercase
# def ai_process(input_string: str):
#     return input_string.upper()

# # Create a POST route that uses the `ai_process` function
# @app.post("/process")
# async def process_string(in_string):
#     # print("********",in_string)
#     sample_data = {
#     in_string: [1],
#     }
#     try:
#         predictions = make_predictions(sample_data, 'trained_model.pkl', 'training_columns.pkl')
#         print("Predictions:", predictions)
#         return {"uppercase": predictions}

#     except ValueError:
#         raise HTTPException(status_code=422, detail="Invalid JSON in the request body")

#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Internal Server Error") from e

# # CORS (Cross-Origin Resource Sharing) settings
# origins = [
#     "http://localhost",        # Allow requests from localhost
#     "http://localhost:3000",   # Allow requests from localhost on port 3000 (adjust as needed)
#     # Add other allowed origins as needed for your frontend
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )




from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from prediction import make_predictions

app = FastAPI()

# Define the custom function `ai_process` to convert input string to uppercase
def ai_process(input_string: str):
    return input_string.upper()

# Create a POST route that uses the `ai_process` function
@app.post("/process")
async def process_string(in_string: str):
    print('check1')
    try:
        # Assuming `make_predictions` returns a dictionary
        predictions = make_predictions(in_string)
        print("Predictions:", predictions)
        return {"uppercase": predictions}

    except ValueError:
        raise HTTPException(status_code=422, detail="Invalid JSON in the request body")

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error") from e

# CORS (Cross-Origin Resource Sharing) settings
origins = [
    "http://localhost",        # Allow requests from localhost
    "http://localhost:3000",   # Allow requests from localhost on port 3000 (adjust as needed)
    # Add other allowed origins as needed for your frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)