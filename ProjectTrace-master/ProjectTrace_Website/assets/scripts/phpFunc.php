<?php
    function PrintAgencies() {
        echo '<form action="" method="post">';
        echo '<div class="LSDM_Projects_List">';
        echo '<p> # </p><p> Organization </p><p> Organization Full Name </p>';
        echo '<p></p>';
        echo '<p> - </p><p> TEST </p><p> TEST </p>';
        echo '<button type="submit" name="TEST" value="TEST"> > </button>';
        echo '<p> 1 </p><p> DOE </p><p> Department of Energy </p>';
        echo '<button type="submit" name="doe" value="doe"> > </button>';
        echo '<p> 2 </p><p> NIH </p><p> National Institutes of Health </p>';
        echo '<button type="submit" name="nih" value="nih"> > </button>';
        echo '<p> 3 </p><p> NSF </p><p> National Sanitation Foundation </p>';
        echo '<button type="submit" name="nsf" value="nsf"> > </button>';
        echo '</div>';
        echo '</form>';
    }

    function PrintProjects($agency, $page) {
        // Data Sanitization
        $agency=addslashes($agency);

        // Fetch information from database
        $dblink=new mysqli(/*'host', 'user', 'password', 'database'*/);
        $sql="SELECT * FROM ".$agency."_content LIMIT ".($page*-100).", 100";
        $results=$dblink->query($sql) or die('ERROR: Database query failed.');
        $count=1;

        echo '<form action="" method="post">';
        echo '<button type="submit" name="" value=""> < Back </button>';

        // Top Page Navigation
        PrintPageNav($agency, $page);

        echo '<div class="LSDM_Projects_List">';
        echo '<p> # </p><p> Funding Agency </p><p> Project Title </p><p></p>';
        while ($data=$results->fetch_array(MYSQLI_NUM)) {
            echo '<p> '.$count++.' </p>';
            echo '<p> '.$data[1].' </p>';
            echo '<p> '.$data[0].' </p>';
            echo '<button type="submit" name="'.$agency.'" value="'.$data[2].'" class="LSDM_List_Button"> > </button>';
        }
        echo '</div>';

        // Bottom Page Navigation
        PrintPageNav($agency, $page);

        echo '<button type="submit" name="" value=""> < Back </button>';
        echo '</form>';
    }

    function PrintPageNav($agency, $page) {
        echo '<div class="LSDM_Projects_Page-Nav">';
        echo '<p></p>';
        if ($page < 0) { echo '<button type="submit" name="'.$agency.'" value="'.($page+1).'"> < Previous Page </button>'; }
        else { echo '<p></p>'; }
        echo '<p> '.($page*-1+1).' </p>';
        echo '<p><button type="submit" name="'.$agency.'" value="'.($page-1).'"> Next Page > </button></p>';
        echo '<p></p>';
        echo '</div>';
    }

    function PrintAward($agency, $award) {
        // Data sanitization
        $agency=addslashes($agency);
        $award=addslashes($award);

        // Fetch information from database
        $dblink=new mysqli(/*host, user, password, database*/);
        $sql='SELECT * FROM '.$agency.' WHERE award_number=\''.$award.'\'';
        $results=$dblink->query($sql) or die('ERROR: Database query failed.');

        while ($data=$results->fetch_array(MYSQLI_NUM)) {
            
            // Print Project Information
            echo '<form action="" method="post">';
            echo '<button type="submit" name="'.$agency.'" value="0"> < Back </button>';
            echo '<p> Award Number: '.$data[2].' </p>';
            echo '<h3> '.$data[0].' </h3>';
            echo '<p> Funding Agency: '.$data[1].' </p>';
            echo '<p> Contact: '.$data[3].' | '.$data[4].' </p>';
            echo '<p> '.$data[6].' </p>';

            // Display images associated with project
            $imageDir='/var/www/html/assets/images/'.preg_replace("/[^A-Za-z0-9 ]/", '', $data[1]).'/';

            if (is_dir($imageDir)) {
                echo '<p><div class="LSDM_Images_Grid">';
                foreach (array_diff(scandir($imageDir), ['.', '..']) as $image) {
                    echo '<img src="/assets/images/'.preg_replace("/[^A-Za-z0-9 ]/", '', $data[1]).'/'.$image.'" class="LSDM_Images_Content">';
                }
                echo '</div></p>';
            }

            echo '<button type="submit" name="'.$agency.'" value="0"> < Back </button>';
            echo '</form>';
        }
    }
?>
