class salad_app {

  package { "python":
    ensure => installed,
  }

  package { "python-pip":
    ensure => installed,
    require => Package['python'],
  }

  exec { "install python packages":
    command => "/usr/bin/pip install -r /www/requirements.txt",
    require => Package['python-pip'],
  }

  supervisor::program { 'saladbar':
    ensure => present,
    enable => true,
    command => '/usr/bin/gunicorn saladbar.wsgi:application',
    directory => '/www',
    user => 'vagrant',
    group => 'vagrant',
    require => Exec['install python packages'],
  }

  class { 'nginx': }

  nginx::resource::vhost { 'saladbar-host':
    ensure => present,
    proxy  => 'http://127.0.0.1:8000',
  } 

}
