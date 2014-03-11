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

  exec { "django syncdb":
    command => "/www/manage.py syncdb --noinput",
    require => Exec['install python packages'],
  }

  supervisor::program { 'saladbar':
    ensure => present,
    enable => true,
    command => '/usr/bin/gunicorn saladbar.wsgi:application',
    directory => '/www',
    user => 'vagrant',
    group => 'vagrant',
    require => Exec['django syncdb'],
  }

  file { "/var/static":
    ensure => directory,
    owner => 'vagrant',
    group => 'vagrant',
  }

  exec { "collectstatic":
    command => "/www/manage.py collectstatic --noinput",
    user => vagrant,
    require => [File['/var/static'],
                Exec['install python packages']],
  }

  class { 'nginx':
    require => File['/var/static'],
  }

  nginx::resource::location { "saladbar-static":
    ensure => present,
    vhost => 'saladbar-host',
    location => '/static',
    www_root => '/var/',
  }

  nginx::resource::vhost { 'saladbar-host':
    ensure => present,
    proxy  => 'http://127.0.0.1:8000',
  } 

  file { "/etc/nginx/conf.d/default.conf":
    ensure => absent,
    require => Package['nginx'],
    notify => Service['nginx'],
  }

}
