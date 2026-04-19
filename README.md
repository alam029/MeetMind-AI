# 🧠 MeetMind AI - Intelligent Meeting Assistant

> An AI-powered meeting assistant that analyzes Google Meet and Zoom meetings, extracts actionable tasks, maintains intelligent memory, and automates team collaboration.

---

## 📸 Project Overview

**MeetMind AI** is a full-stack web application that:
- 📹 Integrates with Google Meet and Zoom
- 🤖 Uses AI (OpenAI/Groq) to extract tasks from meeting transcripts
- 📋 Manages tasks with assignment and tracking
- 🧠 Maintains intelligent memory of decisions and insights
- 📧 Automates email notifications to team members
- 📊 Provides real-time dashboard with productivity metrics
- 👥 Enables team collaboration and task distribution

---

## 🎯 Key Features

### 🔐 Authentication & Security
- Secure JWT-based authentication
- Password hashing with bcrypt
- Token refresh mechanism
- Protected API endpoints

### 📹 Meeting Management
- Store and retrieve meeting recordings
- Support for Zoom and Google Meet
- Meeting transcript storage
- Participant tracking
- Meeting notes and metadata

### 🤖 AI-Powered Task Extraction
- Automatic task extraction from transcripts
- AI-powered meeting summarization
- Task prioritization
- Intelligent task categorization

### 📋 Task Management
- Create, read, update, delete tasks
- Task assignment to team members
- Status tracking (pending, in-progress, completed)
- Priority levels (low, medium, high)
- Due date management
- Task completion tracking

### 🧠 Hindsight Memory System
- Store key decisions and insights
- Timeline view of decisions
- Historical reference
- Context-aware memory retrieval

### 👥 Team Management
- Team member profiles
- Role-based access control
- Team collaboration
- Performance metrics

### 📊 Dashboard & Analytics
- Real-time statistics
- Meeting overview
- Task completion rates
- Team performance metrics
- Upcoming meetings widget

### 📧 Automation
- Automated email notifications
- Task assignment notifications
- Email logging and tracking

---

## 🏗️ Project Structure

```
MeetMind-AI/
│
├── backend/                  # FastAPI Backend (Python)
│   ├── app/
│   │   ├── core/            # Configuration & Security
│   │   ├── db/              # Database Layer
│   │   ├── models/          # SQLAlchemy ORM Models
│   │   ├── schemas/         # Pydantic Validation
│   │   ├── routers/         # API Endpoints
│   │   ├── services/        # Business Logic
│   │   └── utils/           # Helper Functions
│   ├── requirements.txt
│   ├── test_api.py
│   └── README.md
│
├── frontend/                 # React Frontend (JavaScript)
│   ├── src/
│   │   ├── pages/           # Page Components
│   │   ├── components/      # Reusable Components
│   │   ├── context/         # React Context (State)
│   │   ├── routes/          # Routing Config
│   │   ├── data/            # Mock Data
│   │   ├── styles/          # Global Styles
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── public/
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js
│
├── docs/                     # Documentation
├── PROJECT_STRUCTURE.md      # Detailed architecture
├── QUICK_START.md           # Developer guide
└── README.md                # This file
```

👉 **[See detailed structure →](PROJECT_STRUCTURE.md)**

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ (Backend)
- Node.js 16+ (Frontend)
- PostgreSQL or SQLite (Database)
- API Keys: OpenAI/Groq, Gmail (optional)

### Backend Setup (3 steps)

```bash
# 1. Navigate to backend
cd backend

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Linux/Mac
# or: venv\Scripts\activate     # Windows

# 3. Install dependencies and run
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

✅ Backend runs at: **http://localhost:8000**
📖 API Documentation: **http://localhost:8000/docs**

### Frontend Setup (3 steps)

```bash
# 1. Navigate to frontend
cd frontend

# 2. Install dependencies
npm install

# 3. Start development server
npm run dev
```

✅ Frontend runs at: **http://localhost:3000**

### Test the Application

```bash
# Backend: Open in browser
http://localhost:8000/docs     # Swagger UI
http://localhost:8000/health   # Health check

# Frontend: Open in browser
http://localhost:3000          # Main application

# Demo Credentials
Email: any@email.com
Password: anything             # Use any value (demo mode)
```

---

## 🛠️ Tech Stack

### Backend
| Technology | Purpose |
|-----------|---------|
| **FastAPI** | Modern async Python web framework |
| **SQLAlchemy** | ORM for database abstraction |
| **Pydantic** | Data validation using Python type hints |
| **JWT** | Secure authentication |
| **PostgreSQL/SQLite** | Database |
| **Uvicorn** | ASGI server |
| **OpenAI/Groq** | AI task extraction |
| **SMTP** | Email notifications |

### Frontend
| Technology | Purpose |
|-----------|---------|
| **React 18.2** | UI component library |
| **Vite** | Fast build tool & dev server |
| **Tailwind CSS** | Utility-first CSS |
| **React Router v6** | Client-side routing |
| **React Context** | State management |
| **Recharts** | Data visualization |
| **Lucide React** | Icon library |

---

## 📚 Documentation

| Document | Purpose |
|----------|---------|
| **[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)** | Complete architecture guide |
| **[QUICK_START.md](QUICK_START.md)** | Developer reference & commands |
| **[backend/README.md](backend/README.md)** | Backend setup & configuration |
| **[frontend/README.md](frontend/README.md)** | Frontend setup & features |

---

## 🔄 Data Flow

```
┌──────────────────────┐
│  React Frontend      │
│  (Port 3000)         │
│                      │
│ • Dashboard          │
│ • Meetings           │
│ • Tasks              │
│ • Team               │
│ • Memory             │
└──────────┬───────────┘
           │ HTTP/JSON
           ↓ ↑
┌──────────────────────┐
│  FastAPI Backend     │
│  (Port 8000)         │
│                      │
│ • Auth Endpoints     │
│ • CRUD Routes        │
│ • Business Logic     │
│ • Database Layer     │
└──────────┬───────────┘
           │
           ├→ PostgreSQL/SQLite
           ├→ OpenAI/Groq API
           ├→ Gmail SMTP
           └→ External Services
```

---

## 🔌 Core API Endpoints

### Authentication
```
POST   /api/auth/signup
POST   /api/auth/login
POST   /api/auth/refresh-token
```

### Meetings & Tasks
```
GET    /api/meetings              # List meetings
POST   /api/meetings              # Create meeting
PUT    /api/meetings/{id}         # Update meeting
GET    /api/tasks                 # List tasks
POST   /api/tasks                 # Create task
PUT    /api/tasks/{id}            # Update task
```

### Dashboard & Team
```
GET    /api/dashboard/stats       # Get statistics
GET    /api/team                  # List team members
```

👉 **[See all endpoints →](QUICK_START.md#-api-endpoints-cheat-sheet)**

---

## 📋 Typical User Flow

### 1. Authentication
```
User → Enters email/password → Frontend Login Page
     → POST /api/auth/login → Backend validates
     → JWT token returned → Stored in localStorage
```

### 2. View Dashboard
```
User → Views Dashboard → Fetches /api/dashboard/stats
     → Displays statistics, upcoming meetings, recent tasks
```

### 3. Create Meeting
```
User → Creates meeting → POST /api/meetings
     → Provides transcript → AI extracts tasks
     → Tasks saved → Notifications sent to team
```

### 4. Manage Tasks
```
User → Views tasks → PUT /api/tasks/{id}
     → Updates status → Notifications sent
```

---

## 🗄️ Database Schema

### Users
```
id (PK) | email | password_hash | full_name | created_at
```

### Meetings
```
id | user_id | title | transcript | date | source | created_at
```

### Tasks
```
id | meeting_id | title | description | assigned_to | status | priority
```

### Team Members
```
id | user_id | team_id | role | joined_at
```

### Memory (Hindsight)
```
id | user_id | type | content | source_meeting_id | created_at
```

---

## 🔐 Security Features

✅ **Implemented**
- JWT token-based authentication
- Password hashing with bcrypt
- CORS protection
- Protected API endpoints
- Secure environment variables
- SQL injection prevention (SQLAlchemy)

---

## 🎯 Development Guide

### Adding a New Feature

1. **Backend**
   - Create database model in `app/models/`
   - Create Pydantic schema in `app/schemas/`
   - Add API routes in `app/routers/`
   - Add business logic in `app/services/`

2. **Frontend**
   - Create page component in `src/pages/`
   - Create UI components in `src/components/`
   - Add routing in `src/routes/AppRoutes.jsx`
   - Integrate with backend API

👉 **[Detailed feature guide →](QUICK_START.md#-typical-feature-development)**

---

## 🧪 Testing

```bash
# Backend
cd backend
python test_api.py              # Run API tests

# Frontend
cd frontend
npm test                        # Run component tests
npm run build                   # Test production build
```

---

## 🚨 Troubleshooting

| Issue | Solution |
|-------|----------|
| CORS errors | Check backend CORS config in `app/main.py` |
| Authentication failed | Clear localStorage, re-login |
| Database connection | Check `DATABASE_URL` in `.env` |
| Port already in use | Kill process: `lsof -i :8000` or `:3000` |
| Dependencies missing | Run `pip install -r requirements.txt` or `npm install` |

👉 **[More troubleshooting →](QUICK_START.md#-common-issues--fixes)**

---

## 📞 Support & Help

**Stuck?** Start here:
1. Read [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for architecture
2. Check [QUICK_START.md](QUICK_START.md) for common tasks
3. Visit API docs: http://localhost:8000/docs
4. Check browser console: F12 → Console
5. Enable debug logging in code

---

## 🤝 Contributing

### Code Organization
- Keep files focused and single-responsibility
- Use descriptive naming conventions
- Separate business logic from routes/components
- Validate all inputs with Pydantic/schemas
- Add type hints throughout code

### Before Committing
- ✅ Backend tests pass
- ✅ Frontend builds successfully
- ✅ No console errors
- ✅ Code follows project structure
- ✅ Environment variables documented

---

## 📦 Deployment

### Backend Deployment (Production)
```bash
# Use production database (PostgreSQL)
# Set secure environment variables
# Deploy with Gunicorn + Nginx
gunicorn app.main:app --workers 4 --bind 0.0.0.0:8000
```

### Frontend Deployment (Production)
```bash
# Build optimized bundle
npm run build

# Deploy to hosting (Vercel, Netlify, AWS S3)
# Set VITE_API_URL to production backend URL
```

---

## 📝 Environment Setup

### Backend `.env` Example
```env
DATABASE_URL=postgresql://user:password@localhost/meetmind
SECRET_KEY=your-secret-key-at-least-32-chars
ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24
FRONTEND_URL=http://localhost:3000
OPENAI_API_KEY=sk-your-key-here
GROQ_API_KEY=gsk-your-key-here
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=your-email@gmail.com
SENDER_PASSWORD=your-app-password
```

### Frontend `.env.local` Example
```env
VITE_API_URL=http://localhost:8000
VITE_APP_NAME=MeetMind AI
```

---

## 🎓 Learning Resources

- **FastAPI Tutorial**: https://fastapi.tiangolo.com/tutorial/
- **React Documentation**: https://react.dev/
- **Tailwind CSS Guide**: https://tailwindcss.com/docs
- **SQLAlchemy ORM**: https://docs.sqlalchemy.org/
- **JWT Authentication**: https://jwt.io/

---

## 📊 Project Statistics

| Metric | Value |
|--------|-------|
| Backend Routes | 30+ endpoints |
| Database Models | 6 models |
| Frontend Pages | 6 pages |
| UI Components | 10+ reusable components |
| API Documentation | Interactive Swagger UI |
| Database Support | PostgreSQL, SQLite |

---

## ✨ Key Highlights

🚀 **Modern Stack** - FastAPI + React with type safety
🔐 **Secure** - JWT auth, password hashing, CORS protection
📊 **Scalable** - Service layer, clean architecture
🧠 **AI-Powered** - OpenAI/Groq integration
⚡ **Fast** - Async Python, optimized React
📱 **Responsive** - Mobile-first Tailwind design
📚 **Well-Documented** - Clear code and guides
🧪 **Testable** - Separated concerns, testable code

---

## 📋 Roadmap

### Phase 1 ✅
- [x] User authentication
- [x] Meeting management
- [x] Task extraction
- [x] Basic dashboard
- [x] Team collaboration

### Phase 2 🔜
- [ ] Real-time WebSocket updates
- [ ] Advanced analytics
- [ ] Scheduled meetings sync
- [ ] Custom task templates
- [ ] Mobile app

### Phase 3 📅
- [ ] Advanced AI features
- [ ] Integration marketplace
- [ ] Team workflows
- [ ] Audit logs
- [ ] Multi-language support

---

## 📄 License

This project is part of the Hackathon competition. All rights reserved.

---

## 📞 Contact & Support

- **Documentation**: See [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)
- **Quick Help**: See [QUICK_START.md](QUICK_START.md)
- **Issues**: Check [QUICK_START.md#-common-issues--fixes](QUICK_START.md#-common-issues--fixes)

---

## ⭐ Credits

**MeetMind AI** - Intelligent Meeting Assistant
Built for the Hackathon 2026

---

<div align="center">

### 🚀 Ready to Start?

1. **[Quick Start Guide →](QUICK_START.md)**
2. **[Project Structure →](PROJECT_STRUCTURE.md)**
3. **[Backend Setup →](backend/README.md)**
4. **[Frontend Setup →](frontend/README.md)**

**Questions?** Check the relevant README or documentation above.

---

**Happy Coding! 🎉**

</div>
