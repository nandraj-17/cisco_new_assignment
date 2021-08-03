<?php include('server.php'); ?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Insert and Retrieve data from MySQL database with ajax</title>
  <link rel="stylesheet" href="style.css" type="text/css">
</head>
<body>
  <div class="wrapper">
  	<?php echo $saved_detail; ?>
  	<form class="comment_form">
      <div>
        <label>SapId:</label>
      	<input type="text" name="name" id="name">
      </div>
      <div>
      	<label >Hostname:</label>
      	<input type="text" name="name" id="name">
        </div>
        <div>
        <label>Loopback(ipv4):</label>
        <input type="text" name="name" id="name">
      </div>
        <div>
        <label>MAC Address:</label>
        <input type="text" name="name" id="name">
      </div>
      <button type="button" id="submit_btn">submit</button>
      <button type="button" id="update_btn" style="display: none;">UPDATE</button>
  	</form>
  </div>
</body>
</html>
<!-- Add JQuery -->
<script src="jquery.min.js"></script>
<script src="script.js"></script>