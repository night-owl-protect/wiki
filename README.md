# Night Owl Protect Documentation

[![Documentation Status](https://readthedocs.org/projects/night-owl-protect/badge/?version=latest)](https://night-owl-protect.readthedocs.io/en/latest/?badge=latest)

Official documentation for Night Owl Protect - the central mobile app and web portal for managing Night Owl Security Products.

## 📚 Documentation

View the live documentation at: [night-owl-protect.readthedocs.io](https://night-owl-protect.readthedocs.io)

## 🛠️ Local Development

### Prerequisites

- Python 3.11+
- pip

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/night-owl-protect-docs.git
   cd night-owl-protect-docs
   ```

2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r docs/requirements.txt
   ```

4. Build documentation:
   ```bash
   cd docs
   make html
   ```

5. View locally:
   Open `docs/_build/html/index.html` in your browser.

## 📁 Project Structure

```
.
├── .readthedocs.yaml    # Read the Docs configuration
├── README.md            # This file
└── docs/
    ├── conf.py          # Sphinx configuration
    ├── requirements.txt # Python dependencies
    ├── index.rst        # Main page
    ├── _static/         # Static files (CSS, images)
    ├── getting-started/ # Getting started guides
    ├── user-guide/      # User documentation
    ├── devices/         # Device documentation
    ├── support/         # FAQ and troubleshooting
    └── api/             # API reference
```

## 🚀 Deploying to Read the Docs

1. Push this repository to GitHub
2. Go to [readthedocs.org](https://readthedocs.org)
3. Import your project
4. Documentation builds automatically on each push

## 📝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-guide`)
3. Commit your changes (`git commit -am 'Add new guide'`)
4. Push to the branch (`git push origin feature/new-guide`)
5. Create a Pull Request

## 📄 License

This documentation is licensed under the [MIT License](LICENSE).
