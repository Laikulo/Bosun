# Bosun

## Summary
While bosun's initial scope only included managing versions of klipper MCU's Bosun's scope has expanded to be a management wrapper for Klipper.

## Desired functionality
Note: Bosun's functions are intended to be modular, one or more may be used or not.

### Lifecycle mangement of klipper.
* Install klipper host, manage dependencies of same, using OS packages as much as possible.
    * (wrap kiauah as possible)
* Build and flash klipper mcu firmware

### Configuration externalization
* Shim printer.cfg to allow storing save_config items in an external storage.
* Retrieve klipper config from some other storage.

### Config templating
* Generate configuration from a higher level configuraiton langauge, covering most cases, and avoiding dumb cases (probes w/o safe_z_home)
* Also a set of validation rules to help prevent mistakes.

### Extension and python path management.
* Allow specification of extentions, either by modifying pythonpath, or building one with overlays (or possibly symlinks in a tempdir)

### Configuration
* A UI to manage bosun's configs, or configs of other systems.