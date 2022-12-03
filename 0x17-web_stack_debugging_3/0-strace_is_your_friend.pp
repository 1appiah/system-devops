# debug the wordpress stack
exec { 'correct file name':
  command => 'mv /var/www/html/wp-includes/wp-settings.php\
   /var/www/html/wp-includes/wp-settings.phpp',
}
