<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SQL Server Query Export</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f7f6;
            color: #333;
            margin: 0;
            padding: 0;
            text-align: center;
        }
        header {
            background-color: #1e3d58;
            color: white;
            padding: 20px;
            font-size: 1.5em;
        }
        .container {
            margin: 20px;
        }
        .section {
            background-color: white;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h2 {
            color: #1e3d58;
        }
        ul {
            text-align: left;
            margin: 0 auto;
            padding-left: 20px;
            max-width: 600px;
        }
        img {
            width: 100%;
            max-width: 600px;
            border-radius: 8px;
            margin-top: 20px;
        }
        footer {
            background-color: #1e3d58;
            color: white;
            padding: 10px;
            position: fixed;
            width: 100%;
            bottom: 0;
        }
    </style>
</head>
<body>

<header>
    SQL Server Query Export Project
</header>

<div class="container">
    <div class="section">
        <h2>About the Project</h2>
        <p>This project helps to export SQL Server query results into a CSV file. It is designed for both local and remote database connections, allowing flexible usage for different environments.</p>
        <img src="https://via.placeholder.com/600x300" alt="Project Screenshot">
    </div>

    <div class="section">
        <h2>Features</h2>
        <ul>
            <li>Supports both local and remote SQL Server connections</li>
            <li>Export query results to CSV</li>
            <li>Customizable queries for data retrieval</li>
            <li>Easy setup and use</li>
        </ul>
    </div>

    <div class="section">
        <h2>How to Use</h2>
        <p>Simply clone the repository and run the Python script to connect to your SQL Server database. The script will prompt you to choose between a local or remote connection and will execute the query to export results to a CSV file.</p>
        <pre><code>git clone https://github.com/yourusername/sql-server-query-export.git</code></pre>
        <pre><code>python query_sqlserver.py</code></pre>
    </div>

    <div class="section">
        <h2>Prerequisites</h2>
        <ul>
            <li>Python 3.x</li>
            <li>PyODBC</li>
            <li>SQLAlchemy</li>
            <li>pandas</li>
        </ul>
        <p>Install the required libraries with:</p>
        <pre><code>pip install pyodbc sqlalchemy pandas</code></pre>
    </div>
</div>

<footer>
    <p>&copy; 2024 Your Name | SQL Server Query Export Project</p>
</footer>

</body>
</html>
