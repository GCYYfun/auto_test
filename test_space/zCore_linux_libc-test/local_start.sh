cd zCore

rustup show

cargo build --release -p linux-loader

python3.8 libc-test.py
