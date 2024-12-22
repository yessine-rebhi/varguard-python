import subprocess
import shutil
import sys

if not shutil.which("varguard"):
    print(
        "❌ VarGuard CLI not found! Please install it globally using:\n"
        "   npm install -g varguard"
    )
    sys.exit(1)

class VarGuard:
    @staticmethod
    def run_command(command, *args):
        cmd = ['varguard', command, *args]
        try:
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error running command: {' '.join(cmd)}")
            print(e.stderr)

    @staticmethod
    def validate(token=None, repo=None, schema_path=None):
        args = []
        if token:
            args += ['--token', str(token)]
        if repo:
            args += ['--repo', str(repo)]
        if schema_path:
            args += ['--schemaPath', str(schema_path)]
        VarGuard.run_command('validate', *args)

    @staticmethod
    def generate():
        VarGuard.run_command('generate')