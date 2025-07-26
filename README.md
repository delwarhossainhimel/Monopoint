# Monopoint

Monopoint is an open-source Flask web application that visualizes infrastructure metadata such as database servers, monitoring tool URLs, service catalogs, Jenkins build servers, and other critical service endpoints. It reads YAML files from a `carts` directory and presents them in an easy-to-read web dashboard.

## Features

- 📋 Reads and renders infrastructure resource details from YAML files
- 📂 Organize resources by environment, type, and purpose
- 💻 Lightweight Flask-based backend
- 🌐 Clean, user-friendly web frontend

## Example Use Case

Developers often waste time hunting down:

- What's the URL for log monitoring on the dev server?
- Where's the Jenkins build server for UAT?
- What are the endpoints for staging service APIs?
- Where are service catalog definitions stored?

Monopoint centralizes these answers in one simple web UI.

You just define them once in YAML and Monopoint displays them categorized by environment, purpose, or team.

---

## Installation

```bash
git clone https://github.com/delwarhossainhimel/monopoint.git
cd monopoint
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000` to view the dashboard.

---

## File Structure

```
Monopoint/
├── app.py                  # Main Flask application
├── config.py               # Configuration settings
├── requirements.txt        # Dependencies
├── carts/                  # Directory for YAML files
│   ├── Database.yaml
│   └── Monitoring.yaml
├── static/
│   └── style.css           # CSS for styling
├── templates/
|   ├── base.html           # Base template
|   ├── index.html          # Main page showing all files
|   └── resource.html       # Page showing resource details
└── README.md
```

### Sample YAML file (`carts/databases.yaml`)

```yaml
name: Database Resources
description: List of all database servers
resources:
  - reason: Development
    type: MySQL
    ip: 192.168.20.20
    port: 3306
    owner: Dev Team A
    environment: dev
  - reason: Production
    type: PostgreSQL
    ip: 10.10.10.10
    port: 5432
    owner: DevOps
    environment: prod
```

Each file should contain:

- `name`: Section title
- `description`: Short info
- `resources`: List of entries with metadata

---

## Contributing

Contributions are welcome! Please:

- Fork this repository
- Create a branch
- Open a pull request with a clear description of changes

## License

This project is licensed under the MIT License. See the LICENSE file for more info.

## Author

Delwar Hossain Himel — [@delwarhossainhimel]([https://github.com/delwarhimel](https://github.com/delwarhossainhimel))

---
