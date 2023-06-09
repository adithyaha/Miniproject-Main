<?php
// Execute cam.py script
$output = array();
$retval = 0;
exec('python3 cam.py', $output, $retval);

// Check if the script executed successfully
if ($retval === 0) {
    // Process the output or perform any necessary actions
    $response = array('status' => 'success', 'message' => 'cam.py script executed successfully.', 'output' => $output);
} else {
    // Handle the error if the script failed to execute
    $response = array('status' => 'error', 'message' => 'Failed to execute the cam.py script.', 'output' => $output);
}

// Send the response as JSON
header('Content-Type: application/json');
echo json_encode($response);
?>
