"""Main module."""
from core.app import App


try:
    from secrets import secret_config
except ImportError:
    print("ERROR: Configuration not defined")
    raise RuntimeError("No secrets.py to import")

DEBUG = True


def main():
    """App entry point."""
    with App(name="/app", config=secret_config, debug=DEBUG) as app:
        try:
            app.run()
        except RuntimeError as e:
            print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
