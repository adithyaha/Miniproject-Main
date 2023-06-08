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
    // Retrieve the image data
    $imageData = $_POST["imageData"];
    $username = $_SESSION["username"]; // Assuming you have stored the username in the session

    // Prepare the statement to insert the image data into the user's table
    $stmt = $conn->prepare("UPDATE users SET image = ? WHERE username = ?");
    $stmt->bind_param("ss", $imageData, $username);

    // Execute the statement
    if ($stmt->execute()) {
        // Image stored successfully
        echo "Image stored successfully.";
    } else {
        // Error storing the image
        echo "Failed to store the image.";
    }

    // Close the statement
    $stmt->close();
}

// Close the database connection
$conn->close();
?>
