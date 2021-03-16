<?php
if ($_GET['pass'] == 'p4pu4b4r4t123') {
        echo '<form action="" method="POST">
<input type="text" name="name" placeholder="name"><br>
<input type="text" name="link" placeholder="link"><br>
<button type="submit">Submit</button></form>';

        if ($_POST['link'] && $_POST['name']) {
                $name = $_POST['name'];
                $link = $_POST['link'];
                $data = $name.'{SPACE}'.$link.'{ENTER}';
                shell_exec("echo ".$data." >> /var/www/html/data/kasdgd87gbkubweu3yg4oblkjdash.json");
        }
        echo '<pre>Data</pre>';
        $mycat = shell_exec("cat /var/www/html/data/kasdgd87gbkubweu3yg4oblkjdash.json");
        $mycat = explode("{ENTER}", $mycat);
        foreach ($mycat as $rowcat){
                $rowcat = str_replace(' ', '', $rowcat);
                $cat = explode("{SPACE}", $rowcat);
//              $url = explode("?", $_SERVER[REQUEST_URI])[0];
//              $name = "http://$_SERVER[HTTP_HOST]/sh".$url."?lk=".$cat[0];
                $name = "http://$_SERVER[HTTP_HOST]/sh?lk=".$cat[0];
                $link = $cat[1];
        echo '<a href="'.$name.'">'.$cat[0].'</a> : <a href="'.$link.'">'.$link.'</a><br>';
        }
}

if ($_GET['lk']){
        $mycat = shell_exec("cat /var/www/html/data/kasdgd87gbkubweu3yg4oblkjdash.json");
        $mycat = explode("{ENTER}", $mycat);
        foreach ($mycat as $rowcat){
                $rowcat = str_replace(' ', '', $rowcat);
                $cat = explode("{SPACE}", $rowcat);
                if (strpos($cat[0], $_GET['lk']) !== false) {
                        header("Location: ".$cat[1]);
                }
        }
}

echo '404 NotFound';
