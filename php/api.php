<?php
header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['status' => 'error', 'message' => 'Méthode non autorisée.']);
    exit;
}

$json_data = file_get_contents('php://input');
$data = json_decode($json_data, true);

if (!isset($data['action']) || empty($data['action'])) {
    http_response_code(400);
    echo json_encode(['status' => 'error', 'message' => 'Action non spécifiée.']);
    exit;
}

$action = $data['action'];
$python_script_path = '';
$response_message = '';

switch ($action) {
    case 'allumer':
        $python_script_path = '/py/allume.py';
        $response_message = "L'effaroucheur a été activé.";
        break;
    case 'eteindre':
        $python_script_path = '/py/eteint.py';
        $response_message = "L'effaroucheur a été désactivé.";
        break;
    default:
        http_response_code(400);
        echo json_encode(['status' => 'error', 'message' => 'Action non reconnue.']);
        exit;
}

$command = 'python3 ' . $python_script_path . ' 2>&1';

$output = shell_exec($command);

echo json_encode([
    'status' => 'success',
    'message' => $response_message,
    'python_output' => $output
]);
?>
