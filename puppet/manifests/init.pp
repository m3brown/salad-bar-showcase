hiera_include('classes')

class { 'yum':
  extrarepo => [
    'epel',
    'repoforgeextras',
  ],
}

# configure repo before installing any packages
Class['yum::repo::epel'] -> Package <| |>
