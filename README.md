# 1️⃣ Clone the repository

git clone <your-repo-url>

# 2️⃣ Navigate to the project folder

cd fastapi_mvc # Change to your project directory

# 3️⃣ Create and activate a virtual environment

python -m venv .venv

# Mac/Linux:

source .venv/bin/activate

# Windows:

.venv\Scripts\activate

# 4️⃣ Install dependencies

pip install -r requirements.txt

# 5️⃣ Run the FastAPI server

uvicorn main:app --reload
