# kill a process
exec { 'killmenow':
  command => '/bin/bash pkill killmenow',
}
