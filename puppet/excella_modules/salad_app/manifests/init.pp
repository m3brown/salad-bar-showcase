class salad_app {

  package { "python":
    ensure => installed,
  }

  package { "python-pip":
    ensure => installed,
  }

  exec { "install python packages":
    command => "/usr/bin/pip install -r /www/requirements.txt",
    require => Package['python-pip'],
  }

}
