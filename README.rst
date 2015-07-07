PruneBib
================================================================================

``prunebib`` creates a database of BibTeX entries by pruning a pre-existing
BibTeX database down to only the entries that are referenced in a LaTeX
document. This is done by:

#. Loading all entries from a pre-existing BibTeX database.
#. Scanning a LaTeX file for all BibTeX keys referenced within citation
   (\cite{}) commands.
#. Returning a new BibTeX database containing only the entries that are:
    * valid entries in the pre-existing BibTeX database.
    * referenced in the LaTeX document.

``prunebib`` was designed for finalising documents that reference large, general
purpose BibTeX databases. For example, if multiple authors contribute to a
BibTeX database, this may cause the contents of a rendered bibliography to
change over time. Even worse, the original LaTeX document may no longer compile
due to missing references or changed BibTeX keys. ``prunebib`` allows the BibTeX
database to be 'frozen' before distribution. The published version of the LaTeX
document will be independent from changes to the original BibTeX database. The
source code of the distributed BibTeX file will also only contain entries
referenced in the published document.

The process is demonstrated graphically below::

        +--------------------------+     +--------------------------+
        |    Large BibTeX file     |     |      LaTeX document      |
        +--------------------------+     +--------------------------+
        | @article{A,              |     |                          |
        |    ...                   |     | \documentclass{article}  |
        | }                        |     | \begin{document}         |
        |                          |     |    ...                   |
        | @book{B,                 |     |    ... \cite{A,C} ...    |
        |    ...                   |     |    ...                   |
        | }                        |     |    \cite{A} ...          |
        |                          |     |    ...                   |
        | @article{C,              |     |    ...                   |
        |    ...                   |     | \bibliography{large.bib} |
        | }                        |     | \end{document}           |
        |                          |     |                          |
        +--------------------------+     +--------------------------+
                     |                                |
                     |                                |
                     +----------------+---------------+
                                      |
                                      |
                                +-----V------+
                                |  prunebib  |
                                +------------+
                                      |
                                      |
                         +------------V-------------+
                         |    Small BibTeX file     |
                         +--------------------------+
                         | @article{A,              |
                         |    ...                   |
                         | }                        |
                         |                          |
                         | @article{C,              |
                         |    ...                   |
                         | }                        |
                         |                          |
                         +--------------------------+

Installation
--------------------------------------------------------------------------------

This code supports installation using pip (via `setuptools
<https://pypi.python.org/pypi/setuptools>`_). To install from the git
repository:

.. code-block:: bash

    git clone https://github.com/asherbender/prunebib
    cd prunebib
    sudo pip install .

Once installed, the command ``prunebib`` is available from the command-line. The
script is typically installed in

.. code-block:: bash

    /usr/local/bin/

To uninstall the package:

.. code-block:: bash

    pip uninstall prunebib

Dependencies
--------------------------------------------------------------------------------

The following libraries are used in ``prunebib`` and are managed by pip:

* `bibtexparser <https://pypi.python.org/pypi/bibtexparser>`_

Usage
--------------------------------------------------------------------------------

To print the pruned bibliography to standard out:

.. code-block:: bash

    prunebib input.bib input.tex

To save the pruned bibliography to a file:

.. code-block:: bash

    prunebib input.bib input.tex output.bib

or pipe the output into a file:

.. code-block:: bash

    prunebib input.bib input.tex > output.bib

License
--------------------------------------------------------------------------------

This code is licensed under the `GNU General Public License Version 3 (GPLv3)
<https://gnu.org/licenses/gpl.html>`_.
