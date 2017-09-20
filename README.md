# Enpass to 1Password

A script to migrate from [Enpass](https://enpass.io) to [1Password](https://1password.com).

1. Open Enpass and click File > Export > To CSV
2. Run `python3 e2op.py <enpass csv export>` to create `out.csv`
3. Import `out.csv` into 1Password

# FAQ

## Will this steal my passwords?

It's 50 lines of really basic Python. Read it yourself and verify it.
