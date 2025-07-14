Copr repository for COPR repo for https://github.com/PancakeTAS/lsfg-vk, commits are fetched every hour.

The packages in this repo should work on Fedora 41+.

See the COPR page here: https://copr.fedorainfracloud.org/coprs/jackgreiner/lsfg-vk-git

## Installation 

Activate the repo with `sudo dnf copr enable jackgreiner/lsfg-vk-git`.

Install the package with `sudo dnf install lsfg-vk`

To revert this, remove the package with `sudo dnf remove lsfg-vk` and remove the copr repository with `sudo dnf copr remove jackgreiner/lsfg-vk-git`.

For more info about setting this up for your usecase, see the upstream Wiki here: https://github.com/PancakeTAS/lsfg-vk/wiki

### You will need to own Lossless Scaling on Steam for this to work.

## Issues

Feel free to open issues when there are build issues I haven't fixed for a few days: https://github.com/ProjectSynchro/copr-lsfg-vk-git/issues

If you'd like me to attempt to package this for other RPM based distros like SUSE, open an issue and I'll see what I can do :)

## Testing

To test build this package locally using `fedpkg`, follow these steps:

1. Install `fedpkg`:
   ```sh
   sudo dnf install fedpkg
   ```

3. Prepare the sources:
   ```sh
   fedpkg prep
   ```

4. Build the package:
   ```sh
   fedpkg local
   ```

This will create the RPM packages in the `x86_64` (or whatever arch you are building this package for) directory under the current working directory.