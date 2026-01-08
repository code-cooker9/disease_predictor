# 📋 Project Requirements - Multi-Disease Prediction System

## 🎯 Project Overview
A comprehensive web-based healthcare AI platform that leverages machine learning to predict multiple diseases and provide actionable health insights to users through an interactive web interface.

---

## 💻 System Requirements

### Hardware Requirements
- **Processor**: Intel Core i5 or equivalent (minimum)
- **RAM**: 4 GB (minimum), 8 GB (recommended)
- **Storage**: 2 GB free disk space
- **Display**: 1920x1080 resolution (recommended)

### Software Requirements
- **Operating System**: 
  - Windows 10/11
  - macOS 10.14+
  - Linux (Ubuntu 18.04+)
- **Python**: Version 3.8 or higher
- **Package Manager**: pip or conda
- **Version Control**: Git (optional, for cloning)

---

## 📦 Python Dependencies

### Core Framework
| Package | Version | Purpose |
|---------|---------|---------|
| Flask | >=2.3, <3.0 | Web framework for building the application |
| Jinja2 | >=3.1 | Template engine for dynamic HTML rendering |
| Werkzeug | Built-in | WSGI utility library (included with Flask) |

### Data Processing & Machine Learning
| Package | Version | Purpose |
|---------|---------|---------|
| numpy | >=1.27 | Numerical computing and array operations |
| pandas | >=2.1 | Data manipulation and analysis |
| scikit-learn | >=1.3 | Machine learning algorithms and utilities |
| joblib | >=1.3 | Serialization of Python objects (model persistence) |

### Security & Authentication
| Package | Version | Purpose |
|---------|---------|---------|
| bcrypt | >=4.0 | Password hashing and verification |
| Werkzeug.security | Built-in | Cryptographic functions for Flask |

### Environment Management
| Package | Version | Purpose |
|---------|---------|---------|
| python-dotenv | >=1.0 | Load environment variables from .env files |

---

## 🗄️ Database Requirements

- **SQLite3**: Built into Python - used for:
  - User account management
  - Prediction history storage
  - Consultation records
  - Contact/feedback storage

---

## 🤖 Machine Learning Models

### Pre-trained Models
The system includes the following trained ML models:

1. **Diabetes Prediction**
   - Model: Logistic Regression / Decision Tree
   - Features: 8 health parameters
   - File: `models/diabetes_model.pkl`

2. **Heart Disease Prediction**
   - Model: Random Forest / SVM
   - Features: 7 cardiac parameters
   - File: `models/heart_model.pkl`

3. **Kidney Disease Prediction**
   - Model: Ensemble methods
   - Features: 8 kidney function parameters
   - File: `models/kidney_model.pkl`

4. **Liver Disease Prediction**
   - Model: Gradient Boosting
   - Features: 7 liver function tests
   - File: `models/liver_model.pkl`

5. **Malaria Detection** (Rule-based)
   - File: `models/rule_based/malaria_rules.py`
   - Logic: Symptom and CBC-based rules

6. **Pneumonia Detection** (Rule-based)
   - File: `models/rule_based/pneumonia_rules.py`
   - Logic: Clinical symptom assessment

7. **Thyroid Disorder Prediction** (Rule-based)
   - File: `models/rule_based/thyroid_rules.py`
   - Logic: Hormonal parameter ranges

### Model Scalers
- Scikit-learn StandardScaler objects for feature normalization
- Files: `models/{disease}_scaler.pkl`

---

## 📊 Data Requirements

### Dataset Files
Located in `data/` directory:
- `diabetes_simple.csv` - 768 records
- `heart_simple.csv` - 152 records
- `kidney_simple.csv` - 142 records
- `liver_simple.csv` - 152 records
- `malaria_simple.csv` - 152 records
- `pneumonia_simple.csv` - 162 records
- `thyroid_simple.csv` - 162 records

### Training Dataset Location
- `l_models/` directory contains original training datasets
- Used for model retraining and validation

---

## 🎨 Frontend Requirements

### HTML/Template Engine
- Jinja2 for dynamic template rendering
- Bootstrap/CSS for responsive design

### CSS Framework
- Custom styles in `static/css/style.css`
- Responsive grid layout
- Mobile-friendly design

### JavaScript
- Vanilla JavaScript for frontend interactions
- AJAX for asynchronous form submissions
- Files: `static/js/main.js`, `static/js/script.js`

### Template Files
- `templates/base.html` - Base layout template
- `templates/index.html` - Homepage
- `templates/login.html` - Authentication
- `templates/signup.html` - User registration
- `templates/dashboard.html` - User dashboard
- `templates/detect.html` - Disease prediction interface
- `templates/prediction.html` - Prediction results
- `templates/consult.html` - Doctor consultation
- `templates/history.html` - Prediction history
- `templates/about.html` - About page

---

## 🔐 Security Requirements

### Authentication
- User registration and login system
- Password hashing using bcrypt
- Session management with Flask sessions
- Secure password storage

### Data Protection
- SQL injection prevention (parameterized queries)
- CSRF protection (Flask-WTF recommended for future)
- Secure headers configuration
- Environment variable management for sensitive data

---

## 📈 Performance Requirements

### Response Time
- Homepage load: < 2 seconds
- Prediction generation: < 1 second
- Dashboard load: < 1.5 seconds

### Scalability
- Support for 100+ concurrent users
- Database connection pooling
- Model inference optimization

---

## 🚀 Deployment Requirements

### Development Environment
- Python virtual environment
- Flask development server
- SQLite local database

### Production Environment (Optional)
- Production WSGI server (Gunicorn/uWSGI)
- Environment variables configuration
- SSL/TLS certificates (for HTTPS)
- Cloud hosting (AWS/Heroku/Azure)
- Docker containerization (optional)

### Deployment Dependencies
- Gunicorn: 21.2.0+ (for production)

---

## 📚 Documentation Requirements

### Required Documentation
- README.md - Project overview
- REQUIREMENTS.md - This file
- ML_TRAINING.md - Model training guide
- API documentation
- User guide

### Code Documentation
- Inline comments for complex logic
- Function docstrings
- Clear variable naming conventions

---

## 🧪 Testing Requirements

### Unit Testing
- Flask route testing
- ML model prediction testing
- Database operations testing

### Integration Testing
- End-to-end user workflows
- Form validation and submission
- Database transaction testing

---

## 🌐 Browser Compatibility

### Supported Browsers
- Chrome/Chromium 90+
- Firefox 88+
- Safari 14+
- Edge 90+

### Mobile Support
- iOS Safari 12+
- Android Chrome 90+
- Responsive design for all screen sizes

---

## 📝 Software Development Requirements

### Code Standards
- PEP 8 Python code style
- Clear variable and function naming
- Modular code architecture
- DRY (Don't Repeat Yourself) principle

### Version Control
- Git for source code management
- Feature branch workflow
- Meaningful commit messages

---

## ⚙️ Additional Configuration

### Environment Variables
```
FLASK_APP=app.py
FLASK_ENV=development
FLASK_SECRET=your_secret_key_here
DATABASE=database.db
```

### Model Features
- Each disease model has specific required input features
- Feature scaling required for ML predictions
- Validation of input ranges required

---

## 🔄 Maintenance Requirements

### Regular Updates
- Security patches for dependencies
- Model retraining with new data
- Database backups
- Log monitoring

### Monitoring
- Application error logs
- User activity logs
- Model performance metrics
- Server resource monitoring

---

## 📞 Support & Contact

For issues, questions, or feature requests related to these requirements, please contact the development team or submit an issue in the project repository.

---

**Last Updated**: January 3, 2026  
**Version**: 1.0  
**Project**: Multi-Disease Prediction System
