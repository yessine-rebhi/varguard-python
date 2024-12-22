# VarsGuard Python Wrapper

This is a Python wrapper for the [VarsGuard](https://www.npmjs.com/package/varsguard) library, enabling secure and efficient management of environment variables for Python projects. This wrapper allows you to use VarsGuard's functionality directly within your Python code, ensuring your environment variables are properly validated and managed according to best practices.

## Prerequisites

Before using this wrapper, ensure that you have the `varsguard` CLI tool installed globally on your system. You can do this by running the following command:

```bash
npm install -g varsguard
```

This command installs the VarsGuard CLI globally on your machine, which is necessary for the wrapper to function correctly.

## Installation

To install the **VarsGuard Python Wrapper** in your Python environment, you can use **pip**:

1. Install the package from PyPI:

   ```bash
   pip install varsguard
   ```

2. Alternatively, you can clone the repository and install it locally for development purposes:

   ```bash
   git clone https://github.com/your-username/var-guard-python-wrapper.git
   cd var-guard-python-wrapper
   pip install .
   ```

## Usage

Once the wrapper is installed, you can use it in your Python projects. Below are the available commands you can execute.

### 1. **Generate .env.example File**

Use the `generate` method to scan your codebase for environment variables and automatically generate a `.env.example` file.

```python
from varsguard.cli import VarsGuard

# Generate .env.example from your codebase
VarsGuard.generate()
```

### 2. **Validate .env File**

Use the `validate` method to validate your `.env` file against the `.env.example` or a schema file. You can also pass a GitHub token and repository if needed for additional context.

```python
from varsguard.cli import VarsGuard

# Validate your .env file
VarsGuard.validate(token="your_github_token", repo="owner/repo", schema_path="path/to/schema.json")
```

## Commands Reference

### `generate()`
- Scans your codebase and generates a `.env.example` file.
  
### `validate(token, repo, schema_path)`
- Validates your `.env` file against the `.env.example` or a schema file.
- Parameters:
  - `token` (str): GitHub token for accessing the repository (optional).
  - `repo` (str): GitHub repository in the format `owner/repo` (optional).
  - `schema_path` (str): Path to the schema file (optional).


## CI/CD Integration

You can integrate **VarsGuard** validation into your CI/CD pipeline. The Python wrapper can be used to automatically validate environment variables during your build or deployment process. Here’s an example GitHub Actions workflow that uses the `VarsGuard.validate()` method to ensure that your `.env` file is correctly configured:

### Example GitHub Actions Workflow

```yaml
name: Validate .env File

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  validate:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install varsguard

      - name: Validate .env file
        run: |
          python -c "from varsguard.cli import VarsGuard; VarsGuard.validate(token='${{ secrets.GITHUB_TOKEN }}', repo='owner/repo')"
```

## Testing Locally

To test the wrapper locally before publishing, make sure you have the necessary dependencies installed and test it using the following steps:

1. Clone the repository locally:

   ```bash
   git clone https://github.com/your-username/var-guard-python-wrapper.git
   cd var-guard-python-wrapper
   ```

2. Install the Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Test your Python wrapper methods:

   ```python
   from varsguard.cli import VarsGuard

   # Run generate method
   VarsGuard.generate()

   # Run validate method
   VarsGuard.validate(token="your_github_token", repo="owner/repo", schema_path="path/to/schema.json")
   ```

## Contributing

We welcome contributions! If you would like to contribute to the **VarsGuard Python Wrapper**, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Commit your changes.
4. Push the changes to your fork.
5. Open a pull request with a description of your changes.

Please ensure that you have tested your changes locally before submitting a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
