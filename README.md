# j

Backend API for j

## Tech Stack

- **Frontend**: React
- **Backend**: FastAPI + SQLAlchemy
- **Frontend Source**: GitHub ([Repository](https://github.com/HimaShankarReddyEguturi/Hotelbookinguidesign))

## Project Structure

```
j/
├── frontend/          # Frontend application
├── backend/           # Backend API
├── README.md          # This file
└── docker-compose.yml # Docker configuration (if applicable)
```

## Getting Started

### Prerequisites

- Node.js 18+ (for frontend)
- Python 3.11+ (for Python backends)
- Docker (optional, for containerized setup)

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Backend Setup

```bash
cd backend
# Follow backend-specific setup instructions in backend/README.md
```

## Features

- User registration and login
- User profile management
- Data entry creation, reading, updating, and deletion

## API Endpoints

- `POST /api/register` - Create a new user account.
- `POST /api/login` - Log in to the application.
- `GET /api/profile` - Get the current user's profile information.
- `PUT /api/profile` - Update the current user's profile information.
- `POST /api/data` - Create a new data entry.
- `GET /api/data` - Get all data entries for the current user.
- `GET /api/data/{id}` - Get a single data entry by ID.
- `PUT /api/data/{id}` - Update a single data entry by ID.
- `DELETE /api/data/{id}` - Delete a single data entry by ID.

## License

MIT
