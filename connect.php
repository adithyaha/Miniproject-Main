<?php
// Establish a connection to the MySQL database
$servername = "localhost"; // Replace with your MySQL server name if different
$username = "afeef"; // Use the username you created
$password = "123"; // Use the passsword you set for the user
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
    $gender = $_POST["gender"];
    $dob = $_POST["dob"];

    // Calculate age from the date of birth
    $dobTimestamp = strtotime($dob);
    $nowTimestamp = time();
    $ageTimestamp = $nowTimestamp - $dobTimestamp;
    $age = floor($ageTimestamp / (365 * 24 * 60 * 60));

    // Insert the data into the database
    $sql = "INSERT INTO users (username, password, gender, dob, age) VALUES ('$username', '$password', '$gender', '$dob', $age)";
    if ($conn->query($sql) === TRUE) {
        echo "User created successfully.";
        header("Location: login.html");
        exit();
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}

// Close the database connection
$conn->close();
?>
