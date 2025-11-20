# Dev Skeleton - Minimal Authentication Base

An ultra-minimal authentication skeleton extracted from The Flex PMS. This skeleton contains ONLY basic authentication - perfect for giving new developers a clean starting point to build features.

## What You Get

Just the essentials:
- ✅ Login with email/password
- ✅ Blank dashboard after login
- ✅ Profile page
- ✅ Logout functionality
- ✅ Protected routes

That's it. No user management UI, no settings, no business features. Just authentication and a blank canvas.

## Purpose

This skeleton is designed to:
1. Give new developers email/password credentials
2. Let them login
3. See a blank dashboard
4. Build whatever features they're assigned

## Tech Stack

### Infrastructure
- ✅ FastAPI backend
- ✅ React + TypeScript frontend
- ✅ Supabase (PostgreSQL) database
- ✅ Redux/Context for state management
- ✅ Protected route architecture

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ and npm
- Python 3.11+
- Supabase account (or local Supabase)
- Redis (optional, for caching)

### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your Supabase credentials

# Run the server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env
# Edit .env with your API URL

# Run development server
npm run dev
```

The app will be available at `http://localhost:5173`

## 📁 Project Structure

```
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── api/v1/         # API endpoints (auth only)
│   │   │   ├── auth_info.py
│   │   │   ├── persistent_auth.py
│   │   │   ├── profile.py
│   │   │   └── ...
│   │   ├── core/           # Core services
│   │   │   ├── auth.py
│   │   │   └── ...
│   │   ├── models/         # Data models
│   │   └── main.py         # Application entry point
│   └── requirements.txt
│
└── frontend/               # React frontend
    ├── src/
    │   ├── components/     # React components
    │   │   ├── profile/    # User profile
    │   │   ├── LoginPage.tsx
    │   │   ├── Dashboard.tsx (blank canvas)
    │   │   ├── Sidebar.tsx
    │   │   └── Header.tsx
    │   ├── contexts/       # React contexts
    │   │   ├── AuthContext.new.tsx
    │   │   └── AppContext.tsx
    │   ├── lib/            # Utilities & API clients
    │   │   ├── auth.ts
    │   │   └── supabase.ts
    │   └── App.tsx
    └── package.json
```

## 🛠️ Technology Stack

### Frontend
- **React 18** with TypeScript
- **Tailwind CSS** for styling
- **React Router** for navigation
- **React Query** for data fetching
- **Vite** as build tool

### Backend
- **FastAPI** (async Python web framework)
- **Python 3.11+**
- **Pydantic** for data validation
- **SQLAlchemy** (optional)

### Database & Infrastructure
- **Supabase** (PostgreSQL)
- **Redis** for caching
- **Supabase Auth** for authentication
- **Supabase Storage** for file uploads

## 🔐 Authentication Flow

1. **Login**: Developer enters email/password
2. **Token Generation**: Backend generates JWT token
3. **Session Storage**: Token stored securely in localStorage
4. **Dashboard**: Developer sees blank canvas
5. **Logout**: Tokens cleared and session invalidated

## 📋 Database Tables

The backend has access to the full auth database:
- `auth.users` - Supabase auth users
- `user_profiles` - User information
- Organization and permission tables

But the frontend UI only exposes:
- Login page
- Blank dashboard
- Profile page

## 🧪 How to Use This Skeleton

1. Create a test user in Supabase
2. Give the email/password to the new developer
3. They login and see a blank dashboard
4. They build whatever features you assign them
5. The auth system is already handled - they just focus on features

## 🚧 What's NOT Included

This skeleton has been stripped of all business features:
- ❌ Property management
- ❌ Reservations
- ❌ Cleaning operations
- ❌ Financial analytics
- ❌ Guest portals
- ❌ External integrations (Hostaway, Stripe, etc.)
- ❌ ~125 business database tables
- ❌ ~90% of the original codebase

## 📝 Common Development Commands

```bash
# Frontend
npm run dev          # Start dev server
npm run build        # Build for production
npm run lint         # Run ESLint

# Backend
uvicorn app.main:app --reload  # Start dev server
python -m pytest                # Run tests (if added)

# Docker (optional)
docker-compose up --build      # Start all services
```

## 🐛 Troubleshooting

### Frontend won't start
- Check Node.js version (18+)
- Delete `node_modules` and reinstall
- Check `.env` file configuration

### Backend errors
- Verify Python version (3.11+)
- Check virtual environment is activated
- Verify Supabase credentials in `.env`
- Ensure database tables exist

### Authentication issues
- Clear browser localStorage
- Check JWT secret key in backend `.env`
- Verify Supabase auth is configured
- Check Redis connection (if using cache)

## 📚 Learn More

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [Supabase Documentation](https://supabase.com/docs)
- [Tailwind CSS](https://tailwindcss.com/)

## ⚖️ License

This is a development testing skeleton - use internally for evaluation purposes.

---

**Dev Skeleton v1.0** - Minimal authentication base for new developers
