# debug the wordpress stack
exec { 'correct file name':
  command => 'mv /var/www/html/wp-includes/class-wp-locale.php\
   /var/www/html/wp-includes/class-wp-locale.php',
  path    => '/bin',
}
