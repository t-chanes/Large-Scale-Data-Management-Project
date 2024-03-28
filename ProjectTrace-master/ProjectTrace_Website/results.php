<html class="LSDM_BasePage">
    <head>
        <title> Results </title>
        <link rel="stylesheet" href="/assets/styles/LSDM.css">
    </head>

    <body>
        <!-- [PERSISTENT] Page Header -->
        <div class="LSDM_Header_Area">
            <div class="LSDM_Header_Banner">
                <h1> ProjectTrace </h1>
            </div>

            <!-- [PERSISTENT] Navigation -->
            <div class="LSDM_Header_Nav">
                <a href="./" class="LSDM_Nav_Buttons">              Home  </a>
                <a href="./results.php" class="LSDM_Nav_Buttons">   Results </a>
                <a href="./resources.php" class="LSDM_Nav_Buttons"> Resources </a>
                <a href="./contact.php" class="LSDM_Nav_Buttons">   Contact </a>
            </div>
        </div>

        <!-- Page Content -->
        <div class="LSDM_Body_Subheader">
            <h2> Results </h2>
        </div>

        <div class="LSDM_Body_Content">
            <?php
                // tail -f /var/log/nginx/error.log for error checking

                require __DIR__ . '/assets/scripts/phpFunc.php';

                if (isset($_POST['doe'])) {
                    if ($_POST['doe'] > 0) { PrintAward('doe', $_POST['doe']); }
                    else { PrintProjects('doe', $_POST['doe']); }
                }
                elseif (isset($_POST['nih'])) {
                    if ($_POST['nih'] > 0) { PrintAward('nih', $_POST['nih']); }
                    else { PrintProjects('nih', $_POST['nih']); }
                }
                elseif (isset($_POST['nsf'])) {
                    if ($_POST['nsf'] > 0) { PrintAward('nsf', $_POST['nsf']); }
                    else { PrintProjects('nsf', $_POST['nsf']); }
                }
                else { PrintAgencies(); }
            ?>
        </div>
    </body>
</html>
