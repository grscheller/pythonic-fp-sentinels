CHANGELOG
=========

PyPI pythonic-fp.singletons project.

Semantic Versioning
-------------------

Strict 3 digit semantic versioning adopted 2025-05-19.

- **MAJOR** version incremented for incompatible API changes
- **MINOR** version incremented for backward compatible added functionality
- **PATCH** version incremented for backward compatible bug fixes

See `Semantic Versioning 2.0.0 <https://semver.org>`_.

Releases and Important Milestones
---------------------------------

2.0.0 - TBA
~~~~~~~~~~~

- moved module pythonic_fp.singletons.sbool -> pythonic_fp.booleans.{ibool,sbool}.
- removed pythonic_fp.nada module

  - learned a lot about Python getting it to work
  - decided it use case was not worth the effort to maintain it

- extended class Singleton

  - from declaring multiple singletons with strings
  - to declaring multiple "flavors" of any hashable type


1.0.0 - 2025-08-02
~~~~~~~~~~~~~~~~~~

Moved singletons.py from fptools. Also incorporated bool.py into the
singleton's package.
