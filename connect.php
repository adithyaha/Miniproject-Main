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
    $gender = $_POST["gender"];
    $dob = $_POST["dob"];
    $dateOfEntry = date("Y-m-d"); // Get the current date

    // Additional attributes
    $emotion = ""; // Empty for now
    $notes = ""; // Empty for now

    // Calculate age from the date of birth
    $dobTimestamp = strtotime($dob);
    $nowTimestamp = time();
    $ageTimestamp = $nowTimestamp - $dobTimestamp;
    $age = floor($ageTimestamp / (365 * 24 * 60 * 60));

    // Check if the user already exists in the users table
    $checkUserQuery = "SELECT * FROM users WHERE username = '$username'";
    $checkUserResult = $conn->query($checkUserQuery);

    if ($checkUserResult->num_rows > 0) {
        echo "Error: User already exists.";
    } else {
        // Insert the data into the users table
        $insertUserQuery = "INSERT INTO users (username, password, gender, dob, age) VALUES ('$username', '$password', '$gender', '$dob', $age)";

        if ($conn->query($insertUserQuery) === TRUE) {
            echo "User created successfully.";
            header("Location: login.html");
            exit();
        } else {
            echo "Error: " . $insertUserQuery . "<br>" . $conn->error;
        }

        // Create a new table for the user
        $createTableQuery = "CREATE TABLE IF NOT EXISTS {$username}_table (
            id INT(11) AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            date DATE,
            emotion VARCHAR(50),
            notes TEXT,
            privatenotes TEXT,
            FOREIGN KEY (username) REFERENCES users(username)
        )";

        if ($conn->query($createTableQuery) === TRUE) {
            echo "User table created successfully.";

            // Insert initial data into the user's table using prepared statement
            $insertDataQuery = "INSERT INTO {$username}_table (username, date, emotion, notes, privatenotes) VALUES (?, ?, ?, ?, '')";

            $stmt = $conn->prepare($insertDataQuery);
            $stmt->bind_param("ssss", $username, $dateOfEntry, $emotion, $notes);

            if ($stmt->execute() === TRUE) {
                echo "Initial data inserted successfully.";
            } else {
                echo "Error inserting initial data: " . $stmt->error;
            }

            $stmt->close();
        } else {
            echo "Error creating user table: " . $conn->error;
        }
    }
}

// Close the database connection
$conn->close();
?>
