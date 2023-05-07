<!DOCTYPE html>
<html>
<title>Weather</title>
<body>
<center>
<p>
<h1>Weather Forecast</h1>
<form method="POST">
What is your preferred city?
<select name="city">
  <option value="">Select...</option>
  <option value="states">New York</option>
  <option value="California">Los Angeles</option>
  <option value="Illinois">Chicago</option>
  <option value="Texas">Houston</option>
  <option value="Arizona">Phoneix</option>
  <option value="Pennsylvania">Philadelphia</option>
  <option value="Florida">Jacksonville</option>
</select>
<input type="submit" name="submit" value="Select"/>
</form>
<?php
$servername = "localhost";
$username = "root";
$dbname = "data";
$password = "";

$conn = new mysqli($servername, $username, $password, $dbname);
  $sql = "SELECT state,city,date,shortdesc FROM states";

  $result = $conn->query($sql);

  if ($result->num_rows > 0) {
  while($row = $result->fetch_assoc()) {
    echo "state: " . $row["state"]."\ncity: " . $row["city"]."\ndate: " . $row["date"]."\nshort description: " . $row["shortdescription"]."<br>";
  }

}
?>

</p>
</center>
</body>
</html>
