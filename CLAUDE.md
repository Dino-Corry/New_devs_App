# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Dev Skeleton** - An ultra-minimal authentication base for new developers.

This is a stripped-down version of The Flex PMS containing ONLY:
- Login page
- Blank dashboard
- Profile page
- Logout functionality
- Protected routes

**Purpose**: Give new developers email/password credentials, let them login, see a blank dashboard, and build whatever features they're assigned.

## Development Philosophy

- Keep it ultra-minimal - just auth + blank canvas
- No user management UI, no settings, no business features
- The frontend is intentionally bare - let developers build what they need
- Focus on clean, simple code
- Always ask if you're not sure about something

## Tech Stack

### Frontend
- React 18 + TypeScript
- Tailwind CSS
- React Router
- React Query (@tanstack/react-query)
- Vite

### Backend
- FastAPI (Python 3.11+)
- Supabase (PostgreSQL)
- Redis (optional, for caching)
- Pydantic for validation

## Project Structure

```
├── backend/
│   ├── app/
│   │   ├── api/v1/          # API endpoints (auth, profile)
│   │   ├── core/            # Core services (auth, sessions)
│   │   ├── models/          # Data models
│   │   └── main.py          # App entry point
│   └── requirements.txt
│
└── frontend/
    ├── src/
    │   ├── components/      # React components (minimal)
    │   │   ├── profile/     # User profile
    │   │   ├── LoginPage.tsx
    │   │   ├── Dashboard.tsx    # Blank canvas
    │   │   ├── Sidebar.tsx      # Dashboard + Profile + Logout
    │   │   └── Header.tsx
    │   ├── contexts/        # React contexts (Auth, App)
    │   ├── lib/             # Utilities & API clients
    │   └── App.tsx
    └── package.json
```

## Development Commands

### Frontend Development (from `/frontend` directory)
```bash
npm install          # Install dependencies
npm run dev          # Start development server
npm run build        # Build for production
npm run lint         # Run ESLint
```

### Backend Development (from `/backend` directory)
```bash
# Setup virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Run development server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## Database

### Tables to Keep (Auth & User Management)
- `auth.users` - Supabase auth users
- `user_profiles` - User information
- `user_permissions` - Permissions
- `users_city` - City-based access
- `organizations` - Organization info
- `company_settings` - Company config
- `departments` - Department management
- `permission_templates` - Permission templates
- `audit_logs` - Audit trail

### ⚠️ Important: No Migrations
- **NEVER run database migrations yourself**
- Only the repository owner should run migrations
- If migrations are needed, ask the user to run them

## Key Features

### What's Included
1. Login page - Developer enters email/password
2. Authentication - Backend generates JWT token, stored in localStorage
3. Blank dashboard - Clean canvas for building features
4. Profile page - View/edit user profile
5. Logout - Clear tokens and session
6. Protected routes - Authentication enforcement

### What's NOT Included (Intentionally)
This skeleton has NO UI for:
- User management (no CRUD, no user list, no create user)
- Settings pages
- Signup flow
- Business features (properties, reservations, cleaning, etc.)
- ~95% of the original frontend codebase

The backend has full auth infrastructure, but the frontend only exposes login → dashboard → profile → logout.

## Guidelines for Claude

### DO:
- Keep the frontend minimal - it's intentionally bare
- Let developers build what they need on the blank dashboard
- Use TypeScript properly
- Handle errors gracefully
- Test authentication flows
- Document changes clearly

### DON'T:
- Add user management UI (it's intentionally removed)
- Add settings pages (intentionally removed)
- Add business features (properties, reservations, cleaning, etc.)
- Run database migrations
- Make assumptions - ask if unsure

### When Implementing Features:
1. Plan first
2. Implement step by step
3. Test thoroughly
4. Ensure mobile-friendly
5. Follow best practices
6. Maintain security

## API Interactions

- Use Supabase for all database operations
- Never hardcode credentials
- Use environment variables
- Handle auth tokens securely
- Validate all inputs

## Common Tasks

### Adding a New Feature to the Dashboard
1. Create backend endpoint in `backend/app/api/v1/`
2. Add frontend component in `frontend/src/components/`
3. Add route in `App.tsx` if needed
4. Update Sidebar navigation if needed
5. Test with authentication
6. Update documentation

### Modifying Authentication
1. Backend changes in `backend/app/core/auth.py`
2. Frontend changes in `frontend/src/contexts/AuthContext.new.tsx`
3. Test login/logout flows
4. Check token refresh
5. Verify protected routes work

### Important: This is a Minimal Skeleton
- Don't add user management UI - create users via Supabase directly
- Don't add settings pages - the skeleton is intentionally minimal
- Let developers build what they need on top of the blank dashboard

## Using This Skeleton for New Developers

### Setup Process
1. Create a test user in Supabase Auth
2. Give the developer the email/password
3. They login and see a blank dashboard
4. Assign them features to build
5. They have full auth already - just focus on building

### What They Can Learn
- How to work with an authenticated app
- React + TypeScript patterns
- FastAPI backend integration
- Building features from scratch
- Working with an existing auth system

The skeleton handles auth so they can focus on feature development.

## Troubleshooting

### Frontend Issues
- Clear browser cache and localStorage
- Check `.env` file configuration
- Verify API URL is correct
- Check console for errors

### Backend Issues
- Verify Supabase credentials
- Check Redis connection (if used)
- Ensure virtual environment is activated
- Check logs for detailed errors

### Auth Issues
- Clear localStorage
- Check JWT secret in backend
- Verify Supabase auth is configured
- Check token expiry settings

## Security Reminders

- Never commit `.env` files
- Keep secrets in environment variables
- Validate all user inputs
- Use parameterized queries
- Implement CSRF protection
- Check permissions on all endpoints

## Questions to Ask User

Before implementing anything significant:
- "Should this feature require specific permissions?"
- "Do you want this mobile-friendly?"
- "Should I add tests for this?"
- "Where should this feature live in the navigation?"

---

**Remember**: This is a MINIMAL DEV SKELETON. The frontend is intentionally bare - just login, blank dashboard, profile, and logout. Let developers build what they need!
