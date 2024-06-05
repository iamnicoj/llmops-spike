# Conditional Execution of a Workflow Based on the Files Modified

## Overview

The purpose of this spike is to simulate how a workflow gets triggered based on modified files.

- When a file is modified, the workflow will detect it and execute pytest's that correspond to the modified file.

  - This is achieved using the [Paths Changes Filter](https://github.com/marketplace/actions/paths-changes-filter) plugin.

## Workflow Syntax

- Base: changes are detected against the most recent commit before the push.
  - If base is not used, the default is set to main.

- Filters: Allow us to set filters on specific files or entire directories.

  - The path expressions are evaluated using the [picomatch](https://github.com/micromatch/picomatch) library.

### Picomatch

  - Picomatch is a versatile library for evaluating path expressions, it's useful in scenarios involving file matching and filtering.

      > Note: It doesn't directly handle the contents in the files. For example: if you're looking to ignore whitespace changes within the content of files, you would need to use a different tool or library tailored for that purpose.

    - Picomatch doesn't perform diff checks directly; instead, it focuses on matching file paths against glob patterns or specific file paths.

      - Glob Pattern: When you provide a glob pattern to Picomatch, it converts this pattern into a regular expression (regex). This conversion allows the library to match paths against the pattern efficiently.

        - Once the pattern is compiled, you can use the generated matcher function to test if a given path matches the pattern.

      - Specific File Path: When you provide a specific file path to Picomatch without any wildcards or glob pattern syntax, it will only match if the pattern you specify exactly matches the provided file path.
      
