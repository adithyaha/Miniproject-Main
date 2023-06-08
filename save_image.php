<?php
// Retrieve the image data from the request
$imageData = $_POST['imageData'];

// Decode the base64 image data
$decodedImageData = base64_decode(str_replace('data:image/png;base64,', '', $imageData));

// Generate a unique filename for the image
$filename = 'todays_selfie.jpg';

// Specify the path to store the image
$filePath = 'files/' . $filename;

// Check if a file with the same name exists
if (file_exists($filePath)) {
    // Delete the existing file
    unlink($filePath);
}

// Save the image to the specified path
file_put_contents($filePath, $decodedImageData);

// Return a success response to the client
http_response_code(200);
?>
