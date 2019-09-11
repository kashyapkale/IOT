<?php
shell_exec("/usr/bin/gpio -g mode 3 out");
if(isset($_GET['off']))
{
	echo "LED is OFF";
	shell_exec("/usr/bin/gpio -g write 3 0");
}
else if(isset($_GET['on']))
{
	echo "LED is ON";
	shell_exec("/usr/bin/gpio -g write 3 1");
}
?>
