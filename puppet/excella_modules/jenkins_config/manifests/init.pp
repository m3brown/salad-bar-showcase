class jenkins_config {

  $jenkins_config_home = "/var/jenkins_config"
  $jenkins_cli_bin = "${jenkins_config_home}/jenkins-cli.jar"

  file { "jenkins_config":
    path => "${jenkins_config_home}",
    ensure => directory,
    owner => 'vagrant',
    group => 'vagrant',
  }

  file { "jenkins-cli":
    path => "${jenkins_cli_bin}",
    ensure => file,
    owner => 'vagrant',
    group => 'vagrant',
    source => 'puppet:///modules/jenkins_config/jenkins-cli.jar',
  }

}
