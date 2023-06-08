<?php
// Get the content and filename from the request
$content = $_POST['content'];
$filename = $_POST['filename'];

// Save the content to a file
$file = fopen($filename, 'w');
fwrite($file, $content);
fclose($file);

// Return a response indicating success or failure
if ($file) {
    echo 'File saved successfully';
} else {
    echo 'Failed to save file';
}
?>
