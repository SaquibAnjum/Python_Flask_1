# Student Management API (Flask on Vercel)

A RESTful API built with **Flask** and configured for serverless deployment on **Vercel**.

---

## 🚀 Features & Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | API status and root documentation |
| `GET` | `/test` | Health test route |
| `POST` | `/students` | Register a new student |
| `GET` | `/students` | Get list of all students |
| `GET` | `/students/passed` | Get list of students who passed (marks &ge; 40) |
| `GET` | `/students/stats` | Get grade & score statistics |
| `GET` | `/students/<student_id>` | Get details for a specific student |
| `PATCH` | `/students/<student_id>` | Update student details |
| `DELETE` | `/students/<student_id>` | Delete a student |

### Sample Payload for `POST /students`:
```json
{
  "student_id": "101",
  "name": "Saquib",
  "age": 22,
  "course": "Computer Science",
  "marks": 85
}
```

---

## 📁 Project Structure

```text
├── api/
│   └── index.py            # Vercel serverless entry point
├── src/
│   └── api_prac/
│       ├── __init__.py     # Flask application routes
│       └── student.py      # Student & StudentManager models
├── app.py                  # Root fallback entry point
├── .gitignore
├── .python-version         # Python runtime version for Vercel (3.12)
├── pyproject.toml
├── requirements.txt        # Python dependencies for Vercel
├── vercel.json             # Vercel routing configuration
└── README.md
```

---

## ☁️ Deploying to Vercel

### Option 1: Deploy via GitHub (Recommended)
1. Push your latest code to GitHub:
   ```bash
   git add .
   git commit -m "Configure project for Vercel deployment"
   git push origin main
   ```
2. Go to [Vercel Dashboard](https://vercel.com/dashboard).
3. Click **"Add New..."** &rarr; **"Project"**.
4. Import your repository (`Python_Flask_1`).
5. Keep the default settings and click **Deploy**.

### Option 2: Deploy using Vercel CLI
1. Install Vercel CLI (if not already installed):
   ```bash
   npm i -g vercel
   ```
2. Run deployment:
   ```bash
   vercel
   ```
3. Deploy to production:
   ```bash
   vercel --prod
   ```

---

## 💻 Local Development

```bash
# Activate virtual environment
.venv\Scripts\activate

# Run the Flask app
python -m src.api_prac
```
