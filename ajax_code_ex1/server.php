<?php 
  $conn = mysqli_connect('localhost', 'root', '', 'ajaxex1');
  if (!$conn) {
    die('Connection failed ' . mysqli_error($conn));
  }
  if (isset($_POST['save'])) {
    $sapid = $_POST['sapid'];
  	$hostname = $_POST['hostname'];
    $loopback = $_POST['loopback'];
    $macaddress = $_POST['macaddress'];
  	$sql = "INSERT INTO systems (sapid, hostname, loopback, macaddress) VALUES ('{$sapid}', '{$hostname}', '{$loopback}', '{$macaddress}')";
  	if (mysqli_query($conn, $sql)) {
  	  $id = mysqli_insert_id($conn);
      $saved_detail = '<div class="comment_box">
      		<span class="delete" data-id="' . $sapid . '" >delete</span>
      		<span class="edit" data-id="' . $sapid . '">edit</span>
      		<div class="display_name">'. $name .'</div>
      		<div class="display_name">'. $hostname .'</div>
          <div class="display_name">'. $loopback .'</div>
          <div class="display_name">'. $macaddress .'</div>
      	</div>';
  	  echo $saved_detail;
  	}else {
  	  echo "Error: ". mysqli_error($conn);
  	}
  	exit();
  }
  // delete comment fromd database
  if (isset($_GET['delete'])) {
  	$sapid = $_GET['sapid'];
  	$sql = "DELETE FROM systems WHERE sapid=" . $sapid;
  	mysqli_query($conn, $sql);
  	exit();
  }
  if (isset($_POST['update'])) {
  	$sapid = $_POST['sapid'];
  	$hostname = $_POST['hostname'];
  	$loopback = $_POST['loopback'];
    $macaddress = $_POST['macaddress'];
  	$sql = "UPDATE system SET hostname='{$hostname}', loopback='{$loopback}', macaddress='{$macaddress}'  WHERE sapid=".$sapid;
  	if (mysqli_query($conn, $sql)) {
  		$id = mysqli_insert_id($conn);
  		$saved_detail = '<div class="comment_box">
  		  <span class="delete" data-id="' . $sapid . '" >delete</span>
  		  <span class="edit" data-id="' . $sapid . '">edit</span>
  		  <div class="display_name">'. $hostname .'</div>
  		  <div class="display_name">'. $loopback .'</div>
        <div class="display_name">'. $macaddress .'</div>
  	  </div>';
  	  echo $saved_detail;
  	}else {
  	  echo "Error: ". mysqli_error($conn);
  	}
  	exit();
  }

  // Retrieve comments from database
  $sql = "SELECT * FROM systems";
  $result = mysqli_query($conn, $sql);
  $system = '<div id="display_area">'; 
  while ($row = mysqli_fetch_array($result)) {
  	$saved_detail .= '<div class="comment_box">
  		  <span class="delete" data-id="' . $row['sapid'] . '" >delete</span>
  		  <span class="edit" data-id="' . $row['sapid'] . '">edit</span>
  		  <div class="display_name">'. $row['hostname'] .'</div>
  		  <div class="display_name">'. $row['loopback'] .'</div>
        <div class="display_name">'. $row['macaddress'] .'</div>
  	  </div>';
  }
  $saved_detail .= '</div>';
?>