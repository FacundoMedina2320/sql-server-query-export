
# SQL Server Query Export Project

<img src="https://media.licdn.com/dms/image/v2/C5612AQFsHHGugpQFNw/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1540697982892?e=1739404800&v=beta&t=HsjxszpRT0QVGJc7dh9HLtHIQ0Qd40nM3L71P-S6IPk" alt="CSV to SQL" width="600" />

## About the Project

This project helps to export SQL Server query results into a CSV file. It is designed for both local and remote database connections, allowing flexible usage for different environments.

## Features

- Supports both local and remote SQL Server connections
- Export query results to CSV
- Customizable queries for data retrieval
- Easy setup and use

## How to Use

Simply clone the repository and run the Python script to connect to your SQL Server database. The script will prompt you to choose between a local or remote connection and will execute the query to export results to a CSV file.

```bash
git clone https://github.com/yourusername/sql-server-query-export.git
python query_sqlserver.py
```

## Prerequisites

- Python 3.x
- PyODBC
- SQLAlchemy
- pandas

Install the required libraries with:

```bash
pip install pyodbc sqlalchemy pandas
```

---

© 2024 Your Name | SQL Server Query Export Project
