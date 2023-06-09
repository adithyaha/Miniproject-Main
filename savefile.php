<?php
// Retrieve the content from the request
$content = $_POST['content'];

// Generate the filename using today's date
$filename = date('Ymd') . '_notes.txt';

// Specify the path to store the file
$filePath = 'files/' . $filename;

// Save the content to the specified file
file_put_contents($filePath, $content);

// Check if the file was saved successfully
if (file_exists($filePath)) {
    // Return a success response to the client
    echo 'File saved successfully';
} else {
    // Return an error response to the client
    echo 'Failed to save file';
}
?>
