<?php
// Establish a connection to the MySQL database
$servername = "localhost"; // Replace with your MySQL server name if different
$username = "afeef"; // Use the username you created
$password = "123"; // Use the password you set for the user
$dbname = "miniproject"; // Replace with your MySQL database name

$conn = new mysqli($servername, $username, $password, $dbname);

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Process the form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve the form data
    $username = $_POST["username"];
    $password = $_POST["password"];

    // Query the database to check if the user exists
    $sql = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
    $result = $conn->query($sql);

    // Check if the query returned any rows
    if ($result->num_rows > 0) {
        
        session_start();
        // User exists, redirect to the index page
        header("Location: index.html");
        exit();
    } else {
        // User does not exist or invalid credentials, display an error message
        echo "Invalid username or password.";
    }
}

// Close the database connection
$conn->close();
?>
