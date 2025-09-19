# Career Solutions Website

## Overview
A Flask-based career site solution that provides job listings, company information, and contact functionality. The site features a responsive design using Bootstrap and includes basic career management functionality.

## Recent Changes (September 19, 2025)
- Set up complete Flask web application structure
- Created responsive HTML templates with Bootstrap styling
- Implemented job listings page with sample data
- Added contact form with API endpoint
- Configured for Replit environment with proper host settings
- Set up deployment configuration for autoscale

## Project Architecture
- **Backend**: Flask (Python)
- **Frontend**: HTML templates with Bootstrap CSS framework
- **Deployment**: Configured for Replit autoscale deployment
- **Port Configuration**: Frontend serves on port 5000 with 0.0.0.0 host binding

## File Structure
```
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Homepage
│   ├── about.html        # About page
│   ├── careers.html      # Job listings
│   └── contact.html      # Contact form
└── static/               # Static assets
    ├── css/style.css     # Custom styles
    └── js/main.js        # JavaScript functionality
```

## Features
- Responsive navigation
- Job listings with sample data
- Contact form with AJAX submission
- About page with company information
- Modern Bootstrap-based design

## Development
The application runs on Flask development server and is configured for the Replit environment with proper host binding and port configuration.